import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("./data/housing.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print("-" * 100)

# Does this mean include na? need to exclude na first?
average_bedrooms = df["total_bedrooms"].mean().astype(int)
df["total_bedrooms"].fillna(average_bedrooms)

print(df["total_bedrooms"].isnull().sum())
print("-" * 100)

# Calculate the average Rooms per House and save the results in a new column "average_rooms"
# Calculate the average Bedrooms per House and save the results in a new column "average_bedrooms"
# Calculate Number of People per household and save the results in a new column "people_house"
df["average_rooms"] = (df["total_rooms"] / df["households"]).round(1)
df["average_bedrooms"] = (df["total_bedrooms"] / df["households"]).round(1)
df["people_house"] = (df["population"] / df["households"]).round(1)
print(df.head())
print("-" * 100)

# Plot as a scatter x = longitude, y = latitude, and get long and lat for LA and SF and plot them as * and ** respectively

#! Fixed tupple for SF and LA, Constants should be in all caps
SF = (-122.43, 37.77)
LA = (-118.25, 34.05)

plt.figure(figsize = (10, 8))
plt.scatter(df["longitude"], df["latitude"], alpha = 0.5)
plt.scatter(SF[0], SF[1], color = "orange", marker = "*", label = "San Francisco")
plt.scatter(LA[0], LA[1], color = "orange", marker = "*", label = "Los Angeles")
plt.legend()
plt.annotate("San Francisco", SF, textcoords = "offset points", xytext = (0, 10), ha = "center", color = "red")
plt.annotate("Los Angeles", LA, textcoords = "offset points", xytext = (0, 10), ha = "center", color = "red")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Housing Data")
plt.savefig("./assets/housing_data.png")
plt.show()

# Plot as a bar chart number of houses based on ocean proximity
#! Can be added True to .value_counts(True) in descending order and normalize to get the percentage
ocean_proximity = df["ocean_proximity"].value_counts() 
plt.figure(figsize = (10, 8))
plt.bar(ocean_proximity.index, ocean_proximity.values)
plt.xlabel("Ocean Proximity")
plt.ylabel("Number of Houses")
plt.title("Number of Houses based on Ocean Proximity")
plt.savefig("./assets/ocean_proximity_data.png")
plt.show()

# Plot as a bar chart number of houses based on ocean proximity using seaborn and value_counts
plt.figure(figsize = (10, 8))
sns.countplot(x = "ocean_proximity", data = df)
plt.xlabel("Ocean Proximity")
plt.ylabel("Number of Houses")
plt.title("Number of Houses based on Ocean Proximity")
plt.savefig("./assets/ocean_proximity_data_seaborn.png")
plt.show()

# Plot Average Distribution of median_house_value as a histogram and drop the houses with median_house_value > 500000
houses_filtered = df[df["median_house_value"] <= 500000]
plt.figure(figsize= (10, 8))
plt.hist(houses_filtered["median_house_value"], bins = 50, color = "orange", edgecolor = "black")
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.title("Average Distribution of Median House Value")
plt.savefig("./assets/median_house_value_distribution.png")
plt.show()

