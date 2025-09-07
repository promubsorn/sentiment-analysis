from google_api import search_places, get_place_reviews
from save_file import save_reviews_to_excel, save_reviews_to_csv
from fitness_branches import all_fitness_queries

all_reviews = []

for query in all_fitness_queries:
    places = search_places(query, max_results=5)  # limit per query
    for place in places:
        place_id = place["place_id"]
        place_name = place.get("name")
        data = get_place_reviews(place_id)
        reviews_raw = data.get("result", {}).get("reviews", [])
        for r in reviews_raw:
            all_reviews.append({
                "place_name": place_name,
                "author": r.get("author_name"),
                "rating": r.get("rating"),
                "text": r.get("text")
            })

# Save all reviews
save_reviews_to_csv(all_reviews)
save_reviews_to_excel(all_reviews)