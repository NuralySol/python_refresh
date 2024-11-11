
#! Refresh the python skills with the following exercises
#! Material review and practice for the python programming language

#  define some variables x and y
x = 7
y = 2.5

# 1. Print the type of x and y to see what kind of data types are they
# Python is a dynamically typed language, so the type of a variable is determined at runtime
print(f"-" * 50)
print(type(x))
print(type(y))

# 2. Print the sum of x and y, just use the print and f-string to do math operation and only work with integers and floats, and vice versa
print(f"result of x + y is : {type(x + y)}") # it will be float
print(f"-" * 50)

# 3. Print the difference of x and y and save the variable in the total
total = x + y
print(f"result of x + y is : {total}") # it will be float and it still is a float
print(f"-" * 50)

#! String is a sequence of characters, and it is immutable, and it holds many characters, and anything you wrap in the quotes is a string 
s = "7"
print(f"type(s)", type(s))
print(f"-" * 50)

converted_from_string = 7 + int(s) # it will be 14
print(f"converted_from_string", converted_from_string)
print(f"-" * 50)

# 4. Print the product of x and y and save the variable in the total
print(f"ord of 7 string is: {ord('7')}") # 55 returns the Unicode code point of the character at the given index
print(f"-" * 50)

# 5. Tax and tip calculator 
# Define what is given check is 50, tax is 8% and the tip is 20% of the check
check = float(input("Enter the check amount: ")) # There is a need to floatify the input
tax = 0.08
tip = 0.20

# Calculate the tax and tip and add them to the check
tax_amount = check * tax
tip_amount = check * tip
total = check + tax_amount + tip_amount
print(f"total for the check including tax and tip is: ${total:.2f}, {type(total)}") 
# total is going to be float :.2f is used to format the float number to 2 decimal places and use $ sign
print(f"-" * 50)

#! Build an online store coffee shop and muffin shop

"""
Ask the user how many coffee and muffins they want to buy
calculate the total price and print it out 
static variables for the purpose of the exercise but better way to use capital 
letters for the constants like COFFEE
and MUFFIN
"""
#! The following code is not handling the exceptions and is not validating the input from the user
"""
coffee = 3.0
muffin = 1.5

coffee_quantity = int(input("Enter the quantity of coffee you wish to buy: "))
muffin_quantity = int(input("Enter the quantity of muffins you wish to buy: "))
total_price = (coffee * coffee_quantity) + (muffin * muffin_quantity)
print(f"total price for the coffee and muffins is: ${total_price:.2f}")
"""

#! The following code is handling the exceptions and is validating the input from the user using the while loop and try except block with ValueError built-in exception of the python language
coffee = 3.0
muffin = 1.5

while True:
	try:
		coffee_quantity = int(input("Enter the quantity of coffee you wish to buy: "))
		if coffee_quantity < 0:
			raise ValueError("Quantity cannot be negative.")
		break
	except ValueError as e:
		print(f"Invalid input: {e}. Please enter a valid non-negative integer.")

while True:
	try:
		muffin_quantity = int(input("Enter the quantity of muffins you wish to buy: "))
		if muffin_quantity < 0:
			raise ValueError("Quantity cannot be negative.")
		break
	except ValueError as e:
		print(f"Invalid input: {e}. Please enter a valid non-negative integer.")

total_price = (coffee * coffee_quantity) + (muffin * muffin_quantity)
print(f"total price for the coffee and muffins is: ${total_price:.2f}")
print(f"-" * 50)

