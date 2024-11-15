import pandas as pd
import matplotlib.pyplot as plt

# The encoding is Latin1 to open the file and read the characters that are not in the ASCII character set
df = pd.read_csv("data/zomato.csv", encoding="Latin1")
print(df.head())  # As always check the first 5 rows
print("-" * 100)
print(df.info())  # Check the information of the data frame
print("-" * 100)

# How to deal with missing values in the data frame
print(df.isna().sum())  # Check the missing values in the data frame
print("-" * 100)

# There are different ways to deal with missing values
# One option is to drop the missing values
df.dropna(inplace=True)  # Drop the missing values
print(df.isna().sum())  # Check the missing values in the data frame
print("-" * 100)

# How many restaurants that have a rating of 4.8 and above
# We can create a condition to filter the data frame for the high rating restaurants and then count the number of rows
# It depends on the value that we set for the condtiion to filter the data frame for the rating
highest_rating = df[df["Aggregate rating"] >= 4.9].shape[0]
print(f"Restaurants with rating of 4.9 and above: \n {highest_rating}")
print("-" * 100)

# Top 5 restaurants with the highest number of aggregate rating using the groupby method
top_5_restaurants = (
    df.groupby("Restaurant Name")["Aggregate rating"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(
    f"Top 5 restaurants with the highest number of aggregate ratings are: \n {top_5_restaurants}"
)
print("-" * 100)

# Use the value counts method to get the aggregate rating of the restaurants
# Value counts method is used to count the number of times a value appears in a column of a data frame
rest_rating_by_value_counts = df["Aggregate rating"].value_counts()
print(f"Restaurants rating by value counts: \n {rest_rating_by_value_counts}")
print("-" * 100)

# How many unique cities are in the data frame and how many restaurants are located in Abu Dhabi
unique_cities = df["City"].nunique()
print(f"Unique cities in the data frame: \n {unique_cities}")
print("-" * 100)
abu_dhabi_restaurants = df[df["City"] == "Abu Dhabi"].shape[0]
print(f"Number of restaurants in Abu Dhabi: \n {abu_dhabi_restaurants}")
# Or use groupby method to get the number of restaurants in Abu Dhabi
print("-" * 100)
abu_dhabi_restaurants_groupby = df.groupby("City")["Restaurant Name"].value_counts()
print(f"Name of those restaurants in Abu Dhabi are: \n {abu_dhabi_restaurants_groupby['Abu Dhabi']}")
print("-" * 100)

# Get me restaurants with the highest rating in New Delhi, first see all the restaurants in New Delhi
# Use the groupby method to get the restaurants in New Delhi and the highest rating restaurant info
rating_above_4 = df[df["Aggregate rating"] >= 4.0]
new_delhi_restaurants = df[df["City"] == "New Delhi"]
print(f"Restaurants in New Delhi: \n {new_delhi_restaurants}")
print("-" * 100)
restauraunts_in_new_delhi = rating_above_4[rating_above_4["City"] == "New Delhi"].sort_values(by="Aggregate rating", ascending=False).head(5)
print(f"Restaurants in New Delhi with rating above 4: \n {restauraunts_in_new_delhi}")

# Which cuisine is more popular in data frame Chinese or American
# Use the groupby method to get the number of restaurants with Chinese and American cuisine
chinese_cuisine = df[df["Cuisines"].str.contains("Chinese", case=False)].shape[0]
american_cuisine = df[df["Cuisines"].str.contains("American", case=False)].shape[0]
difference_in_cuisine = chinese_cuisine - american_cuisine
print(f"Number of restaurants with Chinese cuisine: \n {chinese_cuisine}")
print(f"Number of restaurants with American cuisine: \n {american_cuisine}")
print(f"Difference between Chinese and American cuisine: \n {difference_in_cuisine}")

# The percentage of restaurants with Chinese and American cuisine
total_restaurants = df.shape[0]
chinese_cuisine_percentage = (chinese_cuisine / total_restaurants) * 100
american_cuisine_percentage = (american_cuisine / total_restaurants) * 100
print(f"Percentage of restaurants with Chinese cuisine: \n {chinese_cuisine_percentage:.2f}")
print(f"Percentage of restaurants with American cuisine: \n {american_cuisine_percentage:.2f}")

# What is the name and rating of the most expensive restaurant for two ('Average Cost for two' column)?
# Use the max method to get the most expsive restaurnt for two
most_expensive_restaurant = df[df["Average Cost for two"] == df["Average Cost for two"].max()][["Restaurant Name", "Aggregate rating"]]
print(f"Most expensive restaurant for two: \n {most_expensive_restaurant}")
# Or use the condition to filter the data frame for the most expensive restaurant for two
condition_cost = df["Average Cost for two"] == df["Average Cost for two"].max()
df[condition_cost][["Restaurant Name", "Aggregate rating", "Average Cost for two"]]
print("-" * 100)

# Find the most expensive chinese restaurant in New Delhi in US dollar 1 Indian Rupee = 0.013 USD
# Use the condition to filter the data frame for the most expensive Chinese restaurant in New Delhi
CONVERSION_RATE = 0.013

most_expensive_chinese_restaurant = df[(df["Cuisines"].str.contains("Chinese", case=False)) & (df["City"] == "New Delhi")].sort_values(by="Average Cost for two", ascending=False).head(1)
most_expensive_chinese_restaurant["Average Cost for two"] = most_expensive_chinese_restaurant["Average Cost for two"] * CONVERSION_RATE
print(f"Most expensive Chinese restaurant in New Delhi: \n {most_expensive_chinese_restaurant}")
print("-" * 100)
most_expensive_chinese_restaurant["Average Cost for two"] = most_expensive_chinese_restaurant["Average Cost for two"].apply(lambda x: f"${x:.2f}")
print(f"Most expensive Chinese restaurant in New Delhi in USD: \n {most_expensive_chinese_restaurant[['Restaurant Name', 'Average Cost for two']]}")
print("-" * 100)

