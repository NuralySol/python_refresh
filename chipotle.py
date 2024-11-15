import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/chipotle.csv")
print(df.head())
print(df.info())
print('-'* 100)
# Drop the order_id column
df.drop('order_id', axis=1, inplace=True) # axis=1 means column, and inplace means to modify the original dataframe
print(df)
print('-'* 100)
# Renaming the Column 
df.rename(columns={'item_price':'order_price'}, inplace=True)
print(df)
print('-'* 100)
# Get the most expensive order, what was ordered?
df["order_price"] = df["order_price"].apply(lambda x: float(x.replace("$", "")))
df[df["order_price"] == df["order_price"].max()]
print(df) # This will show the most expensive order
print('-'* 100)
# How many times people ordered chicken bowl?
chicken_bowl_orders = df[df["item_name"] == "Chicken Bowl"].sum()
print(f"Chichen Bowl orders total: \n", chicken_bowl_orders)
print('-'* 100)
# Total revenue for the Chicken Bowl
chicken_bowl_revenue = df[df["item_name"] == "Chicken Bowl"]["order_price"].sum()
print(f"Total revenue for Chicken Bowl: \n ${chicken_bowl_revenue:.2f}")
print('-'* 100)

# Get the total revenue of the Chicken Bowl using groupby method
chicken_bowl_revenue_groupby = df.groupby("item_name")["order_price"].sum()
print(f"Total revenue for Chicken Bowl: \n ${chicken_bowl_revenue_groupby['Chicken Bowl']:.2f}")
print('-'* 100)

# Get top 5 items by revenue
top_5_items = df.groupby("item_name")["order_price"].sum().sort_values(ascending=False).head(5)
print(f"Top 5 items by revenue: \n {type(top_5_items)}, \n {top_5_items}")
print('-'* 100)

# Another way to get top 5 items by revenue
items_by_revenue = df.groupby("item_name")[["order_price"]].sum()
items_by_revenue.reset_index()
items_by_revenue.sort_values("order_price", ascending=False, inplace=True)
items_by_revenue.head(5)
print(f"Top 5 items by revenue: \n {items_by_revenue.head(5)}")
print('-'* 100)
# Add the column "Percentage of Total Revenue" to the top 5 items by revenue
items_by_revenue["Revenue %"] = ((items_by_revenue["order_price"] / items_by_revenue["order_price"].sum()) * 100).round(2)
print(f"Top 5 items by revenue with percentage of total revenue: \n {items_by_revenue.head(5)}")
print('-'* 100)

# Two layers of filtration ( you are not creating a copy data frame)
canned_soda = df[df["item_name"] == "Canned Soda"]
canned_soda_filtered = canned_soda[canned_soda["quantity"] > 1]
print(f"Canned Soda with quantity > 1: \n {canned_soda_filtered}")
print('-'* 100)

condition1 = df["item_name"] == "Canned Soda"
condition2 = df["quantity"] > 1
canned_soda_filtered = df[condition1 & condition2].count().iloc[0]
print(f"Canned Soda with quantity > 1: \n {canned_soda_filtered}")
print('-'* 100)

# Create a data frame with a single column of numbers from 1 to 10
data = pd.DataFrame(list(range(1, 11)), columns=["Numbers"])
print(data) # This will show the data frame

print('-'* 100)
subset = data.iloc[2:5].copy()
print(subset) # This will show the subset of the data frame
print('-'* 100)
subset.iloc[0] = 1000
print(subset) # Creating a subset of data with copy method

