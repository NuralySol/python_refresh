"""
    Functions in Python.
    Some examples of functions in Python, block of reusable code.
    Functions in Python are first class objects, which means they can be passed around as arguments to other functions, returned from other functions, and assigned to variables. This is a key feature of functional programming languages.
"""


def hello():
    print("Hello World!")


def add(a, b):  # Function
    total = a + b
    print(total)
    return total


# Invoking the function add()
add(12, 22)  # Output: 34


# Function with return statement and arguments length and width and can be invoked with arguments anywhere in the code
def area(length, width):
    return length * width


# Invoking the function area()
room1 = area(12, 10)
room2 = area(10, 15)
room3 = area(13, 10)
print(room1)  # Output: 120
print(room2)  # Output: 150
print(room3)  # Output: 130

floor = room1 + room2 + room3
print(floor)  # Output: 400
print("-" * 50)


# block of code that checks if a letter is a vowel or not is reusable throughout the code
def is_vowel(letter):
    vowels = ("a", "e", "i", "o", "u")
    if letter in vowels:
        return True
    else:
        return False


# Invoking the function is_vowel()
word = "apple"
for i in word:
    print(i, is_vowel(i))

print("-" * 50)


# Create a function that will return True if a number is even,
# and count number of even numbers in the range from 1 to 10
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Invoking the function is_even()
# declare the default variable count to 0 and increment it by 1.
count = 0

for i in range(1, 11):
    if is_even(i):
        count += 1
        print(i, is_even(i))
print(f"count of even numbers: {count}")
print(f"count of odd numbers: {10 - count}")

print("-" * 50)

# Use for loop to identify the number of vowels in a word
# and use slicing to replace with the capital letter of that vowel
old_word = "python"
new_word = ""

for i in old_word:
    if is_vowel(i):
        new_word += i.upper()
    else:
        new_word += i
print(f"old_word without capital vowels: {old_word}")
print(f"new_word with vowels capitalized: {new_word}")

print("-" * 50)

#! use of range function for the above example
old_word = "python"
new_word = ""

for i in range(len(old_word)):
    if is_vowel(old_word[i]):
        new_word += old_word[i].upper()
    else:
        new_word += old_word[i]
print(f"old_word without capital vowels: {old_word}")
print(f"new_word with vowels capitalized: {new_word}")

print("-" * 50)

alist = [1, 1, 1, 1, 1, 6, 1, 1, 1, 1]
# use function is_even replace the even numbers in the list, and use range
for i in range(len(alist)):
    if is_even(alist[i]):
        alist[i] = 1

print(alist)  # Output: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("-" * 50)

"""
Pig Latin is a game in Python that changes the word to a new word by adding "way" to the end of the word if the word starts with a vowel and if the word starts with a consonant, it moves the first letter to the end of the word and adds "ay" to the end of the word.
"""


def pig_latin(word):
    first_letter = word[0]
    if is_vowel(first_letter):
        return word + "way"
    else:
        return word[1:] + first_letter + "ay"


print(pig_latin("python"))  # Output: ythonpay
print(pig_latin("apple"))  # Output: appleway
print(pig_latin("elephant"))  # Output: elephantway
print(pig_latin("dog"))  # Output: ogday
print(pig_latin("scratch"))  # Output: ratchsay

print("-" * 50)


# This is a more complete version of the pig_latin function that can handle both uppercase and lowercase vowels
# The other way to write the above code for pig_latin
def pig_latin(word):
    """
    Return the Pig Latin equivalent of the word.
    """
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        # If the word starts with a vowel, add "yay" to the end
        return word + "yay"
    else:
        # Find the first vowel in the word
        for i, letter in enumerate(word):
            if letter in vowels:
                # Move the consonants before the first vowel to the end, and add "ay"
                return word[i:] + word[:i] + "ay"
        # If no vowel is found, return the word as is with "ay" (for rare cases like "rhythm")
        return word + "ay"


def main():  # main function to run the pig_latin game and prompt the user to enter a word, helper function
    word = input("Enter a word for pig latin game: ")
    if word.isalpha and len(word) > 1:
        result = pig_latin(word)
    else:
        result = "Invalid input. Please enter a valid word."
    return result


print(main())
print("-" * 50)

"""
    Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase "i" should be replaced with an uppercase "I" if it is both preceded and followed by a space. The first character in the string should also be capitalized, as well as the first non-space character after a ".", "!" or "?". For example, if the function is provided with the string "what time do i have to be there? what's the address?" then it should return the string "What time do I have to be there? What's the address?". Include a main program that reads a string from the user, capitalizes it using your function, and displays the result
"""


def capitalize(string):
    """
    Capitalize the appropriate characters in the string.
    """

    result = ""  # Initialize an empty string to store the result so that we can return it at the end
    capitalize_next = True  # Flag to indicate when to capitalize the next character

    for i in range(len(string)):
        if string[i] in ".!?":
            result += string[i]
            capitalize_next = True
        elif string[i] == " ":
            result += string[i]
        elif capitalize_next:
            result += string[i].upper()
            capitalize_next = False
        elif (
            i > 0
            and string[i - 1] == " "
            and string[i] == "i"
            and (i + 1 == len(string) or string[i + 1] == " ")
        ):
            result += "I"
        else:
            result += string[i]

    return result


# Main program to run the capitalize function with user input for more interactive experience
# Prompt the user to enter a string
string = input("Enter a string: ")
# print the capitalized string for the user
print(capitalize(string))
