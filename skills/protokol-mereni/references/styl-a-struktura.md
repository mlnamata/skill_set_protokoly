# Styl a struktura elaborátu (podle vzorových protokolů)

Vzorové protokoly jsou v `references/vzory/*.md` (text bez obrázků). Slouží **jen jako vzor
struktury, rozsahu a tónu** – text z nich nikdy nepřebírej doslova (plagiát, vyučující vzory znají).

## Obsah
1. Celkový vzhled dokumentu
2. Teoretický úvod
3. Schéma zapojení
4. Použité přístroje
5. Postup měření
6. Tabulky
7. Příklad výpočtu
8. Grafy
9. Závěr
10. Jazyk a typografie

---

## 1. Celkový vzhled dokumentu – podle Matyášova CV1 (`vzory/CV1_Mlnarik_VZOR_STYLU.md`)

Vše níže nastavuje `protokol.py` sám – jen ho nepřepisuj vlastním formátováním.

- A4 na výšku, okraje 2,5 cm, **Calibri 11 pt, černý text**, zarovnání **vlevo**, mezera za odstavcem 4 pt.
- **Záhlaví:** `Matyáš Mlnařík` vlevo, třída **`4. P`** vpravo. **Zápatí:** číslo stránky **vpravo dole**.
- **Nadpisy jsou černé a tučné, číslované:** H1 20 pt „1. Teoretický úvod“, H2 14 pt „1.1 Zvuk a jeho
  parametry“, H3 11 pt. Číslování dělá skript – do textu nadpisu čísla nepiš.
- Kapitoly (H1, přesně tyto názvy, skript je očísluje 1–8):
  `Teoretický úvod`, `Schéma zapojení`, `Použité přístroje`, `Postup měření`, `Tabulky`,
  `Příklad výpočtu`, `Grafy` (vloží `p.graf()` sám nad první graf), `Závěr`.
- V textu **tučně klíčové pojmy a důležité hodnoty** („**mechanické vlnění pružného prostředí**“,
  „**c ≈ 343 m/s**“), *kurzívou* typy/druhy. V teoretickém úvodu jsou vhodné **odrážky s tučným
  pojmem na začátku** („**Kmitočet f [Hz]** určuje výšku tónu; …“).
- Popisky obrázků kurzívou 10 pt pod obrázkem, bez „Obrázek N:“ (jako v CV1).
- **Tabulky**: kapitola „Tabulky“ na straně **na šířku** (`p.h1("Tabulky", na_sirku=True)`), nad každou
  tabulkou tučný popisek 10 pt „1) Impedance hloubkového reproduktoru ARN 5608“ + drobné podmínky
  9 pt („I = konst. = 15 mA, Z = U / I“). Popisky veličin (1. sloupec / hlavička) tučně na modrém
  podbarvení, **vyznačené hodnoty** (rezonance, maximum, jmenovitá hodnota) tučně na oranžovém
  podbarvení (`vyznacit=`), pod tabulkami případně řádek „**Vyznačeno:** …“.
- **Příklad výpočtu**: nadpis každého výpočtu jako tučný popisek 10 pt („Impedance hloubkového
  reproduktoru – rezonance (f = 75 Hz):“), pak rovnice.
- **Grafy** barevné jako v CV1: modrá proložená křivka s modrými křížky naměřených bodů, zvýrazněné
  body velkým červeným/zeleným/oranžovým křížkem s popiskem, šedé pásmo pro rozsah, legenda pod grafem.
- Desky (titulní list) **negeneruj** – Matyáš si je dělá sám.
- Typický rozsah hotového protokolu: 12–20 stran (z toho 2–3 strany TÚ, 1 strana na každý graf).

## 2. Teoretický úvod

Struktura (H2 pro každé téma):
1. Měřená součástka / obvod – co to je, k čemu slouží, z čeho se skládá, základní vztah.
2. Každá použitá metoda měření – princip, schéma principu, odvození/výsledný vztah, kdy se hodí,
   čím je zatížena chybou.
3. Očekávané průběhy charakteristik (ideální tvar křivky – nakresli si ho sám přes `graf.py`
   nebo matplotlib bez naměřených bodů, s popsanými osami) – na ně se pak odkazuje závěr.
4. Význam parametrů, které se mají určit (činitel stabilizace, vnitřní odpor, účiník, zvlnění…).
5. Na konci H2 **„Použitá literatura“** – konkrétní zdroje (učebnice, podklady k úloze, konkrétní URL).

Pravidla:
- Pokryj **všechny body „Uveďte“ z podkladů** a vše, co budou potřebovat body zadání.
- Vzorce jako rovnice (`p.rovnice`), za vzorcem věta „kde X je …, Y je …“.
- Vlastními slovy, věcně, srozumitelně pro spolužáka. Žádné vatové věty.
- Rozsah 2–3 strany textu + obrázky (~600–1100 slov).
- Obrázky s popiskem `Obrázek N: …` a u převzatých `zdroj: …`. Preferuj vlastní nakreslené obrázky
  (průběhy přes matplotlib, principiální schémata přes schemdraw) – nic nestahuj ani nekopíruj.

## 3. Schéma zapojení

- Každé měřicí zapojení zvlášť pod H2 („Schéma pro měření zatěžovací charakteristiky“ …).
- Vlastní schéma ze `schema.py` (schemdraw, IEC značky), označení prvků = sloupec „Označení ve
  schématu“ v tabulce přístrojů (V1, V2, A, W, RAT, Rz1, OSC, Cx, Ld …).
- Šířka obrázku 12–16 cm, centrovaně.

## 4. Použité přístroje

- `p.pristroje([...])` – řádky `[označení, název/funkce, typ + rozsah, evid. číslo, poznámka]`.
- Název/funkce = jak byl přístroj použit („digitální multimetr – voltmetr“, „odporová dekáda“).
- Typ, rozsah: výrobce a model + použitý rozsah / max. hodnoty („UNI-T UT804, rozsah 20 V“,
  „Pmax = 1 W“, „U2 = 0–230 V“).
- Evidenční číslo přesně podle zápisu z měření (formát školy např. `3207-1956`, `10-9-1861`,
  `9-5b-AL1680`, `T-25-19`). **Nikdy nevymýšlej** – chybí-li, zeptej se předem (krok 1 ve SKILL.md);
  žádná žlutá/prázdná místa v protokolu.

## 5. Postup měření

- Minulý čas, 1. osoba množného čísla („Zapojili jsme…“, „Na regulačním autotransformátoru jsme
  postupně zvyšovali napětí…“). Ve vzorech občas 1. os. j. č. – drž se jednoho čísla v celém textu.
- Člení se podle bodů zadání: H2 nebo úvod odstavce „K bodu 1 zadání – …“, případně číslovaný
  seznam `1) …`.
- Uvádět skutečné přístroje a hodnoty (nastavený rozsah, kmitočet, zvolený odpor, krok měření).
- Bezpečnostní a praktické poznámky (nepřekročit Imax, nejprve snížit napětí na nulu a pak odpojit…).
- **Odchylky od zadání** (jiný kondenzátor, nezměřený bod, náhradní metoda) uvést zde nebo v závěru.

## 6. Tabulky

- Každá tabulka má výstižný popisek (skript ho očísluje „1)“): *„Zatěžovací charakteristika
  usměrňovače z diod KY718, C0 = 4 mF“*, *„Vybíjení kondenzátoru Cx = 330 µF“*; podmínky měření
  do `podminky=`.
- Veličina + jednotka v hranatých závorkách: `U_{0} [V]`, `I [mA]`, `Lx [mH]`, `cos φ [-]`.
- Vzory používají **vodorovné tabulky** (veličiny v řádcích, hodnoty ve sloupcích), dlouhé řady
  zalomené do více bloků → `p.tabulka(..., orientace="vodorovne", max_sloupcu=10–12)`.
  Krátké tabulky parametrů (τ, R, Cx0) svisle jako dvojice veličina–hodnota.
- Počet desetinných míst podle přesnosti přístroje (naměřené jak je naměřil přístroj, vypočítané
  rozumně – zpravidla 2–3 platné číslice navíc nepřidávat).
- Vypočítané veličiny dej do stejné tabulky jako řádky navíc (vzory: U, I, P, L v jedné tabulce)
  nebo do samostatné tabulky „vypočítané hodnoty“.
- U nelineární charakteristiky zkontroluj ≥ 15 bodů; když jich je méně, uveď důvod v závěru.

## 7. Příklad výpočtu

Formát každého výpočtu (Matyášova preference) – `p.vypocet(...)`:
1. tučný popisek „Výpočet …:“ (co a pro jakou hodnotu, např. „Činitel zvlnění pro C0 = 4 mF, I = 2,2 A:“),
2. **obecný vztah**,
3. **popis veličin** („kde ΔU … změna napětí [V], ΔI … změna proudu [A]“),
4. **dosazení** na samostatném řádku (číselné hodnoty z tabulek, s mocninami 10 místo předpon:
   `\frac{3,5\cdot 10^{-3}}{2,64\cdot 10^{-3}}`),
5. **tučný výsledek s jednotkou**.

- Ukázat výpočet **každé** požadované veličiny alespoň jednou (pro jeden řádek tabulky); u řady
  stejných výpočtů stačí jeden vzorový + věta, že ostatní jsou v tabulce.
- Průměr: obecně `\bar{X} = \frac{\sum X_n}{k}` a výsledek.
- Hodnoty odečtené z grafu (ΔU, ΔI z kóty) dosazuj přesně ty, které jsou v grafu.

## 8. Grafy

Viz `references/grafy.md`. Shrnutí: jeden graf = jedna strana na šířku, název nahoře se součástkou
a parametry, rastr, body + proložení, ČB rozlišitelné řady, legenda pod grafem, kóty ΔU/ΔI přes celý
rozsah, vyznačená jmenovitá hodnota/tolerance tam, kde dává smysl.

## 9. Závěr

**Jen souvislý text ve větách** – žádné odrážky, tabulky ani rovnice na samostatných řádcích.
Odstavce (typicky 5–8) v tomto sledu:
1. Co se měřilo a jak (jednou větou), případně odchylky od zadání a proč.
2. Hlavní výsledky **s čísly** (hodnoty parametrů, porovnání metod, procentní odchylka od jmenovité
   hodnoty/tolerance).
3. **Porovnání s teorií** z teoretického úvodu – tvar charakteristik, trend, fyzikální vysvětlení.
4. Chyby měření a jejich příčiny (třída přesnosti, vnitřní odpor přístrojů, tolerance dekád,
   oteplení, nestabilní síť…), vhodnost použitých přístrojů a metod.
5. Odpovědi na vše, co zadání výslovně žádá „v závěru porovnejte/zhodnoťte…“.
6. Co se nepovedlo / co nebylo změřeno a proč (upřímně).
7. Případně doporučení (která metoda je nejpřesnější/nejrychlejší).

Zakázané: „Měření probíhalo dle očekávání.“, „Hodnoty odpovídají teoretickým předpokladům.“ bez
konkrétního rozboru.

## 10. Jazyk a typografie

- Spisovná čeština, odborné termíny správně (indukčnost, ne „indukce“, když jde o L; „zvlnění“,
  „činitel stabilizace“, „vnitřní odpor“). Vzory obsahují překlepy – neopakuj je.
- Desetinná čárka (2,63), mezera mezi číslem a jednotkou (2,63 Ω), znaménko krát `·`/`\cdot`.
- Indexy jako indexy (`U_{0}`, `I_{SC}`), ne „U0“ v běžném textu – mini-markup `X_{..}`.
- Předpony jednotek: mA, µF, kΩ, mH; `µ` je mikro (ne „u“).
