import pandas as pd

# Pandas review - DataFrames and Series
# Series - 1D array
# DataFrame - 2D array
alist = [1, 2, 3, 4, 5]
aseries = pd.Series(alist)  # Series two major components: index and values
print(aseries)

print("_" * 50)

pd.DataFrame(pd.Series(alist), columns=["Numbers"])
print(pd.DataFrame(pd.Series(alist), columns=["Numbers"]))  # Data Frame

print("_" * 50)

# Faster than excel and google sheets
# DataFrames have three major components: index, columns, and values
df = pd.DataFrame()
df["Stock"] = ["AAPL", "GOOGL", "AMZN", "TSLA", "MSFT"]
df["Price"] = [146.92, 2776.40, 3277.71, 687.20, 277.97]
df["Shares"] = [100, 500, 200, 300, 888]  # Now it is a three column DataFrame
print(df)

print("_" * 50)
# slicing the DataFrame
df["Price"]  # Series
print(df["Price"])

print("_" * 50)
df["Amount"] = df["Price"] * df["Shares"]  # Series vectorized operation
print(df)

print("_" * 50)
df.index = df["Stock"]  # Setting the index to the Stock column
print(df)

print("_" * 50)
df.drop(
    "Stock", axis=1, inplace=True
)  #! Drop the Stock column axis=1 is for columns axis=0 is for rows
print(df)
print("_" * 50)

# two ways to slice by rows in a DataFrame, function loc and iloc
df.loc["AAPL" : "MSFT", "Shares": "Amount"]  # loc is for label-based slicing
print(df.loc["AAPL"])
print("_" * 50)

df.iloc[0]  # iloc is for position-based slicing
print(df.iloc[0])
print("_" * 50)

# Slicing two-or-more columns
print(df.loc[["AAPL", "TSLA"], ['Price', 'Shares']])  #! Double brackets
print("_" * 50)

# Filering the DataFrames
# Reset the index
df.reset_index(inplace=True)
print(df)
print("_" * 50)

conditional_df = df["Stock"] == "AAPL"  # Boolean mask True or False
print("_" * 50)
print(f" Price of AAPL is ${df[conditional_df]['Price'].squeeze()}")  # Filtering the DataFrame
print("_" * 50)
print(conditional_df) # Boolean mask print out the whole DataFrame with True or Fale values
print("_" * 50)

# Finding the stocks less than $1000
conditional_df_1000 = df["Price"] < 1000
print(f"Stocks less than 1000$ \n{df[conditional_df_1000]}")

print("_" * 50)
# Max amount with the conditional DataFrame
max_amount = df["Amount"].max()
conditional_df_max = df["Amount"] == max_amount
print(f"Stock with the max amount \n{df[conditional_df_max]}") # The stock with the max amount

print("_" * 50)

