# Teoretický úvod

## Třífázový činný výkon(P)

Jedná se o základní veličinu, která nám říká kolik energie se skutečně přemění na práci, či teplo. Jednotkou je Watt. Pro střídavé obvody se počítá dle tohoto vzorce.

$$P = U.I.\cos\varphi\ \lbrack W\rbrack$$

V třífázové soustavě je roven součtu výkonů na jednotlivých fází neboli:

$$\sum_{}^{}P = P_{L1} + P_{L2} + P_{L3}$$

## Třífázový jalový výkon (Q)

Jalový výkon v třífázové soustavě představuje složku výkonu, která v obvodu kmitá mezi zdrojem a zátěží (indukčního či kapacitního charakteru), aniž by se přeměnila na užitečnou práci, jako je teplo nebo mechanický pohyb. V AC obvodech se počítá dle vzorce:

$$Q = U.I.\sin\varphi\lbrack VAr\rbrack$$

Jednotkou je voltampér reaktanční. A v třífázové soustavě se počítá takto:

$$\sum_{}^{}Q = Q_{L1} + Q_{L2} + Q_{L3}$$

## Třífázový Zdánlivý výkon(S)

Je to celkový výkon tekoucí vodiči, který určuje dimenzování jističů a kabelů. V obvodech střídavého proudu má vzorec:

$$S = U.I\ \lbrack VA\rbrack$$

V třífázové soustavě se opět počítá jako součet zdánlivého výkonu na jednotlivých fází:

$$\sum_{}^{}S = S_{L1} + S_{L2} + S_{L3}$$

## Účiník

Dalším důležitým parametrem je účiník (cos ϕ), který vyjadřuje efektivitu využití elektrické energie. Udává podíl mezi činným a zdánlivým výkonem:

$$\cos\varphi = \frac{P}{S}\ \lbrack - \rbrack$$

## Trojúhelník výkonů

[obrázek]

## Možnosti zapojení motoru

Existují 2 možnosti zapojení motoru:

## Zapojení do hvězdy(Y)

Jedná se o zapojení, kdy jsou konce vinutí jsou spojeny do jednoho uzlu. Na každé fázi je fázové napětí (230 V). Při tomto zapojení má motor nižší rozběhový proud i výkon.

## Zapojení do trojúhelníku(Δ)

Při tomto zapojení jsou jednotlivá vinutí zapojena do série. Na jednotlivých vinutí je pak sdružené napětí Us (400 V), to se počítá dle vzorce:

$$U_{s} = U_{f}.\sqrt[3]{3}$$

Kde Uf je napětí fáze=230 V

[obrázek]

## Měřící přístroj PROVA 6830

[obrázek]

[obrázek]

# Schéma zapojení

[obrázek]

# Použité přístroje

| OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA |
| Analyzátor PROVA | analyzátor sítě | PROVA 6830 | 3207a- CL 226 |  |

# Postup měření

Připojili jsme motor ke svorkám boosteru/regulačního transformátoru pomocí vhodných vodičů. Vybalili jsme analyzátor výkonů a zkontrolovali jsme příslušenství. Zapojení jsme provedli podle doporučeného schématu. Proudové kleště jsme přiložili k propojovacím vodičům tak, aby jimi prokázaly, a napěťové svorky jsme uchytili na vývody motoru. V případě nutnosti jsme použili propojovací můstek. Zapnuli jsme si booster/regulační transformátor a začali jsme měřit od nejnižšího napětí. Po skončení měření jsme nejprve snížili hodnotu napájecího napětí z boosteru na nulu a poté odpojili jsme zdroj od sítě

# 

# Tabulky

[obrázek]

# Příklad výpočtu

## Výpočet celkového činného výkonu:

$$\sum_{}^{}P = P_{L1} + P_{L2} + P_{L3}$$

$$\sum_{}^{}P = 0,098 + 0,117 + 0,106$$

$$\sum_{}^{}P = 0,321\ W$$

## Výpočet celkového jalového výkonu:

$$\sum_{}^{}Q = Q_{L1} + Q_{L2} + Q_{L3}$$

$$\sum_{}^{}Q = 0,71 + 0,740 + 0,699$$

$$\sum_{}^{}Q = 2,149\ VAr$$

## Výpočet celkového zdánlivého výkonu:

$$\sum_{}^{}S = S_{L1} + S_{L2} + S_{L3}$$

$$\sum_{}^{}S = 0,717 + 0,714 + 0,707$$

$$\sum_{}^{}S = 2,138\ VA$$

## Výpočet účiníku:

$$\cos\varphi = \frac{P}{S}\ $$

$$\cos\varphi = \frac{0,321}{2,138}\ $$

$$\cos\varphi = 0,15$$

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

## Fázorový diagram motoru ŠKODA AK 6a Umax=220 V, Imax=11,4 A, Pmax=15 kW

[obrázek]

# Závěr

Při našem měření jsme měřili třífázový motor od cca 20 V do 220 V  fázového napětí. Z měření jsme zjistili, že třífázová soustava funguje tak jak má, protože se snižujícím napětím klesá i v jednotlivých fázích i proud.

Se zvyšujícím se napětí nelineárně roste velikost jalového výkonu, zatímco velikost činného výkonu je téměř konzistentní, To je způsobeno tím, že Motor je tvořen cívkami, které pro svoji práci potřebují vcelku velký jalový výkon.

Při měření nám hodnoty jalového výkonu a fázových posunů vycházely se znaménkem mínus. To však může být způsobeno otočenými kleštěmi směrem od zátěže. A tak jsme pro lepší přehlednost a aby měření odpovídalo realitě vynásobili hodnoty -1.

Fázové posuny rostou cca od hodnoty 30 V. Předtím se motor nedokáže točit, a tak fázové posuny postrádají smysl.

Při harmonické analýze jsme zjistili, že nejvíce je zastoupena na fázi L3 neboli na svorce W 3. harmonická frekvence, která měla velikost amplitudy 13,7 V. U tohoto měření jsme zapomněli naměřit harmonickou analýzu pro ostatní fáze a pro proud. A tak tento bod není úplně zcela splněn.

Fázorový diagram zobrazený na analyzátoru potvrdil symetrii napěťové soustavy (napětí fází V1, V2, V3 svírají úhel 120°), ale zároveň odhalil příčinu nízkého naměřeného účiníku cosϕ = 0,16). Proudové fázory jsou vůči napěťovým výrazně opožděny (fázový posuv cca 80°). což odpovídá silně induktivnímu charakteru motoru. Ten i při nízkém činném výkonu (např. při chodu naprázdno) vyžaduje značný magnetizační proud, který tvoří dominantní jalovou složku výkonu.
