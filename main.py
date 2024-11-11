
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
# Define what is given check is 50, tax is 8% and the tip is 20% 
# Use the int and float to calculate the tax and tip and add them to the check
check = 50
tax = 0.08
tip = 0.20

# Calculate the tax and tip and add them to the check
tax_amount = check * tax
tip_amount = check * tip
total = check + tax_amount + tip_amount
print(f"total for the check is: ${total:.2f}, {type(total)}") 
# total is going to be float :.2f is used to format the float number to 2 decimal places and use $ sign
print(f"-" * 50)

