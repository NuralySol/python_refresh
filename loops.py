
#! Loops in Python are used to execute the same block of code a specified number of times.

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
flipped = word[::-1]
print(f"flipped word is: {flipped}")
# using range function to flip the word
flipped2 = ''.join(word[index] for index in range(len(word)-1, -1, -1))
print(f"flipped word is: {flipped2}")