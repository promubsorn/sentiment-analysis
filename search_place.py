import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# The endpoint for text search
url = "https://places.googleapis.com/v1/places:searchText"

# Request payload
payload = {
    "textQuery": "24/7 Fitness gym Bangkok Thailand"
}

# Headers
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress"
}

# Make POST request
response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    for place in data.get("places", []):
        print("Place ID:", place.get("id"))
        print("Name:", place.get("displayName"))
        print("Address:", place.get("formattedAddress"))
        print("-" * 50)
else:
    print("Error:", response.status_code, response.text)
