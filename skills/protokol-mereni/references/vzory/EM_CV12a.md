# Teoretický úvod

## Cívka

Cívka je součástka, která se používá hlavně v elektrotechnice a elektronice. Základ cívky tvoří vodič (nejčastěji měděný drát) navinutý do smyček. Když cívkou prochází elektrický proud, vytváří se kolem ní magnetické pole. Právě schopnost ukládat energii v magnetickém poli je jejím hlavním principem a důvodem, proč je tak důležitá v elektrických obvodech.

Cívky se využívají například v transformátorech, elektromotorech, reproduktorech nebo v rádiích. Často slouží k filtraci signálů, omezení změn proudu nebo k přeměně elektrické energie na magnetickou a zpět. Jejich vlastnosti závisí na počtu závitů, materiálu jádra a tvaru cívky. Díky tomu mohou mít velmi široké uplatnění jak v běžných spotřebičích, tak i v průmyslových zařízeních.

Její odpor narůstá s délkou vodiče.

Zde je vzorec pro výpočet statické indukčnosti cívky ve stejnosměrném obvodu

$$L = \frac{\mu N^{2}}{l}.S$$

Kde N je počet závitů. µ je permeabilita, l je aktivní délka cívky a S je průřez cívky.

Ve střídavých obvodech se cívka chová jako dolní propust (propouští nízké frekvence). Zde je vzorec pro indukci.

$$L = \frac{Xl}{\omega}$$

Kde Xl je reaktance cívky a ω je úhlová rychlost.

Mezi další důležitý vzorec patří indukované napětí.

$$ui = - L.\frac{dI}{dt}$$

Druhy cívek:

- Toroid

- Solenoid

- S jádrem

- Bez jádra

- 

## VA metoda

[obrázek]

Tato metoda využívá Ohmova zákona. Aby však byla možná změřit indukce, musíme znát stejnosměrný sériový odpor cívky (Rs). Poté platí vztah:

$$Lx = \frac{\sqrt{\frac{U^{2}}{I^{2}} - {Rs}^{2}}}{\omega}$$

## VAW metoda

[obrázek]

Tato metoda používá pro výpočet činný výkon P. Z tohoto výkonu se pak dá vypočíst fázový posun.

$$\varphi = arcos\left( \frac{P}{UI} \right)$$

Poté stačí jen dosadit do tohoto vzorce:

$$Lx = \frac{1}{\omega}.\frac{U}{I}.sin\varphi$$

## Rezonanční můstek

[obrázek]

Jedná se o druh můstku, který využívá rezonančního obvodu. Při rezonanční frekvenci se reaktance, a tedy i celková impedance vyrovná a poté se tento můstek chová jako klasický odporový můstek. Takže pro rovnováhu na můstku je tato rovnice.

$$R1.R3 = Z.R2$$

$$Z = \frac{R1}{R2}.R3$$

Neboli při rezonanční frekvenci f0 platí následující vztah:

$$Z = Xl = Xc = Rs$$

Z toho si pak můžeme vyjádřit neznámou indukčnost Lx:

$$Lx = \frac{1}{4\pi^{2}{f0}^{2}Cd}$$

Nejlépe můstková metoda funguje při poměru rezistorů R1 a R2 rovno 1. Tudíž budeme volit hodnoty rezistorů stejné. Před měřením bychom též měli nastavit hodnotu odporu R3 na hodnotu sériového odporu cívky, který si musíme naměřit před začátkem měření.

# Schéma zapojení

## VAW metoda-tlumivka

[obrázek]

## VA metoda

[obrázek]

## Rezonanční můstek

[obrázek]

## LRC metr

[obrázek]

# Použité přístroje

| OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA |
| LRC | APPA703 | f = 100 Hz – 100 kHz | 9-3B-AL1917 |  |
| RAT | Autotransformátor HSN 0203 Metex | U = 230 V; f = 50 Hz | 5-1957 |  |
| A | Ampérmetr Uni-T UT804 | δ = +-(0,025 % + 5 d) | 10-1954 |  |
| V | Voltmetr – Uni-T UT804 | δ = +-(0,025 % + 5 d) | 10-7 |  |
| W | Wattmetr Prova 21 | Umax = 600 V; Imax = 600 mA; Pmax = 999 W | 6-5-1941 |  |
| R1 | odporová dekáda | Pmax = 1 W | 3206-1-4b |  |
| R2 | odporová dekáda | Pmax = 1 W | 3206-1-4a |  |
| Cd | kapcitní dekáda | Pmax = 1 W | 9-6b-AL162 |  |
| NI | Osciloskop GoldStar OS-5020P | - | 3206-2-2b |  |
| R3 | odporová dekáda | P = 1 W | 9-5c-Al1624 |  |
| R0 | potenciometr | R = 2000 Ω | 3207-6c |  |

# Postup měření

K bodu 1 zadání – cívku jsme napájeli střídavým napětím ze sítě přes regulační autotransformátor Kmitočet jsme měli kontrolovat měřičem frekvence. Ale nakonec jsme neměřili, jelikož síť je velmi stabilní. Velikost nastavovaného proudu (15 hodnot) jsme ze začátku volili v jednotkách miliampér a postupně jsme hodnotu zvyšovali až skoro na 500 mA

K bodu 2b zadání – vzduchovou cívku jsme napájeli střídavým napětím ze sítě přes regulační autotransformátor (pozor na maximální dovolený proud cívky!!!). Před měřením jsme zkontrolovali ohmickou hodnotu odporu ohmetrem. Měření jsme provedli pro 3 různé hodnoty napětí a výslednou indukčnost jsme spočítali jako aritmetický průměr. Poté jsme připojili generátor a provedli jsme toto měření i pro frekvenci 1000 Hz.

K bodu 2c zadání – můstkovou metodu měření indukčnosti jsme nechali na konec měření. U osciloskopu jsme museli nastavit mód ADD a spojit země channelu 1 a channelu 2.

Na začátek měření jsme si změřili hodnotu odporu cívky a nastavili ho na odporové dekádě(přibližný). Poté jsme si spočítali přibližnou hodnotu mezní frekvence pro určitou hodnotu kondenzátoru a nastavili jsme ji na generátoru. Poté jsme jen upravovali hodnotu frekvence dokud se výchylka na osciloskopu neblížila k nule.

# Tabulky

## Tabulka měření indukčnosti cívky s jádrem(tlumivky)

| fkonst \[Hz\] | 50      |       |        |       |       |       |       |       |       |       |       |       |       |        |        |
|---------------|---------|-------|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|
| I\[A\]        | 0,00145 | 0,002 | 0,0025 | 0,003 | 0,004 | 0,006 | 0,009 | 0,012 | 0,02  | 0,05  | 0,075 | 0,1   | 0,2   | 0,3    | 0,4    |
| U\[V\]        | 0,455   | 0,65  | 0,84   | 1,09  | 1,45  | 2,27  | 3,53  | 4,84  | 8,5   | 22,78 | 35    | 47,5  | 95    | 138,72 | 175,98 |
| P\[W\]        | 0       | 0     | 0      | 0     | 0     | 0     | 0     | 0     | 0     | 0,112 | 0,3   | 0,5   | 1,86  | 3,93   | 6,75   |
| L\[mH\]       | 0,997   | 1,033 | 1,068  | 1,155 | 1,152 | 1,203 | 1,247 | 1,282 | 1,351 | 1,449 | 1,484 | 1,511 | 1,511 | 1,470  | 1,399  |

## Odpor tlumivky

| Rs\[Ω\] | 20,2 |
|---------|------|

## 

## Tabulka stejnosměrného odporu neznámé vzduchové cívky

| Rs\[Ω\] | 0,7 |
|---------|-----|

## Tabulka měření neznámé indukčnosti vzduchové cívky, Imax=5 A, N=300- VA metoda

| f\[Hz\] | Rs\[\] | U\[V\] | I\[A\] | Lx\[\] | Lx\[mH\] |
|---------|--------|--------|--------|--------|----------|
| 50      | 0,74   | 0,1112 | 0,10   | 2,64   | 2,68     |
|         |        | 0,2258 | 0,20   | 2,71   |          |
|         |        | 0,5606 | 0,50   | 2,68   |          |
| 1000    |        | 2,09   | 0,11   | 3,05   | 3,09     |
|         |        | 0,981  | 0,05   | 3,12   |          |
|         |        | 1,457  | 0,08   | 3,09   |          |

Tabulka měření neznámé indukčnosti vzduchové cívky, Imax=5 A, N=300- LRC metr

| f\[Hz\]  | 100  | 120  | 1000  | 10000 | 100000 |
|----------|------|------|-------|-------|--------|
| Ls\[mH\] | 2,97 | 2,97 | 2,949 | 2,856 | 3,04   |

## Tabulka měření neznámé indukčnosti vzduchové cívky, Imax=5 A, N=300 - rezonanční můstek

| f0\[HZ\]    | 4109,36 |
|-------------|---------|
| R1\[Ω\]     | 1000    |
| R2\[Ω\]     | 2000    |
| R3\[Ω\]     | 1       |
| fskut\[Hz\] | 4212    |
| Cd\[nF\]    | 500     |
| Lx\[mH\]    | 2,86    |

# Příklad výpočtu

## Výpočet indukce z VA metody

$$Lx = \frac{\sqrt{\frac{U^{2}}{I^{2}} - {Rs}^{2}}}{\omega}$$

$$Lx = \frac{\sqrt{\frac{{0,1112}^{2}}{{0,10}^{2}} - {20,2}^{2}}}{100\pi}$$

$$Lx = 2,64\ mH$$

## Výpočet indukce z VAW metody

$$Lx = \frac{1}{\omega}.\frac{U}{I}.sin\varphi$$

$$Lx = \frac{1}{100\pi}.\frac{22,78}{0,05}.sin(84{^\circ})$$

$$Lx = 1,44\ mH$$

## Výpočet indukce z Rezonančního můstku

$$Lx = \frac{1}{4\pi^{2}{f0}^{2}Cd}$$

$$Lx = \frac{1}{4.\pi^{2}.4212^{2}.500.10^{- 9}}$$

$$Lx = 2,86\ mH$$

[obrázek]

[obrázek]

# Závěr

Při tomto měření jsme zjistili že indukčnost tlumivky neboli cívky s feritovým jádrem se zvyšujícím proudem prudce roste až do cca75 mA poté se indukčnost začne pomalu stabilizovat a drží se na přibližné hodnotě 1,4 mH. Pro toto měření jsme nemohli provést měření VAW metodou vždy jelikož byl proud velmi malý a wattmetr neukazoval hodnoty.

Při měření neznáme vzduchové cívky jsme nenarazili na žádný problém. U měření rezonančního můstku však nebylo možné na osciloskopu zobrazit přesnou, jelikož všechny součástky mají svojí vlastní toleranci a na odporu R3 jsme nemohli nastavit přesnou ohmickou hodnotu cívky, jelikož měla hodnotu 0,7Ω, a tak jsme na odporové dekádě nastavili 1Ω.

Metoda rezonančního můstku je velmi přesná, zato však velmi časově náročná. Takže pokud chceme změřit indukčnost nějaké neznámé cívky a chceme rychlou a poměrně přesnou hodnotu, tak bych doporučil LRC metr.
