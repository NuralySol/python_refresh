import os
import requests
import csv
from matplotlib import pyplot as plt
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Obscure the API key for security
API_KEY = os.getenv("SECRET_KEY")
# URL for the Yelp API
URL = "https://api.yelp.com/v3/businesses/search"

# Set the request headers and parameters
headers = {"Authorization": f"Bearer {API_KEY}"}
params = {"term": "restaurant", "location": "New York City", "limit": 50}

response = requests.get(URL, headers=headers, params=params)
# parse the response as JSON
data = response.json()
# get the restaurants, ratings and prices from the response
restaurants = [business["name"] for business in data["businesses"]]
ratings = [business["rating"] for business in data["businesses"]]
prices = [
    business["price"] if "price" in business else None
    for business in data["businesses"]
]

response_text = "\n".join(
    [
        f"Restaurant: {restaurant}, Rating: {rating}, Price: {price}"
        for restaurant, rating, price in zip(restaurants, ratings, prices)
    ]
)

print(response_text)

# Sort the restaurants by rating
sorted_data = sorted(data["businesses"], key=lambda x: x["rating"], reverse=True)
# Get the top 10 restaurants
top_ten_sort = sorted_data[:10]
restaurants_top = [restaurant["name"] for restaurant in top_ten_sort]
print("\nTop 10 Restaurants by Rating:", restaurants_top)

# save the top 10 restaurants as a csv file in the data folder with columns Name, Rating and Price
with open("./data/top_10_restaurants.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Rating", "Price"])
    for restaurant in top_ten_sort:
        writer.writerow(
            [restaurant["name"], restaurant["rating"], restaurant.get("price", "N/A")]
        )

