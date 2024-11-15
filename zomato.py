import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
print(
    f"Name of those restaurants in Abu Dhabi are: \n {abu_dhabi_restaurants_groupby['Abu Dhabi']}"
)
print("-" * 100)

# Get me restaurants with the highest rating in New Delhi, first see all the restaurants in New Delhi
# Use the groupby method to get the restaurants in New Delhi and the highest rating restaurant info
rating_above_4 = df[df["Aggregate rating"] >= 4.0]
new_delhi_restaurants = df[df["City"] == "New Delhi"]
print(f"Restaurants in New Delhi: \n {new_delhi_restaurants}")
print("-" * 100)
restauraunts_in_new_delhi = (
    rating_above_4[rating_above_4["City"] == "New Delhi"]
    .sort_values(by="Aggregate rating", ascending=False)
    .head(5)
)
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
print(
    f"Percentage of restaurants with Chinese cuisine: \n {chinese_cuisine_percentage:.2f}"
)
print(
    f"Percentage of restaurants with American cuisine: \n {american_cuisine_percentage:.2f}"
)

# What is the name and rating of the most expensive restaurant for two ('Average Cost for two' column)?
# Use the max method to get the most expsive restaurnt for two
most_expensive_restaurant = df[
    df["Average Cost for two"] == df["Average Cost for two"].max()
][["Restaurant Name", "Aggregate rating"]]
print(f"Most expensive restaurant for two: \n {most_expensive_restaurant}")
# Or use the condition to filter the data frame for the most expensive restaurant for two
condition_cost = df["Average Cost for two"] == df["Average Cost for two"].max()
df[condition_cost][["Restaurant Name", "Aggregate rating", "Average Cost for two"]]
print("-" * 100)

# Find the most expensive chinese restaurant in New Delhi in US dollar 1 Indian Rupee = 0.013 USD
# Use the condition to filter the data frame for the most expensive Chinese restaurant in New Delhi
CONVERSION_RATE = 0.013

most_expensive_chinese_restaurant = (
    df[
        (df["Cuisines"].str.contains("Chinese", case=False))
        & (df["City"] == "New Delhi")
    ]
    .sort_values(by="Average Cost for two", ascending=False)
    .head(1)
)
most_expensive_chinese_restaurant["Average Cost for two"] = (
    most_expensive_chinese_restaurant["Average Cost for two"] * CONVERSION_RATE
)
print(
    f"Most expensive Chinese restaurant in New Delhi: \n {most_expensive_chinese_restaurant}"
)
print("-" * 100)
most_expensive_chinese_restaurant["Average Cost for two"] = (
    most_expensive_chinese_restaurant["Average Cost for two"].apply(
        lambda x: f"${x:.2f}"
    )
)
print(
    f"Most expensive Chinese restaurant in New Delhi in USD: \n {most_expensive_chinese_restaurant[['Restaurant Name', 'Average Cost for two']]}"
)
print("-" * 100)

# Plot the top 5 cities in the Data Frame by number of restaurants as a horizontal bar chart
plt.barh(df["City"].value_counts().head(5).index, df["City"].value_counts().head(5))
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.title("Top 5 Cities by Number of Restaurants")
plt.show()

# Plot the top 5 cities in the Data Frame by number of restaurants as a pie chart
plt.pie(
    df["City"].value_counts().head(5),
    labels=df["City"].value_counts().head(5).index,
    autopct="%1.1f%%",
)
plt.title("Top 5 Cities by Number of Restaurants")
plt.show()

#! Logical statements in Python
# Create a data frame with a list of numbers from 1 to 10 and name the column "Numbers"
df = pd.DataFrame(list(range(1, 11)), columns=["Numbers"])
print(df)
df["Even_Odd"] = df["Numbers"].apply(lambda x: "Even" if x % 2 == 0 else "Odd")
print("-" * 100)
print(df)
print("-" * 100)
#! In pandas you should be using universal functions (ufuncs) for element-wise operations
# Use the np.where method to create a new column "Where" and assign the value "Even" if the number is even and "Odd" if the number is odd
df["Where"] = np.where(df["Numbers"] % 2 == 0, "Even", "Odd")
print(df)
print("-" * 100)

# Use the loc method to create a new column "Loc" and assign the value "Even" if the number is even and "Odd" if the number is odd, with loc you can
df.loc[df["Numbers"] % 2 == 0, "Col_loc"] = "Even"
df.loc[df["Numbers"] % 2 != 0, "Col_loc"] = "Odd"
print(df)
print("-" * 100)

df["Even_Odd_100"] = df.apply(
    lambda dataframe: (
        dataframe["Numbers"] * 100
        if dataframe["Numbers"] % 2 == 0
        else dataframe["Numbers"]
    ),
    axis=1,
)
print(df)
print("-" * 100)
print(f"Even Odd times by 100: \n", type(df["Even_Odd_100"]), df["Even_Odd_100"])

# Create two data frames with the same products and somewhat different prices, some of whom are the same and some are not
store1 = pd.DataFrame()
store1["Product1"] = ["Mac", "Iphone", "Ipad", "Apple Watch", "Apple TV"]
store1["Price1"] = [1000, 800, 500, 700, 200]

store2 = pd.DataFrame()
store2["Product2"] = ["Mac", "Iphone", "Ipad", "Apple Watch", "Apple TV"]
store2["Price2"] = [900, 700, 500, 250, 150]

# Compare the prices "Price1" vs "Price2" if same Ture if not False use np.where
# You can only need to select the columns that you want to compare
# You can also use the np.where method to compare the prices of the products in the two stores
store1["Price_Comparison"] = np.where(store1["Price1"] == store2["Price2"], True, False)
print(store1)
print("-" * 100)

# if price is not the same then decrease the price by 10% in store1 and save results under column name "Sale"
store1["Sale"] = np.where(
    store1["Price1"] != store2["Price2"], store1["Price1"] * 0.9, store2["Price2"]
)
print(store1)

# Solve this problem using the method loc, if by price is 700 then decrease it by 20% and save the results under column name "Sale_loc", otherwise keep the price as it is
print("-" * 100)
store1["Sale_loc"] = store1["Price1"]
store1.loc[store1["Price1"] == 700, "Sale_loc"] = store1["Price1"] * 0.8
print(store1)
print("-" * 100)

