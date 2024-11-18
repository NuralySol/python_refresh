# import the necessary libraries to work with the data frame 2-d data structure
import pandas as pd
import matplotlib.pyplot as plt

# Read the data frame from the csv file
df = pd.read_csv("data/LargestCompanies.csv")
print(df.head())  # print the first 5 rows as always to check the data and its headers
print("-" * 100)
# How many countries are in this data frame, and how many companies are located in the United Kingdom.
unique_countries = df[
    "country"
].unique()  #! or you use can nunuqiue() to get the number of unique countries
print(f"Unique countries: {unique_countries}")
print("-" * 100)
# UK comanies and their number
uk_companies = df[df["country"] == "United Kingdom"]
print(f"Companies in the UK: {uk_companies.shape[0]}")
print("-" * 100)
# Get me the list of uk companies and group by Rank and Name
print(uk_companies.groupby(["Rank", "Name"]).size())
print("-" * 100)
companies_by_country = df.groupby("country")["Name"].count()
country_count = companies_by_country.count()
uk_count = companies_by_country["United Kingdom"]
print(
    f"The number of countries that have major companies are {country_count} and the number of countries in the UK are {uk_count}"
)
print("-" * 100)

df["marketcap"] = df["marketcap"] / 1_000_000_000_000

# What is the market cap of the all of the companies in the United Kingdom
uk_market_cap = uk_companies["marketcap"].sum()
print(f"UK Market Cap: $ {uk_market_cap:,.2f} ")  # Better formating for easier to read
print("-" * 100)

# Groupby solution to get the market cap of all the companies in the UK
uk_mark_cap = df.groupby("country")["marketcap"].sum()
print(
    f"UK Market Cap: $ {uk_mark_cap['United Kingdom']:.2f} trillions "
)  # Better formating for easier to read

# Similar ways to get NSRGY company name and country of origin, using different methods and synthax
# Which company got the Symbol NSRGY, get the company name and the country of origin
print("-" * 100)
nsrgy = df[df["Symbol"] == "NSRGY"]
print(f"Company Name: {nsrgy['Name'].values[0]}")
print(f"Country: {nsrgy['country'].values[0]}")

# Use the groupby method for the above problem
print("-" * 100)
nsrgy = df.groupby("Symbol").first()
print(
    f"Company Name: {nsrgy.at['NSRGY', 'Name']}"
)  # use at to get the single value like loc
print(f"Country: {nsrgy.at['NSRGY', 'country']}")
print("-" * 100)

# Use query method to get the company name and country of origin
nsrgy = df.query(
    "Symbol == 'NSRGY'"
)  #! or you can use @ instead of == to get the same result like sql query
print(f"Company Name: {nsrgy['Name'].values[0]}")
print(f"Country: {nsrgy['country'].values[0]}")
print("-" * 100)

# How many companies have stock prive less than $100
stock_100 = df[df["price (USD)"] < 100]
print(f"Companies with stock price < $100: \n {stock_100.shape[0]}")

# Plot five top countries by market cap as a pie chart use the matplotlib library for the plot
top_countries_market = df.groupby("country")["marketcap"].sum().nlargest(5)
plt.figure(figsize=(10, 8))
plt.pie(
    top_countries_market,
    labels=top_countries_market.index,
    autopct="%1.1f%%",
    colors=plt.cm.tab20.colors,
)
plt.title("Top 5 Countries by Market Cap", fontsize=14, fontdict={"weight": "bold"})
plt.legend(title="Countries", loc="upper right")
plt.axis("equal")
#! Save the plot as a png file (SHOULE BE DONE BEFORE plt.show()) is called
plt.savefig("./assets/top_countries_market_cap.png")
print("Plot saved as top_countries_market_cap.png")
# Show the plot, always at the end of the code
plt.show()

print("-" * 100)
