
# Begin class definition by assigning the class keyword followed by the class name and attributes.
# Class is a blueprint for creating objects. It defines the attributes and methods that an object will have.
class Car:
    def __init__(self, make, model, color): # self is always the first argument in the __init__ method
        # Assign the attributes to the class
        self.make = make
        self.model = model
        self.color = color
        
    # Define a method that will return the make of the car

a = Car("Toyota", "Corolla", "Red")
b = Car("Honda", "Civic", "Blue")

# Create a class called Customer with the __init__ method that takes in the name and balance of the customer.
# Bank account class
class Customer:
    def __init__ (self, name, balance = 0.0):
        self.name = name
        self.balance = balance
    # Define a method that will return the name of the customer and the balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError("Amount greater than available balance.")
        else:
            self.balance -= amount
            return self.balance
    # Define a deposit method that will add the amount to the balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
# Create an instance of the Customer class
john = Customer("John Doe", 1000.0)
# Print the name and balance of the john object
print(f"John's balance: {john.balance}")
print("-" * 100)
# Call the withdraw method on the john object
john.withdraw(500)
print(f"John's balance after withdrawal: {john.balance}")
print("-" * 100)
# John wants to add more money to his account
john.deposit(1200)
print(f"John's balance after deposit: {john.balance}")
print("-" * 100)