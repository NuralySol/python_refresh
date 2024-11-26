import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data to the Data Frame and skip the first row
df = pd.read_csv("./data/BabyNames.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print("-" * 100)
# Drop columns that are not needed: Unnamed and Id
df.drop(["Unnamed: 0", "Id"], axis=1, inplace=True)
print(df.head())
# Plot as a pie-chart male names vs female 
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Male vs Female Baby Names')
plt.show()

# What is the most popular name?
name_counts = df['Name'].value_counts()
print(name_counts.head())
print("-" * 100)

names = df.groupby("Name")["Count"].sum().sort_values(ascending=False).head(5)
print(names)
print("-" * 100)

# What is the most popular name in the state of NY in 2004?
# Need two conditions: State = NY and Year = 2004 then group by Name and sum the Count column and sort in descending order and get the first row. 

popular_name_ny_2004 = df[(df["State"] == "NY") & (df["Year"] == 2004)].groupby("Name")["Count"].sum().sort_values(ascending=False).head(10)
print(f"The most popular names in NY 2004 are:\n",popular_name_ny_2004)
print("-" * 100)

# Popular names in CA in 2004?
popular_name_ca_2004 = df[(df["State"] == "CA") & (df["Year"] == 2004)].groupby("Name")["Count"].sum().sort_values(ascending=False).head(10)
print(f"The most popular names in CA 2004 are:\n",popular_name_ca_2004)
print("-" * 100)

# Get the number of of the name "Michael" for each state in all years use contains
michael_counts = df[df["Name"].str.contains("Michael", case = False)].groupby("State")["Count"].sum().sort_values(ascending=False)
print(f"The number of Michaels in each state are:\n",michael_counts)
print("-" * 100)
# Get the total number of Michaels in all states
total_michael = df[df["Name"].str.contains("Michael", case = False)]["Count"].sum()
print(f"The total number of Michaels in all states is: {total_michael}")
print("-" * 100)
