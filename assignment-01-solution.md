Závěrečné hodnocení – Benchmarking LLM v oblasti programování (React)
=====================================================================

V rámci úkolu jsem si stanovil cíl porovnat výkon různých velkých jazykových modelů (LLM) při řešení programovacích úloh při programování ve js frameworku React. Cílem bylo získat přehled o vhodnosti jednotlivých modelů pro účely co nejlevnějšího řešení běžných každodenních programovacích tasků.

Postup řešení
-------------

- Připravil jsem testovací sadu pěti otázek (Q1–Q5), zaměřenou na běžné chyby a koncepty v Reactu v souboru prompts.json.
 
- Každou otázku jsem formuloval ve čtyřech variantách: zero-shot, one-shot, few-shot a chain-of-thought.

- Pro testování modelů jsem využil platformu OpenRouter a modely specifikoval v souboru models.txt.

- Všechny odpovědi jsem nechal automaticky ohodnotit modelem Claude Opus 4, který vrací skóre v rozsahu 1–5.

- Výsledným souborem je pak [scored_results.json](scored_results.json).

Automatizace
------------

- Skript main.py spouští všechny kombinace modelů a promptovacích stylů a ukládá výsledky do results.json (starší výstup se vždy zálohuje).

- Skript scorer.py načte výstupy a pomocí LLM je vyhodnotí podle předdefinovaného hodnoticího promptu.

Shrnutí
-------

Řešení plně odpovídá zadání:

- Pokrývá různé strategie prompt engineeringu

- Umožňuje porovnat více modelů z hlediska nákladů a přesnosti

- Je snadno rozšiřitelné o další otázky i modely

Celý projekt je připraven k dalšímu použití nebo rozšíření pro jiné domény i hlubší analýzu.

Adresa projektu: 

