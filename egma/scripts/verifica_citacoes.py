"""Verifica citações literais contra PDFs e devolve páginas do arquivo.

Uso:
    python scripts/verifica_citacoes.py quotes.json saida.json [offsets.json]

quotes.json:
    [{"id": "Q01", "trecho": "...", "arquivo": "opcional.pdf"}]
offsets.json (opcional):
    {"arquivo.pdf": 36}
    página impressa estimada = página do PDF + offset. Use somente offset
    confirmado contra evidência independente.

Dependência: PyMuPDF (import fitz).
`ok=True` exige correspondência única. Múltiplas ocorrências ficam `estado=ambigua`,
sem página única escolhida, e produzem código de saída de pendência.
A correspondência textual não valida contexto, tradução ou paginação impressa.
"""
import json
import os
import re
import sys
import unicodedata

import fitz


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\u00ad\u2010-\u2015-]\s*\n\s*", "", s)
    s = re.sub(r"[\u00ad\u2010-\u2015-]", "", s)
    s = s.replace("\n", " ")
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


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

    docs = {}
    for root, _, files in os.walk(base):
        for filename in sorted(files):
            if filename.lower().endswith(".pdf"):
                docs[filename] = fitz.open(os.path.join(root, filename))

    pages = {name: [norm(p.get_text()) for p in doc] for name, doc in docs.items()}
    printed = {}
    for name, doc in docs.items():
        printed[name] = []
        for page in doc:
            lines = [x.strip() for x in page.get_text().strip().split("\n") if x.strip()]
            candidates = lines[:1] + lines[-1:]
            number = next((int(x) for x in candidates if x.isdigit()), None)
            printed[name].append(number)

    out = []
    for quote in quotes:
        needle = norm(quote["trecho"])
        targets = [quote["arquivo"]] if quote.get("arquivo") else list(pages)
        hits = [(name, i) for name in targets if name in pages
                for i, page in enumerate(pages[name], start=1) if needle and needle in page]
        rec = {"id": quote["id"], "trecho": quote["trecho"][:90], "arquivo": None,
               "pagina_pdf": None, "pagina_impressa": None, "encontrado": bool(hits),
               "ok": len(hits) == 1, "n_hits": len(hits),
               "estado": "verificado" if len(hits) == 1 else ("ambigua" if hits else "nao_encontrado")}
        if len(hits) == 1:
            name, i = hits[0]
            rec.update(arquivo=name, pagina_pdf=i)
            if printed[name][i - 1] is not None:
                rec["pagina_impressa"] = printed[name][i - 1]
            elif name in offsets:
                rec["pagina_impressa"] = i + offsets[name]
                rec["pagina_impressa_origem"] = "offset_declarado"
        elif hits:
            rec["candidatos"] = hits
        out.append(rec)

    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    failures = [r for r in out if not r["ok"]]
    ambiguous = [r for r in out if r["estado"] == "ambigua"]
    print(f"verificadas: {len(out) - len(failures)}/{len(out)}")
    for rec in ambiguous:
        print("  AMBÍGUA:", rec["id"], f"{rec['n_hits']} correspondências")
    for rec in failures:
        if rec["estado"] == "nao_encontrado":
            print("  FALHOU:", rec["id"], rec["trecho"][:70])
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
