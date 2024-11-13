
fruit = ["apple", "banana", "pear", "orange"]
# count number of letters in a string and add these numbers to a new list
fruit_letter_count = [len(fruit) for fruit in fruit]
print(f"fruit_letter_count" , fruit_letter_count)
print("-" * 100)

#! List comprehension 
numbers = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
fives = [number for number in numbers if number == 5]
print("numbes: ", numbers)
print("-" * 100)
print(f"fives: {fives}")
print("-" * 100)

#! [Expression for loop filer] **List comprehension** is more efficient than using a for loop

weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
# Capitilize weekdays using list comprehension 
weekdays_capitalized = [day.capitalize() for day in weekdays]
print(f"weekdays_capitalized: {weekdays_capitalized}")

print("-" * 100)
# Function join in a list comprehension

string = "a1b2c3d4e5f6"
# use list comprehension and multiply all numbers by 100
numbers = [int(char) * 100 for char in string if char.isdigit()]
print(f"numbers: {numbers}")

print("-" * 100)
# Join method to convert the list of numbers to a string
numbers_string = ", ".join(map(str, numbers))
print(f"numbers_string: {numbers_string}")

print("-" * 100)

# if and else with list comprehension
numbers = list(range(1, 11))
# if the number is even or odd with list comprehension returns a tuple of a list of numbers with key value pairs
even_odd = [(number, "even" if number % 2 == 0 else "odd") for number in numbers]
print(f"even_odd new list is : {even_odd}")
print("-" * 100)
