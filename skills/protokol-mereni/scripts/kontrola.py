"""
kontrola.py – kontrola hotového protokolu (.docx) proti Zásadám a připomínkám vyučujících.

    python kontrola.py protokol.docx [--autor "Matyáš Mlnařík"] [--nahled]

Vypíše ✔/✘/! pro každý bod. --nahled vyrenderuje strany do PNG (LibreOffice + pdftoppm),
POZOR: LibreOffice v kontejneru nezobrazuje rovnice Wordu (OMML) – v náhledu budou prázdné,
proto skript rovnice vypíše zvlášť jako LaTeX (zpětně načtené pandocem), ať jde zkontrolovat obsah.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys

from docx import Document
from docx.oxml.ns import qn

POVINNE = ["Teoretický úvod", "Schéma zapojení", "Použité přístroje", "Postup měření",
           "Tabulky", "Příklad výpočtu", "Závěr"]
ZAKAZANE_FRAZE = [
    "probíhalo dle očekávání", "proběhlo dle očekávání", "odpovídají teoretickým předpokladům",
    "odpovídá teoretickým předpokladům", "podle očekávání",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--autor", default="Matyáš Mlnařík")
    ap.add_argument("--trida", default="4. P")
    ap.add_argument("--nahled", action="store_true")
    a = ap.parse_args()
    d = Document(a.docx)
    ok, chyby, varovani = [], [], []

    # --- pořadí hlavních částí
    h1 = [p.text.strip() for p in d.paragraphs if p.style.name == "Heading 1"]
    chybi = [s for s in POVINNE if not any(s.lower() in h.lower() for h in h1)]
    if chybi:
        chyby.append("Chybí části: " + ", ".join(chybi))
    else:
        poradi = [next(i for i, h in enumerate(h1) if s.lower() in h.lower()) for s in POVINNE]
        (ok if poradi == sorted(poradi) else chyby).append(
            "Pořadí částí " + ("odpovídá" if poradi == sorted(poradi) else "NEODPOVÍDÁ") + " deskám: " + " → ".join(POVINNE))

    # --- záhlaví se jménem a číslem stránky
    hdr_ok = True
    for i, s in enumerate(d.sections):
        hx, fx = s.header._element.xml, s.footer._element.xml
        if a.autor not in hx or a.trida not in hx or "PAGE" not in fx:
            hdr_ok = False
    (ok if hdr_ok else chyby).append(
        f"Záhlaví „{a.autor}“ vlevo + „{a.trida}“ vpravo a číslo stránky v zápatí vpravo ve všech sekcích"
        + ("" if hdr_ok else " – CHYBÍ"))

    # --- grafy: každý ve vlastní sekci na šířku
    body = d.element.body
    sekce_obsah, akt = [], []
    for el in body.iterchildren():
        akt.append(el)
        if el.tag == qn("w:p") and el.find(".//" + qn("w:sectPr")) is not None:
            sekce_obsah.append(akt); akt = []
    sekce_obsah.append(akt)
    grafy = 0
    for sec, obsah in zip(d.sections, sekce_obsah):
        if sec.orientation == 1:  # landscape
            obr = sum(len(e.findall(".//" + qn("w:drawing"))) for e in obsah)
            grafy += obr
            if obr != 1:
                varovani.append(f"Sekce na šířku obsahuje {obr} obrázků – graf má být sám na stránce.")
    (ok if grafy else varovani).append(f"Počet grafů přes celou stranu: {grafy}")

    # --- tabulky: jednotky
    bez_jednotek = 0
    for t in d.tables:
        txt = " ".join(c.text for c in t.rows[0].cells) + " " + " ".join(r.cells[0].text for r in t.rows)
        if "OZNAČENÍ" in txt:
            continue
        if "[" not in txt:
            bez_jednotek += 1
    (ok if not bez_jednotek else varovani).append(
        "Jednotky v [ ] u veličin v tabulkách" + ("" if not bez_jednotek else f" – {bez_jednotek} tabulek bez jednotek?"))

    # --- tabulka přístrojů
    prist = any("OZNAČENÍ" in t.rows[0].cells[0].text for t in d.tables)
    (ok if prist else chyby).append("Tabulka použitých přístrojů (5 sloupců dle Zásad)" + ("" if prist else " – CHYBÍ"))

    # --- závěr: jen souvislý text, bez frází
    paras = d.paragraphs
    try:
        i = next(k for k, p in enumerate(paras) if p.style.name == "Heading 1" and "závěr" in p.text.lower())
        zav = [p for p in paras[i + 1:] if p.style.name != "Heading 1"]
        styly = {p.style.name for p in zav if p.text.strip()}
        if any("List" in s for s in styly):
            chyby.append("Závěr obsahuje odrážky – má být jen souvislý text (věty).")
        txt = " ".join(p.text for p in zav).lower()
        for f in ZAKAZANE_FRAZE:
            if f in txt:
                chyby.append(f"Závěr obsahuje zakázanou frázi „{f}“ – napiš konkrétně, co a proč vyšlo.")
        slov = len(txt.split())
        (ok if slov >= 80 else varovani).append(f"Závěr má {slov} slov" + ("" if slov >= 80 else " – asi příliš stručný"))
        if not re.search(r"\d", txt):
            varovani.append("Závěr neobsahuje žádná čísla – porovnej konkrétní výsledky.")
    except StopIteration:
        pass

    # --- teoretický úvod: rozsah
    try:
        i = next(k for k, p in enumerate(paras) if p.style.name == "Heading 1" and "teoretick" in p.text.lower())
        j = next(k for k, p in enumerate(paras) if k > i and p.style.name == "Heading 1")
        slov = sum(len(p.text.split()) for p in paras[i:j])
        (ok if slov >= 450 else varovani).append(f"Teoretický úvod: {slov} slov (cíl 2–3 strany ≈ 600–1100 slov + obrázky)")
        txt = " ".join(p.text.lower() for p in paras[i:j])
        if "literatura" not in txt and "zdroj" not in txt:
            varovani.append("Teoretický úvod nemá uvedenou literaturu/zdroje (Zásady: uvést na konci TÚ).")
    except StopIteration:
        pass

    # --- nedoplněná místa
    dopl = [r.text for p in paras for r in p.runs if r.font.highlight_color is not None]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                dopl += [r.text for p in c.paragraphs for r in p.runs if r.font.highlight_color is not None]
    if dopl:
        varovani.append("Zbývá doplnit (žlutě): " + "; ".join(sorted(set(dopl))))

    # --- rovnice
    n_eq = len(body.findall(".//" + qn("m:oMath")))
    ok.append(f"Rovnic (OMML): {n_eq}")

    for t in ok: print("✔", t)
    for t in varovani: print("!", t)
    for t in chyby: print("✘", t)

    if shutil.which("pandoc"):
        out = subprocess.run(["pandoc", a.docx, "-t", "markdown", "--wrap=none"], capture_output=True, text=True).stdout
        rov = re.findall(r"\$\$(.+?)\$\$", out)
        if rov:
            print("\nRovnice (zpětně načtené z dokumentu):")
            for r in rov:
                print("   ", r)

    if a.nahled:
        od = os.path.splitext(a.docx)[0] + "_nahled"
        os.makedirs(od, exist_ok=True)
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", od, a.docx],
                       capture_output=True)
        pdf = os.path.join(od, os.path.splitext(os.path.basename(a.docx))[0] + ".pdf")
        if os.path.exists(pdf):
            subprocess.run(["pdftoppm", "-r", "60", "-png", pdf, os.path.join(od, "str")])
            print(f"\nNáhled stran: {od}/str-*.png  (rovnice v náhledu chybí – viz výpis výše)")
    sys.exit(1 if chyby else 0)


if __name__ == "__main__":
    main()
