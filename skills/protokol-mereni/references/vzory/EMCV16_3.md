| [obrázek] | Vyšší odborná škola a Střední průmyslová škola elektrotechnická Plzeň | Protokol o měření |
| Předmět: | EM |
| Název úlohy: | Stabilizátory napětí v napájecích zdrojích-měření základních parametrů | Číslo úlohy |
| 16 |
| Vypracoval: | Ladislav Neblecha | Třída / skupina |
| 3. P/ S1 |
| Datum měření: | Účast: | Datum odevzdání: | Počet listů: |
| 14. 4. 2026 | Přítomen | 14.4. 2026 | 12 |
| Zkoušený předmět: | stabilizátory-integrovaný, zenerova dioda |
| Katalogové hodnoty, udané parametry, podmínky měření (teplota, vlhkost, tlak): |
| L200 – U inMAX = 40 V, U out = 3-36 V, I zMAX = 0,4A0,4A/1,2A (zvoleno 0,4A) IN5346B - U inMAX = 40 V, U out = 9,1V, I zMAX = 1 A |
| Zadání | Splněno |
| 1) Na vzorcích stabilizátorů napětí změřte a znázorněte stabilizační charakteristiku. |  |
| 2) V samostatném grafu znázorněte (ve vhodném měřítku) stabilizační oblast. |  |
| 3) Určete činitel stabilizace jednotlivých zapojení. Hodnoty potřebné pro jeho určení v grafu vyznačte. |  |
| 4) Změřte a znázorněte zatěžovací charakteristiky stabilizátorů od stavu naprázdno do doporučené maximální hodnoty proudu. |  |
| 5) Určete hodnotu vnitřního odporu Ri. Hodnoty potřebné pro jeho určení v grafu vyznačte. |  |
| 6) Porovnejte jednotlivé stabilizátory z hlediska kvality stabilizace a tvrdosti |  |

# Teoretický úvod

## Stabilizátor

Stabilizátor je elektrické zapojení diskrétních součástek nebo elektrotechnická součástka na principu integrovaného obvodu, která umožňuje stabilizovat výstupní napětí nebo proud při změnách výstupního proudu, vstupního napětí a teploty okolí.

Na jiných veličinách není obvykle hodnota výstupního napětí závislá, pokud ano, je třeba sledovat i takovéto vlivy (např. stárnutí součástek, vliv elektromagnetického rušení apod.). Kromě stabilizačních účinků (kterými je míněna regulace na konstantní hodnotu) každý typ stabilizátoru více či méně snižuje střídavou složku výstupního napětí (zvlnění) a pracuje tedy jako filtr.

## Rozdělení stabilizátorů 

Podle principu funkce se stabilizátory dělí na několik skupin v sériovém nebo paralelním zapojení parametrické – bez zpětné vazby nebo se zpětnovazební smyčkou lineární nebo spínané stabilizátory podle stabilizace polarity napětí kladné/záporné stabilizátory proudu, stabilizátory napětí.

## Parametrický stabilizátor:

základní zapojení se zenerovou diodou-sériové provedení stabilizátoru

[obrázek]

Využívají parametrů součástek, nejčastěji velmi strmého průběhu volt-ampérové (VA) charakteristiky zenerovy diody nebo lavinové diody v závěrném směru. Nevýhoda je, že zenerovou diodou musí protékat poměrně velký proud. Proud protékající zátěží přes odpor R snižuje účinnost. Výhodou je jednoduché zapojení a omezení zkratového proudu (odporem R).

Zdokonalený stabilizátor využívá stejného principu funkce zenerovy diody. Pro regulaci je však použit regulační tranzistor zapojený jako emitorový sledovač

## Stabilizační charakteristika

Jedná se o charakteristiku, ze které lze určit stabilizační oblast neboli hranice napětí, kdy stabilizátor drží jedno napětí. Dále se z něj dá vypočítat i činitel stabilizace k. Zde je vzorec:

$$k = \frac{\mathrm{\Delta}U_{výst}}{\mathrm{\Delta}U1}$$

Takto pak může vypadat charakteristika i s vyznačenými parametry, potřebných k výpočtu:

[obrázek]

## Zatěžovací charakteristika

Jedná se o charakteristiku, která nám říká kolik se změní výstupní napětí v závislosti na zatěžovacím proudu. Ze zatěžovací charakteristiky lze určit vnitřní odpor pomocí vzorce:  
$$Ri = \frac{\mathrm{\Delta}U_{výst}}{\mathrm{\Delta}I_{z}}\lbrack\mathrm{\Omega}\rbrack$$

Takto vypadá zatěžovací charakteristika s vyznačenýma parametry pro výpočet:

[obrázek]

## Měřené stabilizátory

Zde jsou fotky stabilizátorů, které jsme měli na výkladové hodině.

Poté jsem z přílohy vyčetl jednotlivé hodnoty součástek.

[obrázek]

L200 je integrovaný stabilizátor, který umožňuje stabilizovat poměrně velký rozsah napětí a proudu. Takto by mělo vypadat typické zapojení:

[obrázek]

V našem případě je vynechány kondenzátory. Dále musíme počítat s tím, že stabilizátor by měl fungovat od napětí 3V jelikož samotný stabilizátor spotřebuje 3V na svůj provoz.

Druhý přípravek byl typický parametrický stabilizátor realizovaný pomocí zenerovy diody a tranzistoru zde je foto:

[obrázek]

Zde je typické schéma zapojení z podkladů:

[obrázek]

# Schéma zapojení

[obrázek]

# Použité přístroje

| OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA |
| Uz1 | Stejnosměrný zdroj | Power supply, 3x0-18V, 1,8A |  |  |
| V1 | Multimetr, voltmetr | UNI-T UT804 | 10-10-1862 |  |
| V2 | Multimetr, voltmetr | UNI-T UT890D+ | T-25-05 |  |
| A | Multimetr, ampérmetr | UNI-T UT890D+ | T-25-19 |  |
| Rz1 | Posuvný rezistor | METRA 250Ω, 1,6A | 3205-9F-581 |  |
| Rz2 | Posuvný rezistor | METRA 120Ω, 2A | 3205-10a-1350 |  |

# Postup měření

Při měření stabilizační charakteristiky jsme nastavili na zdroji U1 napětí od nuly a poté jsme postupně zvyšovali. Před měřením jsme museli mít k dispozici informaci o maximálním vstupním napětí, při kterém je možné ještě stabilizátor provozovat. Změny měřeného výstupního napětí byli po dosažení stabilizační oblasti malé, proto jsme použili na výstupu voltmetr V2 s dostatečnou citlivostí (min. 5místný displej pro současné měření jednotek i tisícin voltů).

(V případě, že by nebyl takový voltmetr k dispozici mohli jsme použít metodu dvou voltmetrů V2 a V3 zapojených do série a pomocného stejnosměrného zdroje. Pomocné napětí na zdroji U2 jsme nastavili tak, aby na voltmetru V3 bylo možné využít nejmenší rozsah (asi tak 0,2 až 1 V) a výstupní napětí jsme určili z II. Kirchhoffova zákona. Protože napětí na voltmetru V2 bylo stabilizované, odečítali jsme na voltmetru V3 prakticky změny výstupního napětí.)

Při měření zatěžovací charakteristiky jsme měnili zatěžovací odpor, který jsme sestavili ze sériové kombinace více reostatů. Jejich hodnoty jsme určili alespoň přibližně z výstupního napětí a rozsahu zatěžovacího proudu. Napětí U1 jsme nastavili takové, aby bylo dodrženo potřebné pracovní napětí stabilizátoru.

# Tabulky

## Tabulka pro stabilizační charakteristiku stabilizátoru IN5346B – UinMAX= 40 V, Uout= 9,1V, IzMAX= 1 A

| U1\[V\]    | 3,31   | 4,81 | 7,28  | 8,67 | 9,56  | 10,7  | 12,2 | 14   | 16    | 17,5  | 18,3  | 20,42 | 22,8  | 25,4  | 30,56 |
|------------|--------|------|-------|------|-------|-------|------|------|-------|-------|-------|-------|-------|-------|-------|
| Uvýst\[V\] | 2,6148 | 4,05 | 6,318 | 7,66 | 7,942 | 7,982 | 8,14 | 8,04 | 8,064 | 8,082 | 8,096 | 8,117 | 8,139 | 8,164 | 8,199 |

## Tabulka pro zatěžovací charakteristiku stabilizátoru IN5346B – UinMAX= 40 V, Uout= 9,1V, IzMAX= 1 A

| Iz\[mA\]   | 61    | 120   | 180   | 245   | 300   | 360   | 420  | 500    | 536   | 620   | 730    | 810   | 880    | 920    | 990    |
|------------|-------|-------|-------|-------|-------|-------|------|--------|-------|-------|--------|-------|--------|--------|--------|
| Uvýst\[V\] | 7,549 | 7,274 | 6,589 | 5,911 | 5,183 | 4,721 | 4,18 | 3,4431 | 3,226 | 3,018 | 2,5013 | 2,167 | 1,7704 | 1,5169 | 1,0043 |

## Tabulka pro stabilizační charakteristiku stabilizátoru L200 – UinMAX= 40 V, Uout= 3-36 V, IzMAX= 0,4A

| U1\[V\]    | 1,87   | 4,48   | 6,5   | 7,62 | 8,2  | 9,18 | 11,3 | 13,23 | 14,42 | 16    | 17,1  | 18    | 19,5  | 21,4  | 25,4  |
|------------|--------|--------|-------|------|------|------|------|-------|-------|-------|-------|-------|-------|-------|-------|
| Uvýst\[V\] | 0,0057 | 2,6423 | 4,059 | 4,06 | 4,06 | 4,06 | 4,06 | 4,062 | 4,062 | 4,063 | 4,064 | 4,064 | 4,065 | 4,066 | 4,066 |

## Tabulka pro zatěžovací charakteristiku stabilizátoru L200 – UinMAX= 40 V, Uout= 3-36 V, IzMAX= 0,4A

| Iz\[mA\]   | 23    | 41   | 70,6  | 102,4 | 117,5  | 142,8  | 163,9  | 188,6  | 208,8  | 236,9  | 274    | 290,3  | 318,7  | 340,3  | 390,6 |
|------------|-------|------|-------|-------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|-------|
| Uvýst\[V\] | 4,062 | 4,03 | 3,961 | 3,92  | 3,9001 | 3,8584 | 3,8289 | 3,7945 | 3,7653 | 3,7273 | 3,6626 | 3,6546 | 3,6128 | 3,5738 | 3,505 |

# Příklad výpočtu

## Výpočet vnitřního odporu stabilizátoru IN5346B – UinMAX= 40 V, Uout= 9,1V, IzMAX= 1 A

$$Ri = \frac{\mathrm{\Delta}U_{výst}}{\mathrm{\Delta}I_{z}}\lbrack\mathrm{\Omega}\rbrack$$

$$Ri = \frac{2,167 - 1,0043}{(990 - 810).10^{- 3}}$$

$$Ri = 6,46\mathrm{\Omega}$$

## Výpočet činitele stabilizace stabilizátoru IN5346B – UinMAX= 40 V, Uout= 9,1V, IzMAX= 1 A

$$k = \frac{\mathrm{\Delta}U_{výst}}{\mathrm{\Delta}U1}$$

$$k = \frac{8,199 - 7,982}{30,56 - 10,7}$$

$$k = 0,0109$$

## Výpočet vnitřního odporu stabilizátoru L200 – UinMAX= 40 V, Uout= 3-36 V, IzMAX= 0,4A 

$$Ri = \frac{\mathrm{\Delta}U_{výst}}{\mathrm{\Delta}I_{z}}\lbrack\mathrm{\Omega}\rbrack$$

$$Ri = \frac{3,92 - 3,7273}{(236,9 - 102,4).10^{- 3}}$$

$$Ri = 1,43\ \mathrm{\Omega}$$

## Výpočet činitele stabilizace stabilizátoru L200 – UinMAX= 40 V, Uout= 3-36 V, IzMAX= 0,4A

$$k = \frac{\mathrm{\Delta}U_{výst}}{\mathrm{\Delta}U1}$$

$$k = \frac{4,066 - 4,06}{25,4 - 7,62}$$

$$k = 3,37.10^{- 4}$$

# Závěr

Při tomto měření nám vyšly charakteristiky, dle předpokladů.

U stabilizátoru se zenerovou diodou nám vyšel vyšší vnitřní odpor než u stabilizátoru L200.

Stabilizátor se zenerovou diodou měl vnitřní odpor 6,46 ohmů a u stabilizátoru L200 pak 1,43 ohmů.

Obě hodnoty činitele stabilizace byli velmi malé a to 0,0109 u zenerovy diody a $3,37.10^{- 4}$ u stabilizátoru L200. Vnitřní odpory jsem počítal z nejlineárnější části zatěžovací charakteristiky.

| Kontrola vypracování protokolu: S – student, U – učitel, / = splněno dle zásad a zadání, - = nesplněno |        |       |       |       |       |       |       |       |       |       |          |
|--------------------------------------------------------------------------------------------------------|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|----------|
| Datum                                                                                                  |        |       |       |       |       |       |       |       |       |       | Poznámka |
| Kontrola                                                                                               | S      | U     | S     | U     | S     | U     | S     | U     | S     | U     |          |
| Teoret. úvod                                                                                           | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Schéma zapojení                                                                                        | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Použité přístroje                                                                                      | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       | ** ** |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Postup měření                                                                                          | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Tabulky                                                                                                | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Příklady výpočtů                                                                                       | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Grafy                                                                                                  | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Závěr                                                                                                  | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** |       |       |       |       |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
| Originál hodnot                                                                                        | ** /** | ** ** | ** ** | ** ** | ** ** | ** ** | ** ** | ** ** | ** ** | ** ** |          |
|                                                                                                        |        |       |       |       |       |       |       |       |       |       |          |
