import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SCORING_MODEL = "anthropic/claude-opus-4"

def score_response(prompt, model_response):
    scoring_prompt = f"""
You are an impartial evaluator of LLM-generated responses.

Question:
"{prompt}"

Model response:
{model_response}

Rate the quality of the answer on a scale of 1–5:
1 = poor, 5 = excellent.
Respond only with a number.
"""
    
    data = {
        "model": SCORING_MODEL,
        "messages": [
            {"role": "user", "content": scoring_prompt}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

def main(results_path="results.json", output_path="scored_results.json"):
    with open(results_path, "r", encoding="utf-8") as infile:
        results = json.load(infile)

    for entry in results:
        try:
            print(f"Scoring {entry['question_id']} | {entry['model']} | {entry['style']}")
            entry["score"] = score_response(entry["question_id"], entry["response"])
        except Exception as e:
            print(f"Error scoring entry: {e}")
            entry["score"] = "error"

    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(results, outfile, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
