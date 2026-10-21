---
name: protokol-mereni
description: Sestaví kompletní protokol o měření (elaborát) z praktických cvičení VOŠ a SPŠE Plzeň (předměty EM, ESO …) jako Word .docx – teoretický úvod, vlastní schémata podle normy, tabulku přístrojů, postup, tabulky, příklady výpočtu s rovnicemi Wordu, grafy přes celou A4 s proložením a závěr – jen ze zaslaného zadání a naměřených hodnot. Použij vždy, když Matyáš pošle zadání úlohy, tabulku/fotku naměřených hodnot, podklady k měření nebo napíše „elaborát“, „protokol“, „elab“, „vypracuj měření“, „CV12“, „úloha č.“, i když neřekne slovo protokol; také pro opravy vráceného protokolu a pro samostatné grafy či výpočty do protokolu.
---

# Protokol o měření (elaborát) – VOŠ a SPŠE Plzeň

Cíl: z **zadání + naměřených hodnot (+ seznamu přístrojů)** vyrobit hotový `.docx`, který projde
kontrolou vyučujícího napoprvé (Zásady: ≥ 90 % požadavků, jinak se vrací). Autor protokolu je
**Matyáš Mlnařík** (záhlaví každé strany). **Desky (titulní list) negeneruj** – dělá si je sám.

Komunikuj česky a stručně. Výstup = hotový soubor, ne návod.

## Co je ve skillu

| Soubor | Kdy číst |
|---|---|
| `references/pravidla.md` | vždy na začátku – školní Zásady + co vyučující vrací |
| `references/styl-a-struktura.md` | vždy – jak psát každou část, formát výpočtů, závěr |
| `references/grafy.md` | před tvorbou grafů |
| `references/schemata.md` | před kreslením schémat |
| `references/vzory/README.md` + nejbližší vzor | pro představu rozsahu a hloubky podobné úlohy |
| `scripts/protokol.py` | knihovna pro sestavení .docx (nadpisy, text, rovnice LaTeX → Word, tabulky, grafy na šířku) |
| `scripts/graf.py` | grafy podle pravidel (rastr, body, proložení, kóty ΔU/ΔI, legenda dole) |
| `scripts/schema.py` | schémata v IEC značkách (schemdraw) + voltmetr/ampérmetr/wattmetr/osciloskop |
| `scripts/kontrola.py` | závěrečná kontrola .docx proti Zásadám |

`SKILL` níže = adresář tohoto skillu (kde leží tento SKILL.md).

## Postup

### 1. Sběr vstupů
Přečti vše, co Matyáš poslal (PDF/DOCX/fotky zadání, xlsx/csv/fotky tabulek ze sešitu, podklady
s body „Uveďte“). Vypiš si:
- číslo a název úlohy, předmět, měřené součástky a jejich **katalogové/jmenovité parametry**,
- **body zadání** (1, 2a, 2b …) – každý musí být v protokolu splněn (tabulka/graf/výpočet/věta v závěru),
- body „Uveďte“ → obsah teoretického úvodu,
- co má výslovně obsahovat **závěr** a které **grafy** (co na osách, v jednom/samostatném grafu),
- naměřené hodnoty (přepiš do Pythonu/CSV přesně, včetně jednotek),
- přístroje: označení, typ, rozsah, **evidenční čísla**, případně poznámka „NEMĚŘIL“.

Chybí-li něco podstatného (naměřené hodnoty, evid. čísla), **nic si nevymýšlej**:
- bez naměřených hodnot protokol nedělej – zeptej se (můžeš mezitím připravit TÚ, schémata, postup),
- chybějící evid. čísla / drobnosti dej jako `[[DOPLNIT: …]]` (žlutě) a na konci je vyjmenuj.
Nejasnosti v zadání vyřeš rozumným výkladem a zmiň ho v odpovědi.

### 2. Výpočty (Python, ne z hlavy)
Napiš skript `vypocty.py`: načti data, spočítej všechny požadované veličiny (numpy), zaokrouhli
rozumně. Kontroluj věrohodnost – porovnej s jmenovitými hodnotami, řády, znaménka (např. záporný
jalový výkon = otočené kleště → komentovat). Výsledky (včetně hodnot z kót grafů) používej
konzistentně v tabulkách, výpočtech i závěru.

### 3. Grafy → `references/grafy.md`
Pro každý graf, který zadání žádá: `graf.graf(...)` → PNG. Název se součástkou a parametry,
proložení (přímka / hladká křivka / exp), kóty ΔU/ΔI přes celý rozsah, kde se určuje odpor.
Každé PNG si prohlédni a oprav, co nesedí.

### 4. Schémata → `references/schemata.md`
Každé měřicí zapojení nakresli přes `schema.py`. Označení prvků = označení v tabulce přístrojů.
PNG prohlédni.

### 5. Text
Podle `references/styl-a-struktura.md`:
- **Teoretický úvod** 2–3 strany vlastními slovy, pokrýt body „Uveďte“, vzorce jako rovnice,
  vlastní obrázky ideálních průběhů, na konci „Použitá literatura“.
- **Postup měření** v minulém čase, po bodech zadání, se skutečnými přístroji a odchylkami.
- **Příklad výpočtu**: obecný vztah → popis veličin → dosazení → **tučný výsledek** (`p.vypocet`).
- **Závěr** jen v souvislých větách, s čísly, porovnání s teorií z TÚ, chyby měření, splnění bodů
  zadání, co se nepovedlo. Žádné „proběhlo dle očekávání“.

### 6. Sestavení .docx
Napiš `build.py`:

```python
import sys; sys.path.insert(0, f"{SKILL}/scripts")
from protokol import Protokol
p = Protokol(autor="Matyáš Mlnařík")

p.h1("Teoretický úvod")
p.h2("Usměrňovač"); p.text("…vlastní text s indexy U_{0}, $inline$ rovnicemi…")
p.rovnice(r"\varphi_{ZVL} = \frac{2\sqrt{2}\cdot U_{ZVL}}{U_0}\cdot 100\ [\%]")
p.obrazek("ideal.png", 12, popisek="Ideální zatěžovací charakteristika")
p.h2("Použitá literatura"); p.odrazky(["…"])

p.h1("Schéma zapojení");  p.schema("s1.png", "Měření zatěžovací charakteristiky")
p.h1("Použité přístroje"); p.pristroje([["RAT", "regulační autotransformátor", "0–250 V, 2,5 A", "3207-1956", ""], …])
p.h1("Postup měření");    p.text("…")
p.h1("Tabulky");          p.tabulka("Tabulka … (součástka + parametry)", {"U_{0} [V]": U, "I_{0} [mA]": I}, des={"U_{0} [V]": 2, "I_{0} [mA]": 1})
p.h1("Příklad výpočtu")
p.vypocet("Výpočet vnitřního odporu pro C0 = 4 mF", r"R_i = \frac{\Delta U}{\Delta I}",
          [("$\\Delta U$", "změna napětí odečtená z grafu [V]"), ("$\\Delta I$", "změna proudu [A]")],
          r"R_i = \frac{3,72}{1,14}", r"R_i = 3,26\ \Omega")
p.graf("g1.png")          # každý graf = samostatná strana na šířku
p.h1("Závěr");            p.text("…odstavce oddělené prázdným řádkem…")
p.uloz("EM_CVxx_Mlnarik.docx")
```

Mini-markup v textu: `**tučně**`, `*kurzíva*`, `X_{index}`, `X^{exp}`, `$LaTeX$`,
`[[DOPLNIT: …]]`. Rovnice v LaTeXu (`\frac`, `\sqrt`, `\Delta`, `\varphi`, `\cdot`, `\Omega`,
`\mu`, `\sum`); desetinná čárka normálně „2,63“. Jednotky v rovnicích jako `\ \Omega`, `\ \mathrm{V}`.

Závislosti: `python-docx`, `matplotlib`, `numpy`, `scipy`, `schemdraw`, `pandoc` (rovnice).
Chybí-li: `pip install python-docx matplotlib scipy schemdraw` (+ `--break-system-packages`),
pandoc přes `apt` nebo `pip install pypandoc_binary`.

### 7. Kontrola
```bash
python3 "$SKILL/scripts/kontrola.py" EM_CVxx_Mlnarik.docx --nahled
```
Oprav vše označené ✘, zvaž „!“. Prohlédni náhled stran (PNG). LibreOffice v náhledu **nezobrazí
rovnice** (OMML) – to je omezení náhledu, ve Wordu jsou; obsah rovnic kontroluj z výpisu skriptu.
Projdi body zadání jeden po druhém: je každý splněn a je to vidět?

### 8. Předání
Pošli .docx (název `EM_CV<číslo>_<úloha>.docx`) a stručně: co je v protokolu, co je potřeba
doplnit (žlutá místa), případné odchylky/nejistoty. Připomeň jen to, co skill nedělá: desky a
originál naměřených hodnot s podpisem vyučujícího.

## Zásady chování

- **Nikdy nevymýšlej naměřené hodnoty, evidenční čísla ani výsledky.** Jen počítej z dodaných dat.
- Text piš nově a vlastními slovy – žádné kopírování ze vzorů ani z webu (plagiát = 5).
- Konzistence: stejné označení veličin a přístrojů ve schématu, tabulkách, výpočtech, grafech i závěru.
- Když Matyáš pošle vrácený protokol s připomínkami, oprav přesně ty body a zbytek zachovej.
- Ručně zpracovávaný protokol (maturitní úlohy): připrav stejný obsah, ale upozorni, že grafy patří
  na milimetrový papír – grafy vygeneruj jako podklad pro překreslení.
