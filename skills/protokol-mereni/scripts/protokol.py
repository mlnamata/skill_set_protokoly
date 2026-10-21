"""
protokol.py – sestavení protokolu o měření (elaborátu) do Wordu (.docx)
ve stylu VOŠ a SPŠE Plzeň.

Použití (z vlastního build skriptu):

    import sys; sys.path.insert(0, "<cesta ke skillu>/scripts")
    from protokol import Protokol

    p = Protokol(autor="Matyáš Mlnařík")
    p.h1("Teoretický úvod")
    p.h2("Usměrňovač")
    p.text("Usměrňovač mění střídavé napětí na stejnosměrné. Výstupní napětí U_{0} ...")
    p.rovnice(r"R_i = \\frac{\\Delta U}{\\Delta I}\\ [\\Omega]")
    p.obrazek("schema.png", sirka_cm=14, popisek="Schéma Graetzova můstku")
    ...
    p.uloz("EM_CV14.docx")

Mini-markup v textu (text, odrážky, buňky tabulek, popisky):
    **tučně**, *kurzíva*, X_{index}, X^{exponent}, $inline LaTeX$,
    [[DOPLNIT: co chybí]]  -> žlutě zvýrazněné místo k doplnění

Rovnice se píší v LaTeXu a převádí se přes pandoc na nativní rovnice Wordu (OMML).
Desetinná čárka: piš normálně "2,63" – skript čísla s čárkou slepí do jednoho bloku.
"""
from __future__ import annotations

import copy
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from typing import Iterable, Sequence

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_COLOR_INDEX, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# ---------------------------------------------------------------- vzhled
PISMO = "Calibri"
PISMO_NADPIS = "Calibri Light"
VELIKOST = 11
BARVA_NADPISU = RGBColor(0x2F, 0x54, 0x96)  # výchozí modrá Wordu jako ve vzorech
OKRAJ_CM = 2.5

PRISTROJE_HLAVICKA = [
    "OZNAČENÍ\nVE SCHÉMATU",
    "NÁZEV, FUNKCE",
    "TYP, ROZSAH",
    "EVIDENČNÍ (VÝROBNÍ)\nČÍSLO",
    "POZNÁMKA",
]
PRISTROJE_SIRKY_CM = [2.6, 4.2, 4.4, 3.4, 2.4]

_INLINE_RE = re.compile(
    r"(\[\[DOPLNIT:[^\]]*\]\]|\$[^$]+\$|\*\*[^*]+\*\*|\*[^*]+\*|_\{[^}]*\}|\^\{[^}]*\})"
)


def fmt(cislo, des=2) -> str:
    """Číslo -> text s desetinnou čárkou, zaokrouhlený na `des` míst."""
    if isinstance(cislo, str):
        return cislo
    if cislo is None:
        return ""
    if isinstance(cislo, int) and des is None:
        return str(cislo)
    s = f"{cislo:.{des}f}" if des is not None else f"{cislo:g}"
    return s.replace(".", ",")


class Protokol:
    def __init__(self, autor: str = "Matyáš Mlnařík", pismo: str = PISMO):
        self.autor = autor
        self.doc = Document()
        self._rovnice: list[tuple[str, bool]] = []  # (latex, display)
        self._cislo_obr = 0
        self._cislo_tab = 0
        self.doplnit: list[str] = []
        self._styly(pismo)
        self._strana(self.doc.sections[0], na_sirku=False)
        self._zahlavi(self.doc.sections[0])

    # ------------------------------------------------------------ nastavení
    def _styly(self, pismo):
        st = self.doc.styles
        n = st["Normal"]
        n.font.name = pismo
        n.font.size = Pt(VELIKOST)
        n.element.rPr.rFonts.set(qn("w:eastAsia"), pismo)
        n.paragraph_format.space_after = Pt(6)
        n.paragraph_format.line_spacing = 1.08
        for jmeno, vel, pred in (("Heading 1", 20, 18), ("Heading 2", 16, 10), ("Heading 3", 13, 8)):
            s = st[jmeno]
            s.font.name = PISMO_NADPIS
            s.font.size = Pt(vel)
            s.font.bold = False
            s.font.color.rgb = BARVA_NADPISU
            rpr = s.element.get_or_add_rPr()
            rf = rpr.find(qn("w:rFonts"))
            if rf is None:
                rf = OxmlElement("w:rFonts")
                rpr.append(rf)
            for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
                rf.set(qn(a), PISMO_NADPIS)
            for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
                if rf.get(qn(a)) is not None:
                    del rf.attrib[qn(a)]
            s.paragraph_format.space_before = Pt(pred)
            s.paragraph_format.space_after = Pt(4)
            s.paragraph_format.keep_with_next = True
        cap = st["Caption"]
        cap.font.name = pismo
        cap.font.size = Pt(9)
        cap.font.italic = True
        cap.font.color.rgb = RGBColor(0x40, 0x40, 0x40)

    def _strana(self, sec, na_sirku: bool):
        sir, vys = Cm(21.0), Cm(29.7)
        if na_sirku:
            sec.orientation = WD_ORIENT.LANDSCAPE
            sec.page_width, sec.page_height = vys, sir
        else:
            sec.orientation = WD_ORIENT.PORTRAIT
            sec.page_width, sec.page_height = sir, vys
        for a in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
            setattr(sec, a, Cm(OKRAJ_CM))
        sec.header_distance = Cm(1.25)
        sec.footer_distance = Cm(1.25)

    def _zahlavi(self, sec):
        """Záhlaví: jméno vlevo, číslo stránky vpravo (Zásady: očíslované listy se jménem)."""
        sec.header.is_linked_to_previous = False
        hdr = sec.header
        p = hdr.paragraphs[0]
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
        sirka = sec.page_width - sec.left_margin - sec.right_margin
        p.paragraph_format.tab_stops.clear_all() if hasattr(p.paragraph_format.tab_stops, "clear_all") else None
        p.paragraph_format.tab_stops.add_tab_stop(sirka, WD_TAB_ALIGNMENT.RIGHT)
        r = p.add_run(self.autor)
        r.font.size = Pt(9)
        r = p.add_run("\t")
        self._pole(p, "PAGE", "1", Pt(9))

    @staticmethod
    def _pole(p, instr, vychozi, size=None):
        def run():
            r = p.add_run()
            if size:
                r.font.size = size
            return r
        r = run(); fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "begin"); r._r.append(fc)
        r = run(); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} \\* MERGEFORMAT "; r._r.append(it)
        r = run(); fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "separate"); r._r.append(fc)
        r = run(); r.text = vychozi
        r = run(); fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "end"); r._r.append(fc)

    def _nova_sekce(self, na_sirku: bool):
        sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self._strana(sec, na_sirku)
        self._zahlavi(sec)  # vlastní záhlaví – správná pozice tabulátoru pro výšku i šířku
        return sec

    # ------------------------------------------------------------ text
    def _runs(self, p, text: str, bold=False, italic=False, size=None):
        """Vloží text s mini-markupem do odstavce p."""
        for kus in _INLINE_RE.split(text):
            if not kus:
                continue
            b, i, sub, sup, hl = bold, italic, False, False, False
            t = kus
            if kus.startswith("[[DOPLNIT:"):
                t = kus[2:-2].strip()
                hl = True
                self.doplnit.append(t)
            elif kus.startswith("$") and kus.endswith("$") and len(kus) > 2:
                self._inline_rovnice(p, kus[1:-1])
                continue
            elif kus.startswith("**"):
                t, b = kus[2:-2], True
            elif kus.startswith("*") and kus.endswith("*") and len(kus) > 2:
                t, i = kus[1:-1], True
            elif kus.startswith("_{"):
                t, sub = kus[2:-1], True
            elif kus.startswith("^{"):
                t, sup = kus[2:-1], True
            parts = t.split("\n")
            for k, part in enumerate(parts):
                r = p.add_run(part)
                r.bold, r.italic = b, i
                if sub:
                    r.font.subscript = True
                if sup:
                    r.font.superscript = True
                if hl:
                    r.font.highlight_color = WD_COLOR_INDEX.YELLOW
                if size:
                    r.font.size = size
                if k < len(parts) - 1:
                    r.add_break()
        return p

    def h1(self, text: str, nova_strana: bool = False):
        """Hlavní část protokolu (Teoretický úvod, Schéma zapojení, …)."""
        self._na_vysku()
        p = self.doc.add_heading(level=1)
        self._runs(p, text)
        p.paragraph_format.page_break_before = nova_strana
        return p

    def h2(self, text: str):
        self._na_vysku()
        p = self.doc.add_heading(level=2)
        self._runs(p, text)
        return p

    def h3(self, text: str):
        self._na_vysku()
        p = self.doc.add_heading(level=3)
        self._runs(p, text)
        return p

    def text(self, text: str, zarovnat: str = "do_bloku"):
        """Odstavec. Víc odstavců = víc volání (nebo prázdný řádek \\n\\n)."""
        self._na_vysku()
        posledni = None
        for odst in re.split(r"\n\s*\n", text.strip()):
            p = self.doc.add_paragraph()
            if zarovnat == "do_bloku":
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            elif zarovnat == "na_stred":
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            self._runs(p, odst.strip())
            posledni = p
        return posledni

    def odrazky(self, polozky: Iterable[str], cislovane: bool = False):
        self._na_vysku()
        styl = "List Number" if cislovane else "List Bullet"
        for t in polozky:
            p = self.doc.add_paragraph(style=styl)
            self._runs(p, t)

    def zalomeni_strany(self):
        self._na_vysku()
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ------------------------------------------------------------ rovnice
    def rovnice(self, latex: str, tucne: bool = False):
        """Samostatná (vycentrovaná) rovnice v LaTeXu -> nativní rovnice Wordu."""
        self._na_vysku()
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(4)
        idx = len(self._rovnice)
        self._rovnice.append((latex, True, tucne))
        p.add_run(f"@@ROVNICE{idx}@@")
        return p

    def _inline_rovnice(self, p, latex: str):
        idx = len(self._rovnice)
        self._rovnice.append((latex, False, False))
        p.add_run(f"@@ROVNICE{idx}@@")

    def vypocet(self, nadpis: str, obecne: str, promenne: str | Sequence[tuple[str, str]] | None,
                dosazeni: str | Sequence[str], vysledek: str, poznamka: str | None = None):
        """Příklad výpočtu ve stylu: obecný vztah -> popis veličin -> dosazení -> TUČNÝ výsledek.

        promenne: "kde U je ..." (text s mini-markupem) nebo [("$U$", "napětí na zátěži [V]"), ...]
        dosazeni: LaTeX řádek nebo seznam řádků (každý na samostatném řádku)
        vysledek: LaTeX výsledku i s jednotkou, např. r"R_i = 2,63\\ \\Omega"
        """
        self.h2(nadpis)
        self.rovnice(obecne)
        if promenne:
            if isinstance(promenne, str):
                self.text(promenne)
            else:
                casti = [f"{sym} … {popis}" for sym, popis in promenne]
                p = self.doc.add_paragraph()
                self._runs(p, "kde " + casti[0])
                for c in casti[1:]:
                    p = self.doc.add_paragraph()
                    p.paragraph_format.left_indent = Cm(0.75)
                    p.paragraph_format.space_after = Pt(0)
                    self._runs(p, c)
                p.paragraph_format.space_after = Pt(6)
        for r in ([dosazeni] if isinstance(dosazeni, str) else dosazeni):
            self.rovnice(r)
        self.rovnice(vysledek, tucne=True)
        if poznamka:
            self.text(poznamka)

    # ------------------------------------------------------------ obrázky
    def obrazek(self, cesta: str, sirka_cm: float = 14, popisek: str | None = None, zdroj: str | None = None):
        """Obrázek na střed; s popiskem 'Obrázek N: …, zdroj: …' (ve TÚ uváděj zdroj převzatých obrázků)."""
        self._na_vysku()
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = bool(popisek)
        p.add_run().add_picture(cesta, width=Cm(sirka_cm))
        if popisek:
            self._cislo_obr += 1
            t = f"Obrázek {self._cislo_obr}: {popisek}"
            if zdroj:
                t += f", zdroj: {zdroj}"
            c = self.doc.add_paragraph(style="Caption")
            c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            self._runs(c, t)
        return p

    def schema(self, cesta: str, nadpis: str | None = None, sirka_cm: float = 15):
        """Schéma zapojení: nadpis H2 (např. 'Měření VA metodou') + obrázek."""
        if nadpis:
            self.h2(nadpis)
        return self.obrazek(cesta, sirka_cm=sirka_cm)

    def graf(self, cesta: str, na_sirku: bool = True):
        """Graf přes celou stranu A4 – vždy sám na stránce (název je přímo v obrázku grafu).

        Vloží novou sekci na šířku, graf, a vrátí se zpět na výšku.
        """
        self._nova_sekce(na_sirku=na_sirku)
        sec = self.doc.sections[-1]
        sirka = (sec.page_width - sec.left_margin - sec.right_margin) / 360000  # cm
        vyska = (sec.page_height - sec.top_margin - sec.bottom_margin) / 360000 - 1.2
        from PIL import Image
        with Image.open(cesta) as im:
            pomer = im.height / im.width
        sirka_obr = min(sirka, vyska / pomer)
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.add_run().add_picture(cesta, width=Cm(sirka_obr))
        self._v_grafu = True  # zpět na výšku až před dalším obsahem (žádné prázdné strany mezi grafy)

    def _na_vysku(self):
        if getattr(self, "_v_grafu", False):
            self._v_grafu = False
            self._nova_sekce(na_sirku=False)

    # ------------------------------------------------------------ tabulky
    def _tabulka(self, data: list[list[str]], tucny_radek0=True, tucny_sloupec0=False,
                 sirky_cm: Sequence[float] | None = None, velikost=10):
        self._na_vysku()
        rows, cols = len(data), max(len(r) for r in data)
        t = self.doc.add_table(rows=rows, cols=cols)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, r in enumerate(data):
            for j in range(cols):
                v = r[j] if j < len(r) else ""
                c = t.cell(i, j)
                p = c.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                b = (tucny_radek0 and i == 0) or (tucny_sloupec0 and j == 0)
                self._runs(p, str(v), bold=b, size=Pt(velikost))
        if sirky_cm:
            for j, w in enumerate(sirky_cm):
                for i in range(rows):
                    t.cell(i, j).width = Cm(w)
        # opakovat záhlaví na další stránce
        if tucny_radek0:
            trPr = t.rows[0]._tr.get_or_add_trPr()
            h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)
        return t

    def pristroje(self, radky: Sequence[Sequence[str]]):
        """Tabulka použitých přístrojů (5 sloupců dle Zásad). Chybějící evid. číslo -> '[[DOPLNIT: evid. č.]]'."""
        data = [PRISTROJE_HLAVICKA] + [list(r) + [""] * (5 - len(r)) for r in radky]
        t = self._tabulka(data, tucny_radek0=True, tucny_sloupec0=True, sirky_cm=PRISTROJE_SIRKY_CM)
        return t

    def tabulka(self, nazev: str | None, data: dict | Sequence[Sequence], orientace: str = "vodorovne",
                des: int | Sequence[int] | dict | None = 2, max_sloupcu: int = 12, velikost: int = 10):
        """Tabulka naměřených/vypočítaných hodnot.

        nazev: nadpis H2 nad tabulkou – musí říct CO a NA ČEM se měřilo (součástka + parametry).
        data:  dict {"U_{0} [V]": [..], "I_{0} [mA]": [..]}  (veličina i s jednotkou v [ ])
               nebo seznam řádků včetně hlavičky.
        orientace: "vodorovne" = veličiny v řádcích (jako ve vzorech), dlouhé řady se zalomí
                   po `max_sloupcu` hodnotách; "svisle" = veličiny ve sloupcích.
        des:   počet desetinných míst – jedno číslo, seznam podle veličin, nebo dict {klíč: des}.
        """
        if nazev:
            self.h2(nazev)
        if isinstance(data, dict):
            klice = list(data.keys())
            def d_for(k, idx):
                if isinstance(des, dict):
                    return des.get(k, 2)
                if isinstance(des, (list, tuple)):
                    return des[idx]
                return des
            sloupce = [[fmt(v, d_for(k, n)) for v in data[k]] for n, k in enumerate(klice)]
            n = max(len(s) for s in sloupce)
            sloupce = [s + [""] * (n - len(s)) for s in sloupce]
            if orientace == "vodorovne":
                kusy = [(a, min(a + max_sloupcu, n)) for a in range(0, n, max_sloupcu)]
                vse = []
                for a, b in kusy:
                    for k, s in zip(klice, sloupce):
                        vse.append([k] + s[a:b] + [""] * (max_sloupcu - (b - a) if len(kusy) > 1 else 0))
                    if (a, b) != kusy[-1]:
                        vse.append([""] * (len(vse[-1])))
                return self._tabulka(vse, tucny_radek0=False, tucny_sloupec0=True, velikost=velikost)
            data2 = [klice] + [list(r) for r in zip(*sloupce)]
            return self._tabulka(data2, tucny_radek0=True, velikost=velikost)
        data2 = [[fmt(v, des if isinstance(des, int) else 2) for v in r] for r in data]
        return self._tabulka(data2, tucny_radek0=True, velikost=velikost)

    # ------------------------------------------------------------ uložení
    def uloz(self, cesta: str):
        self.doc.save(cesta)
        if self._rovnice:
            _vloz_rovnice(cesta, self._rovnice)
        print(f"Uloženo: {cesta}")
        if self.doplnit:
            print("K DOPLNĚNÍ (žlutě zvýrazněno v dokumentu):")
            for d in self.doplnit:
                print("  -", d)
        return cesta


# ================================================================ OMML přes pandoc
def _pandoc_bin():
    b = shutil.which("pandoc")
    if b:
        return b
    try:
        import pypandoc  # type: ignore
        return pypandoc.get_pandoc_path()
    except Exception:
        raise RuntimeError("Chybí pandoc (apt install pandoc, nebo pip install pypandoc_binary).")


def _latex_na_omml(rovnice):
    """Vrátí seznam XML elementů m:oMath (v pořadí) pro zadané LaTeX rovnice."""
    with tempfile.TemporaryDirectory() as td:
        md = os.path.join(td, "r.md")
        out = os.path.join(td, "r.docx")
        with open(md, "w", encoding="utf-8") as f:
            for i, (lx, _disp, _b) in enumerate(rovnice):
                lx = lx.strip().replace("\n", " ")
                f.write(f"MARK{i}\n\n$${lx}$$\n\n")
        subprocess.run([_pandoc_bin(), md, "-f", "markdown", "-o", out], check=True)
        with zipfile.ZipFile(out) as z:
            xml = z.read("word/document.xml").decode("utf-8")
    from lxml import etree
    root = etree.fromstring(xml.encode("utf-8"))
    body = root.find(qn("w:body"))
    vysl = {}
    akt = None
    for p in body.iter(qn("w:p")):
        txt = "".join(t.text or "" for t in p.iter(qn("w:t")))
        m = re.fullmatch(r"MARK(\d+)", txt.strip())
        if m:
            akt = int(m.group(1))
            continue
        om = p.find(".//" + qn("m:oMath"))
        if om is not None and akt is not None and akt not in vysl:
            vysl[akt] = om
    chybi = [i for i in range(len(rovnice)) if i not in vysl]
    if chybi:
        raise RuntimeError("Nepodařilo se převést rovnice: " + "; ".join(rovnice[i][0] for i in chybi))
    return [vysl[i] for i in range(len(rovnice))]


def _slep_cisla(om):
    """'2' ',' '63' -> '2,63' (aby Word nevkládal mezeru za čárku)."""
    for parent in list(om.iter()):
        deti = list(parent)
        i = 0
        while i < len(deti) - 2:
            a, b, c = deti[i], deti[i + 1], deti[i + 2]
            if all(x.tag == qn("m:r") for x in (a, b, c)):
                ta, tb, tc = (x.find(qn("m:t")) for x in (a, b, c))
                if (ta is not None and tb is not None and tc is not None and ta.text and tc.text
                        and re.fullmatch(r"[0-9]+", ta.text) and tb.text == "," and re.fullmatch(r"[0-9]+", tc.text)):
                    ta.text = ta.text + "," + tc.text
                    parent.remove(b); parent.remove(c)
                    deti = list(parent)
                    continue
            i += 1


def _ztucni(om):
    for r in om.iter(qn("m:r")):
        t = r.find(qn("m:t"))
        txt = (t.text or "") if t is not None else ""
        rpr = r.find(qn("m:rPr"))
        if rpr is None:
            rpr = OxmlElement("m:rPr")
            r.insert(0, rpr)
        sty = rpr.find(qn("m:sty"))
        puvodni = sty.get(qn("m:val")) if sty is not None else None
        nova = "b" if (puvodni == "p" or not re.search(r"[A-Za-zÀ-ž]", txt)) else "bi"
        if sty is None:
            sty = OxmlElement("m:sty")
            rpr.append(sty)
        sty.set(qn("m:val"), nova)
        wrpr = r.find(qn("w:rPr"))
        if wrpr is None:
            wrpr = OxmlElement("w:rPr")
            r.append(wrpr) if t is None else t.addprevious(wrpr)
        if wrpr.find(qn("w:b")) is None:
            wrpr.append(OxmlElement("w:b"))


def _vloz_rovnice(cesta, rovnice):
    omml = _latex_na_omml(rovnice)
    doc = Document(cesta)
    mapa = {}
    for p in doc.element.body.iter(qn("w:p")):
        for r in p.findall(qn("w:r")):
            t = r.find(qn("w:t"))
            if t is not None and t.text and t.text.startswith("@@ROVNICE"):
                mapa[int(re.search(r"\d+", t.text).group())] = (p, r)
    # rovnice v tabulkách/záhlavích tu nejsou podporované – jen tělo dokumentu
    for idx, (p, r) in mapa.items():
        lx, disp, tucne = rovnice[idx]
        om = copy.deepcopy(omml[idx])
        _slep_cisla(om)
        if tucne:
            _ztucni(om)
        if disp:
            omp = OxmlElement("m:oMathPara")
            ppr = OxmlElement("m:oMathParaPr")
            jc = OxmlElement("m:jc"); jc.set(qn("m:val"), "center"); ppr.append(jc)
            omp.append(ppr); omp.append(om)
            r.addprevious(omp)
        else:
            r.addprevious(om)
        p.remove(r)
    doc.save(cesta)
