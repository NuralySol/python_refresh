
#! Classes are a way to bundle data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

class CreditCardValidator:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = self.determine_card_type()
        self.valid = self.validate()

    def determine_card_type(self):
        if self.card_number[0] == '4':
            return 'Visa'
        elif self.card_number[0:2] in ['51', '52', '53', '54', '55']:
            return 'Mastercard'
        elif self.card_number[0:2] in ['34', '37']:
            return 'AMEX'
        elif self.card_number[0:2] == '60':
            return 'Discover'
        else:
            return 'INVALID'

    def check_length(self):
        if self.card_type == 'Visa' or self.card_type == 'Mastercard' or self.card_type == 'Discover':
            return len(self.card_number) == 16
        elif self.card_type == 'AMEX':
            return len(self.card_number) == 15
        else:
            return False
    
    # A function to validate the credit card number using the Luhn Algorithm
    def validate(self):
        
        """
        Validates a credit card number using the Luhn algorithm.

        Steps:
        1. Check if the card number length is valid using the `check_length` method.
        2. Initialize a total sum to 0.
        3. Iterate over each digit in the card number, starting from the rightmost digit:
            a. If the position is odd (1-based index), double the digit.
            If the doubled value is greater than 9, subtract 9 from it.
            b. Add the resulting value to the total sum.
            c. If the position is even, add the digit directly to the total sum.
        4. Check if the total sum modulo 10 is equal to 0.
        
        Returns:
            bool: True if the card number is valid according to the Luhn algorithm, False otherwise.
        """
        if self.check_length() == False:
            return False
        total = 0
        for i, digit in enumerate(self.card_number[::-1]):
            if i % 2 == 1:
                double = int(digit) * 2
                if double > 9:
                    double -= 9
                total += double
            else:
                total += int(digit)
        return total % 10 == 0
    

# Some test cases to see if the class is working as expected 
# Test cases
myCard = CreditCardValidator('347650202246884')
print(myCard.valid) # True

# True Test cases 
myCard = CreditCardValidator('6011053711075799')
print(myCard.valid) # True

# False Test cases
myCard = CreditCardValidator('379179')
print(myCard.valid) # False

# Use the input method to get the card number from the user and validate it and print the result of it
card_number = input("Enter your card number: ")
myCard = CreditCardValidator(card_number)

if myCard.valid:
    print(f"{myCard.card_type} Card is Valid")
else:
    print(f"{myCard.card_type} card please check the card number and try again")

"""
We want our class to have its three main properties set on  - card_number, card_type, and valid.
If the card number given passes the Luhn algorithm, valid should be true and cardType should be set to 'VISA', 'AMEX', etc. If it does not pass, valid should be false and cardType should be set to "INVALID"

This way, we can do this:
```python
    myCard = CreditCard('347650202246884')
    myCard.valid ## true
    myCard.card_type ## 'AMEX'
    myCard.card_number ## '347650202246884'
```
There are three instance methods. You may perform these methods in the order you see fit.
`determine_card_type` should check whether or not the credit card has valid starting numbers and return the card type.
Visa must start with 4  
Mastercard must start with 51, 52, 53, 54 or 55  
AMEX must start with 34 or 37  
Discover must start with 60 
`check_length` should check whether or not a credit card number is a valid length.
Visa, MC and Discover have 16 digits  
AMEX has 15  
`validate` should run the Luhn Algorithm and return true or false.
The Algorithm
From the right most digit, double the value of every second digit. For example:
`4 4 8 5 0 4 0 9 9 3 2 8 7 6 1 6`
becomes
`8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6`
Now, sum all the individual digits together. That is to say, split any numbers with two digits into their individual digits and add them. Like so:
`8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2 + 6`
Now take the sum of those numbers and modulo 10.
80 % 10
If the result is 0, the credit card number is valid.
Keep your code super clean and DRY.
If you are repeating yourself, stop and think about how to better approach the problem.
"""

# '6011053711075799'  "Discover Card is Valid"
# '379179199857686' "AMEX is Valid"
# '4929896355493470' "Visa Card is Valid"
# Write a Python class to validate credit cards.
# the Luhn Algorithm , also known as "modulus 10", we will be determining the validity of a given credit card number.




