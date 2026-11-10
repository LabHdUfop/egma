"""Verifica citações literais contra PDFs e devolve a localização no arquivo.

Uso:
    python scripts/verifica_citacoes.py quotes.json saida.json [offsets.json]

quotes.json:
    [{"id": "Q01", "trecho": "...", "arquivo": "opcional/caminho/relativo.pdf"}]
offsets.json (opcional):
    {"arquivo.pdf": 36}
    página impressa estimada = página do PDF + offset. Use somente offset
    confirmado contra evidência independente.

Dependência: PyMuPDF.

Estados de saída, por citação:

    verificado        ocorrência única, dentro de uma página
    entre_paginas     localizado na junção de duas páginas adjacentes; exige
                      conferência visual, por isso ok=False
    ambigua           mais de uma ocorrência, sem localização única
    nao_encontrado    o texto não ocorre nas fontes existentes
    arquivo_ausente   a fonte declarada não existe na base
    arquivo_ambiguo   o nome declarado existe em mais de um arquivo; exige caminho

`ok=True` exige ocorrência única e dentro de uma página. Fonte ausente é distinta
de texto ausente: confundir as duas faz uma falha de indexação passar por achado.
Todo registro informa `caminho` e `sha256` do arquivo usado, para que o resultado
diga qual exemplar foi lido. A correspondência textual não valida contexto,
tradução ou paginação impressa.
"""
import hashlib
import json
import os
import re
import sys
import unicodedata

try:  # PyMuPDF 1.26+ expõe `pymupdf`; versões anteriores, `fitz`.
    import pymupdf as fitz
except ImportError:
    import fitz


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\u00ad\u2010-\u2015-]\s*\n\s*", "", s)
    s = re.sub(r"[\u00ad\u2010-\u2015-]", "", s)
    s = s.replace("\n", " ")
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def linhas(texto: str):
    return [x.strip() for x in texto.strip().split("\n") if x.strip()]


def artefatos_de_folha(paginas):
    """Cabeçalhos, rodapés e números de folha: primeira/última linha das páginas.

    Uma linha é artefato se for número isolado ou se repetir como borda em mais
    da metade das páginas do documento. Serve apenas à junção entre páginas; a
    busca dentro da página usa o texto íntegro.
    """
    contagem = {}
    for texto in paginas:
        ls = linhas(texto)
        for l in set(ls[:1] + ls[-1:]):
            contagem[l] = contagem.get(l, 0) + 1
    n = max(1, len(paginas))
    return {l for l, c in contagem.items() if l.isdigit() or (c >= 2 and c > n / 2)}


def limpar(texto: str, artefatos) -> str:
    return "\n".join(l for l in linhas(texto) if l not in artefatos)


def sha256(caminho: str) -> str:
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print(__doc__.strip(), file=sys.stderr)
        return 2

    with open(sys.argv[1], encoding="utf-8") as f:
        quotes = json.load(f)
    offsets = {}
    if len(sys.argv) == 4 and os.path.exists(sys.argv[3]):
        with open(sys.argv[3], encoding="utf-8") as f:
            offsets = json.load(f)
    base = os.path.dirname(os.path.abspath(sys.argv[1]))

    # Índice por caminho relativo à base, não por basename: dois arquivos de mesmo
    # nome em pastas diferentes são fontes distintas, e a ordem do os.walk não
    # pode decidir qual delas prevalece.
    brutos, limpos, impressos, hashes = {}, {}, {}, {}
    for root, _, files in os.walk(base):
        for filename in sorted(files):
            if not filename.lower().endswith(".pdf"):
                continue
            caminho = os.path.join(root, filename)
            rel = os.path.relpath(caminho, base).replace(os.sep, "/")
            doc = fitz.open(caminho)
            try:
                paginas = [p.get_text() for p in doc]
            finally:
                doc.close()
            brutos[rel] = [norm(t) for t in paginas]
            artefatos = artefatos_de_folha(paginas)
            limpos[rel] = [limpar(t, artefatos) for t in paginas]
            impressos[rel] = []
            for texto in paginas:
                ls = linhas(texto)
                candidatos = ls[:1] + ls[-1:]
                impressos[rel].append(
                    next((int(x) for x in candidatos if x.isdigit()), None))
            hashes[rel] = sha256(caminho)

    rel_paths = sorted(brutos)
    por_basename = {}
    for rel in rel_paths:
        por_basename.setdefault(os.path.basename(rel), []).append(rel)

    out = []
    for quote in quotes:
        needle = norm(quote["trecho"])
        rec = {"id": quote["id"], "trecho": quote["trecho"][:90], "arquivo": None,
               "caminho": None, "sha256": None, "pagina_pdf": None, "paginas_pdf": None,
               "pagina_impressa": None, "pagina_impressa_origem": "indeterminado",
               "encontrado": False, "ok": False, "n_hits": 0, "n_ocorrencias": 0,
               "estado": "nao_encontrado"}

        declarado = quote.get("arquivo")
        if declarado:
            alvo = declarado.replace("\\", "/").lstrip("./")
            if alvo in brutos:
                alvos = [alvo]
            else:
                candidatos = por_basename.get(os.path.basename(alvo), [])
                if len(candidatos) == 1:
                    alvos = candidatos
                elif candidatos:
                    rec["estado"] = "arquivo_ambiguo"
                    rec["candidatos"] = candidatos
                    out.append(rec)
                    continue
                else:
                    rec["estado"] = "arquivo_ausente"
                    out.append(rec)
                    continue
        else:
            alvos = rel_paths

        if not needle:
            rec["estado"] = "trecho_vazio"
            out.append(rec)
            continue

        # Ocorrências, não pares (arquivo, página): duas vezes na mesma página
        # também é ambiguidade, e não localização única.
        ocorrencias = [(rel, i, pagina.count(needle))
                       for rel in alvos
                       for i, pagina in enumerate(brutos[rel], start=1)
                       if needle in pagina]
        total = sum(n for _, _, n in ocorrencias)
        rec["n_hits"] = len(ocorrencias)
        rec["n_ocorrencias"] = total

        if total == 1:
            rel, i, _ = ocorrencias[0]
            rec.update(estado="verificado", ok=True, encontrado=True,
                       arquivo=rel, caminho=rel, sha256=hashes[rel], pagina_pdf=i)
            if impressos[rel][i - 1] is not None:
                rec["pagina_impressa"] = impressos[rel][i - 1]
                rec["pagina_impressa_origem"] = "observado"
            elif rel in offsets:
                rec["pagina_impressa"] = i + offsets[rel]
                rec["pagina_impressa_origem"] = "offset_declarado"
            out.append(rec)
            continue

        if total > 1:
            rec.update(estado="ambigua", encontrado=True,
                       candidatos=[[rel, i] for rel, i, _ in ocorrencias])
            out.append(rec)
            continue

        # Sem ocorrência dentro de uma página: tentar a junção de adjacentes,
        # descontando cabeçalho, rodapé e número de folha.
        juncao = [(rel, i) for rel in alvos
                  for i in range(1, len(limpos[rel]))
                  if needle in norm(limpos[rel][i - 1] + "\n" + limpos[rel][i])]
        if juncao:
            rel, i = juncao[0]
            rec.update(estado="entre_paginas", encontrado=True, arquivo=rel,
                       caminho=rel, sha256=hashes[rel], paginas_pdf=[i, i + 1],
                       forma_juncao="paginas adjacentes sem cabecalho/rodape")
            if len(juncao) > 1:
                rec["candidatos"] = [[r, j] for r, j in juncao]
            if all(impressos[rel][p - 1] is not None for p in (i, i + 1)):
                rec["paginas_impressas"] = [impressos[rel][i - 1], impressos[rel][i]]
            out.append(rec)
            continue

        out.append(rec)

    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    failures = [r for r in out if not r["ok"]]
    print(f"verificadas: {len(out) - len(failures)}/{len(out)}")
    for rec in out:
        if rec["estado"] == "ambigua":
            print("  AMBÍGUA:", rec["id"], f"{rec['n_ocorrencias']} ocorrências")
        elif rec["estado"] == "entre_paginas":
            print("  ENTRE PÁGINAS:", rec["id"], rec["paginas_pdf"], "(conferir visualmente)")
        elif rec["estado"] in ("arquivo_ausente", "arquivo_ambiguo"):
            print(f"  {rec['estado'].upper()}:", rec["id"])
        elif rec["estado"] == "nao_encontrado":
            print("  FALHOU:", rec["id"], rec["trecho"][:70])
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
