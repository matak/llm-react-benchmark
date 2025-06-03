# LLM React Benchmarking Tool

This project benchmarks multiple large language models (LLMs) on React programming tasks using various prompt engineering techniques. It evaluates the response quality of each model and automates scoring with Claude Opus 4 via OpenRouter.

## ✅ Goals
- Identify the cheapest sufficient model for different programming tasks
- Evaluate how prompt engineering affects performance
- Automate scoring using another LLM (Claude Opus 4)
- Store results in JSON for traceability and structured analysis

## 📦 Project structure
```
├── main.py                  # Runs prompts through selected LLMs, saves results.json with backup
├── scorer.py                # Scores results using Claude Opus 4, writes to scored_results.json
├── prompts.json             # List of all benchmark questions and prompt styles
├── models.txt               # List of OpenRouter model names (one per line)
├── results.json             # Output file from benchmark run
├── scored_results.json      # Output file with appended scores
├── .env                     # Contains your OpenRouter API key
├── pyproject.toml           # uv-based project definition
├── .gitignore               # Ignore backups, environments, secrets
```

## 🚀 Setup (Python 3.12 with uv only)
```bash
uv venv
uv add requests python-dotenv
```

Add your API key to `.env`:
```
OPENROUTER_API_KEY=your_api_key_here
```

## 🧪 Run benchmark
This will:
- Load prompts from `prompts.json`
- Load models from `models.txt`
- Backup `results.json` if it exists
- Write all outputs to `results.json`
```bash
uv run main.py
```

## 📊 Score results
This will:
- Read `results.json`
- Score each response using `anthropic/claude-opus-4`
- Save output to `scored_results.json`
```bash
uv run scorer.py
```

## 🧠 Prompt types supported
- `zero-shot`
- `one-shot`
- `few-shot`
- `chain-of-thought`

## 📁 Extend prompts or models
- Add new questions or prompt styles to `prompts.json`
- Add or remove model IDs in `models.txt`

---
MIT License
