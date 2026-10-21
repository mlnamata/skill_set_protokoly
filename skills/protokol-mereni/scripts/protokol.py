"""
protokol.py – sestavení protokolu o měření (elaborátu) do Wordu (.docx)
ve stylu Matyášova protokolu CV1 (VOŠ a SPŠE Plzeň).

Vzhled (podle CV1):
  * A4, okraje 2,5 cm, Calibri 11 pt, černý text, zarovnání vlevo, mezera za odstavcem 4 pt
  * nadpis 1. úrovně: tučně, černě, 20 pt, číslovaný „1. Teoretický úvod“
  * nadpis 2. úrovně: tučně, černě, 14 pt, číslovaný „1.1 …“; 3. úroveň tučně 11 pt
  * záhlaví: jméno vlevo, třída („4. P“) vpravo; zápatí: číslo stránky vpravo dole
  * tabulky: popisek „1) Název …“ tučně 10 pt + podmínky 9 pt; první sloupec (nebo
    hlavička) tučně s modrým podbarvením D9E2F3, vyznačené hodnoty oranžově FCE4D6
  * grafy: každý na samostatné straně na šířku, před prvním grafem nadpis „Grafy“

Použití:
    import sys; sys.path.insert(0, "<skill>/scripts")
    from protokol import Protokol
    p = Protokol(autor="Matyáš Mlnařík", trida="4. P")
    p.h1("Teoretický úvod"); p.h2("Usměrňovač"); p.text("… **klíčový pojem** … U_{0} …")
    p.rovnice(r"R_i = \\frac{\\Delta U}{\\Delta I}")
    ...
    p.uloz("EM_CV14.docx")

Mini-markup v textu (text, odrážky, buňky tabulek, popisky):
    **tučně**, *kurzíva*, X_{index}, X^{exponent}, $inline LaTeX$,
    [[DOPLNIT: co chybí]]  -> žlutě zvýrazněné místo k doplnění
Rovnice se píší v LaTeXu a převádí se přes pandoc na nativní rovnice Wordu (OMML).
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
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# ---------------------------------------------------------------- vzhled (CV1)
PISMO = "Calibri"
VELIKOST = 11
CERNA = RGBColor(0, 0, 0)
NADPISY = {1: (20, 12, 4), 2: (14, 10, 4), 3: (11, 8, 2)}  # velikost, mezera před, za
OKRAJ_CM = 2.5
PODBARVENI_HLAVICKY = "D9E2F3"   # modrá – popisky veličin v tabulkách
PODBARVENI_VYZNACENI = "FCE4D6"  # oranžová – vyznačené hodnoty (rezonance, maxima …)

PRISTROJE_HLAVICKA = ["Označení ve schématu", "Název, funkce", "Typ, rozsah",
                      "Evidenční (výrobní) číslo", "Poznámka"]
PRISTROJE_SIRKY_CM = [3.0, 3.4, 3.6, 3.4, 2.6]

_INLINE_RE = re.compile(
    r"(\[\[DOPLNIT:[^\]]*\]\]|\$[^$]+\$|\*\*[^*]+\*\*|\*[^*]+\*|_\{[^}]*\}|\^\{[^}]*\})"
)


def fmt(cislo, des=2) -> str:
    """Číslo -> text s desetinnou čárkou, zaokrouhlený na `des` míst (des=None -> jak je)."""
    if isinstance(cislo, str):
        return cislo
    if cislo is None:
        return ""
    try:
        import math
        if isinstance(cislo, float) and math.isnan(cislo):
            return ""
    except Exception:
        pass
    s = f"{cislo:.{des}f}" if des is not None else f"{cislo:g}"
    return s.replace(".", ",")


def _shd(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


class Protokol:
    def __init__(self, autor: str = "Matyáš Mlnařík", trida: str = "4. P", cislovat: bool = True,
                 pismo: str = PISMO):
        self.autor = autor
        self.trida = trida
        self.cislovat = cislovat
        self.doc = Document()
        self._rovnice: list[tuple[str, bool, bool]] = []
        self._n1 = 0
        self._n2 = 0
        self._n3 = 0
        self._ntab = 0
        self.doplnit: list[str] = []
        self._rezim = None        # None | "graf" | "sirka" – aktuální sekce na šířku
        self._grafy_nadpis = False
        self._styly(pismo)
        sec = self.doc.sections[0]
        self._strana(sec, na_sirku=False)
        self._zahlavi_zapati(sec)

    # ------------------------------------------------------------ nastavení
    def _styly(self, pismo):
        st = self.doc.styles
        n = st["Normal"]
        n.font.name = pismo
        n.font.size = Pt(VELIKOST)
        n.font.color.rgb = CERNA
        rf = n.element.rPr.rFonts
        for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rf.set(qn(a), pismo)
        n.paragraph_format.space_before = Pt(0)
        n.paragraph_format.space_after = Pt(4)
        n.paragraph_format.line_spacing = 1.0
        for lvl, (vel, pred, za) in NADPISY.items():
            s = st[f"Heading {lvl}"]
            s.font.name = pismo
            s.font.size = Pt(vel)
            s.font.bold = True
            s.font.italic = False
            s.font.color.rgb = CERNA
            rpr = s.element.get_or_add_rPr()
            rf = rpr.find(qn("w:rFonts"))
            if rf is None:
                rf = OxmlElement("w:rFonts"); rpr.append(rf)
            for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
                if rf.get(qn(a)) is not None:
                    del rf.attrib[qn(a)]
            for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
                rf.set(qn(a), pismo)
            s.paragraph_format.space_before = Pt(pred)
            s.paragraph_format.space_after = Pt(za)
            s.paragraph_format.keep_with_next = True
        for jmeno in ("List Bullet", "List Number"):
            st[jmeno].paragraph_format.space_after = Pt(2)
        for jmeno in ("Header", "Footer"):
            ppr = st[jmeno].element.get_or_add_pPr()
            for t in ppr.findall(qn("w:tabs")):
                ppr.remove(t)
        cap = st["Caption"]
        cap.font.name = pismo
        cap.font.size = Pt(10)
        cap.font.italic = True
        cap.font.bold = False
        cap.font.color.rgb = CERNA
        cap.paragraph_format.space_after = Pt(6)

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

    def _zahlavi_zapati(self, sec):
        """Záhlaví: jméno vlevo, třída vpravo. Zápatí: číslo stránky vpravo dole."""
        sirka = sec.page_width - sec.left_margin - sec.right_margin
        sec.header.is_linked_to_previous = False
        p = sec.header.paragraphs[0]
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.tab_stops.add_tab_stop(sirka, WD_TAB_ALIGNMENT.RIGHT)
        p.add_run(self.autor)
        p.add_run("\t" + (self.trida or ""))
        sec.footer.is_linked_to_previous = False
        f = sec.footer.paragraphs[0]
        for r in list(f.runs):
            r._element.getparent().remove(r._element)
        f.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f.paragraph_format.space_after = Pt(0)
        self._pole(f, "PAGE", "1")

    @staticmethod
    def _pole(p, instr, vychozi, size=None):
        def run():
            r = p.add_run()
            if size:
                r.font.size = size
            return r
        r = run(); fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "begin"); r._r.append(fc)
        r = run(); it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} "; r._r.append(it)
        r = run(); fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "separate"); r._r.append(fc)
        r = run(); r.text = vychozi
        r = run(); fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "end"); r._r.append(fc)

    def _nova_sekce(self, na_sirku: bool):
        sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self._strana(sec, na_sirku)
        self._zahlavi_zapati(sec)
        return sec

    # ------------------------------------------------------------ orientace stran
    def na_sirku(self):
        """Další obsah na stranu na šířku (např. široké tabulky jako v CV1). Platí do na_vysku()
        nebo do dalšího nadpisu 1. úrovně."""
        if self._rezim != "sirka":
            self._nova_sekce(na_sirku=True)
        self._rezim = "sirka"

    def na_vysku(self):
        if self._rezim is not None:
            self._rezim = None
            self._nova_sekce(na_sirku=False)

    def _priprav(self, h1=False):
        """Před běžným obsahem: po grafu (nebo před novou kapitolou) vrátit stránku na výšku."""
        if self._rezim == "graf" or (h1 and self._rezim == "sirka"):
            self.na_vysku()

    # ------------------------------------------------------------ text
    def _runs(self, p, text: str, bold=False, italic=False, size=None):
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
                if b:
                    r.bold = True      # jinak nechat dědit ze stylu (nadpisy jsou tučné)
                if i:
                    r.italic = True
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

    def h1(self, text: str, nova_strana: bool = False, na_sirku: bool = False):
        """Kapitola protokolu – automaticky číslovaná „1. Teoretický úvod“.
        na_sirku=True: kapitola začne na straně na šířku (např. „Tabulky“ se širokými tabulkami
        jako v CV1); zpět na výšku se přejde u další kapitoly nebo p.na_vysku()."""
        self._priprav(h1=True)
        if na_sirku:
            self.na_sirku()
        self._n1 += 1; self._n2 = 0; self._n3 = 0
        p = self.doc.add_heading(level=1)
        self._runs(p, f"{self._n1}. {text}" if self.cislovat else text)
        p.paragraph_format.page_break_before = nova_strana
        return p

    def h2(self, text: str):
        """Podkapitola – automaticky číslovaná „1.1 …“."""
        self._priprav()
        self._n2 += 1; self._n3 = 0
        p = self.doc.add_heading(level=2)
        self._runs(p, f"{self._n1}.{self._n2} {text}" if self.cislovat else text)
        return p

    def h3(self, text: str):
        self._priprav()
        p = self.doc.add_heading(level=3)
        self._runs(p, text)
        return p

    def text(self, text: str, zarovnat: str = "vlevo"):
        """Odstavec(e) – oddělené prázdným řádkem. zarovnat: vlevo | do_bloku | na_stred."""
        self._priprav()
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

    def popisek(self, text: str, velikost: float = 10, tucne: bool = True, mezera_pred: float = 8):
        """Krátký tučný popisek (jako nadpisy výpočtů v CV1)."""
        self._priprav()
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(mezera_pred)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        self._runs(p, text, bold=tucne, size=Pt(velikost))
        return p

    def odrazky(self, polozky: Iterable[str], cislovane: bool = False):
        """Odrážky (v TÚ s tučnými klíčovými pojmy jako v CV1: '**Kmitočet f [Hz]** určuje …')."""
        self._priprav()
        styl = "List Number" if cislovane else "List Bullet"
        for t in polozky:
            p = self.doc.add_paragraph(style=styl)
            self._runs(p, t)

    def zalomeni_strany(self):
        self._priprav()
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ------------------------------------------------------------ rovnice
    def rovnice(self, latex: str, tucne: bool = False):
        """Samostatná (vycentrovaná) rovnice v LaTeXu -> nativní rovnice Wordu."""
        self._priprav()
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
        """Příklad výpočtu: tučný popisek (10 pt) -> obecný vztah -> popis veličin ->
        dosazení -> TUČNÝ výsledek.

        promenne: "kde U je ..." nebo [("$U$", "napětí na zátěži [V]"), ...]
        dosazeni: LaTeX řádek nebo seznam řádků
        vysledek: LaTeX výsledku i s jednotkou, např. r"R_i = 2,63\\ \\Omega"
        """
        self.popisek(nadpis)
        self.rovnice(obecne)
        if promenne:
            if isinstance(promenne, str):
                self.text(promenne)
            else:
                casti = [f"{sym} … {popis}" for sym, popis in promenne]
                p = self.doc.add_paragraph()
                p.paragraph_format.space_after = Pt(0)
                self._runs(p, "kde " + casti[0])
                for c in casti[1:]:
                    p = self.doc.add_paragraph()
                    p.paragraph_format.left_indent = Cm(0.75)
                    p.paragraph_format.space_after = Pt(0)
                    self._runs(p, c)
                p.paragraph_format.space_after = Pt(4)
        for r in ([dosazeni] if isinstance(dosazeni, str) else dosazeni):
            self.rovnice(r)
        self.rovnice(vysledek, tucne=True)
        if poznamka:
            self.text(poznamka)

    # ------------------------------------------------------------ obrázky
    def obrazek(self, cesta: str, sirka_cm: float = 14, popisek: str | None = None, zdroj: str | None = None):
        """Obrázek na střed s popiskem pod ním (kurzíva 10 pt, jako v CV1)."""
        self._priprav()
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = bool(popisek)
        p.add_run().add_picture(cesta, width=Cm(sirka_cm))
        if popisek:
            t = popisek + (f", zdroj: {zdroj}" if zdroj else "")
            c = self.doc.add_paragraph(style="Caption")
            c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            self._runs(c, t)
        return p

    def schema(self, cesta: str, nadpis: str | None = None, sirka_cm: float = 15):
        """Schéma zapojení: (volitelně) podnadpis + obrázek."""
        if nadpis:
            self.h2(nadpis)
        return self.obrazek(cesta, sirka_cm=sirka_cm)

    def graf(self, cesta: str, nadpis_kapitoly: str | None = "Grafy"):
        """Graf přes celou stranu A4 na šířku – každý graf sám na stránce.
        Před prvním grafem se na téže straně vloží kapitola „N. Grafy“ (jako v CV1);
        nadpis_kapitoly=None ji vynechá."""
        if self._rezim == "sirka":
            self._rezim = None
        self._nova_sekce(na_sirku=True)
        sec = self.doc.sections[-1]
        sirka = (sec.page_width - sec.left_margin - sec.right_margin) / 360000  # cm
        vyska = (sec.page_height - sec.top_margin - sec.bottom_margin) / 360000 - 1.0
        if nadpis_kapitoly and not self._grafy_nadpis:
            self._grafy_nadpis = True
            self._n1 += 1; self._n2 = 0
            h = self.doc.add_heading(level=1)
            h.paragraph_format.space_before = Pt(0)
            self._runs(h, f"{self._n1}. {nadpis_kapitoly}" if self.cislovat else nadpis_kapitoly)
            vyska -= 1.6
        from PIL import Image
        with Image.open(cesta) as im:
            pomer = im.height / im.width
        sirka_obr = min(sirka, vyska / pomer)
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.add_run().add_picture(cesta, width=Cm(sirka_obr))
        self._rezim = "graf"

    # ------------------------------------------------------------ tabulky
    def _tabulka(self, data: list[list[str]], tucny_radek0=True, tucny_sloupec0=False,
                 sirky_cm: Sequence[float] | None = None, velikost=10.5, podbarvit=True,
                 zvyraznene: set | None = None, zarovnat_vlevo=False, velikost_hlavicky=None):
        self._priprav()
        rows, cols = len(data), max(len(r) for r in data)
        if cols > 14 and velikost > 9:
            velikost = 9 if cols <= 24 else 8          # hodně sloupců -> menší písmo (CV1: 9 pt)
        t = self.doc.add_table(rows=rows, cols=cols)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        if cols > 8:  # široká tabulka přes celou šířku textu
            tblPr = t._tbl.tblPr
            for old in tblPr.findall(qn("w:tblW")):
                tblPr.remove(old)
            tw = OxmlElement("w:tblW"); tw.set(qn("w:w"), "5000"); tw.set(qn("w:type"), "pct"); tblPr.append(tw)
        zvyraznene = zvyraznene or set()
        for i, r in enumerate(data):
            for j in range(cols):
                v = r[j] if j < len(r) else ""
                c = t.cell(i, j)
                p = c.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT if zarovnat_vlevo else WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                hlav = (tucny_radek0 and i == 0) or (tucny_sloupec0 and j == 0)
                zv = (i, j) in zvyraznene
                vel = velikost_hlavicky if (velikost_hlavicky and tucny_radek0 and i == 0) else velikost
                self._runs(p, str(v), bold=(hlav and not velikost_hlavicky) or zv, size=Pt(vel))
                if podbarvit and hlav and str(v).strip():
                    _shd(c, PODBARVENI_HLAVICKY)
                if zv:
                    _shd(c, PODBARVENI_VYZNACENI)
        sec = self.doc.sections[-1]
        k = (sec.page_width - sec.left_margin - sec.right_margin) / 360000  # šířka textu v cm
        if not sirky_cm and cols > 8:
            # široká tabulka: úzké okraje buněk, 1. sloupec podle popisku, zbytek rovnoměrně
            mar = OxmlElement("w:tblCellMar")
            for strana in ("left", "right"):
                e = OxmlElement(f"w:{strana}"); e.set(qn("w:w"), "40"); e.set(qn("w:type"), "dxa"); mar.append(e)
            t._tbl.tblPr.append(mar)
            delka = max(len(re.sub(r"[_^{}*$]", "", str(r[0]))) for r in data)
            prvni = min(3.0, max(1.2, 0.02 * velikost * delka + 0.3))
            zbytek = (k - prvni) / (cols - 1)
            sirky_cm = [prvni] + [zbytek] * (cols - 1)
            lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); t._tbl.tblPr.append(lay)
        elif not sirky_cm:
            # malá tabulka: kompaktní šířka (jako v CV1), ne přes celou stránku
            delky = [max(len(re.sub(r"[_^{}*$]", "", str(r[j] if j < len(r) else ""))) for r in data) for j in range(cols)]
            sirky_cm = [min(6.0, max(1.6, 0.022 * velikost * d + 0.6)) for d in delky]
            if sum(sirky_cm) > k:
                sirky_cm = [w * k / sum(sirky_cm) for w in sirky_cm]
            t.autofit = False
        if sirky_cm:
            grid = t._tbl.tblGrid
            for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
                if j < len(sirky_cm):
                    gc.set(qn("w:w"), str(int(sirky_cm[j] * 567)))
            for j, w in enumerate(sirky_cm):
                for i in range(rows):
                    t.cell(i, j).width = Cm(w)
        if tucny_radek0:
            trPr = t.rows[0]._tr.get_or_add_trPr()
            h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)
        mez = self.doc.add_paragraph()
        mez.paragraph_format.space_after = Pt(2)
        return t

    def pristroje(self, radky: Sequence[Sequence[str]]):
        """Tabulka použitých přístrojů (5 sloupců). Chybějící evid. číslo -> '[[DOPLNIT: evid. č.]]'."""
        data = [PRISTROJE_HLAVICKA] + [list(r) + [""] * (5 - len(r)) for r in radky]
        return self._tabulka(data, tucny_radek0=True, sirky_cm=PRISTROJE_SIRKY_CM, velikost=11,
                             podbarvit=False, zarovnat_vlevo=True, velikost_hlavicky=12)

    def tabulka(self, nazev: str | None, data: dict | Sequence[Sequence], orientace: str = "vodorovne",
                des: int | Sequence[int] | dict | None = 2, max_sloupcu: int = 16, velikost: float = 10.5,
                podminky: str | None = None, vyznacit: dict | None = None, cislovat: bool = True):
        """Tabulka naměřených/vypočítaných hodnot ve stylu CV1.

        nazev:     popisek nad tabulkou – CO a NA ČEM se měřilo (součástka + parametry);
                   automaticky očíslovaný „1) …“, tučně 10 pt.
        podminky:  drobný text za názvem (9 pt), např. "I = konst. = 15 mA,  Z = U / I".
        data:      dict {"U_{0} [V]": [..], ...} (veličina i s jednotkou v [ ]) nebo seznam řádků
                   včetně hlavičky.
        orientace: "vodorovne" = veličiny v řádcích (1. sloupec podbarvený), dlouhé řady se zalomí
                   po `max_sloupcu`; "svisle" = veličiny ve sloupcích (podbarvená hlavička).
        des:       desetinná místa – číslo, seznam podle veličin nebo dict {klíč: des}.
        vyznacit:  {klíč veličiny: [indexy hodnot]} -> oranžově podbarvené a tučné (rezonance, max…).
        Široké tabulky: před nimi p.na_sirku() (jako v CV1), max_sloupcu ~ 30.
        """
        if nazev:
            self._ntab += 1
            p = self.popisek(f"{self._ntab}) {nazev}" if cislovat else nazev, velikost=10)
            if podminky:
                r = p.add_run("    ")
                self._runs(p, podminky, size=Pt(9))
        vyznacit = vyznacit or {}
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
                vse, zv = [], set()
                for a, b in kusy:
                    for k, s in zip(klice, sloupce):
                        for idx in vyznacit.get(k, []):
                            if a <= idx < b:
                                zv.add((len(vse), idx - a + 1))
                        vse.append([k] + s[a:b] + [""] * ((max_sloupcu - (b - a)) if len(kusy) > 1 else 0))
                    if (a, b) != kusy[-1]:
                        vse.append([""] * len(vse[-1]))
                return self._tabulka(vse, tucny_radek0=False, tucny_sloupec0=True, velikost=velikost,
                                     zvyraznene=zv)
            data2 = [klice] + [list(r) for r in zip(*sloupce)]
            zv = {(idx + 1, j) for j, k in enumerate(klice) for idx in vyznacit.get(k, [])}
            return self._tabulka(data2, tucny_radek0=True, velikost=velikost, zvyraznene=zv)
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
    """Vrátí seznam elementů m:oMath (v pořadí) pro zadané LaTeX rovnice."""
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
    vysl, akt = {}, None
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
