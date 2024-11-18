# Convert HTML into Python object (Web scraping).
import requests
from bs4 import BeautifulSoup

URL = "http://shakespeare.mit.edu/lll/full.html"  # Constant URL variable for the link to scrape data from

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.title) use prettify() method to print the entire HTML content
print(soup.prettify())
print("-" * 100)

# use for loop to get all the headings in the HTML content h3 tags
headings = soup.find_all("h3")
for heading in headings:
    print(heading.get_text())  # get text from the h3 tags
print("-" * 100)

# Do the same using list comprehension (returns a list of all the headings), similar to the above!
# .find_all() method returns a list of all the headings in the HTML content and can take many arguments!
h3_list = soup.find_all("h3")
h3_list = [heading_list.get_text() for heading_list in h3_list]
print(f" H3 using the list comrehension: \n", h3_list)
print("-" * 100)

# Suppose I want to get only one item.
single_phrase = soup.find(
    "a", {"name": "1.1.9"}
)  # fetch the single phrase from the text
print(
    f"Single phrase: \n", single_phrase.get_text()
)  # Output: 'That war against your own affections'
print("-" * 100)
