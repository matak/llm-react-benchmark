import os
import json
import time
import shutil
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def load_prompts(path="prompts.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_models(path="models.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def backup_file(path):
    if os.path.exists(path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{path}.{timestamp}.bak"
        shutil.copy2(path, backup_path)
        print(f"Backed up existing {path} to {backup_path}")

def call_model(model: str, prompt: str):
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    response.raise_for_status()
    content = response.json()
    return content["choices"][0]["message"]["content"].strip()

def write_results(results, output_path="results.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def main():
    backup_file("results.json")
    prompts = load_prompts()
    models = load_models()
    results = []
    for q in prompts:
        for variant in q["prompts"]:
            for model in models:
                try:
                    print(f"Testing {q['id']} | {variant['style']} | {model}")
                    response = call_model(model, variant["input"])
                    results.append({
                        "question_id": q["id"],
                        "model": model,
                        "style": variant["style"],
                        "response": response
                    })
                    time.sleep(1.5)
                except Exception as e:
                    print(f"Error: {e}")
    write_results(results)

if __name__ == "__main__":
    main()
