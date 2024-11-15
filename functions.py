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

"""
    Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope.
"""

# 1. Basic Lambda: Simple arithmetic operation
add_5 = lambda x: x + 5
print("Add 5 to 10:", add_5(10))  # Output: 15

# 2. Lambda with multiple arguments: Area of a rectangle
area = lambda length, width: length * width
print("Area of 5x3 rectangle:", area(5, 3))  # Output: 15

# 3. Using lambda with map(): Transforming a list of numbers by squaring each element
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 4. Using lambda with filter(): Filtering out odd numbers from a list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)  # Output: [2, 4]

# 5. Using lambda with sorted(): Sorting a list of tuples by the second element
points = [(2, 3), (1, 2), (3, 1), (5, 0)]
sorted_by_second = sorted(points, key=lambda x: x[1])
print("Sorted by second element:", sorted_by_second)  # Output: [(5, 0), (3, 1), (1, 2), (2, 3)]

# 6. Lambda in a dictionary for conditional mapping
operation = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Undefined"
}
print("Addition:", operation["add"](10, 5))           # Output: 15
print("Subtraction:", operation["subtract"](10, 5))   # Output: 5
print("Multiplication:", operation["multiply"](10, 5)) # Output: 50
print("Division:", operation["divide"](10, 0))        # Output: Undefined

# 7. Lambda in a higher-order function: Function that applies a given operation to two numbers
def apply_operation(x, y, func):
    return func(x, y)

result = apply_operation(10, 20, lambda a, b: a + b)
print("Applying addition operation:", result)  # Output: 30

# 8. Lambda with sorted() for complex structures: Sorting a list of dictionaries by a specific key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)
print("Students sorted by grade (desc):", sorted_students)
# Output: [{'name': 'Bob', 'grade': 92}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 78}]

# 9. Lambda with reduce() to compute the product of a list (requires functools)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)  # Output: 120

# 10. Lambda to capitalize a days of week in a list
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
capitalize_days = list(map(lambda day: day.capitalize(), days))
print("Capitalized days:", capitalize_days)  # Output: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

numbers = list(range(1, 11))
even_odd = map(lambda x: (x, "Even" if x % 2 == 0 else "Odd"), numbers)
print(f"Even and Odd numbers: {list(even_odd)}")

# if number is greater than 5, multiply it by 100, otherwise leave the number as it is, use map and lambda in numbers list

numbers = list(range(1, 11))
result = map(lambda x: x * 100 if x > 5 else x, numbers)
print(f"Numbers multiplied by 100 if greater than 5: {list(result)}")

# Quirks of floating point arithmetic: 0.1 + 0.2 is not equal to 0.3 in Python
# This is because of the way floating point numbers are stored in memory
# You can use the math.isclose method to compare floating point numbers
a = 0.2 + 0.4
b = 0.6
print(a == b)  # False

a = 0.1 + 0.3
b = 0.4
print(a == b)  # True
