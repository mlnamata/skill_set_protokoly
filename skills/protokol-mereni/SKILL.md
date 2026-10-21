---
name: protokol-mereni
description: Sestaví kompletní protokol o měření (elaborát) z praktických cvičení VOŠ a SPŠE Plzeň (EM, ESO …) jako Word .docx – teoretický úvod, vlastní schémata podle normy, tabulku přístrojů, postup, tabulky, příklady výpočtu s rovnicemi Wordu, grafy přes celou A4 s proložením a závěr – jen ze zaslaného zadání a naměřených hodnot. Použij vždy, když Matyáš pošle zadání úlohy, naměřené hodnoty (xlsx, csv, fotka sešitu), podklady k měření nebo napíše elaborát, elab, protokol, vypracuj měření, CV12, úloha č., i když slovo protokol nepadne; také pro opravu vráceného protokolu a pro samostatné grafy, výpočty nebo závěr do protokolu.
---

# Protokol o měření (elaborát) – VOŠ a SPŠE Plzeň

Cíl: ze **zadání + naměřených hodnot (+ seznamu přístrojů)** vyrobit hotový `.docx`, který projde
kontrolou vyučujícího napoprvé (Zásady školy: ≥ 90 % požadavků, jinak se vrací). Autor protokolu je
**Matyáš Mlnařík** (záhlaví každé strany). **Desky (titulní list) negeneruj** – dělá si je sám.
Komunikuj česky a stručně. Výstup = hotový soubor, ne návod.

## 0. Nástroje skillu (nejdřív)

Skripty a podrobná pravidla jsou v repu `https://github.com/mlnamata/skill_set_protokoly`
(složka `skills/protokol-mereni/`). Najdi je v tomto pořadí a cestu ulož do `SKILL`:

1. adresář tohoto SKILL.md, pokud obsahuje `scripts/protokol.py`;
2. jinak repo stáhni:
   ```bash
   R=$HOME/skill_set_protokoly
   [ -d "$R/.git" ] && git -C "$R" pull -q || git clone -q --depth 1 https://github.com/mlnamata/skill_set_protokoly "$R"
   SKILL=$R/skills/protokol-mereni
   ```
   (bez gitu: `curl -L https://github.com/mlnamata/skill_set_protokoly/archive/refs/heads/main.zip -o s.zip && unzip -q s.zip`)
3. když síť nejde, pokračuj podle pravidel níže a docx sestav přímo přes python-docx + pandoc.

Závislosti: `pip install python-docx matplotlib numpy scipy schemdraw openpyxl`
(případně `--break-system-packages`) a `pandoc` (rovnice LaTeX → nativní rovnice Wordu;
alternativa `pip install pypandoc_binary`).

| Soubor v `$SKILL` | Kdy číst |
|---|---|
| `references/pravidla.md` | vždy – školní Zásady + co vyučující vrací |
| `references/styl-a-struktura.md` | vždy – jak psát každou část, formát výpočtů, závěr |
| `references/grafy.md` | před tvorbou grafů |
| `references/schemata.md` | před kreslením schémat |
| `references/vzory/README.md` + nejbližší vzor | rozsah a hloubka podobné úlohy (nekopírovat text!) |
| `scripts/protokol.py` | sestavení .docx (nadpisy, text, rovnice, tabulky, grafy na šířku, záhlaví) |
| `scripts/graf.py` | grafy podle pravidel (rastr, body, proložení, kóty ΔU/ΔI, legenda dole) |
| `scripts/schema.py` | schémata v IEC značkách (schemdraw) + V/A/W/osciloskop |
| `scripts/kontrola.py` | závěrečná kontrola .docx proti Zásadám |

## Nejdůležitější pravidla (platí vždy)

- Pořadí částí (nadpis 1. úrovně, přesně takto): **Teoretický úvod → Schéma zapojení → Použité
  přístroje → Postup měření → Tabulky → Příklad výpočtu → (grafy) → Závěr**.
- Každá strana: záhlaví „Matyáš Mlnařík“ vlevo, číslo stránky vpravo. A4, okraje 2,5 cm, Calibri 11.
- **Teoretický úvod** 2–3 strany *vlastními slovy*, pokrýt body „Uveďte“ z podkladů, vzorce jako
  rovnice s popisem veličin, vlastní obrázky ideálních průběhů, na konci „Použitá literatura“.
- **Schéma** vlastní, značky podle ČSN EN 60617 (rezistor = obdélník, přístroj = kroužek s písmenem),
  označení prvků shodné s tabulkou přístrojů.
- **Použité přístroje**: tabulka `OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ
  (VÝROBNÍ) ČÍSLO | POZNÁMKA`. Evidenční čísla **nikdy nevymýšlej** – chybí-li: `[[DOPLNIT: evid. č.]]`.
- **Postup** v minulém čase („zapojili jsme…“), po bodech zadání, se skutečnými přístroji a odchylkami.
- **Tabulky**: název říká co a na čem (součástka + parametry), jednotky v `[ ]`, rozumné zaokrouhlení,
  u nelineárních charakteristik ≥ 15 bodů.
- **Příklad výpočtu** pro každou požadovanou veličinu: obecný vztah → popis veličin → dosazení na
  samostatném řádku → **tučný výsledek s jednotkou**.
- **Grafy**: každý sám na straně A4 na šířku; název nahoře se součástkou a parametry; osy
  `veličina [jednotka]`; hustý rastr; body jako křížky/kolečka **proložené** přímkou/hladkou křivkou;
  řady rozlišitelné černobíle; legenda pod grafem; Ri apod. z proložené přímky s **ΔU a ΔI
  okótovanými přes celý rozsah**; hodnoty potřebné pro výpočet v grafu vyznač.
- **Závěr** jen souvislý text ve větách (žádné odrážky/tabulky), s konkrétními čísly: porovnání
  s teorií z TÚ, porovnání metod/součástek, chyby měření a jejich příčiny, vhodnost přístrojů,
  splnění všech bodů zadání, co se nepovedlo a proč. Zakázané: „proběhlo dle očekávání“,
  „hodnoty odpovídají teoretickým předpokladům“ bez rozboru.
- **Nikdy nevymýšlej naměřené hodnoty, evidenční čísla ani výsledky.** Nekopíruj text ze vzorů ani z webu.
- Desetinná čárka, mezera před jednotkou, µ pro mikro, indexy jako indexy.

## Postup

### 1. Sběr vstupů
Přečti vše, co Matyáš poslal (PDF/DOCX/fotky zadání, xlsx/csv/fotky tabulek ze sešitu, podklady).
Vypiš si: číslo a název úlohy, předmět; měřené součástky a jejich **katalogové parametry**; **body
zadání** (1, 2a …) – každý musí být v protokolu viditelně splněn; body „Uveďte“; co má obsahovat
závěr a které grafy (osy, v jednom/samostatném grafu); naměřené hodnoty; přístroje s evid. čísly;
případně „NEMĚŘIL“.
- Bez naměřených hodnot protokol nedokončuj – zeptej se (mezitím můžeš připravit TÚ, schémata, postup).
- Drobnosti, které chybí, dej jako `[[DOPLNIT: …]]` (žlutě) a vyjmenuj je na konci.
- Pokud Matyáš není k dispozici, zvol rozumný výklad zadání a napiš ho v odpovědi.

### 2. Výpočty v Pythonu
`vypocty.py`: načti data, spočítej vše požadované (numpy), zaokrouhli rozumně. Kontroluj věrohodnost
(řády, znaménka, porovnání s jmenovitými hodnotami). Stejná čísla pak používej v tabulkách,
výpočtech, grafech i závěru.

### 3. Grafy → `references/grafy.md`
```python
import sys; sys.path.insert(0, f"{SKILL}/scripts")
from graf import graf
info = graf("g1.png", nazev="Zatěžovací charakteristika stabilizátoru L200\nU_in = 20 V, I_MAX = 0,4 A",
            osa_x="I [mA]", osa_y="U_2 [V]",
            rady=[dict(x=I, y=U, popis="naměřené hodnoty", prolozeni="primka")],
            kota=dict(rada=0, dx="ΔI", dy="ΔU"))
ri = abs(info[0]["kota"]["pomer"])   # pozor na jednotky os
```
`prolozeni`: `primka` | `hladka` | `poly2` | `poly3` | `exp` | `spojnice` | `None`. Každé PNG si
prohlédni (Read) a oprav, co nesedí (překryvy, nevhodné proložení, useknutý název).

### 4. Schémata → `references/schemata.md`
```python
from schema import novy, ulozit, Meter, Wattmetr, Osciloskop, elm
d = novy(); d += elm.SourceV().up().label("Uz1", loc="left"); d += Meter("A").right().label("A") …
ulozit(d, "s1.png")
```
Každé měřicí zapojení zvlášť; PNG prohlédni.

### 5. Sestavení .docx
```python
from protokol import Protokol
p = Protokol(autor="Matyáš Mlnařík")
p.h1("Teoretický úvod"); p.h2("…"); p.text("… U_{0} … $R_i$ …"); p.rovnice(r"R_i = \frac{\Delta U}{\Delta I}")
p.obrazek("ideal.png", 12, popisek="…"); p.h2("Použitá literatura"); p.odrazky(["…"])
p.h1("Schéma zapojení");  p.schema("s1.png", "Měření zatěžovací charakteristiky")
p.h1("Použité přístroje"); p.pristroje([["V1", "multimetr – voltmetr", "UNI-T UT804", "10-10-1862", ""]])
p.h1("Postup měření");    p.text("…")
p.h1("Tabulky");          p.tabulka("Tabulka … (součástka + parametry)", {"U_{1} [V]": U1, "U_{2} [V]": U2}, des=3)
p.h1("Příklad výpočtu")
p.vypocet("Výpočet vnitřního odporu L200", r"R_i = \frac{\Delta U}{\Delta I}",
          [("$\\Delta U$", "změna výstupního napětí [V]"), ("$\\Delta I$", "změna proudu [A]")],
          r"R_i = \frac{0,557}{0,3676}", r"R_i = 1,52\ \Omega")
p.graf("g1.png")          # každý graf = samostatná strana na šířku
p.h1("Závěr");            p.text("odstavec…\n\nodstavec…")
p.uloz("EM_CV16_Stabilizatory.docx")
```
Mini-markup: `**tučně**`, `*kurzíva*`, `X_{index}`, `X^{exp}`, `$LaTeX$`, `[[DOPLNIT: …]]`.
Rovnice v LaTeXu, desetinná čárka normálně „2,63“, jednotky `\ \Omega`, `\ \mathrm{V}`.
`p.tabulka(..., orientace="vodorovne"|"svisle", des=2 | [..] | {klíč: des}, max_sloupcu=12)`.

### 6. Kontrola
```bash
python3 "$SKILL/scripts/kontrola.py" EM_CV16_Stabilizatory.docx --nahled
```
Oprav vše ✘, zvaž „!“. Prohlédni náhled stran. LibreOffice v náhledu **nezobrazí rovnice** (OMML) –
ve Wordu jsou; obsah rovnic kontroluj z výpisu skriptu. Projdi body zadání jeden po druhém.

### 7. Předání
Pošli .docx (`EM_CV<číslo>_<Úloha>.docx`) a stručně: co obsahuje, co doplnit (žlutá místa),
případné odchylky/předpoklady. Připomeň jen desky a originál naměřených hodnot s podpisem.

## Další situace
- **Vrácený protokol s připomínkami**: oprav přesně připomínky, zbytek zachovej.
- **Ručně psaný protokol** (maturitní úlohy): stejný obsah jako podklad k přepsání; grafy jako
  předloha pro milimetrový papír.
- **Jen část** (graf, výpočet, závěr): dodrž stejná pravidla pro tu část.
