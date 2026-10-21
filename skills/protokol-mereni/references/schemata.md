# Schémata zapojení – `scripts/schema.py` (schemdraw)

Instalace, pokud chybí: `pip install schemdraw` (případně `--break-system-packages`).

## Základ

```python
import sys; sys.path.insert(0, SKILL + "/scripts")
from schema import novy, ulozit, Meter, Wattmetr, Osciloskop, elm

d = novy()                                   # IEC styl, černobíle, unit = 3
d += (zdroj := elm.SourceSin().up().label("RAT", loc="left"))
d += elm.Line().right(1)
d += Meter("A").right().label("A", loc="top")
d += (u1 := elm.Dot())
d += elm.ResistorIEC().right().label("Rz1")
d += (u2 := elm.Dot())
d.push()
d += Meter("V").down().label("V1", loc="bottom")
d.pop()
d += elm.Line().right(2)
d += elm.Capacitor().down().label("C0")
d += elm.Line().left().tox(zdroj.start)
ulozit(d, "s01_va.png")
```

Pak v dokumentu: `p.schema("s01_va.png", "Schéma pro měření VA metodou", sirka_cm=14)`.

## Značky podle normy (ČSN EN 60617)

| Prvek | schemdraw |
|---|---|
| rezistor | `elm.ResistorIEC()` (obdélník) |
| reostat / potenciometr / odporová dekáda | `elm.ResistorVarIEC()` / `elm.PotentiometerIEC()` |
| kondenzátor, elektrolytický | `elm.Capacitor()`, `elm.Capacitor(polar=True)` |
| cívka, tlumivka (s jádrem) | `elm.Inductor2()` (+ `elm.Line` nad ní pro jádro) / `elm.Inductor()` |
| dioda, Zenerova, LED, fotodioda | `elm.Diode()`, `elm.Zener()`, `elm.LED()`, `elm.Photodiode()` |
| tranzistor | `elm.BjtNpn()`, `elm.BjtPnp()` |
| zdroj střídavý / stejnosměrný / baterie | `elm.SourceSin()`, `elm.SourceV()`, `elm.Battery()` |
| transformátor | `elm.Transformer(t1=4, t2=4)` |
| regulační autotransformátor (RAT) | `elm.SourceSin()` s popiskem „RAT“ nebo `elm.Transformer` + šipka |
| usměrňovací můstek | `elm.Rectifier()` |
| žárovka / světelný zdroj | `elm.Lamp()` |
| FV článek/panel | `elm.Solar()` |
| motor | `elm.Motor()` |
| spínač | `elm.Switch()` |
| voltmetr / ampérmetr / ohmmetr / frekvenciometr | `Meter("V")`, `Meter("A")`, `Meter("Ω")`, `Meter("Hz")` |
| wattmetr | `Wattmetr()` – kotvy `i1`, `i2` (proudová cesta), `u` (napěťová cesta) |
| osciloskop / nulový indikátor | `Osciloskop()` (obdélník se sinusovkou) |
| uzel | `elm.Dot()`, svorka `elm.Dot(open=True)` |
| zem | `elm.Ground()` |

## Zásady kreslení

- Pravoúhlé vedení, uzly (tečky) jen na skutečných odbočeních, žádné křížení bez nutnosti.
- Popisky = označení z tabulky přístrojů (V1, V2, A, W, Rz, RAT, OSC, Cx, Rd, Ld, FVP…), případně
  s hodnotou („C0 = 4 mF“).
- Napájení vlevo, zátěž/měřený objekt vpravo, měřicí přístroje tak, jak byly skutečně zapojeny
  (ampérmetr před/za voltmetrem – u VA metody to rozhoduje o metodické chybě!).
- Kreslíš-li úpravu podle schématu ze zadání, **překresli ho celé po svém** (nekopírovat obrázek).
- Po uložení PNG otevři (Read) a zkontroluj, že nic nevisí, popisky se nepřekrývají a vodiče jsou spojené.

## Užitečné triky

- `d.push()` / `d.pop()` – uložit/vrátit pozici (odbočky).
- `.tox(prvek.start)`, `.toy(...)` – dotáhnout vodič na souřadnici jiného prvku.
- `.at(prvek.end)` – začít kreslit od kotvy.
- `.label("text", loc="top"|"bottom"|"left"|"right")`, víc řádků přes `\n`.
- `elm.Line().length(1.5)` / `.right(1.5)` – délka úseku.
- Můstky: `elm.Wheatstone()` nebo kreslit ručně kosočtverec přes `.theta(45)`.
