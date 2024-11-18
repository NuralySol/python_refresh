# Begin class definition by assigning the class keyword followed by the class name and attributes.
# Class is a blueprint for creating objects. It defines the attributes and methods that an object will have.
class Car:
    def __init__(
        self, make, model, color
    ):  # self is always the first argument in the __init__ method
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
    def __init__(self, name, balance=0.0):
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


# Create a class to calculate area of the room
class AreaRoom:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    # static method to be called on the class itself rather through an instance of the class since the formula does not depend on the instance of the class
    @staticmethod
    def area_static(width, length):
        return width * length


# Create an instance of the AreaRoom class
living_room = AreaRoom(10, 20)
print(f"Area of the living room: {living_room.area()}")
print("-" * 100)
# call the static method on the class itself without an instance of the class
print(f"Area of the living room using static method: {AreaRoom.area_static(10, 20)}")
print("-" * 100)


# The most comprehensive example of the Class and Object.
class Employee:
    def __init__(self, *args, **kwargs):
        # Handle positional arguments
        if args:
            self.id = args[0]
        else:
            self.id = None

        # Handle keyword arguments
        self.name = kwargs.get("name", "Unknown")
        self.role = kwargs.get("role", "Unknown")
        self.salary = kwargs.get("salary", 0)
        self.details = kwargs

    def display_info(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: ${self.salary}")
        print(f"Additional Details: {self.details}")

# Create a Manager class that inherits from the Employee class 
class Manager(Employee):
    def __init__(self, *args, **kwargs):
        # Call the parent class constructor
        super().__init__(*args, **kwargs)
        self.team_size = kwargs.get("team_size", 0)

    def display_info(self):
        # Extend the parent class method
        super().display_info()
        print(f"Team Size: {self.team_size}")

    def allocate_bonus(self, *args, **kwargs):
        """Allocate bonuses dynamically to team members."""
        print("\nAllocating Bonuses:")
        total_bonus = kwargs.get("total_bonus", 0)
        team_members = kwargs.get("team_members", [])
        if team_members:
            per_member_bonus = total_bonus / len(team_members)
            for member in team_members:
                print(f"{member} receives a bonus of ${per_member_bonus:.2f}")
        else:
            print("No team members to allocate bonus to.")


# Usage example
# Create a generic Employee
employee = Employee(101, name="John Doe", role="Developer", salary=75000)
employee.display_info()

print("-" * 100)

# Create a Manager with additional team details
manager = Manager(201, name="Jane Smith", role="Team Lead", salary=120000, team_size=5)
manager.display_info()

print("-" * 100)

"""
When to Use *args and **kwargs:
*args:
- Use *args when you don’t know beforehand how many positional arguments a method might receive.
- Example: Passing a list of values for processing.

**kwargs:
- Use **kwargs when you want to handle a variable number of keyword arguments.
- Example: Setting optional attributes for a class.
"""
