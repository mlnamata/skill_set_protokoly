"""
schema.py – kreslení schémat zapojení podle normy (IEC / ČSN EN 60617) přes schemdraw.

    pip install schemdraw   (pokud chybí)

    from schema import novy, ulozit, Meter, Wattmetr, elm
    d = novy()
    d += (src := elm.SourceSin().up().label("U~", loc="left"))
    d += elm.Line().right()
    d += Meter("A").right().label("A", loc="top")      # ampérmetr
    ...
    ulozit(d, "schema_va.png")

Pravidla pro schémata v protokolu:
  * vlastní nakreslené schéma, žádné kopie z internetu/zadání,
  * značky podle normy: rezistor = obdélník (ResistorIEC), potenciometr/reostat = PotentiometerIEC
    nebo ResistorVarIEC, měřicí přístroje = kroužek s písmenem (V, A, W, Hz, Ω),
  * každá součástka i přístroj má OZNAČENÍ, které je shodné se sloupcem
    „Označení ve schématu“ v tabulce použitých přístrojů (V1, A, Rz1, RAT, OSC …),
  * černobíle, čisté pravoúhlé vedení, uzly (tečky) na odbočeních.
"""
from __future__ import annotations

import schemdraw
import schemdraw.elements as elm
from schemdraw.segments import SegmentText, SegmentCircle, Segment

schemdraw.config(fontsize=13, lw=1.6, color="black")
try:
    elm.style(elm.STYLE_IEC)  # rezistory jako obdélníky
except Exception:
    pass


class Meter(elm.Source):
    """Měřicí přístroj = kroužek s písmenem: Meter('V'), Meter('A'), Meter('W'), Meter('Hz'), Meter('Ω')."""

    def __init__(self, pismeno: str = "V", **kwargs):
        super().__init__(**kwargs)
        self.segments.append(SegmentText((0.5, 0), pismeno, fontsize=13 if len(pismeno) == 1 else 10))


class Wattmetr(elm.Element):
    """Wattmetr: kroužek 'W' s proudovou cestou (vodorovně, svorky 'pin_i1','pin_i2')
    a napěťovou cestou (svorka 'pin_u' dole). Kotvy: i1, i2, u."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        r = 0.5
        self.segments.append(SegmentCircle((r, 0), r))
        self.segments.append(SegmentText((r, 0.05), "W"))
        self.segments.append(Segment([(0, 0), (-0.0, 0)]))
        self.segments.append(Segment([(r, -r), (r, -r - 0.4)]))
        self.anchors["i1"] = (0, 0)
        self.anchors["i2"] = (2 * r, 0)
        self.anchors["u"] = (r, -r - 0.4)
        self.anchors["start"] = (0, 0)
        self.anchors["end"] = (2 * r, 0)
        self.params["drop"] = (2 * r, 0)


class Osciloskop(elm.Element2Term):
    """Osciloskop / nulový indikátor: obdélník (stínítko) se sinusovkou – odlišný od zdroje
    střídavého napětí (kroužek se sinusovkou). Vstup mezi start a end."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        import numpy as np
        w, h = 1.2, 0.45
        gap = (float("nan"), float("nan"))
        self.segments.append(Segment([(0, 0), (0, h), (w, h), (w, -h), (0, -h), (0, 0), gap, (w, 0)]))
        t = np.linspace(0.15, w - 0.15, 60)
        self.segments.append(Segment(list(zip(t, 0.22 * np.sin((t - 0.15) / (w - 0.3) * 2 * np.pi)))))


def novy(unit: float = 3.0) -> schemdraw.Drawing:
    d = schemdraw.Drawing(show=False)
    d.config(unit=unit)
    return d


def ulozit(d: schemdraw.Drawing, soubor: str, dpi: int = 300):
    d.save(soubor, dpi=dpi)
    return soubor


__all__ = ["elm", "schemdraw", "novy", "ulozit", "Meter", "Wattmetr", "Osciloskop"]
