# Teoretický úvod

## Usměrňovač

Usměrňovače jsou elektronické obvody, které slouží k přeměně střídavého napětí a proudu na napětí a proud stejnosměrný. V praxi se používají například v napájecích zdrojích, nabíječkách nebo různých elektronických zařízeních, kde je potřeba stabilní stejnosměrné napětí. Základním prvkem usměrňovačů je polovodičová dioda, která propouští proud pouze jedním směrem a tím umožňuje odstranit část střídavé sinusovky.

Mezi základní druhy usměrňovačů patří jednocestný a dvoucestný usměrňovač.

## Jednocestný usměrňovač

[obrázek]

Jednocestný usměrňovač využívá jednu diodu a propouští pouze jednu půlperiodu střídavého signálu, zatímco druhou blokuje. Výsledné napětí je tedy pulzující stejnosměrné napětí s poměrně velkým zvlněním. Zde je obrázek průběhu usměrněného pomocí diody.

[obrázek]

## Dvoucestný usměrňovač

[obrázek]

Dvoucestný usměrňovač naopak využívá obě půlperiody střídavého napětí, čímž dosahuje vyšší účinnosti a menšího zvlnění na výstupu.

Dvoucestné usměrňovače mohou být realizovány například pomocí transformátoru se středním vývodem a dvou diod nebo pomocí tzv. Graetzova můstku, který je tvořen čtyřmi diodami zapojenými do můstkového uspořádání. Toto zapojení je v praxi velmi rozšířené, protože umožňuje efektivní využití obou půlperiod střídavého napětí bez nutnosti speciálního transformátoru. Pro další vyhlazení výstupního napětí se za usměrňovač často zapojuje filtrační kondenzátor.

Zde je opět obrázek signálu, který byl dvoucestně usměrněný. Tím že signál je dvoucestně usměrněný, tak má dvojnásobnou periodu než na vstupu.

[obrázek]

## Zvlnění

Zvlnění je jev, který se objevuje na výstupu usměrňovače. I když usměrňovač převádí střídavé napětí na stejnosměrné, výsledné napětí není úplně konstantní, ale obsahuje malé kolísání. Toto kolísání vzniká proto, že usměrněné napětí má stále pulzující charakter podle původního střídavého signálu. Velikost zvlnění závisí například na typu usměrňovače, zatížení obvodu a také na použitých filtračních součástkách. Ke snížení zvlnění se často používají filtrační kondenzátory nebo další vyhlazovací obvody, které pomáhají udržet výstupní napětí stabilnější. Na výpočet činitele zvlnění se používá vzorec:

$$\varphi_{ZVL} = \frac{2.\sqrt{2}.U_{ZVL}}{U_{0}}.100\ \lbrack\%\rbrack$$

Takto může vypadat zvlnění:

[obrázek]

## Filtrační kondenzátor

Dává se za usměrňovací prvek, aby se co nejvíce vyhladilo zvlnění. U dvojcestného usměrnění se kondenzátor počítá dle tohoto vzorce:

$$C_{0} = \frac{300.I\lbrack mA\rbrack}{p\lbrack\%\rbrack.U\lbrack V\rbrack}\lbrack\mu F\rbrack$$

U jednocestného usměrnění se konstanta s hodnotou 300 změní na 600.

Zde je vidět, jak kondenzátor ovlivňuje napětí:

[obrázek] t

## Zatěžovací charakteristika

Zatěžovací charakteristika je závislost napětí na proudu. Říká nám, jak moc se zmenší napětí zdroje, při zvyšování zatěžovacího proudu. Zde je příklad, jak může zatěžovací charakteristika vypadat. Z této charakteristiky můžeme určit vnitřní odpor zdroje. Ovšem vždy musíme dbát na to abychom odpor počítali z co nejlineárnější části křivky. Zde je příklad, jak může zatěžovací charakteristika

[obrázek]

Takto se počítá vnitřní odpor:

$$Ri = \frac{\mathrm{\Delta}U}{\mathrm{\Delta}I}\lbrack\mathrm{\Omega}\rbrack$$

Pokud je charakteristika lineární, může se vztah zjednodušit na klasický Ohmův zákon.

# Schéma zapojení

## Měření jednocestného usměrnění

[obrázek]

## Měření dvoucestně usměrněného usměrnění

[obrázek]

## Měření zatěžovací charakteristiky dvojcestného usměrňovači

[obrázek]

# Použité přístroje

| OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA |
| RAT | regulovatelný autotransformátor | U2=0 - 230V | 3207-1956 |  |
| Traf | Transformátor | U1=230V, U2=30V, I2=2,5A | bez |  |
| OSC | digitální osciloskop | UNI-T UPO2104E | 11-15-1973 |  |
| C0 | vyhlazovací kondenzátor-elektrolytický | C=4 mF, 8 mF, 2 mF | bez |  |
| A | digitální multimetr | UNI-T-UT890D+ | T-25-09 |  |
| Vss | digitální voltmetr | UNI-T-UT890D+ | T-25-19 |  |
| Vstř | analogový voltmetr | fmax=500kHz | 3208-2 |  |
| gen | stolní generátor | fmax=500kHz | 3207-2 |  |
| Rz1 | nastavitelný odpor | R=105Ω, Imax=2,5A | D1-20-584 |  |
| Rz2 | nastavitelný odpor | R=39Ω, Imax=4A | 3208 |  |

# Postup měření

1\) Na stínítku digitálního osciloskopu jsme zobrazili několik period usměrněného pulsujícího napětí, načetli do počítače, popsali a vytiskli.

2\) Vypočítali hodnotu vyhlazovacího kondenzátoru C0 pro zadané hodnoty U0, I0MAX, ᵠZVL. Vypočítanou velikost jsme zaokrouhlily na takovou, kterou lze realizovat s použitím dostupných kondenzátorů

3\) Zatěžovací i vyhlazovací charakteristiku jsme měřili najednou. Zatěžovací odpor Rz realizovali sériovým spojením 2 í potenciometrů s odstupňovanými hodnotami odporu (stovky – desítky ohmů), při nastavování odebíraného proudu jsme postupně hodnotu Rz snižovali. Abychom nepřekročili maximální jmenovitý proud I0MAX. Voltmetrem V1 jsme měřili stejnosměrné napětí U0, voltmetrem V2 jsme měřili efektivní hodnotu střídavé složky UZVL (zvlnění). Měření jsme provedli do I0MAX, cca 12–14 hodnot, pro tři hodnoty vyhlazovacího kondenzátoru.

# Tabulky

## Měření zatěžovací charakteristiky usměrňovače z 4 diod KY718, s vyhlazovacím kondenzátorem C0= 4mF

| U0\[V\]   | 29,05 | 28,8 | 28   | 27,71 | 27,5 | 27,3  | 27   |
|----------------------|-------|------|------|-------|------|-------|------|
| I0\[mA\]  | 1,03  | 1,3  | 1,41 | 1,5   | 1,58 | 1,61  | 1,75 |
| UZVL\[V\] | 0,2   | 0,4  | 0,45 | 0,5   | 0,55 | 0,6   | 0,61 |
| Zvlnění\[%\]         | 1,95  | 3,93 | 4,55 | 5,10  | 5,66 | 6,22  | 6,39 |
|                      |       |      |      |       |      |       |      |
|                      |       |      |      |       |      |       |      |
| U0\[V\]   | 26,8  | 26,6 | 26,4 | 26,2  | 25,6 | 25,4  |      |
| I0\[mA\]  | 1,84  | 1,86 | 1,96 | 2     | 2,13 | 2,17  |      |
| UZVL\[V\] | 0,62  | 0,65 | 0,7  | 0,75  | 0,8  | 1     |      |
| Zvlnění\[%\]         | 6,54  | 6,91 | 7,50 | 8,10  | 8,84 | 11,14 |      |

##  Měření zatěžovací charakteristiky usměrňovače z 4 diod KY718, s vyhlazovacím kondenzátorem C0= 8mF

| U0\[V\]   | 29,2 | 28,8 | 28,6 | 28,4 | 28,2 | 28    | 27,8 |
|----------------------|------|------|------|------|------|-------|------|
| I0\[mA\]  | 1,21 | 1,4  | 1,48 | 1,5  | 1,57 | 1,63  | 1,72 |
| UZVL\[V\] | 0,26 | 0,32 | 0,33 | 0,37 | 0,34 | 0,36  | 0,4  |
| Zvlnění\[%\]         | 2,52 | 3,14 | 3,26 | 3,68 | 3,41 | 3,64  | 4,07 |
|                      |      |      |      |      |      |       |      |
| U0\[V\]   | 27,5 | 27,3 | 27   | 26,6 | 26,4 | 26,18 | 26,1 |
| I0\[mA\]  | 1,83 | 1,9  | 1,99 | 2,1  | 2,18 | 2,24  | 2,28 |
| UZVL\[V\] | 0,4  | 0,41 | 0,44 | 0,45 | 0,48 | 0,49  | 0,75 |
| Zvlnění\[%\]         | 4,11 | 4,25 | 4,61 | 4,78 | 5,14 | 5,29  | 8,13 |

## Měření zatěžovací charakteristiky usměrňovače z 4 diod KY718, s vyhlazovacím kondenzátorem C0= 2mF

| U0\[V\]   | 29,8  | 28,8  | 28,6  | 28,4  | 28,2  | 28    | 27,8  |
|----------------------|-------|-------|-------|-------|-------|-------|-------|
| I0\[mA\]  | 1,09  | 1,5   | 1,55  | 1,6   | 1,61  | 1,64  | 1,74  |
| UZVL\[V\] | 0,8   | 1,2   | 1,25  | 1,25  | 1,3   | 1,3   | 1,3   |
| Zvlnění\[%\]         | 7,59  | 11,79 | 12,36 | 12,45 | 13,04 | 13,13 | 13,23 |
|                      |       |       |       |       |       |       |       |
| U0\[V\]   | 27,6  | 27,5  | 27,3  | 27    | 26,6  | 26,5  | 26    |
| I0\[mA\]  | 1,75  | 1,79  | 1,87  | 1,94  | 2     | 2,07  | 2,25  |
| UZVL\[V\] | 1,38  | 1,4   | 1,4   | 1,48  | 1,5   | 1,6   | 1,7   |
| Zvlnění\[%\]         | 14,14 | 14,40 | 14,50 | 15,50 | 15,95 | 17,08 | 18,49 |

# Příklad výpočtu

## Výpočet filtračního kondenzátoru, pro U0=25V, Imax=2,5A a zvlněním 10%

$$C_{0} = \frac{300.I\lbrack mA\rbrack}{p\lbrack\%\rbrack.U\lbrack V\rbrack}\lbrack\mu F\rbrack$$

$$C_{0} = \frac{300.2500}{10.25}$$

$$C_{0} = 3mF$$

## Výpočet činitele zvlnění při I=2,2A a s různými filtračními kondenzátory

$$\varphi_{ZVL} = \frac{2.\sqrt{2}.U_{ZVL}}{U_{0}}.100\ \lbrack\%\rbrack$$

Pro C0=4 mF

$$\varphi_{ZVL} = \frac{2.\sqrt{2}.1}{25,4}.100\ $$

$$\varphi_{ZVL} = 11,14\%$$

Pro C0=8mF

$$\varphi_{ZVL} = \frac{2.\sqrt{2}.0,75}{26,1}.100\ $$

$$\varphi_{ZVL} = 8,13\%$$

Pro C0=2mF

$$\varphi_{ZVL} = \frac{2.\sqrt{2}.1,7}{26}.100\ $$

$$\varphi_{ZVL} = 18,49\ \%\ $$

Výpočet vnitřního odporu ze zatěžovacích charakteristik pro různé hodnoty C0

$$Ri = \frac{\mathrm{\Delta}U}{\mathrm{\Delta}I}\lbrack\mathrm{\Omega}\rbrack$$

Pro C0=4mF

$$Ri = \frac{0,21}{0,08}$$

$$Ri = 2,63\ \mathrm{\Omega}$$

Pro C0=8mF

$$Ri = \frac{0,4}{0,08}$$

$$Ri = 5\ \mathrm{\Omega}$$

Pro C0=2mF

$$Ri = \frac{0,4}{0,07}$$

$$Ri = 5,71\ \mathrm{\Omega}$$

## Oscilogram jednocestně usměrněného signálu diody IN5408

[obrázek]

## Oscilogram usměrněného signálu Graetzovým můstkem z diod KY718

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

# Závěr

Při našem měření, jsme narazili na mnoho překážek, ale při následném doměření se nám je podařilo odstranit. Oscilogram z jednocestného usměrnění obsahuje i výstup z generátoru, jelikož jsme v té době nevěděli, že kanál 2 přizemňuje potencionál na ground a tak nám nešel odbočkový transformátor.

Při doměření odbočkový transformátor opět nefungoval, a tak nám byl dán transformátor s výstupním napětím 30 V a maximálním proudem 2,5 A.

Při měření zatěžovací charakteristiky jsme místo filtračního kondenzátoru 3mF použili kondenzátor s hodnotou 4mF, kvůli tomu, že při hodnotě 3mF nebylo maximální zvlnění v zadaném pásmu a to do 10 %.

Vnitřní odpor při hodnotě filtračního kondenzátoru 4mF vyšel 2,63 ohmů. Při hodnotě 8mF pak 5 ohmů a při hodnotě 2mF dokonce 5,71 ohmů.

Nejmenšího zvlnění jsme dosáhli u dvojnásobné velikosti kondenzátoru, ale vnitřní odpor byl téměř dvojnásobný.

Vnitřní odpor by se dal počítat jako statický, jelikož charakteristiky vyšli téměř lineární, já jsme ovšem zvolil vždy jen 2 sousední body, které mi přišli nejlineárnější.
