# Dictionaires are a collection of key-value pairs
# The keys are unique and immutable, and only immutable objects can be used as keys and value can be any object (data type)

#! Syntax: dictionary = {key1: value1, key2: value2, key3: value3}
# Creating dictionaries
person = {"name": "Alice", "age": 28, "city": "New York"}
car = dict(make="Toyota", model="Camry", year=2022)
empty_dict = {}

# Accessing values
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 28
print(person.get("height", "Unknown"))  # Output: Unknown

# Modifying values
person["occupation"] = "Engineer"  # Adding a new key-value pair
person["age"] = 29  # Updating an existing value
print(
    person
)  # Output: {'name': 'Alice', 'age': 29, 'city': 'New York', 'occupation': 'Engineer'}

# Removing key-value pairs
person.pop("city")  # Removes "city"
print(person)  # Output: {'name': 'Alice', 'age': 29, 'occupation': 'Engineer'}
last_item = person.popitem()  # Removes the last inserted item
print(last_item)  # Output: ('occupation', 'Engineer')
del person["age"]  # Removes "age"
print(person)  # Output: {'name': 'Alice'}

# Dictionary methods
keys = car.keys()  # Gets all keys
values = car.values()  # Gets all values
items = car.items()  # Gets all key-value pairs
print(keys, values, items)

# Iterating through a dictionary
for key, value in car.items():
    print(f"{key}: {value}")

# Nested dictionary
students = {
    "student1": {"name": "Bob", "age": 20},
    "student2": {"name": "Carol", "age": 22},
}
print(students["student1"]["name"])  # Output: Bob

# Dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#! More advanced examples of dictionary examples.

# 1. Merging dictionaries using `update()` and dictionary unpacking
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Using `update()` method (modifies dict1 in place)
dict1.update(dict2)
print("After update:", dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Merging with dictionary unpacking (does not modify original dictionaries)
merged_dict = {**dict1, **dict2}
print("Merged with unpacking:", merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# 2. Setting default values with `setdefault()`
person = {"name": "Alice", "age": 30}
person.setdefault("city", "Unknown")
print(
    "With default city:", person
)  # Output: {'name': 'Alice', 'age': 30, 'city': 'Unknown'}

# 3. Creating a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Bob", 25, "San Francisco"]
person_from_lists = dict(zip(keys, values))
print(
    "Dictionary from lists:", person_from_lists
)  # Output: {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}

# 4. Nested dictionaries and accessing deeply nested values
company = {
    "HR": {"employees": 5, "manager": {"name": "John", "age": 45}},
    "Engineering": {"employees": 10, "manager": {"name": "Anna", "age": 40}},
}
print("HR manager name:", company["HR"]["manager"]["name"])  # Output: John

# Safely accessing deeply nested values using `get`
hr_manager_age = company.get("HR", {}).get("manager", {}).get("age", "N/A")
print("HR manager age:", hr_manager_age)  # Output: 45

# 5. Applying a function to dictionary values
# Let's say we have a dictionary of items with their prices and we want to apply a 10% discount to each item
prices = {"apple": 1.0, "banana": 0.5, "orange": 0.75}
discounted_prices = {item: price * 0.9 for item, price in prices.items()}
print(
    "Discounted prices:", discounted_prices
)  # Output: {'apple': 0.9, 'banana': 0.45, 'orange': 0.675}

# 6. Counting occurrences with dictionaries
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print("Word counts:", word_counts)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# 7. Grouping items by a key
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"},
]
# Group students by grade
from collections import defaultdict

grouped_students = defaultdict(list)
for student in students:
    grouped_students[student["grade"]].append(student["name"])
print("Grouped students by grade:", dict(grouped_students))
# Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}

# 8. Sorting a dictionary by values
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(
    "Sorted scores by value:", sorted_scores
)  # Output: {'Bob': 92, 'Alice': 85, 'Charlie': 78}

# 9. Dictionary comprehension with conditional logic
items = {"apple": 2, "banana": 5, "cherry": 0, "date": 10}
# Filter out items with quantity 0
available_items = {k: v for k, v in items.items() if v > 0}
print(
    "Available items:", available_items
)  # Output: {'apple': 2, 'banana': 5, 'date': 10}

# 10. Using a dictionary as a frequency counter with `collections.Counter`
from collections import Counter

char_counter = Counter("hello world")
print(
    "Character counts:", dict(char_counter)
)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

"""
Summary of Dictionaries in Python:

1. **Definition**: Dictionaries store data as key-value pairs, allowing quick data retrieval based on unique keys.

2. **Creation**:
- Using `{}` or `dict()` with key-value pairs.
- From lists or other structures using `zip()` or comprehensions.

3. **Accessing and Modifying**:
- Use `dict[key]` or `dict.get(key, default)` to retrieve values.
- Update values by assigning to `dict[key]` or adding new pairs.

4. **Common Methods**:
- `update()` merges dictionaries.
- `pop()` removes a specified key and returns its value.
- `setdefault()` provides a default if a key is missing.
- `keys()`, `values()`, `items()` access dictionary parts for iteration.

5. **Advanced Uses**:
- **Nested Dictionaries** for multi-level data storage.
- **Dictionary Comprehensions** for generating dictionaries dynamically.
- **Counting & Grouping**: Use dictionaries to count occurrences or group items by a key.
- **Sorting by Values** using `sorted()` with a custom key.

6. **Libraries**:
- `collections.defaultdict` simplifies grouping with default lists.
- `collections.Counter` efficiently counts occurrences of items.

Dictionaries are highly versatile and widely used in Python for structured data storage and manipulation.
"""
