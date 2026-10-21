# skill_set_protokoly

Knihovna Claude skillů pro tvorbu **protokolů o měření (elaborátů)** z praktických cvičení
VOŠ a SPŠE Plzeň (EM, ESO …).

Stačí poslat **zadání + naměřené hodnoty (+ přístroje)** a skill sestaví hotový Word `.docx`:
teoretický úvod, schémata podle normy, tabulku přístrojů, postup, tabulky, příklady výpočtu
s rovnicemi Wordu, grafy přes celou A4 s proložením a okótováním a závěr. Desky si autor dělá sám.

## Obsah repa

```
skills/
  protokol-mereni/            ← skill (formát Claude Agent Skills)
    SKILL.md                  ← instrukce + postup
    references/               ← pravidla školy, styl, grafy, schémata, vzorové elaboráty (text)
    scripts/                  ← protokol.py (docx), graf.py, schema.py, kontrola.py
podklady/
  elaboraty/                  ← originální vzorové elaboráty (.docx)
  Zasady2026.pdf              ← Zásady pro zpracování a hodnocení protokolů
  Zpracovani_protokolu_o_mereni.pptx
evals/                        ← testovací zadání pro ověření skillu
.claude-plugin/marketplace.json
```

## Instalace

**Claude.ai / desktop app:** zabal složku `skills/protokol-mereni` do ZIPu
(`cd skills && zip -r protokol-mereni.zip protokol-mereni`) a nahraj v *Settings → Capabilities → Skills*.

**Claude Code:**
```bash
/plugin marketplace add mlnamata/skill_set_protokoly
/plugin install protokoly@skill_set_protokoly
```
nebo zkopíruj `skills/protokol-mereni` do `~/.claude/skills/`.

## Závislosti (při běhu skillu)

Python 3 s `python-docx`, `matplotlib`, `numpy`, `scipy`, `schemdraw`, `openpyxl` a `pandoc`
(převod LaTeX rovnic na nativní rovnice Wordu). Skill si chybějící balíčky doinstaluje.

## Použití

> „Udělej mi elaborát z CV16, zadání a naměřené hodnoty posílám.“

Výstup: `EM_CV16_….docx` + seznam míst k doplnění (žlutě zvýrazněno – např. chybějící evidenční čísla).
