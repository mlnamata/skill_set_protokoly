> **HLAVNÍ VZOR STYLU** – Matyášův vlastní protokol CV1 (reproduktory). Vzhled, členění a hustota textu,
> které má mít každý nový protokol. Text nekopírovat.

## 1.1 Zvuk a jeho parametry

Zvuk je **mechanické vlnění pružného prostředí**, které vyvolává sluchový vjem. Ve vzduchu se šíří jako **podélné vlnění** (zhušťování a zřeďování částic), ve vakuu se nešíří. Ucho vnímá kmitočty přibližně **16 Hz až 20 kHz**, pod nimi je infrazvuk, nad nimi ultrazvuk.

- **Kmitočet f \[Hz\]** určuje výšku tónu; s vlnovou délkou souvisí vztahem $\lambda = c/f$ (ve vzduchu 17 m až 17 mm).
- **Rychlost šíření c \[m/s\]** – ve vzduchu $c \approx 331,4 + 0,6 \cdot \vartheta$, při 20 °C **c ≈ 343 m/s**.
- **Akustický tlak p \[Pa\]** – střídavá složka tlaku superponovaná na atmosférický tlak. Práh slyšení **p₀ = 2·10⁻⁵ Pa**, práh bolesti asi 20–60 Pa.
- **Hladina akustického tlaku Lₚ \[dB\]** (SPL) – logaritmická míra odpovídající vnímání sluchu:

$$L_{P} = 20 \cdot \log\frac{p}{p_{0}}\ \ \left\lbrack \text{dB} \right\rbrack$$

Práh slyšení = 0 dB, rozhovor ≈ 60 dB, práh bolesti ≈ 120–130 dB. Zvukoměr měří lineárně nebo přes váhový filtr A (dB(A)).

**Závislost na vzdálenosti a příkonu:** U bodového zdroje ve volném poli klesá akustický tlak nepřímo úměrně vzdálenosti – **každé zdvojnásobení vzdálenosti sníží hladinu o 6 dB**. Dvojnásobný příkon zvýší hladinu o 3 dB:

$$L_{P2} = L_{P1} + 10 \cdot \log\frac{P_{2}}{P_{1}}\ \ \left\lbrack \text{dB} \right\rbrack$$

V místnosti se přičítá odražený zvuk, takže skutečný pokles se vzdáleností je menší.

## 1.2 Elektroakustické měniče

Elektroakustické měniče přeměňují **elektrickou energii na akustickou** (reproduktory, sluchátka) nebo naopak (mikrofony). Přeměna probíhá přes kmitající mechanický systém – membránu.

- **Podle principu:** *elektrodynamické* (cívka v poli magnetu, síla F = B·l·I – nejrozšířenější), *elektromagnetické* (feromagnetická kotva), *elektrostatické* (membrána mezi elektrodami), *piezoelektrické* (deformace krystalu), *magnetostrikční*.
- **Podle vyzařování:** *přímovyzařující* (kónusové, kalotové – malá účinnost) a *tlakové (horní)* – membrána pracuje do tlakové komory a zvuk vychází zvukovodem (horní), která působí jako akustický transformátor a zvyšuje účinnost (např. **HS30**).
- **Podle kmitočtu:** *hloubkové* (woofer, cca 20 Hz – 1 kHz), *středotónové* (300 Hz – 5 kHz), *výškové* (tweeter, 2–20 kHz), *širokopásmové*.
- **Podle impedance:** *nízkoimpedanční* **4, 8, 16 Ω** a *pro 100V rozhlasové rozvody* s vestavěným transformátorem, kde impedance závisí na zvolené odbočce příkonu: $Z = U^{2}/P$

## 1.3 Konstrukce elektrodynamického reproduktoru

[obrázek]

Řez elektrodynamickým reproduktorem

- **Magnetický obvod** – permanentní magnet (ferit, neodym), pólové nástavce a středový sloupek soustřeďují magnetický tok do úzké **vzduchové mezery**.
- **Kmitací cívka** na nosiči – leží ve vzduchové mezeře, protéká jí proud zesilovače a působí na ni síla **F = B·l·I**.
- **Membrána (kónus)** – spojená s cívkou, rozkmitává vzduch; lehká a tuhá (papír, polypropylen, hliník).
- **Závěs membrány a středicí membrána** – pružně drží membránu a vystřeďují cívku v mezeře.
- **Prachovka** chrání mezeru před nečistotami, **koš** nese celou konstrukci a svorky.

## 1.4 Parametry reproduktorů

- **Jmenovitá impedance Zₙ \[Ω\]** – impedance reproduktoru se mění s kmitočtem. Zₙ odpovídá **minimu impedance nad rezonancí** (bývá 1,1–1,3× odpor vinutí RDC). K vyšším kmitočtům impedance roste vlivem indukčnosti cívky.
- **Rezonanční kmitočet fₛ \[Hz\]** – vlastní rezonance kmitajícího systému (hmotnost *m* membrány a poddajnost *C* závěsu), $f_{s} = \frac{1}{2\pi\sqrt{mC}}$. Projeví se **ostrým maximem impedance** a určuje dolní mez přenášeného pásma. V uzavřené ozvučnici se fₛ zvyšuje.
- **Charakteristická citlivost Lₛ \[dB/W, 1 m\]** – hladina akustického tlaku v ose ve vzdálenosti 1 m při příkonu 1 W. Z měření: $L_{S} = L_{P1} - 10 \cdot \log P_{1}$. Hladina v libovolné vzdálenosti: $L_{P} = L_{S} + 10 \cdot \log P - 20 \cdot \log l$.
- **Kmitočtová charakteristika** – závislost Lₚ = f(f) při konstantním příkonu; určuje kmitočtový rozsah.
- **Směrová charakteristika** – závislost Lₚ na úhlu od osy (polární diagram). S rostoucím kmitočtem (λ srovnatelná s průměrem membrány) se vyzařování zužuje do osy.
- **Příkon \[W\]** – jmenovitý (RMS, trvalý), hudební a špičkový.
- **Účinnost** – přímovyzařující reproduktory jen **0,5–2 %**, tlakové **10–30 %**. **Zlepšení:** silnější magnet a užší mezera, lehčí membrána, horna s tlakovou komorou, vhodná ozvučnice.

## 1.5 Reproduktorové soustavy, ozvučnice a akustický zkrat

**Reproduktorová soustava** je sestava několika reproduktorů pro různá pásma (hloubkový, středový, výškový) ve společné ozvučnici. **Kmitočtová výhybka** (LC filtr) rozděluje signál tak, aby každý reproduktor dostával jen kmitočty, které umí přenést.

**Akustický zkrat:** Přední a zadní strana membrány vyzařují vlny **v protifázi**. Na nízkých kmitočtech (λ velká vůči rozměrům) vzduch obteče okraj membrány, tlaky se vyrovnají a hloubky zaniknou.

**Ozvučnice** odděluje přední a zadní stranu membrány, a tím zabraňuje akustickému zkratu. Typy: plošná deska, otevřená skříň, **uzavřená** (zvyšuje fₛ), **basreflex** (využívá zadní vlnu přes nátrubek) a **hornová** (zvyšuje účinnost a směrovost).

#  Schéma zapojení

[obrázek][obrázek]

#  Použité přístroje

| Označení ve schématu | Název, funkce | Typ, rozsah       | Evidenční (výrobní) číslo | poznámka   |
|----------------------|---------------|-------------------|---------------------------|------------|
| zvukoměr             | zvukoměr      | CEM dt-8852       | NO.09090801               |            |
| A1                   | ampérmetr     | UNI-T UT803       | 10-7a-1920                |            |
| V1                   | voltmetr      | TESLA BM579       | 3207-4a                   |            |
| G                    | Generátor     | METEX MS-9140     | 3207-14a-cl141            |            |
| V2                   | Voltmetr      | Laboratorní       |                           | Zabudovaný |
| A2                   | ampérmetr     | UNI-T UT804       | 10-9-1861                 |            |
| G                    | Generátor     | GoldStar FG-2002C | 6-3                       |            |

# Postup měření

## 4.1 Impedanční charakteristika hloubkového a výškového reproduktoru

Impedanci jsme měřili **voltampérovou metodou**. Reproduktor jsme připojili k nízkofrekvenčnímu generátoru s **nízkou výstupní impedancí**, do série jsme zařadili ampérmetr a paralelně ke svorkám reproduktoru nízkofrekvenční milivoltmetr (viz schéma zapojení). Reproduktor byl při měření volně uložen (bez ozvučnice), aby nebyl ovlivněn rezonanční kmitočet.

Protože běžné ampérmetry nemají dostatečný kmitočtový rozsah, využili jsme k měření proudu **druhý nf voltmetr**: do série s reproduktorem jsme zařadili **snímací (bočníkový) rezistor známé hodnoty R** (např. 1 Ω, bezindukční) a měřili úbytek napětí *U*R na něm. Proud jsme vypočítali podle Ohmova zákona:

$$I = \frac{U_{R}}{R}\ \ \left\lbrack \text{A} \right\rbrack$$

Na generátoru jsme při každém kmitočtu doregulovali výstupní napětí tak, aby **proud zůstával konstantní** (I = konst.). Impedance je pak přímo úměrná napětí na reproduktoru:

$$Z = \frac{U}{I}\ \ \lbrack\Omega\rbrack$$

Kmitočet jsme měnili v rozsahu cca **20 Hz až 20 kHz** s logaritmickým krokem. **V okolí vlastní rezonance** (u hloubkového reproduktoru desítky Hz, u výškového stovky Hz až jednotky kHz) jsme kmitočet měnili **velmi jemně**, protože rezonance se projeví prudkým nárůstem napětí (impedance) v úzkém pásmu a při hrubém kroku by nebyla zachycena. Maximum jsme dohledali a zaznamenali kmitočet **fₛ** a hodnotu **Z**max. Dále jsme zhustili měření v oblasti **minima impedance** nad rezonancí, kde jsme odečetli **jmenovitou impedanci Zₙ**. Směrem k vyšším kmitočtům jsme ověřili opětovný nárůst impedance.

Stejný postup jsme zopakovali pro výškový reproduktor. U něj jsme nastavovali jen malé napětí a nepouštěli na něj nízké kmitočty s velkou amplitudou, aby nedošlo k jeho poškození. Naměřené hodnoty jsme zapsali do tabulky a vynesli do grafů Z = f(f) s logaritmickou osou kmitočtu, ve kterých jsme vyznačili fₛ a Zₙ.

## 4.2 Vstupní impedance tlakového reproduktoru HS30 při 1 kHz

Tlakový reproduktor HS30 jsme zapojili stejnou VA metodou. Na zadní straně reproduktoru jsme zjistili nastavenou odbočku (příkon) a odpovídající jmenovitou impedanci. Na generátoru jsme nastavili kmitočet **f = 1 kHz**, změřili napětí *U* a proud *I* a vypočítali **Z = U / I**. Naměřenou hodnotu jsme **ihned porovnali s údajem výrobce** (případně s hodnotou vypočtenou ze vztahu Z = U²/P pro 100V rozvod), abychom včas odhalili chybné zapojení nebo nastavení odbočky.

## 4.3 Amplitudová kmitočtová charakteristika HS30

Reproduktor HS30 jsme napájeli z generátoru přes výkonový zesilovač. **Zvukoměrný mikrofon** jsme umístili **do osy reproduktoru ve vzdálenosti 1 m** ve stejné výšce jako střed ústí horny. Před měřením jsme změřili hladinu hluku pozadí, která byla alespoň o 10 dB nižší než měřené hladiny. Na zvukoměru jsme nastavili lineární (případně váhový filtr C) a časovou konstantu *Slow*.

Při měření jsme udržovali **konstantní příkon** reproduktoru *P*₁ (kontrolou napětí a proudu na jeho vstupu, P = U·I). Kmitočet jsme měnili v rozsahu přibližně **200 Hz až 12 kHz** (výrobcem udávaný rozsah je 400 až 10 000 Hz) a pro každý kmitočet jsme zaznamenali hladinu akustického tlaku *L*ₚ. Výsledky jsme vynesli do grafu *L*ₚ = f(f) s logaritmickou osou kmitočtu.

## 4.4 Hladina akustického tlaku ve vzdálenosti 1 m a 2 m

Při kmitočtu **1 kHz** a nezměněném příkonu jsme změřili hladinu *L*ₚ ve vzdálenosti **1 m** a následně po posunutí mikrofonu v ose reproduktoru ve vzdálenosti **2 m**. Hodnotu pro 2 m jsme ověřili výpočtem:

a rozdíl mezi naměřenou a vypočtenou hodnotou jsme zdůvodnili vlivem odrazů v místnosti.

## 4.5 Výpočet charakteristické citlivosti

Z hladiny naměřené ve vzdálenosti 1 m při příkonu *P*₁ jsme přepočtem na příkon 1 W určili **charakteristickou citlivost**:

a porovnali ji s údajem výrobce (108 dB). Následně jsme vypočítali hladinu akustického tlaku v zadané vzdálenosti *l* při zadaném příkonu *P*:

Při výpočtech jsme neuvažovali vliv odraženého zvuku.

## 4.6 Směrová charakteristika HS30

Směrovou charakteristiku jsme měřili ve **zvukotěsné místnosti za naprostého klidu**. Reproduktor i zvukoměrný mikrofon byly ve **stejné výšce** a ve vzdálenosti **1 m** od sebe. Na svorkách reproduktoru jsme udržovali **konstantní napětí** *U*₁. Mikrofonem jsme postupně otáčeli kolem reproduktoru **po 30°** v rozsahu 0° až 360° (0° = osa reproduktoru) a v každé poloze jsme odečetli hladinu *L*ₚ.

Měření jsme provedli pro **dva kmitočty** zvolené podle naměřené kmitočtové charakteristiky (např. 1 kHz a 5 kHz). Naměřené hodnoty jsme zapsali do tabulky, přepočítali relativně k hodnotě v ose (0 dB) a vynesli do **polárních diagramů**. Z porovnání obou diagramů jsme posoudili, jak se směrovost reproduktoru mění s kmitočtem.

# 

# Tabulky

**1) Impedance hloubkového reproduktoru ARN 5608** I = konst. = 15 mA, Z = U / I

| **f \[Hz\]** | **20** | **30** | **40** | **50** | **60** | **65** | **70** | **71,5** | **72,5** | **75** | **80** | **82,5** | **85** | **90** | **95** | **100** | **110** | **120** | **130** | **140** | **150** | **175** | **200**  | **250**  | **300** | **400** | **500** |
|--------------|--------|--------|--------|--------|--------|--------|--------|----------|----------|--------|--------|----------|--------|--------|--------|---------|---------|---------|---------|---------|---------|---------|----------|----------|---------|---------|---------|
| **U \[mV\]** | 102    | 129    | 139    | 165    | 210    | 259    | 318    | 375      | 399      | 420    | 410    | 390      | 330    | 310    | 290    | 240     | 190     | 160     | 148     | 141     | 135     | 130     | 125      | 125      | 129     | 135     | 140     |
| **Z \[Ω\]**  | 6,8    | 8,6    | 9,27   | 11     | 14     | 17,27  | 21,2   | 25       | 26,6     | **28** | 27,33  | 26       | 22     | 20,67  | 19,33  | 16      | 12,67   | 10,67   | 9,87    | 9,4     | 9       | 8,67    | **8,33** | **8,33** | 8,6     | 9       | 9,33    |

**2) Impedance výškového reproduktoru ARV 104-60** I = konst. = 15 mA, Z = U / I

| **f \[Hz\]** | **800** | **900** | **920** | **940** | **960** | **980** | **1000** | **1020** | **1040** | **1060** | **1080** | **1100** | **1120** | **1140** | **1160**  | **1180** | **1200** | **1220** | **1240** | **1260** | **1280** | **1300** | **1400** | **1500** | **1600** | **1700** | **1800** | **1900** | **2000** |
|--------------|---------|---------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| **U \[mV\]** | 150     | 160     | 170     | 180     | 186     | 195     | 203      | 221      | 231      | 244      | 268      | 280      | 300      | 305      | 310       | 290      | 280      | 272      | 260      | 240      | 225      | 220      | 181      | 179      | 163      | 129      | 129      | 129      | 129      |
| **Z \[Ω\]**  | 10      | 10,67   | 11,33   | 12      | 12,4    | 13      | 13,53    | 14,73    | 15,4     | 16,27    | 17,87    | 18,67    | 20       | 20,33    | **20,67** | 19,33    | 18,67    | 18,13    | 17,33    | 16       | 15       | 14,67    | 12,07    | 11,93    | 10,87    | **8,6**  | **8,6**  | **8,6**  | **8,6**  |

**Vyznačeno:** ARN 5608 – fₛ = 75 Hz (Zmax = 28 Ω), Zₙ = 8,33 Ω; ARV 104-60 – fₛ = 1 160 Hz (Zmax = 20,67 Ω), Zₙ = 8,6 Ω

**4) Amplitudová kmitočtová charakteristika tlakového reproduktoru HS30** P₁ = konst. = 16 mW, l = 1 m

| **f \[Hz\]**  | **265** | **500** | **750** | **1 000** | **2 000** | **3 000** | **4 000** | **5 000** | **6 000** | **7 000** | **8 000** | **9 000** | **10 000** | **11 000** | **12 000** | **13 000** | **14 000** | **15 000** |
|---------------|---------|---------|---------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------------|------------|------------|------------|------------|------------|
| **Lₚ \[dB\]** | 45      | 60      | 74,5    | 75,8      | 78,2      | 76,5      | 75,7      | 66,9      | 67,2      | 67,7      | 58,1      | 60,7      | 65,5       | 58,9       | 52,4       | 42         | 38,8       | 36,6       |

**4) Hladina akustického tlaku při f = 1 kHz** P₁ = 16 mW

| **l \[m\]**   | 1 (naměřeno) | 2 (naměřeno) | 2 (vypočteno) |
|---------------|--------------|--------------|---------------|
| **Lₚ \[dB\]** | 75,8         | 72,3         | 69,78         |

**6) Směrová charakteristika tlakového reproduktoru HS30** l = 1 m

| **α \[°\]**                             | **0** | **30** | **60** | **90** | **120** | **150** | **180** | **210** | **240** | **270** | **300** | **330** |
|-----------------------------------------|-------|--------|--------|--------|---------|---------|---------|---------|---------|---------|---------|---------|
| **Lₚ \[dB\] – f = 800 Hz, U₁ = 5,46 V** | 70,6  | 69,1   | 67,8   | 68,1   | 63,8    | 59,1    | 61,1    | 55,6    | 63,3    | 59,3    | 65,1    | 68,3    |
| **Lₚ \[dB\] – f = 8 kHz, U₁ = 3,8 V**   | 68    | 53,5   | 46,5   | 41     | 44,8    | 43      | 35,13   | 41,8    | 33,5    | 29      | 34,8    | 46,5    |

# Příklad výpočtu

[obrázek]

#  Grafy

# [obrázek]

# [obrázek]

# [obrázek]

# [obrázek]

# [obrázek][obrázek]

#  Závěr

Změřili jsme impedanční charakteristiky hloubkového reproduktoru ARN 5608 a výškového reproduktoru ARV 104-60.

- **ARN 5608:** rezonance vyšla při **55 Hz** (Zmax = **21 Ω**), výrobce udává **35 Hz**. Jmenovitá impedance vyšla **10 Ω**, výrobce udává **8 Ω**.
- **ARV 104-60:** rezonance vyšla při **800 Hz** (Zmax = **22,5 Ω**), výrobce udává **1 250 Hz**. Jmenovitá impedance vyšla **9 Ω**, výrobce udává **4 Ω**.

Rozdíly jsou způsobeny nepřesným udržováním konstantního proudu, přesností milivoltmetru a vestavěním reproduktorů v ozvučnici, která posouvá rezonanci.

Kmitočtová charakteristika tlakového reproduktoru HS30 má maximum **80,8 dB při 1 250 Hz**. Pod 400 Hz a nad 6,3 kHz hladina výrazně klesá, což odpovídá rozsahu 400–10 000 Hz, který udává výrobce.

Ve vzdálenosti 2 m jsme naměřili **74,9 dB**, výpočtem vyšlo **74,38 dB**. Rozdíl 0,52 dB potvrzuje pokles o 6 dB při zdvojnásobení vzdálenosti.

Charakteristická citlivost vyšla **97,85 dB/W, 1 m**, výrobce udává **108 dB**. Rozdíl je dán velmi malým příkonem při měření (18 mW) a odrazy v místnosti. Ve vzdálenosti 10 m při příkonu 15 W očekáváme hladinu **89,61 dB**.

Směrová charakteristika při 8 kHz je výrazně úzká: v ose jsme naměřili **68 dB**, při 90° hladina klesla o **27 dB** a za reproduktorem (180°) o **32,87 dB**. HS30 je proto vhodný pro směrové ozvučení venkovních prostor a pro rozhlasové rozvody.
