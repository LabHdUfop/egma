"""Suite de aceitacao do verificador de citacoes da EGMA.

Gera uma fixture inteiramente sintetica (PDFs criados com PyMuPDF, nenhum
dado de pesquisa envolvido), roda `verifica_citacoes.py` como subprocasso e
afirma o estado esperado de cada caso. Cada teste e independente: uma falha
nao interrompe os demais.

Uso:
    python tests/test_verifica_citacoes.py [caminho/do/verifica_citacoes.py]

Saida: tabela PASS/FAIL por caso e codigo de saida 1 se houver algum FAIL.
Os casos 4, 5, 6, 7, 8 e 10 falham contra a 1.0.0 por construcao -- sao os
defeitos que a v1.1 precisa corrigir.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz

SCRIPT = Path(sys.argv[1]) if len(sys.argv) > 1 else (
    Path(__file__).resolve().parents[1] / "egma" / "scripts" / "verifica_citacoes.py")

RESULTS = []


def pdf(path: Path, paginas):
    """Cria um PDF; `paginas` e uma lista de listas de linhas (com cabecalho/rodape)."""
    doc = fitz.open()
    for linhas in paginas:
        page = doc.new_page()
        y = 72
        for linha in linhas:
            page.insert_text((72, y), linha)
            y += 18
    doc.save(str(path))
    doc.close()


def montar_fixture(base: Path):
    """Cria os PDFs, o quotes.json e o offsets.json da rodada."""
    pdf(base / "unico.pdf", [["A separacao de contextos e o nucleo do protocolo EGMA."]])
    # Repeticao em paginas diferentes do mesmo PDF.
    pdf(base / "repetido.pdf", [["Trecho repetido aqui.", "Outra coisa."],
                                ["Trecho repetido aqui.", "Fim."]])
    # Repeticao dentro da mesma pagina: hoje o verificador conta (arquivo, pagina),
    # nao ocorrencias, e devolve "verificado" com pagina unica.
    pdf(base / "repetido_mesma_pagina.pdf", [["Trecho repetido aqui.", "Trecho repetido aqui."]])
    pdf(base / "ausente.pdf", [["Nada que interesse a esta busca."]])
    # Quebra de pagina: frase comeca na p.1 e termina na p.2, com cabecalho e
    # rodape no meio. Concatenacao ingenua incorporaria "CAPITULO 3" e "40".
    pdf(base / "quebra.pdf", [
        ["CAPITULO 3", "A revisao exige que o nucleo do protocolo", "", "40"],
        ["CAPITULO 3", "EGMA seja lido em contexto isolado.", "", "41"],
    ])
    (base / "v1").mkdir()
    (base / "v2").mkdir()
    pdf(base / "v1" / "mesmo.pdf", [["Documento da versao um com marcador alfa origem."]])
    pdf(base / "v2" / "mesmo.pdf", [["Documento da versao dois com marcador beta origem."]])
    pdf(base / "impresso.pdf", [["137", "Texto com folha impressa visivel no topo."]])
    pdf(base / "com_offset.pdf", [["Primeira pagina."], ["Frase na segunda pagina do arquivo."]])

    quotes = [
        {"id": "Q01", "trecho": "separacao de contextos"},
        {"id": "Q02", "trecho": "Trecho repetido aqui", "arquivo": "repetido.pdf"},
        {"id": "Q02B", "trecho": "Trecho repetido aqui", "arquivo": "repetido_mesma_pagina.pdf"},
        {"id": "Q03", "trecho": "frase que nao existe em lugar nenhum"},
        {"id": "Q04", "trecho": "o nucleo do protocolo EGMA seja lido"},
        {"id": "Q05A", "trecho": "versao um com marcador alfa"},
        {"id": "Q05B", "trecho": "versao dois com marcador beta"},
        {"id": "Q06", "trecho": "versao um com marcador alfa", "arquivo": "v1/mesmo.pdf"},
        {"id": "Q07", "trecho": "qualquer texto", "arquivo": "inexistente.pdf"},
        {"id": "Q08", "trecho": "folha impressa visivel"},
        {"id": "Q09", "trecho": "Frase na segunda pagina do arquivo"},
    ]
    (base / "quotes.json").write_text(json.dumps(quotes, ensure_ascii=False), encoding="utf-8")
    (base / "offsets.json").write_text(json.dumps({"com_offset.pdf": 40}), encoding="utf-8")


def executar(base: Path):
    saida = base / "saida.json"
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), str(base / "quotes.json"), str(saida),
         str(base / "offsets.json")],
        capture_output=True, text=True, encoding="utf-8")
    registros = json.loads(saida.read_text(encoding="utf-8")) if saida.exists() else []
    return {r["id"]: r for r in registros}, proc.returncode


def teste(nome, esperado):
    """Decorador: registra PASS/FAIL sem abortar a suite."""
    def wrap(fn):
        try:
            fn()
            RESULTS.append((nome, "PASS", esperado, ""))
        except AssertionError as e:
            RESULTS.append((nome, "FAIL", esperado, str(e).strip() or "assertiva violada"))
    return wrap


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        montar_fixture(base)
        recs, code = executar(base)

        def r(cid):
            assert cid in recs, f"registro {cid} ausente na saida"
            return recs[cid]

        @teste("1. pagina unica, ocorrencia unica", "estado=verificado, pagina_pdf=1, ok=True")
        def t1():
            x = r("Q01")
            assert x["estado"] == "verificado", x["estado"]
            assert x["pagina_pdf"] == 1, x["pagina_pdf"]
            assert x["ok"] is True

        @teste("2. repeticao em paginas diferentes", "estado=ambigua, n_hits=2, ok=False")
        def t2():
            x = r("Q02")
            assert x["estado"] == "ambigua", x["estado"]
            assert x["n_hits"] == 2, x["n_hits"]
            assert x["ok"] is False

        @teste("2b. repeticao na mesma pagina", "estado=ambigua (hoje conta como verificado)")
        def t2b():
            x = r("Q02B")
            assert x["estado"] == "ambigua", x["estado"]
            assert x["ok"] is False, "duas ocorrencias nao podem valer como unica"

        @teste("3. ausencia real do texto", "estado=nao_encontrado, ok=False")
        def t3():
            x = r("Q03")
            assert x["estado"] == "nao_encontrado", x["estado"]
            assert x["ok"] is False

        @teste("4. citacao entre paginas", "estado=entre_paginas, paginas_pdf=[1,2], ok=False")
        def t4():
            x = r("Q04")
            assert x["estado"] == "entre_paginas", x["estado"]
            assert x.get("paginas_pdf") == [1, 2], x.get("paginas_pdf")
            assert x["ok"] is False, "texto localizado nao deve valer como verificado"

        @teste("5. PDFs homonimos em pastas diferentes",
               "cada citacao no seu arquivo, por caminho relativo")
        def t5():
            a, b = r("Q05A"), r("Q05B")
            assert a["estado"] == "verificado", f"Q05A: {a['estado']}"
            assert b["estado"] == "verificado", f"Q05B: {b['estado']}"
            pa = str(a["arquivo"]).replace("\\", "/")
            pb = str(b["arquivo"]).replace("\\", "/")
            assert pa.endswith("v1/mesmo.pdf"), pa
            assert pb.endswith("v2/mesmo.pdf"), pb

        @teste("6. caminho explicito no quotes.json", "resolve o homonimo indicado")
        def t6():
            x = r("Q06")
            assert x["estado"] == "verificado", x["estado"]
            assert str(x["arquivo"]).replace("\\", "/").endswith("v1/mesmo.pdf"), x["arquivo"]

        @teste("7. fonte declarada e ausente", "estado=arquivo_ausente (nao nao_encontrado)")
        def t7():
            x = r("Q07")
            assert x["estado"] == "arquivo_ausente", x["estado"]

        @teste("8. folha impressa observada no PDF", "pagina_impressa=137, origem=observado")
        def t8():
            x = r("Q08")
            assert x["pagina_impressa"] == 137, x["pagina_impressa"]
            assert x.get("pagina_impressa_origem") == "observado", x.get("pagina_impressa_origem")

        @teste("9. offset declarado", "pagina_impressa=42, origem=offset_declarado")
        def t9():
            x = r("Q09")
            assert x["pagina_impressa"] == 42, x["pagina_impressa"]
            assert x.get("pagina_impressa_origem") == "offset_declarado", x.get(
                "pagina_impressa_origem")

        @teste("10. identidade da fonte verificada", "caminho e sha256 do arquivo usado")
        def t10():
            x = r("Q01")
            assert x.get("caminho"), "sem caminho do arquivo"
            assert len(x.get("sha256", "")) == 64, "sem SHA-256 do arquivo"

        print(f"\nScript sob teste: {SCRIPT}")
        print(f"Codigo de saida do script: {code}\n")
        largura = max(len(n) for n, *_ in RESULTS)
        for nome, status, esperado, detalhe in RESULTS:
            print(f"[{status}] {nome.ljust(largura)}  {esperado}")
            if detalhe:
                print(f"       obtido: {detalhe}")
        falhas = [x for x in RESULTS if x[1] == "FAIL"]
        print(f"\n{len(RESULTS) - len(falhas)}/{len(RESULTS)} passaram, "
              f"{len(falhas)} falharam")
        return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
