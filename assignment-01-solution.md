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

Adresa projektu: https://github.com/matak/llm-react-benchmark


Finální výstup:

Average score by model:
model
google/gemini-pro-1.5              4.70
mistralai/mixtral-8x7b-instruct    4.00
meta-llama/llama-3-70b-instruct    3.75
openai/gpt-3.5-turbo               3.75
openai/gpt-4                       3.45
Name: score, dtype: float64

Average score by prompt style:
style
zero-shot           4.36
one-shot            4.08
chain-of-thought    3.96
few-shot            3.32
Name: score, dtype: float64

Average score by model and style:
style                            chain-of-thought  few-shot  one-shot  zero-shot
model
google/gemini-pro-1.5                         4.6       4.8       4.6        4.8
meta-llama/llama-3-70b-instruct               4.0       2.4       4.0        4.6
mistralai/mixtral-8x7b-instruct               3.6       4.0       4.0        4.4
openai/gpt-3.5-turbo                          3.4       3.6       4.2        3.8
openai/gpt-4                                  4.2       1.8       3.6        4.2