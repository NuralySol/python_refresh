import requests
from bs4 import BeautifulSoup
import pandas as pd

# Const URL variable for the link to scrape data from (Classic Cars)
URL = "https://classiccars.com/"

# headers to avoid 403 forbidden error (Forbidden: You don't have permission to access [directory] on this server.)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

# Get the response from the URL using requests module (GET request).
response = requests.get(URL, headers=headers)

# Convert HTML into Python object (Web scraping).
bsobj = BeautifulSoup(response.content, "html.parser")

# Get all the titles from the HTML content. {class: h-title}
all_titles = bsobj.find_all("div", {"class": "h-title"})
for title in all_titles:
    string = title.get_text()
    if string[
        :4
    ].isdigit():  # Check if the first 4 characters are digits and then print them (Year)
        print(string)
        print("-" * 100)

# The only way to convert it correctly use try and except block to avoid errors
# Get all the prices from the HTML content. {class: p-price}
prices_all = bsobj.find_all("div", {"class": "p-price"})
for price in prices_all:
    price_text = price.get_text()  # Extract the price text
    print(price_text)
    print("-" * 100)

    try:
        # Clean and convert the price
        cleaned_price_text = (
            price_text.replace("$", "")  # Remove dollar sign
            .replace(",", "")  # Remove commas
            .replace("\xa0", "")  # Remove non-breaking spaces
            .strip()  # Remove leading/trailing whitespace
        )
        # Convert to float
        converted_price = float(
            cleaned_price_text.split()[0]
        )  # Handle extra text after the number
        print(converted_price)
    except ValueError as e:
        print(f"Error converting price: {price_text} -> {e}")

print("-" * 100)

# Convert the data into data frame using pandas and strip, clean the data using list comprehension
df = pd.DataFrame(
    {
        "Title": [title.get_text().strip() for title in all_titles],
        "Price": [
            price.get_text()
            .replace("$", "")
            .replace(",", "")
            .replace("\xa0", "")
            .strip()
            .split()[0]
            for price in prices_all
        ],
    }
)
# print the first 10 rows of the data frame
print(df.head(10))
print("-" * 100)
# print the info of the data frame and see the data types and missing values
print(df.info())
print("-" * 100)
# Convert the prices into floats
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
# Fill the NaN values with 0
df["Price"].fillna(0, inplace=True)
print("Converted prices: \n", df["Price"])
print("-" * 100)
# Use apply and lambda function to split the year into seperate columns
df["Year"] = df["Title"].apply(lambda x: x.split()[0])
df["Make"] = df["Title"].apply(lambda x: " ".join(x.split()[1:]))
print(f" Year split into seperate column: \n", df.head(10))
