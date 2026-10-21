"""
graf.py – grafy do protokolu podle Zásad a připomínek vyučujících.

Pravidla, která skript dodržuje sám:
  * jeden graf = jedna strana A4 na šířku (poměr stran odpovídá ploše stránky),
  * název grafu nahoře (musí obsahovat součástku/obvod a její parametry),
  * osy: veličina [jednotka], desetinná čárka,
  * hustá mřížka (hlavní + vedlejší rastr), čitelná i po černobílém tisku,
  * naměřené body jako výrazné značky (křížky, kolečka …), proložení hladkou křivkou/přímkou,
  * řady rozlišitelné i černobíle (různé značky + styl čáry),
  * legenda pod grafem,
  * volitelně okótovaný trojúhelník ΔU/ΔI přes celý (lineární) rozsah -> vnitřní odpor apod.

Použití:
    from graf import graf
    vys = graf("graf1.png",
        nazev="Zatěžovací charakteristika usměrňovače (Graetzův můstek KY718, C0 = 4 mF)",
        osa_x="I_0 [A]", osa_y="U_0 [V]",
        rady=[dict(x=I, y=U, popis="C0 = 4 mF", prolozeni="primka")],
        kota=dict(rada=0, dx="ΔI", dy="ΔU"))
    print(vys[0]["smernice"])   # ΔU/ΔI z proložené přímky

prolozeni: "primka" | "poly2" | "poly3" | "hladka" (vyhlazovací spline) | "exp" | "spojnice" | None
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import ticker

# A4 na šířku minus okraje 2,5 cm -> 24,7 x 16 cm (ponecháme rezervu na záhlaví)
FIGSIZE = (24.7 / 2.54, 15.4 / 2.54)
ZNACKY = ["x", "o", "^", "s", "D", "v", "+", "*"]
ZNACKY_BAREVNE = ["x", "x", "x", "o", "^", "s", "D", "v"]   # CV1: naměřené body křížky
CARY = ["-", "--", "-.", ":", (0, (5, 1, 1, 1)), (0, (3, 1, 1, 1, 1, 1))]
BARVY_BW = ["black"] * 8
# paleta podle CV1: modrá (hlavní řada), oranžová, zelená, červená …
BARVY = ["#1f5aa6", "#e67e22", "#27ae60", "#c0392b", "#7d3c98", "#117a65", "#5d6d7e", "#b7950b"]


def _tex(s: str) -> str:
    """'U_0 [V]' -> mathtext s indexem, ponechá jednotku v [ ]."""
    import re
    if "$" in s:
        return s
    m = re.match(r"^\s*([^\[]+?)\s*(\[.*\])?\s*$", s)
    if not m:
        return s
    vel, jed = m.group(1), m.group(2) or ""
    if re.fullmatch(r"[A-Za-zΔφωτηδ]+(_\{?[\w,]+\}?)?(\^\{?\w+\}?)?", vel.replace(" ", "")):
        vel = "$" + vel.replace("Δ", r"\Delta ").replace("φ", r"\varphi ") + "$"
    return f"{vel} {jed}".strip()


def _zaokr(v, plat=3):
    """Zaokrouhlí na `plat` platných číslic."""
    if v == 0:
        return 0
    from math import floor, log10
    return round(v, -int(floor(log10(abs(v)))) + plat - 1)


def _zalom(t, n=72):
    import textwrap
    return "\n".join(r for radek in t.split("\n") for r in (textwrap.wrap(radek, n, break_long_words=False) or [""]))


def _carka(x, pos=None):
    """Desetinná čárka a mezera jako oddělovač tisíců (1 000, 20 000) – jako v CV1."""
    if x == 0:
        return "0"
    if abs(x) >= 1000 and float(x).is_integer():
        return f"{int(x):,}".replace(",", "\u00a0")
    s = f"{x:.6g}"
    if "e" in s:
        s = f"{x:.3g}"
    return s.replace(".", ",")


def _fit(x, y, druh):
    x = np.asarray(x, float); y = np.asarray(y, float)
    o = np.argsort(x); x, y = x[o], y[o]
    xs = np.linspace(x.min(), x.max(), 400)
    info = {}
    if druh in ("primka", "lin"):
        k, q = np.polyfit(x, y, 1)
        ys = k * xs + q
        info.update(smernice=k, posun=q, f=lambda t, k=k, q=q: k * np.asarray(t) + q)
    elif druh in ("poly2", "poly3", "poly4"):
        c = np.polyfit(x, y, int(druh[-1]))
        ys = np.polyval(c, xs)
        info.update(koef=c, f=lambda t, c=c: np.polyval(c, t))
    elif druh == "exp":
        # y = A*exp(B*x) (+0)
        msk = y > 0
        B, lnA = np.polyfit(x[msk], np.log(y[msk]), 1)
        A = np.exp(lnA)
        ys = A * np.exp(B * xs)
        info.update(A=A, B=B, tau=(-1 / B if B != 0 else np.inf), f=lambda t, A=A, B=B: A * np.exp(B * np.asarray(t)))
    elif druh == "hladka":
        try:
            from scipy.interpolate import make_smoothing_spline
            # duplicitní x zprůměrovat
            ux, inv = np.unique(x, return_inverse=True)
            uy = np.bincount(inv, y) / np.bincount(inv)
            if len(ux) >= 5:
                spl = make_smoothing_spline(ux, uy)
                ys = spl(xs); info.update(f=spl)
            else:
                c = np.polyfit(ux, uy, min(2, len(ux) - 1)); ys = np.polyval(c, xs); info.update(f=lambda t, c=c: np.polyval(c, t))
        except Exception:
            c = np.polyfit(x, y, 3); ys = np.polyval(c, xs); info.update(f=lambda t, c=c: np.polyval(c, t))
    elif druh == "spojnice":
        xs, ys = x, y
        info.update(f=lambda t: np.interp(t, x, y))
    else:
        return None, None, info
    return xs, ys, info


def graf(soubor: str, nazev: str, osa_x: str, osa_y: str, rady: list[dict],
         xlog: bool = False, ylog: bool = False, xlim=None, ylim=None,
         kota: dict | None = None, barevne: bool = True, legenda: bool | None = None,
         vyznacit: list[dict] | None = None, osa_y2: dict | None = None, dpi: int = 200,
         body: list[dict] | None = None, pasmo: dict | None = None):
    """Vykreslí graf a uloží PNG. Vrací seznam info o proložení pro každou řadu.

    rady: [dict(x=[...], y=[...], popis="...", prolozeni="hladka", znacka=None, cara=None)]
    kota: dict(rada=0, x1=None, x2=None, dx="ΔI", dy="ΔU") – okótuje přírůstky na proložené
          přímce/křivce mezi x1 a x2 (výchozí = celý rozsah naměřených dat).
    vyznacit: [dict(y=…, text="jmenovitá hodnota", styl="--"), dict(x=…, text=…)] – vodorovné/svislé
          čáry (jmenovitá hodnota, tolerance …).
    osa_y2: dict(osa="P [W]", rady=[...]) – druhá osa y vpravo (např. výkon k VA charakteristice).
    body: [dict(x=…, y=…, text="f_s = 75 Hz\nZ_max = 28 Ω", barva="#c0392b", popis="rezonance")]
          – zvýrazněné body (velký křížek + popisek se šipkou), jako rezonance/jmenovitá hodnota v CV1.
    pasmo: dict(x1=…, x2=…, popis="rozsah dle výrobce 400–10 000 Hz") – šedě podbarvené pásmo.
    barevne: True = barvy jako v CV1 (výchozí); False = černobíle.
    """
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.titlesize": 14,
                         "axes.unicode_minus": False, "mathtext.default": "it"})
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=dpi)
    barvy = BARVY if barevne else BARVY_BW
    vysledky = []
    handles = []

    def kresli(axx, rr, offset=0):
        for i, r in enumerate(rr):
            j = i + offset
            x = np.asarray(r["x"], float); y = np.asarray(r["y"], float)
            zn = r.get("znacka", (ZNACKY_BAREVNE if barevne else ZNACKY)[j % len(ZNACKY)])
            ca = r.get("cara", CARY[j % len(CARY)])
            b = r.get("barva", barvy[j % len(barvy)])
            pop = r.get("popis", "")
            axx.plot(x, y, linestyle="none", marker=zn, markersize=7, markeredgewidth=1.6,
                     color=b, markerfacecolor="none" if zn in "osD^v" else b, zorder=3)
            xs, ys, info = _fit(x, y, r.get("prolozeni", "hladka"))
            if xs is not None:
                axx.plot(xs, ys, linestyle=ca, linewidth=1.4, color=b, zorder=2)
            h, = axx.plot([], [], linestyle=ca if xs is not None else "none", marker=zn, color=b,
                          markerfacecolor="none" if zn in "osD^v" else b, label=pop)
            if pop:
                handles.append(h)
            info["x"], info["y"] = x, y
            vysledky.append(info)

    kresli(ax, rady)
    ax2 = None
    if osa_y2:
        ax2 = ax.twinx()
        kresli(ax2, osa_y2["rady"], offset=len(rady))
        ax2.set_ylabel(_tex(osa_y2["osa"]))
        ax2.yaxis.set_major_formatter(ticker.FuncFormatter(_carka))

    if xlog: ax.set_xscale("log")
    if ylog: ax.set_yscale("log")
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    ax.set_title(_zalom(nazev), pad=12)
    ax.set_xlabel(_tex(osa_x)); ax.set_ylabel(_tex(osa_y))

    # rastr: hlavní + vedlejší, aby šlo odečíst libovolnou hodnotu
    for a, lg in ((ax.xaxis, xlog), (ax.yaxis, ylog)):
        if not lg:
            a.set_minor_locator(ticker.AutoMinorLocator(5))
            a.set_major_formatter(ticker.FuncFormatter(_carka))
        else:
            a.set_major_locator(ticker.LogLocator(base=10, subs=(1.0,)))
            a.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
            a.set_major_formatter(ticker.FuncFormatter(_carka))
            # popisky i na 2× a 5× dekády (200, 500, 2 000 …) jako v CV1
            a.set_minor_formatter(ticker.FuncFormatter(
                lambda v, pos: _carka(v) if round(v / 10 ** np.floor(np.log10(v)), 6) in (2.0, 5.0) else ""))
    ax.grid(which="major", color="0.55", linewidth=0.8)
    ax.grid(which="minor", color="0.82", linewidth=0.5)
    ax.set_axisbelow(True)

    for v in (vyznacit or []):
        st = v.get("styl", "--")
        if "y" in v:
            ax.axhline(v["y"], linestyle=st, color="0.2", linewidth=1.1)
            ax.annotate(v.get("text", ""), (ax.get_xlim()[0], v["y"]), xytext=(6, 4),
                        textcoords="offset points", fontsize=10)
        if "x" in v:
            ax.axvline(v["x"], linestyle=st, color="0.2", linewidth=1.1)
            ax.annotate(v.get("text", ""), (v["x"], ax.get_ylim()[1]), xytext=(4, -14),
                        textcoords="offset points", fontsize=10, rotation=0)

    if kota:
        info = vysledky[kota.get("rada", 0)]
        f = info.get("f")
        x = info["x"]
        x1 = kota.get("x1", float(np.min(x))); x2 = kota.get("x2", float(np.max(x)))
        y1, y2 = float(f(x1)), float(f(x2))
        arr = dict(arrowstyle="<|-|>", color="black", linewidth=1.2, shrinkA=0, shrinkB=0,
                   mutation_scale=12)
        # trojúhelník vždy POD křivkou: vodorovná odvěsna ve výšce min(y1, y2),
        # svislá odvěsna u toho konce, kde je křivka výš
        yh = min(y1, y2)
        xv = x2 if y2 >= y1 else x1
        ax.annotate("", (x2, yh), (x1, yh), arrowprops=arr)
        ax.annotate("", (xv, max(y1, y2)), (xv, yh), arrowprops=arr)
        pom = dict(color="black", linewidth=0.8, linestyle=":")
        ax.plot([x1, x1], [y1, yh], **pom); ax.plot([x2, x2], [y2, yh], **pom)
        ax.text((x1 + x2) / 2, yh, kota.get("dx", "Δx") + f" = {_carka(_zaokr(abs(x2 - x1)))}",
                ha="center", va="bottom", fontsize=11, bbox=dict(fc="white", ec="none", pad=1))
        ax.text(xv, (y1 + y2) / 2, "  " + kota.get("dy", "Δy") + f" = {_carka(_zaokr(abs(y2 - y1)))}  ",
                ha="right" if xv == x2 else "left", va="center", fontsize=11,
                bbox=dict(fc="white", ec="none", pad=1))
        info["kota"] = dict(x1=x1, x2=x2, y1=y1, y2=y2, dx=x2 - x1, dy=y2 - y1,
                            pomer=(y2 - y1) / (x2 - x1) if x2 != x1 else np.inf)

    if pasmo:
        h = ax.axvspan(pasmo["x1"], pasmo["x2"], color="0.5", alpha=0.10, zorder=0,
                       label=pasmo.get("popis", ""))
        if pasmo.get("popis"):
            handles.append(h)
    for bd in (body or []):
        b = bd.get("barva", "#c0392b")
        h, = ax.plot([bd["x"]], [bd["y"]], linestyle="none", marker="x", markersize=14,
                     markeredgewidth=3, color=b, zorder=5, label=bd.get("popis", ""))
        if bd.get("popis"):
            handles.append(h)
        if bd.get("text"):
            y0, y1 = ax.get_ylim()
            nahore = (bd["y"] - y0) / (y1 - y0) > 0.75
            ax.annotate(bd["text"], (bd["x"], bd["y"]), xytext=bd.get("posun", (30, -40) if nahore else (25, 20)),
                        textcoords="offset points", fontsize=11,
                        arrowprops=dict(arrowstyle="->", color="black", lw=1))

    if legenda is None:
        legenda = len(handles) > 0
    if legenda and handles:
        fig.legend(handles=handles, loc="lower center", ncol=min(4, len(handles)), frameon=True,
                   fontsize=10, bbox_to_anchor=(0.5, 0.0))
        fig.tight_layout(rect=(0, 0.07, 1, 1))
    else:
        fig.tight_layout()
    fig.savefig(soubor, dpi=dpi)
    plt.close(fig)
    return vysledky


def sloupcovy(soubor: str, nazev: str, kategorie: list[str], hodnoty: list[float], osa_y: str,
              jmenovita: float | None = None, tolerance_pct: float | None = None, ylim=None, dpi=200):
    """Sloupcový graf (např. porovnání metod). Jmenovitou hodnotu a toleranční pásmo vyznačí."""
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.titlesize": 14})
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=dpi)
    hat = ["", "//", "..", "xx", "\\\\", "--", "++", "oo"]
    for i, (k, v) in enumerate(zip(kategorie, hodnoty)):
        ax.bar(k, v, color="white", edgecolor="black", hatch=hat[i % len(hat)], linewidth=1.2)
        ax.annotate(_carka(round(v, 4)), (i, v), xytext=(0, 4), textcoords="offset points", ha="center")
    if jmenovita is not None:
        ax.axhline(jmenovita, color="black", linestyle="--", linewidth=1.2, label="jmenovitá hodnota")
        if tolerance_pct:
            d = jmenovita * tolerance_pct / 100
            ax.axhspan(jmenovita - d, jmenovita + d, color="0.85", zorder=0, label=f"tolerance ±{_carka(tolerance_pct)} %")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2)
    if ylim: ax.set_ylim(*ylim)
    ax.set_title(_zalom(nazev), pad=12); ax.set_ylabel(_tex(osa_y))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(_carka))
    ax.grid(axis="y", which="major", color="0.45", linewidth=0.8)
    ax.grid(axis="y", which="minor", color="0.75", linewidth=0.4)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(soubor, dpi=dpi)
    plt.close(fig)
