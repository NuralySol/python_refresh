import requests
from matplotlib import pyplot as plt

url = "https://rickandmortyapi.com/api/character"

# get the response from the API and store it in a variable called response
response = requests.get(url)
data = response.json()
print(response)

print("-" * 50)
# print all the characters in the response using a list comprehension
name_and_status = [(result["name"], result["species"]) for result in data["results"]]
print("\n", name_and_status)

print("-" * 50)

# How many humans and how many aliens are in the response
humans = [result for result in data["results"] if result["species"] == "Human"]
non_humans = [result for result in data["results"] if result["species"] != "Human"]
print(
    f"\nThere are {len(humans)} humans and {len(non_humans)} non-humans in the response"
)
print("-" * 50)

numbers = [len(humans), len(non_humans)]
print("\n", numbers)
print("-" * 50)

labels = ["Humans", "Non-Humans"]
print("\n", labels)

# Plot the data using matplotlib and display as a pie chart, save it as a png file in assets directory
plt.pie(numbers, labels=labels, autopct="%1.1f%%", explode=[0.2, 0], shadow=True)
plt.title("Humans vs Non-Humans in Rick and Morty")
plt.savefig("./assets/rick_and_morty_piechart.png")
plt.show()

# Plot a bar chart of the number of humans and non-humans
plt.bar(labels, numbers, color=["lightblue", "orange"], edgecolor="black", linewidth=1)
plt.xlabel("Character Type")
plt.ylabel("Number of Characters")
plt.title("Humans vs Non-Humans in Rick and Morty")
plt.savefig("./assets/rick_and_morty_bachart.png")
plt.show()

