# More practices with dictionary data sructures and dictionary methods and manipulations

menu = {"Hamburger": 5.00, "Hotdog": 3.00, "Fries": 2.00, "Soda": 1.00}
print(menu)

print("-" * 50)

# Adding a new item to the menu
menu["Ice Cream"] = 2.55
print(menu)

print("-" * 50)

# updating the price of an item in the menu using the update() method
menu.update({"Cheese Spread": 2.99})
print(menu)

print("-" * 50)

# ask the user to enter the item they want to order
# if the item is in the menu then print the price of the item
# get the 2nd user input and add it to the total price displayed at the end

user_input = input("Enter the item you want to buy: ")
if user_input in menu:
    item_price = menu[user_input]
    print(f"The price of {user_input} is ${item_price:.2f}")
    second_input = input("Enter the second item you want to buy: ")
    if second_input in menu:
        second_item_price = menu[second_input]
        total_price = item_price + second_item_price
        print(f"The price of {second_input} is ${second_item_price:.2f}")
        print(
            f"The total price for {user_input} and {second_input} is ${total_price:.2f}"
        )
    else:
        print(f"{second_input} is not found in the menu")
else:
    print("Item not found in the menu")

print("-" * 50)

sale = {}
# add all items to menu dictionary to sale but decrease the prices by 10% because of the sale of the day
for key, value in menu.items():
    sale[key] = round(value * 0.9, 2)

print(sale)

print("-" * 50)
# create a dictionary and every letter of the word is a key and value is 1
word = "apple"
word_dict = {letter: 1 for letter in word}
print(word_dict)

print("-" * 50)
# how many times each letter appears in the word
another_word = "banana"
another_word_dict = {letter: another_word.count(letter) for letter in another_word}
print(f" {another_word} has the following letters: {another_word_dict}")

print("-" * 50)
# another way to count the number of times each letter appears in the word
# this solution uses the range function to iterate through the word
word = "apple"
word_hash = {}

for i in range(len(word)):
    if word[i] in word_hash:
        word_hash[word[i]] = word_hash[word[i]] + 1
    else:
        word_hash[word[i]] = 1

print(word_hash)

print("-" * 50)

# anogram game in Python, ask the user to enter two words and check if they are anagrams, and create two dictionaries for each word

word1_hash = {}
word2_hash = {}

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")


def hash_word(word):
    word_hash = {}
    for letter in word:
        if letter in word_hash:
            word_hash[letter] = word_hash[letter] + 1
        else:
            word_hash[letter] = 1
    return word_hash


word1_hash = hash_word(word1)
word2_hash = hash_word(word2)

if word1_hash == word2_hash:
    print("The words are anagrams")
else:
    print("The words are not anagrams")

print("-" * 50)

