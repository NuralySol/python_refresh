import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/athlete_events.csv")
print(df.head())
print("-" * 100)
print(df.info())
print("-" * 100)
print(df.isna().sum())

formatted_df = df["Medal"].fillna("No Info")  # Fill the NaN values with No Info
print(formatted_df)
print("-" * 100)

# Get the 3 counties by Gold medals only
gold_medals = df[df["Medal"] == "Gold"]
print(
    gold_medals["NOC"].value_counts().head(3)
)  # pass the parameter to get the top 3 countries
print("-" * 100)

# Other way to get the top 3 countries by Gold medals groupby
gold_medals_grouping = gold_medals.groupby("NOC").size()
print(f"Top 3 counties by gold medals are: \n", gold_medals_grouping.nlargest(3))
print("-" * 100)

# Get the an American athlete who won the most gold medels
american_gold_medalist = gold_medals[gold_medals["NOC"] == "USA"]

top_american_gold_medalist = american_gold_medalist["Name"].value_counts().idxmax()
american_gold_total = american_gold_medalist["Name"].value_counts().max()
# Combine the two vars and print the results to the console (with two variables), and format the string
# Those are the two vars that we can call on them later down the line
print(
    f"American athlete who won the most gold medals is: {top_american_gold_medalist} with {american_gold_total} gold medals"
)

#! ^ Surpise it is Michael Fred Phelps II with 23 gold medals
print("-" * 100)

# Who was the youngest athlete to win any medal in the data frame
youngest_athlete = df[df["Age"] == df["Age"].min()]
youngest_athlete_name = youngest_athlete["Name"].values[0]
print(
    f"The youngest athlete to win any medal is: {youngest_athlete_name} at the age of {youngest_athlete['Age'].values[0]}"
)

print("-" * 100)

# Who was the oldest athlete to gold medal in the data frame
oldest_athlete = gold_medals[gold_medals["Age"] == gold_medals["Age"].max()]
oldest_athlete_name = oldest_athlete["Name"].values[0]
print(
    f"The oldest athlete to win a gold medal is: {oldest_athlete_name} at the age of {oldest_athlete['Age'].values[0]}"
)

print("-" * 100)

# Get all the silver medalists and write them into an excel file
# Ensure the directory exists before writing the file with makedirs method from os module
# Need an openpyxl==3.1.5 library to write the excel file to the disk
os.makedirs("./data", exist_ok=True)

silver_medalists = df[df["Medal"] == "Silver"]
silver_medalists.to_excel("./data/silver_medalists.xlsx", index=False)
print("Silver medalists have been written to an excel file")
