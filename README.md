# LLM React Benchmarking Tool

This project benchmarks multiple large language models (LLMs) on React programming tasks using various prompt engineering techniques. It evaluates the response quality of each model and automates scoring with Claude Opus 4 via OpenRouter.

📄 See the submitted assignment: [assignment-01-solution.md](assignment-01-solution.md)

## ✅ Goals

* Identify the cheapest sufficient model for different programming tasks
* Evaluate how prompt engineering affects performance
* Automate scoring using another LLM (Claude Opus 4)
* Store results in JSON for traceability and structured analysis
* Enable selective and restartable scoring
* Provide result aggregation and comparison

## 📦 Project structure

```
├── main.py                  # Runs prompts through selected LLMs, saves results.json with backup
├── scorer.py                # Scores missing/error results using Claude Opus 4, logs and backs up
├── analyze.py               # Analyzes scored results and prints averages by model and style
├── prompts.json             # List of all benchmark questions and prompt styles
├── models.txt               # List of OpenRouter model names (one per line)
├── results.json             # Output file from benchmark run
├── scored_results.json      # Output file with appended scores
├── scorer.log               # Log file for scoring process and errors
├── .env                     # Contains your OpenRouter API key
├── pyproject.toml           # uv-based project definition
├── .gitignore               # Ignore backups, environments, secrets
```

## 🚀 Setup (Python 3.12 with uv only)

```bash
uv venv
uv add requests python-dotenv pandas
```

Add your API key to `.env`:

```
OPENROUTER_API_KEY=your_api_key_here
```

## 🧪 Run benchmark

```bash
uv run main.py
```

* Runs all prompts × models
* Creates backup of existing `results.json`
* Appends all responses

## 📊 Score results

```bash
uv run scorer.py
```

* Reads from `results.json` or `scored_results.json`
* Skips entries with valid score
* Re-scores entries with `score == "error"`
* Backs up `scored_results.json` before overwrite
* Logs to `scorer.log`

## 📈 Analyze scored results

```bash
uv run analyze.py
```

* Prints average scores by model, prompt style, and combination

## 🧠 Prompt types supported

* `zero-shot`
* `one-shot`
* `few-shot`
* `chain-of-thought`

## 📁 Extend prompts or models

* Add more prompts to `prompts.json`
* Add/remove models in `models.txt`

---

MIT License
