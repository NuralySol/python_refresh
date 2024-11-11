
#! Loops in Python are used to execute the same block of code a specified number of times.
# pandas for better visualization of the multiplication table
import pandas as pd

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

# name is a variable that will be assigned to each element in the list of friends.
for name in friends: # This loop will iterate over the list of friends and print out each name.
    print(f"Hello {name}")

print("-" * 50)

# appending the list of shopping items
shopping_list = ['apples', 'oranges', 'bananas', 'grapes']

item_input = input(" What else should I get: ")
shopping_list.append(item_input)
# do not forget to buy apples, oranges, bananas, grapes, and item_input
print(f"Here is your shopping list: {shopping_list}")
# another way to print the shopping list with the join method
print(f"Here is your shopping list: {', '.join(shopping_list)}")

# for loop to iterate over the shopping list
for item in shopping_list:
    if item == 'beer':
        age = input(f"How old are you: ")
        try:
            age = int(age)
            if age >= 21:
                print(f"Here is your {item}")
            else:
                print(f"Sorry, you are not old enough to buy {item}")
        except ValueError:
            print("Invalid age input. Please enter a number.")
            
    print(f"Don't forget to buy {item}")

# this print stements will be executed after the loop is done and has to be outside the loop for it not to be repeated
# outside of the for loop
print("Thank you for shopping with us!")

print("-" * 50)

numbers = [1, 2, 3, 4, 5, 5, 5, 5, 5]

for even_or_odd in numbers:
    if even_or_odd % 2 == 0:
        print(f"{even_or_odd} is an even number.")
    else:
        print(f"{even_or_odd} is an odd number.")
# more refractored way to print even and odd numbers in the list to print only once and not repeat the print statement
print(f"even numbers are : {[even_or_odd for even_or_odd in numbers if even_or_odd % 2 == 0]}")
print(f"odd numbers are : {[even_or_odd for even_or_odd in numbers if even_or_odd % 2 != 0]}")
        
print("-" * 50)

# for loop to iterate over the numbers list and count the number of times 5 appears in the list
# nothing beats built-in methods in Python
count_of_fives = 0
for number in numbers:
    if number == 5:
        count_of_fives += 1
print(f"The number 5 appears {count_of_fives} times in the list.")
print("-" * 50)



# this is a a more refractored way to count the number of times character appear in a string object that contains different characters and symbols
string = "apple12345@@@@@$$$$$"

num_letters = sum(char.isalpha() for char in string)
num_digits = sum(char.isdigit() for char in string)
at_chars = sum(char == '@' for char in string)
dollar_chars = sum(char == '$' for char in string)

print(f"The number of letters in the string is: {num_letters}")
print(f"The number of digits in the string is: {num_digits}")
print(f"The number of @ characters in the string is: {at_chars}")
print(f"The number of $ characters in the string is: {dollar_chars}")
print("-" * 50)

#! Define vowel, consonant, and ambiguous letter sets
vowels_set = 'aeiou'
consonants_set = 'bcdfghjklmnpqrstvwxz'
y_char = 'y' # this is a special case

# Initialize counters for vowels, consonants, and y special case
vowel_count = 0
consonant_count = 0
y_count = 0

# Get the user input and use the .lower() method to convert the input to lowercase
user_input = input("Please enter a string of letters: ").lower()

# Use for loop with if and elif statements to check if the letter is a vowel, consonant, or is y special case
for letter in user_input:
    if letter in vowels_set:
        vowel_count += 1
        print(f"{letter} is a vowel.")
    elif letter in consonants_set:
        consonant_count += 1
        print(f"{letter} is a consonant.")
    elif letter == y_char:
        y_count += 1
        print(f"{letter} can be either a vowel or a consonant.")
    else: 
        print("Invalid input. Please enter only letters.")
        break
else:
    # Summary of the results for better output and readability
    print("\nSummary:")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"'y' occurrences: {y_count} (that can be either a vowel or a consonant)")
    
print("-" * 50)

#! Tuples in Python
# Tuples are immutable objects in Python unlike lists which are mutable objects
# Tuples can hold different data types and it is okay unlike lists which should BE homogeneous
tuple1 = (1, 2, 3, 4, 5)

# unpacking the tuple
print(divmod(5, 3)) # returns a tuple of the quotient and the remainder

#! Funciton range() in Python produces sequence of integers
# range(start, stop, step) - start is inclusive, stop is exclusive, and step is the increment
for i in range(1, 12, 1):
    print(f"range of i is: {i}")

for n in range(10, 0, -1):
    print(f"range of i is: {n}")

#! using the range function to iterate over the word
word = "apple"

for index in range(len(word)):
    print(f"index of word is: {index, word[index]}")

# flipping using the slice operator [::-1] 
flipped1 = word[::-1]
print(f"flipped word is: {flipped1}")
# using range function to flip the word
flipped2 = ''.join(word[index] for index in range(len(word)-1, -1, -1))
print(f"flipped word is: {flipped2}")

# using the range function to print the pattern of stars
symbol = "*"

for i in range(1, 4):
    print((symbol + " ") * i)
for j in range(4, 0, -1):
    print((symbol + " ") * j)
    
#! Multiplication table using the range function 1-10
# nested for loop for range to get multiplication table of 1-10 
# this multiplication table is stored in a list and then converted to a pandas dataframe for better visualization
multiplication_table = []

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i * j)
    multiplication_table.append(row)

df = pd.DataFrame(multiplication_table, columns=range(1, 11), index=range(1, 11))
print(df)
print("-" * 50)

#! Or do the old school way of printing the multiplication table
for i in range(1, 10 + 1): 
    for j in range(1, 10 + 1): 
        print(f"{i * j:4}", end=" ") 
    print(" ^ ")  # Print a separator to indicate the end of each row

print("-" * 50)    

# given a list of numbers, replace 1 with 0
list_1 = [0, 0, 0, 0, 1, 0, 0, 0, 0]

# for loop to replace the 1 with 0 in the list and print the new list using the for loop
for i in range (0, len(list_1)):
    if (list_1[i] == 1):
        list_1[i] = 0

print(list_1)

"""
Fizzbuzz is a game where you count numbers from 1 to 100 and if the number is divisible by 3 print Fizz.
If the number is divisible by 5 print Buzz, if the number is divisible by both 3 and 5 print FizzBuzz.
If the number is not divisible by 3 or 5 print the number, this is a classic interview question.
"""

# range function can never take a float as an argument or parameter it must be an integer
for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)    
        
print("-" * 50)

# function enumirate() in Python is used to iterate over a sequence and return the index and the value of the item
# this is a more efficient way to iterate over a sequence

#! Maybe a more neater way of doing things compared to range? not sure
e = list(enumerate("apple"))
# unpacking the list of tuples
for index, value in enumerate("apple"):
    print(index, value)

# use a function to check if a word is a palindrome or not
# function are way better use of code than repeating the same code over and over again (functional porgramming)
# palindrome problem in Python

# declare a palindrome word
palindrome = "racecar"

def palindrome_function(word):
    return word == word[::-1]

midpoint = len(palindrome) // 2
palindrome_function = True
for i in range(midpoint):
    if palindrome[i] != palindrome[-i - 1]:
        palindrome_function = False
        break

if palindrome_function:
    print("Is a palindrome")
else:
    print("Not a palindrome")

# another way of solving the palindrome problem

palindrome_candidate = "racecar"
midpoint = len(palindrome_candidate) // 2
is_palindrome = True

for i in range(midpoint):
    print("---->",i, palindrome_candidate[i])
    print("<----",len(palindrome_candidate)-1-i, palindrome_candidate[len(palindrome_candidate)-1-i])
    if palindrome_candidate[i] != palindrome_candidate[len(palindrome_candidate)-1-i]:
        is_palindrome = False

print(is_palindrome)