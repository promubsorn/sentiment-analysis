import pandas as pd
import os
import json

def save_reviews_to_csv(reviews, filename="data/reviews.csv"):
    # Make sure the folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Convert list of reviews to DataFrame
    df = pd.DataFrame(reviews)
    
    # Save to CSV
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    
    print(f"Reviews saved to {filename}")


def save_reviews_to_excel(reviews, filename="data/reviews.xlsx"):
    # Make sure the folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Convert list of reviews to DataFrame
    df = pd.DataFrame(reviews)
    
    # Save to Excel
    df.to_excel(filename, index=False, engine="openpyxl")
    
    print(f"Reviews saved to {filename}")

def save_to_json(data, filename="data/reviews.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)