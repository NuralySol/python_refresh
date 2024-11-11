
#! Strings in Python
# Strings are a sequence of characters, and it is immutable, and it holds many characters, and anything you wrap in the quotes is a string. 
word = "apple"
print(dir(word)) # dir() function returns all the properties and methods of the specified object, without the values
print(f"-" * 50)

name = "John"
greeting = "Hello {}" # {} is a placeholder for an argument
print(greeting.format(name)) # Hello John
print(f"-" * 50)

greeting = f"Hello {name}"
print(greeting) # Hello John
print(f"-" * 50)

# use type(), dir() and help() functions to get the information about any object
#! Conditional statements in Python Boolean (True or False)
# Boolean is a data type that is either True or False
print(2 * 2 == 4) # True == is a comparison operator
print(f"-" * 50)

print("apple"=="Apple") # False because of the case sensitivity apple is not equal to Apple
print(f"-" * 50)

#! if, elif and else statements in Python
# Indentation is a must in Python and it is a part of the syntax for blocks of code
# use .strip() method to remove the white spaces from the string
# use .lower() method to convert the string to lowercase
word = input("Enter a word: ").strip().lower()

if word == "apple": 
    print("I love apples")
elif word == "banana": 
    print("I love bananas instead")
elif word == "mango":
    print("I love cherries")
else: 
    print("I do not like those fruits at all")

print(f"-" * 50)

# how old is the user if they are 21 or older they can drink alcohol with validation of the input
while True:
    age_input = input("Enter your age please: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number.")

if age >= 21:
    print("You can drink alcohol")
else:
    print("Go home kid")

print(f"-" * 50)

# Ask the user for number if the number is even using the modulus operator % and if the remainder is 0 then it is even
# if the remainder is not 0 then it is odd with a validation of the input
user_input = input("Enter a number: ")
while not user_input.isdigit():
    print("Please enter a valid number.")
    user_input = input("Enter a number: ")

user_input = int(user_input)

if user_input % 2 == 0:
    print("The number entered is even")
else:
    print("The number entered is odd")

print(f"-" * 50)

# The optimized version and with better user experience and validation of the input
number = input("Give me a number and I will tell you if it's even or odd: ").strip()
if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")
else:
    print("Invalid input, please enter a valid number.")

print(f"-" * 50)

#! List container in Python

box = []
print(type(box)) # <class 'list'> 

# .append() method is used to add the elements to the list and only takes one argument
box.append(1)
box.append(10)
box.append(5)

print(box) # [1, 10, 5]

# list is a sequence of elements separated by commas and enclosed in square brackets and it is mutable
# You should not use mixed data types in the list BAD PRACTICE (homogeneous data types only)
box.sort() # sort() method is used to sort the elements in the list
print(box) # [1, 5, 10]

print(f"-" * 50)

# you can grab the elements from the list using the index it starts from 0 and last one is always -1
print(box[0]) # 1 
print(box[1]) # 5
print(box[2]) # 10  

print(f"-" * 50)

# slicing the list
print(box[0:2]) # [1, 5] 0 is inclusive and 2 is exclusive
print(box[1:3]) # [5, 10] 1 is inclusive and 3 is exclusive

# shift-return for REPL in the Jupyter notebook
string = "aAbBcCdDeE"

lowercase = string[0::2] 
print(lowercase)

# slicing the zip code from the address object and get last 5 characters of the string
address = "115 W 30th St., 5th Floor, Suite 501, New York, NY, 12345"

zip_code = address[-5:]
print(zip_code)
print(len(address))
address = address.split(", ")[-3] # Get the state from the address 
print(address)