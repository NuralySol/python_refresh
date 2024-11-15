import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv("data/xlf.csv", skiprows=1) # need to skip the first row because it is a comment
print('-'* 100)
print(df.head()) # returns the first 5 rows of the DF or you can pass a number as an argument to return that number of rows

# shape of the DF
print('-'* 100)
print(f"Shape of the DF \n", df.shape) # returns a tuple with the number of rows and columns of the DF
# Before we can do any analysis, we need to clean the data and check for missing values, and data types
print('-'* 100)
print(df.info()) # returns a summary of the DF

# Convert the date column to numeric values
df["IW"] = df["Index Weight"].apply(lambda x: float(x.strip("%"))) # x.strip() removes the % sign from the string
print('-'* 100)
print(df.info())

# get the sum of all values in the IW column
print('-'* 100)
print(df["IW"].sum())

# Get the sum of the Volume column values
df["Volume"] = df["Volume"].apply(lambda x: float(x.replace("M","").replace(",",""))) # remove the comma and convert the string to a float
print('-'* 100)
print(df["Volume"].sum())

# What is the last price of the company with Symbol C use loc
print('-'* 100)
last_price_c = df.loc[df["Symbol"] == "C", "Last"]
print(last_price_c)

# Get stock with the highest volume
print('-'* 100)
largest_volume = df.loc[df["Volume"].idxmax()]
print(f"Stock with the largest volume is\n", largest_volume)

df.nlargest(5, "Volume") # returns the 5 rows with the largest volume
print('-'* 100)
print(df.nlargest(5, "Volume"))

df.nsmallest(5, "Volume") # returns the 5 rows with the smallest volume
print('-'* 100)
print(df.nsmallest(5, "Volume"))

# how many companies use CORP in their name
print('-'* 100)
corps = df[df["Company Name"].str.contains("corp", case=False)].count().iloc[0]
print(corps)

# group vs corp in the company name
print('-'* 100)
group_vs_corp = df["Company Name"].apply(lambda banana: "Group" if "group" in banana.lower() else "Corp" if "corp" in banana.lower() else "Other")
print(group_vs_corp.value_counts())

df.describe() # returns a summary of the DF with the count, mean, std, min, 25%, 50%, 75%, and max
print('-'* 100)
print(df.describe().T) # Transpose the DF to have the columns as rows and rows as columns

# Get the company with the largest/highest Last price
print('-'* 100)
largest_last_price = df.loc[df["Last"].idxmax()]
print(largest_last_price)

# Plot as a pie chart 5 top companies by volume
print('-'* 100)
top_5_companies = df.nlargest(5, "Volume")
plt.figure(figsize = (10, 10))
plt.pie(x = top_5_companies["Volume"], labels = top_5_companies["Company Name"], autopct = "%1.1f%%")
plt.title("Top 5 companies by volume")
plt.show()

# Plot the same data as a bar chart
print('-'* 100)
num_bars = len(top_5_companies["Company Name"])
random_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(num_bars)]

# Create the bar plot with random colors using the import random module
plt.figure(figsize=(10, 10))
plt.bar(
    x=top_5_companies["Company Name"],
    height=top_5_companies["Volume"],
    color=random_colors,
    edgecolor="black"
)
plt.title("Top 5 companies by volume")
plt.xticks(rotation=45)
plt.show()