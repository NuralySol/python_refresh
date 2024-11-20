# For loop is definite loop, while loop is indefinite loop until the condition is met.

condition = 0

while condition < 10:
    print(condition, " + Hello World")
    condition += 1
print("End of the loop")
print("-" * 100)

# Infinite loop - while True:
flag_var = True

while flag_var:
    print("Hello Everyone")
    flag_var = False
    print("End of the loop")
print("-" * 100)

# shopping_list = []
# ask the user what to buy, keep asking the user will enter keyword "stop", make sure the user enters each item only once
# use while loop

#! While loop using the break statement and empty string variable. To include the stop keyword in the shopping list, we can use the break statement to exit the loop when the user enters the stop keyword.

shopping_list = []

item = ""

while item.lower() != "stop":
    item = input("Enter the grocery item you wish to buy: ").lower()
    if item == "stop" or item == "Stop":
        break
    if item not in shopping_list:
        shopping_list.append(item)
    else:
        print("Item already in the shopping list")

print(f"Your shopping list is: \n {shopping_list}, \nYou can go shopping now!")
print("-" * 100)

# Binary Search Algorithm given a sorted alist
alist = [10, 20, 30, 40, 50, 60, 70]


def binary_search(list_bsearch, target):
    low = 0
    high = len(list_bsearch) - 1

    while low <= high:
        mid = (low + high) // 2
        if list_bsearch[mid] == target:
            return mid
        elif list_bsearch[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Art hates while True loop
while True:
    try:
        target = int(input("Enter the target value to search in the list: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

index = binary_search(alist, target)
if index != -1:
    print(
        f"Target found at index: {index} \nThe value is: {alist[index]}, \n*{True}* that it is in the list"
    )
else:
    print("Target not found")

print("-" * 100)

# Swawpping values in Python (only works for mutable objects)
a = 10
b = 20

print(f"Before swapping: a = {a}, b = {b}")
# Only works for mutable objects
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

# Bubble sort algorithm - sorting algorithm
unsorted = [70, 30, 10]

# Used the range function to iterate over the list and compare the adjacent elements to swap them if they are in the wrong order. With the flag check, we can break the loop if the list is already sorted. This is the optimized version of the bubble sort algorithm.

def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = True
        if not swapped:
            break
    return alist

print(f"Unsorted list before bubble sort is:\n{unsorted}")
sorted_list_bsort = bubble_sort(unsorted)
print(f"Your new sorted list using bubble sort is:\n{sorted_list_bsort}")

#! Bubble sort algorithm - needs two loops to sort the list. Which makes it O(n^2) for worst case, O(n) for best case if the list is already sorted.
