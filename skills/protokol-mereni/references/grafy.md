# Grafy – `scripts/graf.py`

## Rychlý start

```python
import sys; sys.path.insert(0, SKILL + "/scripts")
from graf import graf, sloupcovy

info = graf(
    "g01_zatezovaci.png",
    nazev="Zatěžovací charakteristika stabilizátoru L200\n"
          "U_inMAX = 40 V, U_out = 3–36 V, I_MAX = 0,4 A",
    osa_x="I [mA]", osa_y="U_2 [V]",
    rady=[dict(x=I, y=U, popis="naměřené hodnoty", prolozeni="primka")],
    kota=dict(rada=0, dx="ΔI", dy="ΔU"),     # okótuje přes celý rozsah
)
Ri = abs(info[0]["kota"]["pomer"])            # ΔU/ΔI z proložené přímky (pozor na jednotky os!)
```

Pak v dokumentu: `p.graf("g01_zatezovaci.png")` – graf dostane vlastní stranu na šířku.

## Volba proložení (`prolozeni=`)

| Průběh | Volba | Příklad |
|---|---|---|
| lineární závislost, určení směrnice (Ri, R) | `"primka"` | zatěžovací char., Isc = f(E), U = f(I) rezistoru |
| hladká nelineární křivka | `"hladka"` (vyhlazovací spline) | VA char. FV panelu, magnetizační křivka, L = f(I) |
| parabola / kubika | `"poly2"`, `"poly3"` | výkonová char. P = f(U) s maximem |
| exponenciála | `"exp"` (vrací `tau`) | vybíjení kondenzátoru U = f(t) |
| body spojit lomenou čarou | `"spojnice"` | jen když to dává smysl (časové průběhy z přístroje) |
| jen body | `None` | |

- Pokud fit zjevně nesedí (oscilace splinu, přestřelení na koncích), zkus jiný typ nebo rozděl
  data (např. stabilizační charakteristika = dvě oblasti → dvě řady/dvě přímky).
- Kóta: `kota=dict(rada=0, x1=..., x2=...)` pro výběr lineární části; výchozí je celý rozsah
  (připomínka vyučujícího: **ΔU/ΔI okótovat přes celý rozsah** proložené přímky).
- Hodnoty z kóty (`info[i]["kota"]` → `dx`, `dy`, `pomer`) použij v Příkladu výpočtu, ať sedí s grafem.

## Pravidla (vyplývají ze Zásad a prezentace)

- Název grafu: *charakteristika* + *součástka/zapojení* + *parametry* (typ, jmenovité hodnoty,
  podmínky – f, C0, osvětlení …). Delší název zalom `\n`.
- Osy `veličina [jednotka]` – indexy piš `U_0`, `I_{SC}`; skript je převede na matematický zápis.
- Více řad: každá má `popis` do legendy (parametr řady, např. „C0 = 8 mF“); skript automaticky
  střídá značky (×, ○, △, □) a styly čar (plná, čárkovaná, čerchovaná) → čitelné v ČB.
- Barevně jen pokud to Matyáš chce: `barevne=True`.
- Druhá osa (např. P k VA charakteristice): `osa_y2=dict(osa="P [mW]", rady=[...])`.
- Jmenovitá hodnota / tolerance: `vyznacit=[dict(y=2.2, text="jmenovitá hodnota 2,2 µF")]`,
  pro sloupcové grafy `sloupcovy(..., jmenovita=..., tolerance_pct=...)`.
- Logaritmická osa: `xlog=True` (kmitočtové charakteristiky, osvětlení přes řády).
- Jedna stránka = jeden graf. Charakteristiky pro více parametrů buď do jednoho grafu (víc řad),
  nebo každý zvlášť – podle toho, co zadání žádá („v jednom grafu“ / „v samostatném grafu“).

## Kontrola grafu před vložením

Po vygenerování si PNG **otevři a prohlédni** (Read): je název celý, nepřekrývají se popisky kót
s osami/body, jsou body vidět, sedí proložení, jsou jednotky správně? Teprve pak vkládej.
