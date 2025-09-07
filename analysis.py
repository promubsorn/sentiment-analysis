from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

endpoint = "https://demo721.cognitiveservices.azure.com/"
key = os.getenv("AZURE_OPENAI_API_KEY")

# client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# documents = ["I love this place!", "The service was terrible."]

# response = client.analyze_sentiment(documents=documents)
# for doc in response:
#     print(f"Sentiment: {doc.sentiment}, Scores: {doc.confidence_scores}")
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
# Load CSV
df = pd.read_csv("data/reviews.csv")

batch_size = 10  # Max for Standard tier
negative_counts = {}
total_counts = {}
negative_indices = []  # Store original indices

negative_reviews = []  # Store negative review rows

for i in range(0, len(df), batch_size):
    batch = df.iloc[i:i+batch_size]
    # Convert all texts to string & remove empty
    batch_docs = [str(doc) for doc in batch['text'] if pd.notna(doc) and str(doc).strip() != ""]
    batch_locations = batch['place_name'].tolist()
    batch_indices = batch.index.tolist()

    if not batch_docs:
        continue

    response = client.analyze_sentiment(batch_docs)

    for doc_result, loc, idx, original_row in zip(response, batch_locations, batch_indices, batch_docs):
        total_counts[loc] = total_counts.get(loc, 0) + 1
        if doc_result.sentiment == "negative":
            negative_counts[loc] = negative_counts.get(loc, 0) + 1
            negative_indices.append(idx)
            negative_reviews.append(df.loc[idx])  # save original row

# Percentages
for loc in total_counts:
    neg = negative_counts.get(loc, 0)
    total = total_counts[loc]
    print(f"{loc}: {neg}/{total} negative reviews ({neg/total*100:.2f}%)")

overall_neg = sum(negative_counts.values())
overall_total = sum(total_counts.values())
print(f"Overall negative reviews: {overall_neg}/{overall_total} ({overall_neg/overall_total*100:.2f}%)")

# Save negative reviews to new CSV
negative_df = pd.DataFrame(negative_reviews)
negative_df.to_csv("negative_reviews.csv", index=False, encoding="utf-8")
print(f"Saved {len(negative_reviews)} negative reviews to negative_reviews.csv")