
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
        if int(age) >= 21:
            print(f"Here is your {item}")
        else:
            print(f"Sorry, you are not old enough to buy {item}")
            
    print(f"Don't forget to buy {item}")

# this print stements will be executed after the loop is done and has to be outside the loop for it not to be repeated
# outside of the for loop
print("Thank you for shopping with us!")

print("-" * 50)
