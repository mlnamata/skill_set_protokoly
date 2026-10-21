---
name: protokol-mereni
description: Sestaví kompletní protokol o měření (elaborát) VOŠ a SPŠE Plzeň jako Word .docx ze zadání a naměřených hodnot. Použij vždy, když Matyáš pošle zadání, naměřené hodnoty nebo napíše elaborát, elab, protokol, úloha č., CV12.
---

# Protokol o měření (elaborát) – VOŠ a SPŠE Plzeň

Cíl: ze **zadání + naměřených hodnot (+ seznamu přístrojů)** vyrobit hotový `.docx`, který projde
kontrolou vyučujícího napoprvé (Zásady školy: ≥ 90 % požadavků, jinak se vrací). Autor protokolu je
**Matyáš Mlnařík** (záhlaví každé strany). **Desky (titulní list) negeneruj** – dělá si je sám.
Komunikuj česky a stručně. Výstup = hotový soubor, ne návod.

**Pracovní režim:** nejdřív jedno kolo dotazů na vše nejasné (krok 1), potom celý protokol
najednou a kompletně – žádné průběžné dotazy, žádné „mám pokračovat?“, žádné rozpracované části.

## 0. Nástroje skillu (nejdřív)

Skripty a podrobná pravidla jsou v repu `https://github.com/mlnamata/skill_set_protokoly`
(složka `skills/protokol-mereni/`). Najdi je v tomto pořadí a cestu ulož do `SKILL`:

1. adresář tohoto SKILL.md, pokud obsahuje `scripts/protokol.py`;
2. jinak repo stáhni (vždy aktuální verzi – `pull`, pokud už existuje):
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
| `references/styl-a-struktura.md` | vždy – vzhled podle CV1, jak psát každou část, formát výpočtů, závěr |
| `references/vzory/CV1_Mlnarik_VZOR_STYLU.md` | vždy – **hlavní vzor vzhledu a stylu** (Matyášův CV1) |
| `references/grafy.md` | před tvorbou grafů |
| `references/schemata.md` | před kreslením schémat |
| `references/vzory/README.md` + nejbližší vzor | rozsah a hloubka podobné úlohy (nekopírovat text!) |
| `scripts/protokol.py` | sestavení .docx (styl CV1, číslované nadpisy, rovnice, tabulky, grafy na šířku, záhlaví/zápatí) |
| `scripts/graf.py` | grafy ve stylu CV1 (rastr, body, proložení, zvýrazněné body, kóty ΔU/ΔI, legenda dole) |
| `scripts/schema.py` | schémata v IEC značkách (schemdraw) + V/A/W/osciloskop |
| `scripts/kontrola.py` | závěrečná kontrola .docx proti Zásadám |

## Nejdůležitější pravidla (platí vždy)

- Pořadí částí (nadpis 1. úrovně, přesně takto): **Teoretický úvod → Schéma zapojení → Použité
  přístroje → Postup měření → Tabulky → Příklad výpočtu → Grafy → Závěr**.
- **Vzhled = Matyášův protokol CV1** (`references/vzory/CV1_Mlnarik_VZOR_STYLU.md`, originál v repu
  `podklady/elaboraty/CV1_Mlnarik_VZOR_STYLU.docx`): Calibri 11, černý text zarovnaný vlevo; nadpisy
  **černé, tučné, číslované** („1. Teoretický úvod“ 20 pt, „1.1 …“ 14 pt); **záhlaví: „Matyáš Mlnařík“
  vlevo, „4. P“ vpravo; číslo stránky vpravo dole**; klíčové pojmy a hodnoty v textu **tučně**.
  To vše dělá `protokol.py` – nepřebíjej ho vlastním formátováním.
- **Teoretický úvod** 2–3 strany *vlastními slovy*, pokrýt body „Uveďte“ z podkladů, vzorce jako
  rovnice s popisem veličin, odrážky s tučným pojmem na začátku, vlastní obrázky ideálních průběhů,
  na konci „Použitá literatura“.
- **Schéma** vlastní, značky podle ČSN EN 60617 (rezistor = obdélník, přístroj = kroužek s písmenem),
  označení prvků shodné s tabulkou přístrojů.
- **Použité přístroje**: tabulka `Označení ve schématu | Název, funkce | Typ, rozsah | Evidenční
  (výrobní) číslo | Poznámka` (`p.pristroje`). Evidenční čísla **nikdy nevymýšlej** – chybí-li,
  zeptej se v kroku 1.
- **Postup** v minulém čase („zapojili jsme…“), po bodech zadání, se skutečnými přístroji a odchylkami.
- **Tabulky** (kapitola na straně na šířku): popisek „1) co a na čem (součástka + parametry)“ +
  podmínky drobně, veličiny s jednotkami v `[ ]` na modrém podbarvení, vyznačené hodnoty (rezonance,
  maxima…) oranžově, rozumné zaokrouhlení, u nelineárních charakteristik ≥ 15 bodů.
- **Příklad výpočtu** pro každou požadovanou veličinu: tučný popisek → obecný vztah → popis veličin
  → dosazení na samostatném řádku → **tučný výsledek s jednotkou**.
- **Grafy** (kapitolu „Grafy“ vkládá `p.graf()` sám): každý sám na straně A4 na šířku; název nahoře
  se součástkou a parametry; osy `veličina [jednotka]`; hustý rastr; **barevně jako v CV1** – modré
  křížky naměřených bodů **proložené** modrou přímkou/hladkou křivkou, důležité body zvýrazněné
  velkým barevným křížkem s popiskem; další řady jinou barvou i stylem čáry; legenda pod grafem;
  Ri apod. z proložené přímky s **ΔU a ΔI okótovanými přes celý rozsah**; hodnoty potřebné pro
  výpočet v grafu vyznač.
- **Závěr** jen souvislý text ve větách (žádné odrážky/tabulky), s konkrétními čísly (důležité hodnoty
  tučně): porovnání s teorií z TÚ, porovnání metod/součástek, chyby měření a jejich příčiny,
  vhodnost přístrojů, splnění všech bodů zadání, co se nepovedlo a proč. Zakázané: „proběhlo dle
  očekávání“, „hodnoty odpovídají teoretickým předpokladům“ bez rozboru.
- **Nikdy nevymýšlej naměřené hodnoty, evidenční čísla ani výsledky.** Nekopíruj text ze vzorů ani z webu.
- **Žádná prázdná / žlutá místa k doplnění.** Hotový protokol nesmí obsahovat `[[DOPLNIT]]`, „???“,
  „doplnit“ ani nic podobného – všechno chybějící zjisti dotazem v kroku 1.
- Desetinná čárka, mezera před jednotkou, µ pro mikro, indexy jako indexy.

## Postup

### 1. Rozbor vstupů a VŠECHNY dotazy předem (jedno kolo)
Matyáš chce, aby se skill **zeptal na všechno nejasné ještě před začátkem tvorby** a pak už
protokol udělal **celý najednou, bez dalšího vyptávání a bez polotovarů**. Proto:

1. Přečti vše, co poslal (PDF/DOCX/fotky zadání, xlsx/csv/fotky tabulek ze sešitu, podklady).
   Vypiš si: číslo a název úlohy, předmět; měřené součástky a jejich **katalogové parametry**;
   **body zadání** (1, 2a …) – každý musí být v protokolu viditelně splněn; body „Uveďte“; co má
   obsahovat závěr a které grafy (osy, v jednom/samostatném grafu); naměřené hodnoty; přístroje
   s evid. čísly; účast (měřil / „NEMĚŘIL“).
2. Rychle si data zpracuj nanečisto (načti, spočítej hlavní veličiny, mrkni na průběhy), ať
   odhalíš problémy dřív, než začneš psát.
3. Sepiš **všechny** nejasnosti, které by mohly změnit obsah protokolu, a polož je **najednou
   v jedné zprávě** (nástroj AskUserQuestion, pokud je k dispozici – max. 4 otázky na volání,
   případně víc volání hned po sobě; jinak očíslovaný seznam). U každé otázky nabídni
   doporučenou možnost. Typicky se ptej na:
   - chybějící naměřené hodnoty nebo body zadání, ke kterým data nejsou (vynechat / dodá / jak),
   - chybějící evidenční čísla a typy/rozsahy přístrojů (ať je napíše; když přístroj číslo nemá,
     co tam uvést – např. „bez čísla“),
   - podmínky měření, které ze vstupů nevyplývají (zátěž, kmitočet, pevné napětí, teplota, zapojení
     přístrojů – ampérmetr před/za voltmetrem …),
   - podezřelé hodnoty: odlehlé body (vyřadit z proložení?), nesedící jednotky, záměna přístrojů
     (počet číslic neodpovídá přístroji), záporná znaménka,
   - interpretace sporných bodů zadání (které oblasti/rozsahy, v jednom či více grafech, co
     porovnat v závěru),
   - odchylky od zadání, které nastaly při měření (náhradní součástka, nezměřený bod) a jejich důvod,
   - chybějící přílohy (oscilogramy, fotky, printscreeny) – ať je pošle hned, nebo co s nimi
     (vynechat a v textu uvést proč),
   - datum měření, skupina, „NEMĚŘIL“ – jen pokud to ovlivní text.
   Neptej se na věci, které jsou ve vstupech nebo které má skill pevně dané (formát, styl,
   autor, třída, struktura) – na ty platí pravidla výše.
4. **Počkej na odpovědi.** Pak už se nevracej s dalšími otázkami a dodělej **kompletní** protokol
   (kroky 2–7) přesně podle odpovědí. **Nenechávej žádná žlutá/prázdná místa k doplnění** – na
   všechno, co chybí, se zeptej předem. Když Matyáš odpoví, že něco nemá (přístroj bez evid. čísla,
   nezměřený bod, chybějící oscilogram), napiš to do protokolu tak, jak řekl („bez čísla“, věta
   v závěru proč bod chybí …) – nic nevymýšlej a nic nenechávej otevřené. Pokud z odpovědí vyplyne
   další nutná nejasnost, polož ji hned v tom samém kole dotazů, ne až uprostřed tvorby.
5. Pokud je všechno jasné, neptej se a rovnou tvoř. Pokud Matyáš výslovně řekne „neptej se,
   udělej to“ nebo není k dispozici (naplánovaná úloha), zvol nejrozumnější výklad, použij ho
   a všechny předpoklady vypiš při předání (i tak bez žlutých míst v dokumentu).

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
Zvýrazněné body: `body=[dict(x=75, y=28, text="$f_s$ = 75 Hz", barva="#c0392b", popis="rezonance")]`,
pásmo: `pasmo=dict(x1=…, x2=…, popis="…")`. Černobíle jen na přání: `barevne=False`.
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
p = Protokol(autor="Matyáš Mlnařík", trida="4. P")      # nadpisy se číslují samy
p.h1("Teoretický úvod"); p.h2("…"); p.text("… **klíčový pojem** … U_{0} … $R_i$ …")
p.odrazky(["**Kmitočet f [Hz]** určuje výšku tónu; …"]); p.rovnice(r"R_i = \frac{\Delta U}{\Delta I}")
p.obrazek("ideal.png", 12, popisek="…"); p.h2("Použitá literatura"); p.odrazky(["…"])
p.h1("Schéma zapojení");  p.schema("s1.png", "Měření zatěžovací charakteristiky")
p.h1("Použité přístroje"); p.pristroje([["V1", "multimetr – voltmetr", "UNI-T UT804", "10-10-1862", ""]])
p.h1("Postup měření");    p.text("…")
p.h1("Tabulky", na_sirku=True)
p.tabulka("Stabilizační charakteristika L200 (U_{out} ≈ 4 V)", {"U_{1} [V]": U1, "U_{2} [V]": U2},
          des=3, podminky="naprázdno", vyznacit={"U_{2} [V]": [2]}, max_sloupcu=30)
p.h1("Příklad výpočtu")
p.vypocet("Výpočet vnitřního odporu L200:", r"R_i = \frac{\Delta U}{\Delta I}",
          [("$\\Delta U$", "změna výstupního napětí [V]"), ("$\\Delta I$", "změna proudu [A]")],
          r"R_i = \frac{0,557}{0,3676}", r"R_i = 1,52\ \Omega")
p.graf("g1.png")          # 1. graf vloží i kapitolu „Grafy“; každý graf = samostatná strana na šířku
p.h1("Závěr");            p.text("odstavec…\n\nodstavec…")
p.uloz("EM_CV16_Stabilizatory.docx")
```
Mini-markup: `**tučně**`, `*kurzíva*`, `X_{index}`, `X^{exp}`, `$LaTeX$`.
Rovnice v LaTeXu, desetinná čárka normálně „2,63“, jednotky `\ \Omega`, `\ \mathrm{V}`.
`p.tabulka(..., orientace="vodorovne"|"svisle", des=2 | [..] | {klíč: des}, podminky=…, vyznacit=…)`.

### 6. Kontrola
```bash
python3 "$SKILL/scripts/kontrola.py" EM_CV16_Stabilizatory.docx --nahled
```
Oprav vše ✘ (včetně případných žlutých/zástupných míst), zvaž „!“. Prohlédni náhled stran.
LibreOffice v náhledu **nezobrazí rovnice** (OMML) – ve Wordu jsou; obsah rovnic kontroluj z výpisu
skriptu. Projdi body zadání jeden po druhém.

### 7. Předání
Pošli .docx (`EM_CV<číslo>_<Úloha>.docx`) a stručně: co obsahuje a případné odchylky/předpoklady.
Připomeň jen desky a originál naměřených hodnot s podpisem.

## Další situace
- **Vrácený protokol s připomínkami**: oprav přesně připomínky, zbytek zachovej.
- **Ručně psaný protokol** (maturitní úlohy): stejný obsah jako podklad k přepsání; grafy jako
  předloha pro milimetrový papír.
- **Jen část** (graf, výpočet, závěr): dodrž stejná pravidla pro tu část.
