# Teoretický úvod

# Kondenzátor

Kondenzátor je pasivní elektrotechnická součástka, jejíž charakteristickou vlastností je kapacita.

Každý skutečný kondenzátor kromě toho vykazuje další, takzvané parazitní vlastnosti, jako je indukčnost a odpor, čímž se odlišuje od kapacitoru, což je myšlená ideální součástka, která má pouze kapacitu, navíc stálou a nezávislou na okolních podmínkách.

Kondenzátor se skládá ze dvou vodivých desek (elektrod) oddělených dielektrikem. Na každou z desek se přivádí elektrické náboje opačné polarity, které se vzájemně přitahují elektrickou silou. Dielektrikum mezi deskami nedovolí, aby se částice s nábojem dostaly do kontaktu, a tím došlo k neutralizaci, jinak vybití elektrických nábojů. Přitom dielektrikum svou polarizací zmenšuje sílu elektrického pole nábojů na deskách a umožňuje tak umístění většího množství náboje.

Vzhledem k elektrostatické indukci je velikost náboje na obou deskách stejná.

Kapacita C kondenzátoru závisí na ploše S jeho desek, vzájemné vzdálenosti l (malé L) desek mezi sebou a permitivitě ε dielektrika mezi deskami:

$$C = \varepsilon_{0}{.\varepsilon}_{r}.\frac{S}{l}$$

## Obecný impedanční můstek

[obrázek]

Můstky se používají k přesnému měření elektrických veličin – kapacity, odporu nebo indukčnosti. Měření můstkovými metodami se zakládá na dosažení rovnováhy mezi větvemi můstku. Tuto rovnováhu zjišťujeme indikátorem výchylky, zapojeným mezi uzly D a B. Na uzlech A, C je pak připojeno střídavé nebo stejnosměrné napájení (podle měřené veličiny: pro kapacitu a indukčnost střídavé, pro odpory stejnosměrné i střídavé, lepší je však stejnosměrné). Společným znakem je napájení, které je připojeno k jedné úhlopříčce můstku, i způsob indikace: indikátor se zapojí k druhé úhlopříčce, vyvažování větví je stejné, pomocí proměnného rezistoru, zapojeného jako reostat.

Vztahy pro obecný můstek:

$$\frac{Z_{1}}{Z_{2}} = \frac{Z_{3}}{Z_{4}}$$

$${|Z}_{1}\left| .\left| Z_{4} \right| = {|Z}_{2} \right|.|Z_{3}|$$

$${|Z}_{1}| = \frac{{|Z}_{2}|.{|Z}_{3}|}{{|Z}_{4}|}$$

**De Sautyho můstek**

De Sautyho můstek je tvořen dvěma rezistory, dvěma kondenzátory a nulovým indikátorem. Aby bylo možno můstek úplně vyvážit, musely by být kondenzátory $C_{X}\ a\ C_{n}$ bezeztrátové. Což v praxi neplatí, to znamená že nelze můstek úplně vyvážit.

*Bezeztrátové Cx Vyvažování R2, R4, C4*

[obrázek] [obrázek]

Pokud se zanedbají ztrátové odpory kondenzátorů lze podmínku rovnováhy zapsat:

Vztahy pro De Sautyho můstek:

$$Z_{Cx}:Z_{C4} = R1:R2$$

$$\frac{1}{\omega C_{x}}.\frac{1}{\omega C_{4}} = \frac{R1}{R2}$$

$$\frac{C_{4}}{C_{x}} = \frac{R1}{R2}$$

$$Cx = C_{4}\frac{R2}{R1}$$

$$Rx = R4\frac{R1}{R2}$$

$$tg\varphi = \omega.C4.R4$$

## Wienův můstek

Wienův můstek se používal pro přesné měření kapacity pomocí odporu a frekvence. Byl také používán pro měření zvukových frekvencí. Wienův můstek nevyžaduje stejné hodnoty rezistorů a kondenzátorů R a C. Při nějaké frekvenci bude reaktance větve tvořené sériovým zapojením R2–C2 přesným násobkem bočníkové větve Rx–Cx. Pokud budou větve R3 a R4 nastaveny na stejný poměr, pak bude můstek vyvážený.

[obrázek]

Zde jsou již odvozené vzorce pro výpočet:

$$Cx = C4.\frac{R2}{R1}$$

$$Rx = R4.\frac{R2}{R1}$$

$$\varphi = \omega.R4.C4$$

## Rezonanční můstek

[obrázek]

Jedná se o druh můstku, který využívá rezonančního obvodu. Při rezonanční frekvenci se reaktance, a tedy i celková impedance vyrovná a poté se tento můstek chová jako klasický odporový můstek. Takže pro rovnováhu na můstku je tato rovnice.

$$R2.R3 = Z.R4$$

$$Z = \frac{R2}{R4}.R3$$

Neboli při rezonanční frekvenci f0 platí následující vztah:

$$Z = Xl = Xc = Rx$$

Z toho si pak můžeme vyjádřit neznámou kapacitu:

$$Cx = \frac{1}{4\pi^{2}{f0}^{2}Ld}$$

Nejlépe můstková metoda funguje při poměru rezistorů R2 a R4 rovno 1. Tudíž budeme volit hodnoty rezistorů stejné. Poté jen upravujeme lehce frekvenci a odpor R3, než se dostaneme k rezonanci.

## Měření elektrolytických kondenzátorů

Pro měření kondenzátorů s kapacitou řádově jednotky mF a větší neexistuje žádný standardní měřící přístroj ani přesné dekády pro použití výchylkových metod. Lze však použít jednoduché měření úbytku napětí za určitý čas při pomalém vybíjení nabitého kondenzátoru do odporové zátěže.

Nabijeme-li kondenzátor Cx na napětí zdroje U0 a poté ho od zdroje odpojíme, bude se kondenzátor vybíjet přes odpor R a napětí na něm (měřené voltmetrem) se bude exponenciálně zmenšovat (s časovou konstantou ϯ=R\*Cx). Kapacita kondenzátoru pak může být určena poklesem napětí o dU za velmi krátký časový interval dt, při proudu I:

$$C = I.\frac{dU}{dt}$$

Provedeme-li celkově *k* měření po celé vybíjecí křivce (tak, aby bylo možné průběh mezi dvěma měřeními nahradit přímkou), získáme *k* hodnot měřené kapacity a výslednou hodnotu určit jako aritmetický průměr dílčích kapacit.

Pro lepší názornost je dobré změřenou křivku (UC=f(t)) znázornit graficky, přičemž sestrojení tečny k této křivce v počátku můžeme z časové osy odečíst časovou konstantu vybíjecího obvodu ϯ a z ní určit (přibližnou) hodnotu Cx= ϯ/ R.

Chyba měření je dána konečnou hodnotou vnitřního odporu voltmetru (zapojen paralelně k vybíjecímu rezistoru R), třídou přesnosti voltmetru a tolerancí rezistoru R. Celkově můžeme touto metodou měřit velké hodnoty kapacit s přesností řádově 2 ÷ 5 %.

*Vybíjecí charakteristika*

[obrázek]*  
*

# Schéma zapojení

## Schéma zapojení rezonančního můstku

[obrázek]

## Schéma zapojení, pro vybíjení kondenzátoru

[obrázek]

# Použité přístroje

| OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA |
| gen | generátor střídavého signálu |  | 3207-14a-CL141 |  |
| zdr | Zdroj napětí | Stolní zdroj, 3206-stůl 2, Umax=18 V, Imax=1,8 A | 3206 |  |
| R2 | odporová dekáda | Pmax=1 W | 3206-1-4b |  |
| R3 | odporová dekáda | Pmax=1 W | 3206-1-4a |  |
| R4 | odporová dekáda | Pmax=1 W | 9-5b-AL1680 |  |
| Rd | odporová dekáda | Pmax=1 W | 9-5b-AL1680 |  |
| Ld | induktivní dekáda |  | 7-7c-AL1595 |  |
| V | voltmetr | UNI-T UT804 | 10-9-1861 |  |
| osc | Osciloskop GoldStar OS-5020P |  | 3206-2-2a |  |

# Postup měření

Při měření rezonančního můstku jsme nastavili rezistory R2 a R4 na hodnotu 1kΩ. Vypočítali jsme si přibližnou rezonanční frekvenci, kterou jsme vypočítali ze zvolené indukčnosti a kapacity napsané na kondenzátoru. Poté jsme jen nastavovali jemně frekvenci a rezistor R3, dokud můstek nebyl v rezonanci.

Před měřením vybíjecí charakteristiky jsme museli vypočítat hodnotu rezistoru, když jsme měli zadanou dobu 5 tau a z hodnoty kapacity napsané na něm. Poté jsme na dekádě nastavili hodnotu na odporové dekády. Nejprve jsme zapojili kondenzátor do svorky 1. Jelikož byl kondenzátor na 315 V, tak jsme ho nabili celými 18 volty ze zdroje ve stole. Poté jsme propojili voltmetr s počítačem a zapnuli program, poté jsme přepojili kondenzátor přepojili do svorky 2 a nechali ho vybíjet.

# Tabulky

## Tabulka při použití rezonančního můstku Cx=2,2uF

|     | Cx \[uF\] | Lx \[H\] | f0 \[Hz\] | Rx \[Ω\] | R2 \[Ω\] | R3 \[Ω\] | R4 \[Ω\] |
|-----|-----------|----------|-----------|----------|----------|----------|----------|
| Cx1 | 2,24      | 0,05     | 476,00    | 3,00     | 1000,00  | 3,00     | 1000,00  |

## Tabulka pro měření vybíjení kondenzátoru s předpokládanou hodnotou Cx=330uF

| τ\[s\]    | 12    |
|-----------|-------|
| 5τ\[s\]   | 60    |
| R\[Ω\]    | 36364 |
| Cx0\[uF\] | 330   |

## Tabulka vybíjení kondenzátoru Cx=330uF do času 1 tau

| t\[s\] | U\[V\] |
|--------|--------|
| 0,0    | 18,572 |
| 0,5    | 17,286 |
| 1,0    | 16,4   |
| 1,5    | 15,563 |
| 2,0    | 14,77  |
| 2,5    | 14,02  |
| 3,0    | 13,31  |
| 3,5    | 12,636 |
| 4,0    | 11,999 |
| 4,5    | 11,395 |
| 5,0    | 10,822 |
| 5,5    | 10,279 |
| 6,0    | 9,764  |
| 6,5    | 9,274  |
| 7,0    | 8,81   |
| 7,5    | 8,37   |
| 8,0    | 7,952  |
| 8,5    | 7,554  |
| 9,0    | 7,178  |
| 9,5    | 6,821  |
| 10,0   | 6,481  |
| 10,5   | 6,158  |
| 11,0   | 5,852  |
| 11,5   | 5,561  |
| 12,0   | 5,285  |

| Cx\[uF\] | 335,01 |
|----------|--------|

# Příklad výpočtu

Výpočet předpokládané rezonanční frekvence:

$$f0 = \frac{1}{2\pi\sqrt{LC}}$$

$$f0 = \frac{1}{2\pi\sqrt{0,0000022.0,05}}$$

$$f0 = 480\ Hz$$

Výpočet kapacity z rezonance:

$$Cx = \frac{1}{4\pi^{2}{f0}^{2}Ld}$$

$$Cx = \frac{1}{4\pi^{2}{.476}^{2}.0,05}$$

$$Cx = 2,24\ µF$$

Výpočet odporu z časové konstanty tau:

$$R = \frac{\tau}{C}$$

$$R = \frac{12}{330.10^{- 6}}$$

$$R = 36364\ \mathrm{\Omega}$$

Výpočet kapacity kondenzátoru ze změny napětí na čase:

$$\mathrm{\Delta}t = t_{n} - t_{n - 1}$$

$$U_{Sn} = \frac{U_{n} + U_{n - 1}}{2}$$

$$\mathrm{\Delta}U_{n} = U_{Sn} - U_{S(n - 1)}$$

$$C_{n} = \frac{U_{Sn}}{R}.\frac{\mathrm{\Delta}t}{\mathrm{\Delta}U_{n}}$$

$$C_{x} = \frac{\sum_{}^{}C_{n}}{k}$$

$$\ldots$$

$$C_{x} = 335,01\ µF$$

[obrázek]

# Závěr

Toto měření proběhlo v omezené míře, takže neobsahuje měření jinými můstky než rezonančním a než měření vybíjení kondenzátoru. Přesto jsou v teoretickém úvodu zmíněné ještě dva můstky. A to De Sautyho a Wiennův můstek.

V tomto protokolu je tedy jen jediný graf, a to vybíjecí charakteristika kondenzátoru. Jelikož grafy porovnání jednotlivých metod by postrádaly smysl.

U měření pomocí rezonančního nám kapacita vyšla téměř totožná s hodnotou uvedenou na kondenzátoru a to 2,24 uF.

Při měření vybíjecí charakteristiky nám kapacita vyšla o 5uF vyšší, než byla uvedena na elektrolytickém kondenzátoru. Toto může být způsobeno tolerancí dekády, ale také to může být způsobeno tolerancí samotného kondenzátoru.
