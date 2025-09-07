import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
TEXT_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Search for multiple places
def search_places(query, max_results=20):
    places = []
    params = {
        "query": query,
        "key": API_KEY
    }
    while True:
        response = requests.get(TEXT_SEARCH_URL, params=params)
        data = response.json()
        places.extend(data.get("results", []))
        
        # Check for next page token
        next_page_token = data.get("next_page_token")
        if not next_page_token or len(places) >= max_results:
            break
        params["pagetoken"] = next_page_token
    return places[:max_results]

# Get reviews for a place
def get_place_reviews(place_id, fields="name,rating,reviews"):
    url = f"{DETAILS_URL}?place_id={place_id}&fields={fields}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.text}")
    return response.json()
