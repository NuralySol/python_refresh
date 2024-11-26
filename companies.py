import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data to the Data Frame and skip the first row
df = pd.read_csv("./data/xlf.csv", skiprows=1)
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print("-" * 100)

# Get the average index weight
df["IW"] = df["Index Weight"].apply(lambda x: float(x.strip("%")))
average_iw = round(df["IW"].mean(), 2)
print(f"The average index weight is {average_iw}%")
print("-" * 100)

#! Plot a pie chart of the top 5 companies by Volume need to Strip the M from the Volume column and convert it to float
df["Volume"] = df["Volume"].str.strip("M").astype(float)
top_5 = df["Volume"].nlargest(5)
plt.figure(figsize=(10, 8))
plt.pie(top_5, labels=top_5.index, autopct = "%1.1f%%", shadow=True)
plt.show()

# What is the last price of the company with the symbol JPM in the data frame
jpm_last_price = df.loc[df["Symbol"] == "JPM", "Last"].values[0]
print(f"The last price of JPM is {jpm_last_price}")
print("-" * 100)
# Or use contains method to get the last price of JPM
jpm_last_price_contains = df.loc[df["Symbol"].str.contains("JPM"), "Last"].values[0]
print(f"The last price of JPM is {jpm_last_price_contains}")
print("-" * 100)
# Or use the query method to get the last price of JPM
jpm_last_price_query = df.query("Symbol == 'JPM'")["Last"].values[0]
print(f"The last price of JPM is {jpm_last_price_query}")
print("-" * 100)

# add another column called difference and get the difference between high and low prices in 52 week range
year_difference = df["Difference"] = df["52 Week Range"].str.split(" - ").apply(lambda x: float(x[1].replace(",", "")) - float(x[0].replace(",", "")))
# for loop to print the symbol and the difference
for symbol, diff in zip(df["Symbol"], year_difference):
    print(f"Symbol: {symbol}, 52 Week Range Difference: ${diff:.2f}")
print("-" * 100)

#! The below code will give you the same result as the for loop above but is more efficient and faster
#! Use a different method to map the year_difference to the symbol
df["Difference"] = year_difference
print(df[["Symbol", "Difference"]])
print("-" * 100)

# Get the companies with the difference in 52 week range greater than 100
# Use apply and lambda and if Last price is lower than 100 then print "Buy" else "Sell"
# Save the result in a new column called "Advice"
df["Advice"] = df["Last"].apply(lambda x: "Buy" if x < 100 else "Sell")
print(df[["Symbol", "Last", "Advice"]])
print("-" * 100)

# Do the same use np.where method (numpy) to get the same result and it is more concise
df["Advice"] = np.where(df["Last"] < 100, "Buy", "Sell")
print(f"The advise is to buy or sell:\n", df[["Symbol", "Last", "Advice"]])
print("-" * 100)

# Do the same with method loc to get the same result
df.loc[df["Last"] < 100, "Advice"] = "Buy"
df.loc[df["Last"] >= 100, "Advice"] = "Sell"
print(f"The advise is to buy or sell using the loc method is:\n", df[["Symbol", "Last", "Advice"]])
print("-" * 100)
