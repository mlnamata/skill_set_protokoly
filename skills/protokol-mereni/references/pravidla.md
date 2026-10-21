# Pravidla školy pro protokoly (VOŠ a SPŠE Plzeň)

Shrnutí dokumentu *Zásady pro jednotné zpracování a hodnocení protokolů z praktických cvičení
v odborných předmětech* (katedra ODP, Ing. Karel Hajžman) a studentské prezentace
*Zpracování protokolu o měření* (K. Klasnová, 3.T). Originály jsou v repu v `podklady/`.

## Obsah

1. Obecná pravidla
2. Povinné části a jejich pořadí
3. Požadavky na jednotlivé části
4. Co vrací vyučující nejčastěji
5. Odevzdání a hodnocení

---

## 1. Obecná pravidla

- Protokol se odevzdává **za 1 týden** na dalším cvičení. Musí splnit požadavky zadání a kritéria
  technické dokumentace **alespoň z 90 %**, jinak se vrací k přepracování (i opakovaně).
- **Všechny listy očíslované a podepsané** → v elektronické verzi záhlaví „Jméno Příjmení“ vlevo
  a číslo stránky vpravo na každé straně (kromě desek). Počet listů na deskách je **bez desek**.
- Pokud žák na měření nebyl, použije hodnoty své skupiny a na protokol uvede poznámku **„NEMĚŘIL“**.
- Tiskne se jednostranně, nejlépe **černobíle** (grafy musí být čitelné i v ČB).
- Teoretický úvod a závěr musí být **vlastními slovy** – shodné práce = „nedostatečně“ (plagiát).
  Vyučující si pamatují formulace z Wikipedie i protokoly starších ročníků.
- Desky (titulní list A3) si žák vyplňuje sám – stahují se z Filru
  (`VOŠ_a_SPŠE → katedra_odp → ELEKTROTECHNIKA → Desky na protokoly z odborných předmětů`).

## 2. Povinné části a jejich pořadí

Pořadí odpovídá seznamu „Kontrola vypracování protokolu“ na zadní straně desek:

1. **Teoretický úvod** (Teoret. úvod)
2. **Schéma zapojení**
3. **Použité přístroje**
4. **Postup měření**
5. **Tabulky** (naměřené a vypočítané hodnoty)
6. **Příklad výpočtu** (Příklady výpočtů)
7. **Grafy** (grafické znázornění)
8. **Závěr**
9. **Originál hodnot** – podepsaný papír/sešit nebo printscreen z PC; vkládá žák fyzicky (ne generovat).

Zadání je přepsané na deskách (žák si dělá sám).

## 3. Požadavky na jednotlivé části

### Teoretický úvod
- Týká se přímo zadání, rozsah **2–3 strany**.
- Vychází z bodů „**Uveďte**“ v podkladech k úloze a z bodů zadání: funkce a vlastnosti použitých
  součástek, obvodů a metod, princip měření, účel měření.
- Může být proložen obrázky – korektní popis os, jednotky, správné průběhy, rozumná velikost.
- Na konci uvést **použitou literaturu**; u internetu konkrétní stránky.
- Musí být srozumitelný pro autora i jiného čtenáře.

### Schéma zapojení
- **Vlastní výtvor** – nesmí být kopie/sken z literatury, podkladů ani internetu.
- Značky součástek **vždy podle normy** (ČSN EN 60617 / IEC).
- Žák musí umět vysvětlit funkci zapojení; na žádost dodá zdrojový soubor (u nás Python/schemdraw).

### Použité přístroje
- Tabulka s 5 sloupci:
  `OZNAČENÍ VE SCHÉMATU | NÁZEV, FUNKCE (jak jsme přístroj využili) | TYP, ROZSAH | EVIDENČNÍ (VÝROBNÍ) ČÍSLO | POZNÁMKA`
- Musí obsahovat typ přístroje s rozsahy a inventární (evidenční) číslo.
- Označení ve schématu musí sedět se schématem.

### Postup měření
- Sestaven podle teoretického úvodu a doporučeného postupu z podkladů, **přepsán do minulého času**
  („zapojili jsme…“, „nastavili jsme…“).
- S odkazem na **skutečně použité přístroje**; změny a odchylky oproti zadání uvést v pokračování
  postupu nebo v závěru.

### Naměřené a vypočítané hodnoty (Tabulky)
- Kompletní tabulky s rámečky, **jednotky u všech veličin**.
- Každá tabulka má **název**, který vypovídá, co se měřilo (a na čem – součástka + parametry).
- U **nelineárních charakteristik minimálně 15 naměřených hodnot** (pokud zadání neříká jinak).
- Hodnoty zaokrouhlit na reálně měřenou přesnost (nepsat 8 desetinných míst z Excelu).
- Rozlišit naměřené / vypočítané hodnoty, případně aritmetický průměr.

### Příklad výpočtu
- **Obecné vztahy** potřebné pro výpočet + **samostatný výpočet všech požadovaných hodnot s dosazením**.
- Ke každému výpočtu napsat, co se počítá (nadpis „Výpočet …“).
- Dosazovat hodnoty, které jsou skutečně v tabulkách.

### Grafy
- Celá strana A4 na jeden graf, **nikdy dva grafy pod sebou na jedné stránce**.
- Rastr (podrobná mřížka) umožňující odečíst libovolnou hodnotu; čitelný po tisku.
- Osy: měřená veličina + jednotka + měřítko.
- **Název grafu nahoře** s konkrétní charakteristikou a **součástkou/zapojením a jejími parametry**.
- Parametrické závislosti: parametr u křivky nebo v legendě; **legenda pod grafem**.
- **Body grafu čitelně vyznačené** (křížky, tečky); průběh **proložený** křivkou/přímkou (ne lomená čára
  bod-bod, pokud to nemá fyzikální smysl).
- Řady rozlišitelné podle legendy i v ČB (různé značky a styly čar).
- Sloupcové grafy: pojmenované sloupce, rozumné měřítko; nevyhovující sloupec lze uříznout/smazat,
  ale **důvod napsat do závěru**. Jmenovitou hodnotu a toleranci vyznačit.
- Z grafu se často pozná chyba měření (nečekaný propad) – komentovat v závěru.

### Závěr
- **Porovnání výsledků s teoretickými předpoklady** z teoretického úvodu, možné chyby měření,
  posouzení vhodnosti přístrojů, zdůvodnění odchylek od teorie.
- Často je v zadání přímo napsáno, co má závěr obsahovat – to musí být splněno bod po bodu.
- Vlastními slovy, konkrétně s čísly.
- **Zakázané prázdné fráze**: „Měření probíhalo dle očekávání“, „Naměřené hodnoty odpovídají
  teoretickým předpokladům“ (bez konkrétního rozboru) → protokol se vrací.
- Co se nepovedlo, se do závěru také píše (např. nezměřený bod zadání a proč).

## 4. Co vrací vyučující nejčastěji

1. Grafy (chybí název s parametry, chybí rastr, body, proložení, dva grafy na straně, barvy nečitelné v ČB).
2. Teoretický úvod zkopírovaný z internetu.
3. Neúplná tabulka přístrojů (chybí evidenční čísla, rozsahy).
4. Tabulky bez jednotek / bez názvu / nesmyslný počet desetinných míst.
5. Prázdný závěr („vše proběhlo dle očekávání“).
6. Výpočty bez dosazení.

Konkrétní připomínka vyučujícího (zapsaná dříve): **body grafu musí být proloženy křivkou/přímkou
a vnitřní odpor Ri se určuje z proložené přímky s ΔU/ΔI okótovanými přes celý rozsah**.

## 5. Odevzdání a hodnocení

- Sada úloh se klasifikuje celkovou známkou (váha = písemná práce) podle obsahové a grafické kvality
  a včasnosti odevzdání.
- Nedodaný protokol → ústní přezkoušení + ruční zpracování.
- Některé (zejména maturitní) úlohy se zpracovávají **ručně** – pak skill připraví podklad
  (výpočty, grafy, text), který si žák přepíše/překreslí na milimetrový papír.
