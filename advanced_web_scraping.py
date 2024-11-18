import requests
from bs4 import BeautifulSoup

# Const URL variable for the link to scrape data from (Classic Cars)
URL = "https://classiccars.com"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
print("-" * 100)
