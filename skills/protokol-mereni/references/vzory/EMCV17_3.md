# Teoretický úvod

## Solární panel

Solární panel je tvořen solárními (fotovoltaickými) články, které mohou být tvořeny polovodičovými nebo organickými prvky, které mění elektromagnetickou energii světla v energii elektrickou. Přímou přeměnou světla na elektrickou energii se dnes zabývá samostatná specializace. Fotoelektrický efekt vysvětluje vznik volných elektrických nosičů dopadem záření. Celkově se daří za pomoci křemíkových solárních panelů přeměnit v elektrickou energii jen asi 17 % energie dopadajícího záření. Při použití organických solárních panelů vyvinutých v Izraeli by měla být účinnost až 25 %. Teoretická maximální účinnost pro jeden přechod je 34 % (tzv. Shockley-Queisser limit).

## Měření napětí naprázdno a proudu nakrátko v závislosti na osvětlení a teploty

Při měření napětí naprázdno U0sc.Se používá voltmetr připojení paralelně k FV panelu. V ideálním případě by měl mít voltmetr co nejvyšší vstupní odpor. Moderní digitální přístroje toto splňují, a tak můžeme využít digitální voltmetr s dostatečnou citlivostí, abychom si nevzali voltmetr s rozsahem 6 V ale i s menším

Proud nakrátko by měl být přímo úměrný k intenzitě na osvětlení. Při měření proudu nakrátko musíme uvažovat, že v běžné ampérmetry mají vnitřní odpor, což způsobuje, že na panelu vznikne malé napětí a nejde o "ideální" zkrat. Tuto chybu lze zanedbat, pouze pokud je vnitřní odpor ampérmetru alespoň 100krát menší než sériový odpor článku.

Tuto chybu můžeme obejít početní korekcí, když budeme znát úbytek napětí na ampérmetru, tudíž do obvodu s ampérmetrem musíme přidat i paralelní voltmetr, abychom mohli učit i vnitřní odpor ampérmetru.

$$R_{A} = \frac{I_{A}}{U_{A}}$$

Zde je graf napětí nakrátko a proudu nakrátko v závislosti na osvětlení.

[obrázek]

Jelikož se používá jednota W/m2 musíme hodnotu z luxmetru přepočítat. Víme že pro světlo s vlnovou délkou 550 nm se 1 lux rovná 1,46 mW / m2. Pokud bychom chtěli na ose x W/m2 musíme použít tento přepočet:

$$I_{s}\left\lbrack \frac{W}{m^{2}} \right\rbrack = 0,00146.\ E\lbrack lx\rbrack$$

Měření vlivu teploty na vlastnosti FVČ se měří tak, že při zvolené konstantní intenzitě osvětlení měníme teplotu FVP. Zvolenou konstantní intenzitu osvětlení dosáhneme pevným nastavením vzdálenosti mezi světelným zdrojem a FVP. Hůře se však v běžných podmínkách provádí změna teploty. To lze například vyřešit tím, že FVP ofukujeme teplým vzduchem z pevně uchyceného fénu nebo jiného tepelného zdroje. Plocha FVP by měla být ofukována rovnoměrně. Změnu rychlosti proudění teplého vzduchu lze provádět nastavením rychlosti fénu nebo jiného tepelného zdroje. Při měření dbáme na to, abychom nepřesáhli maximální teplotu, kterou je schopen FVP snést.

Z předchozího je zřejmé, že takto lze měřit spíše FVP o malých rozměrech. U velkoplošných FVP musíme pak použít speciálních přípravků.

## Měření VA charakteristiky

[obrázek]

Při měření VA charakteristiky musíme určit hodnotu odporů na zatěžování dle tohoto vzorce.

$$\frac{U_{0C}}{I_{SC}} \gg Ra + Rb$$

Takto by měla vypadat VA charakteristika

[obrázek]

## Měření výkonové charakteristiky

Výkon, který můžeme z FVP odebírat, závisí na intenzitě osvětlení. Ta se v našem okolí velmi mění, lidské oko je schopno se tomu dobře přizpůsobit, ale FVP je při malém osvětlení téměř nepoužitelný.

Například za jasného slunečného dne je intenzita osvětlení venku až 100 000 luxů, při běžném umělém osvětlení v místnostech bývá intenzita stovky luxů (čemuž se oko dobře přizpůsobí) a hranice, při které člověk začíná rozeznávat obrysy (temná místnost, temná noc), je méně než jeden lux. Lidské oko je tedy schopno pracovat v rozsahu intenzit osvětlení až 6 řádů (jeho citlivost je logaritmická), zatímco výkon fotočlánku klesá s poklesem intenzity osvětlení spíše lineárně.

Když fotočlánek zatěžujeme (odebíráme z něho proud), klesá jeho napětí. To je vlastnost všech reálných zdrojů, ale u fotočlánku je tento pokles poměrně velký, jedná se o „měkký zdroj“. Výkon odebíraný z fotočlánku bude maximální při určitém odebíraném proudu, při menším i větším proudu bude výkon menší. V praxi je tedy nejvýhodnější provozovat fotočlánek právě při takovém proudu.

Takto by měla vypadat výkonová charakteristika. Pod ní je i výkonová charakteristika spojena s VA charakteristikou.

[obrázek]

[obrázek]

Obdobně by vypadala i výkonová charakteristika v závislosti na proudu, jen by se na osu x dal proud.

# Schéma zapojení

## Schéma pro měření napětí na prázdno v závislosti na osvětlení:

[obrázek]

## Schéma pro měření proudu nakrátko v závislosti na osvětlení:

[obrázek]

## Schéma pro měření napětí na prázdno v závislosti na teplotě:

[obrázek]

## Schéma pro měření proudu nakrátko v závislosti na teplotě:

[obrázek]

## Měření VA a výkonových charakteristik:

[obrázek]

# Použité přístroje

| OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA |
| luxmetr | luxmetr | Lutron Lx-101 | 7-4a-AL1635 |  |
| A | ampérmetr, multimetr | MASTECH MS8229 | 6-2052 |  |
| V | voltmetr, multimetr | MASTECH MS8229 | 6-2055 |  |
| Ra,Rb | rezistory | R=1450 Ω | 10-13g | Spojení 2 do 1 |
| teploměr | teploměr | Raytek MiniTemp | 6-6c-2013 |  |
| ZDR | halogen | Ecoplanet Model R6501 U=230V, f=50 Hz | SPŠE4595 |  |

# Postup měření

## Měření vlivu intenzity osvětlení na vlastnosti FVP

Intenzitu osvětlení jsem měřil pomocí luxmetru. Luxmetr udává intenzitu osvětlení v jednotkách lx, častěji je ale intenzitou vyjádřena ve W/m2, musel jsem tedy naměřenou intenzitu luxmetrem přepočítat. Závislost závěrného proudu fotodiody lze vyjádřit obecným vztahem:

[obrázek]

kL je konstanta úměrnosti odpovídající spektrální citlivosti FVP při dopadajícím monochromatickém záření se známou vlnovou délkou. Při konstantním světelném spektru lze vztah upravit do podoby:

[obrázek]

kde Km je maximální hodnota světelné účinnosti monochromatického záření, Is je hodnota celkového slunečního záření. Ze vztahu je zřejmé, že proud nakrátko Isc (fotoelektrický proud) je přímo úměrný intenzitě dopadajícího záření E na fotovoltaický článek (panel). Výsledný vztah je tedy

[obrázek][obrázek]

Jeden lux je ekvivalentní hodnotě výkonu o velikosti 1,46 mW při kolmém dopadu elektromagnetického záření o frekvenci 540 THz, což odpovídá vlnové délce viditelného světla o velikosti 550 nm, která leží ve středu referenčního spektra slunečního záření:

[obrázek]

Před vlastním měřením parametrů FVP je vhodné předem změřit pro jednotlivé vzdálenosti světelného zdroje od FVP intenzitu osvětlení v místě, kde bude umístěn FVP. Dbal jsem na to, aby snímač luxmetru byl v rovině přijímací plochy FVP. To samé jsem udělal před měřením vlivu intenzity osvětlení při šikmém dopadu světla.

FVP je umístěn pod/před zdrojem světla. Intenzitu osvětlení jsem měnil změnou vzdálenosti zdroje světla od FVP. Při měření jsem dodržoval pravidlo pro minimální vzdálenost světelného zdroje od FVP.

## Napětí naprázdno v závislosti na osvětlení

Napětí naprázdno je napětí na svorkách FVP, na který není připojena žádná zátěž. Toto napětí jsem měřil pomocí paralelně připojeného voltmetru, který by měl mít co největší vstupní odpor, aby nedocházelo k zatěžování FVP.

## Proud nakrátko v závislosti na osvětlení

Pokud je vnitřní odpor ampérmetru podstatně menší než sériový odpor FVČ (alespoň 100krát), lze metodickou chybu při měření proudu nakrátko zanedbat. I přesto jsem ho měřil alespoň do poloviny hodnot proudu nakrátko a vypočítal hodnotu vnitřního odporu.

Velikost proudu nakrátko se pohybuje řádově v desítkách *mA,* až jednotek *A*.

## Měření vlivu teploty na vlastnosti FVP 

Měření probíhalo při měření osvětlení, jelikož teplota FV panelu rostla při přibližování halogenu, tudíž osvětlení panelu nebylo konstantí. Bohužel jsme neměli jiný zdroj světla a tak bude muset stačit měření teploty a osvětlení na FV panel.

## Měření VA charakteristiky FV panelu

Voltmetr je zapojen přímo paralelně na svorky měřeného FVČ/FVP, abych neměřil navíc úbytek napětí na sériově zapojeném ampérmetru. Odporovou zátěž je vhodnější složit ze dvou sériově zapojených reostatů pro jemnější nastavení odporu zátěže. Reostaty musí být vhodně vybrány tak, abych mohl, pokud možno proměřit celou charakteristiku a zároveň aby nedošlo k jejich přetěžování ztrátovým výkonem v podobě tepla. Hodnotu zatěžovacího odporu mohu určit například z katalogových hodnot napětí naprázdno a proudu nakrátko u FVP:

[obrázek]

Při dané intenzitě osvětlení pomocí voltmetru jsem změřil napětí naprázdno Uoc při odpojené odporové zátěži (Ra+Rb). Poté jsem odporovou zátěž nastavil na největší odpor. Pomocí změny odporů reostatů odporové zátěže jsem nastavoval rovnoměrně rozložené hodnoty napětí U na svorkách FVP od Uock minimální hodnotě. Pro každou nově nastavenou hodnotu napětí jsem odečetl na ampérmetru proud. Změřil jsem proud nakrátko Isc při zkratované odporové zátěži a kontroloval úbytek napětí na ampérmetru. Do grafu jsem vynesl naměřené hodnoty v závislosti I = fce(U).

## Měření Výkonových charakteristik FV panelu

Měření výkonu proběhlo při měření VA charakteristik, jelikož se výkon počítá dle vzorce.

$$P = U.I$$

Poté jen stačilo udělat grafy v aplikaci MS excel v závislostech P=fce(U) a P=fce(I).

# Tabulky

## Závislost napětí naprázdno na teplotě a osvětlení FV panelu WW10 Maxx P=10 W, Imax=0,54A, Umax=18,57 V

[obrázek]

## Závislost proudu nakrátko na teplotě a osvětlení FV panelu WW10 Maxx P=10 W, Imax=0,54A, Umax=18,57 V

[obrázek]

## Tabulka pro určení vnitřního odporu ampérmetru při měření proudu nakrátko

[obrázek]

## Tabulka pro měření VA a výkonové charakteristiky FV panelu WW10 Maxx P=10 W, Imax=0,54A, Umax=18,57 V při sklonu 16° od plochy 

[obrázek]

## Tabulka pro měření VA a výkonové charakteristiky FV panelu WW10 Maxx P=10 W, Imax=0,54A, Umax=18,57 V při sklonu 6° od plochy 

[obrázek]

## Tabulka pro výpočet odporu FV panelu

[obrázek]

# Příklad výpočtu

## Přepočet E\[lx\] na Is\[W/m2\]: 

$$I_{s} = 0,00146.E$$

$$I_{s} = 0,00146.195$$

$$I_{s} = 0,28\ \ W/m^{2}$$

## Výpočet vnitřního odporu ampérmetru:

$$R_{iA} = \frac{Ua}{I}$$

$$R_{iA} = \frac{3,5.10^{- 3}}{2,64.10^{- 3}}$$

$$R_{iA} = 1,33\ \mathrm{\Omega}$$

## Výpočet maximálního odporu při návrhu Ra+Rb k FV:

$$\frac{U_{0C}}{I_{SC}} \gg Ra + Rb$$

$$\frac{15,09}{3,58.10^{- 3}} \gg Ra + Rb$$

$$4215,1 \gg Ra + Rb$$

Zvolil jsem Ra+Rb=1,3 k

## Výpočet činného výkonu FV panelu:

$$P = U.I$$

$$P = 5.3375.10^{- 6}$$

$$P = 0,02012\ W = 20,12\ mW$$

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

[obrázek]

# Závěr

Měření napětí naprázdno v závislosti osvětlení jsme spojili s měřením vlivu teploty na FV panel, jelikož se panel sám o sobě zahřívá, když je vystaven slunečnímu svitu, nebo v našem případě halogenu. Tudíž měření vlivu teploty na konstantním osvětlení jsme neměřili při konstantním osvětlení, jelikož jsme neměli jiný zdroj tepla než halogen. To jsme také provedli u měření proudu nakrátko.

V charakteristice “Závislost proudu nakrátko na osvětlení FV panelu…“ není konečný bod, jelikož hodnota osvětlení byl mnohonásobně vyšší než předchozí, a tak by zanikl lineární průběh a charakteristika by nevypadala dobře.

U měření proudu nakrátko jsme měli připojený voltmetr alespoň do půlky hodnot, abychom si byli jisti že vnitřní odpor ampérmetru neovlivňuje měření. Nejvyšší odpor ampérmetru nám vyšel 2,23 Ω a proto si myslím že můžeme tuto chybu zanedbat.

Při měření VA charakteristik při různém sklonu jsme měli FV panel nastaven proti oknu, ale nezvyšovali jsme nijak osvětlení. Nastavení sklonu jsme dělali pomocí zarážek na nohách FV panelu. Nohy mají v maximálních polohách buď sklon 16° nebo 6°. Tyto sklony jsme zjistili pomocí gyroskopu zabudovaném v mobilním telefonu spolužáka Miroslava Černého. Díky tomuto nám byl ulehčen způsob určení sklonu pomocí goniometrických funkcí sin, cos, tg.

VA charakteristiky se nepodobají těm v teoretickém úvodu. Sice vypadají velmi drasticky, ale musíme vzít v potaz, že maximální napětí jsme měli 5 V a to je 1/3 napětí naprázdno (15,09 V), a tak jsme nebyli schopni proměřit celou charakteristiku. Pokles proudu vypadá velmi vysoký, ale jedná se o pokles v řádu jednotek až desítek mikroampér.

FV panel měl vždy největší napětí naprázdno nebo proud nakrátko při co největším osvětlení, tedy v našem případě 103 000 luxů. Velmi podobně se pak napětí i proud chovalo i při změně teploty.

Vyšší proud jsme zaznamenali při menším sklonu od plochy a to při sklonu 6°.
