import os
import json
import time
import logging
import shutil
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(
    filename="scorer.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

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
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
        logging.error(f"API response: {response.text}")
        raise

    result = response.json()
    if "choices" not in result or not result["choices"]:
        logging.error("Invalid response structure")
        logging.error(json.dumps(result, indent=2))
        raise ValueError("Missing 'choices' in response")

    return result["choices"][0]["message"]["content"].strip()

def backup_file(path):
    if os.path.exists(path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{path}.{timestamp}.bak"
        shutil.copy2(path, backup_path)
        logging.info(f"Backed up existing {path} to {backup_path}")

def main(results_path="results.json", output_path="scored_results.json"):
    if os.path.exists(output_path):
        backup_file(output_path)
        with open(output_path, "r", encoding="utf-8") as infile:
            results = json.load(infile)
    else:
        with open(results_path, "r", encoding="utf-8") as infile:
            results = json.load(infile)

    updated = False
    for entry in results:
        score = entry.get("score")
        if score != "error" and score is not None:
            continue

        model = entry.get("model")
        qid = entry.get("question_id")
        style = entry.get("style")

        try:
            msg = f"Scoring {qid} | {model} | {style}"
            print(msg)
            logging.info(msg)
            entry["score"] = score_response(qid, entry["response"])
            updated = True
        except Exception as e:
            err = f"Error scoring {qid} | {model} | {style}: {e}"
            print(err)
            logging.error(err)
            entry["score"] = "error"
            updated = True

        with open(output_path, "w", encoding="utf-8") as outfile:
            json.dump(results, outfile, indent=2, ensure_ascii=False)

        time.sleep(1.5)  # Rate limiting

    if not updated:
        msg = "Nothing to score or update."
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    main()
