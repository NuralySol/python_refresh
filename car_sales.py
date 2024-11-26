import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Load the data
car_sales = pd.read_csv("./data/Car_sales.csv")
print(car_sales.head()) # print the head of the car sales
print(car_sales.info()) # print the info of the car sales
print(car_sales.describe()) # print the description of the
print("Shape of the data: ", car_sales.shape) # print the shape of the data
print("-" * 100)

# find 3 most expensive cars
print(car_sales.nlargest(3, 'Price_in_thousands')) # print the 3 most expensive cars 
print("-" * 100)
#! Data frame has attributes like columns, index, values.


