# scoring/lead_scorer.py

import pandas as pd
import os

def score_lead(row):
    score = 0
    title = row['name_title'].lower()
    snippet = row['snippet'].lower()

    # Rule 1: Seniority titles
    if any(x in title for x in ['ceo', 'founder', 'co-founder']):
        score += 5
    elif any(x in title for x in ['cto', 'cmo', 'vp', 'head']):
        score += 3

    # Rule 2: Relevant industries/keywords
    if any(x in snippet for x in ['saas', 'ai', 'b2b', 'cloud']):
        score += 2

    # Rule 3: Link is proper LinkedIn
    if '/in/' in row['profile_url']:
        score += 1

    return score

def label_confidence(score):
    if score >= 7:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"

def score_leads(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found: {input_path}")
        return
    
    df = pd.read_csv(input_path)
    df['score'] = df.apply(score_lead, axis=1)
    df['confidence_label'] = df['score'].apply(label_confidence)

    df.to_csv(output_path, index=False)
    print(f"[✔] Scored leads saved to {output_path}")
    print(df[['name_title', 'score', 'confidence_label']])

# Example usage
if __name__ == "__main__":
    score_leads("data/sample_leads.csv", "data/scored_leads.csv")
