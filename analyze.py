
import json
import pandas as pd

def load_data(path='scored_results.json'):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def analyze(data):
    rows = []
    for entry in data:
        score = entry.get('score')
        try:
            score = int(score)
        except (ValueError, TypeError):
            continue  # skip invalid scores
        rows.append({
            'question_id': entry['question_id'],
            'model': entry['model'],
            'style': entry['style'],
            'score': score
        })
    return pd.DataFrame(rows)

def main():
    data = load_data()
    df = analyze(data)
    if df.empty:
        print("No valid scores found.")
        return

    print("\nAverage score by model:")
    print(df.groupby('model')['score'].mean().sort_values(ascending=False).round(2))

    print("\nAverage score by prompt style:")
    print(df.groupby('style')['score'].mean().sort_values(ascending=False).round(2))

    print("\nAverage score by model and style:")
    print(df.groupby(['model', 'style'])['score'].mean().unstack().round(2))

if __name__ == '__main__':
    main()
