# What is abstraction?
from abc import abstractmethod, ABC

# Showing the important details and hiding the complex part from the user

print("Hello")
import random

dice_roll = random.randint(1, 6)
print(dice_roll)

# How to Achieve Abstraction in python?

# Abstract class, Abstract Function

# Real life payment system:

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CashPayment(Payment):
    def make_payment(self, amount):
        print(f"Paying {amount} in cash.")

class CardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paying {amount} using debit card.")

class UpiPayment(Payment):
    def make_payment(self, amount):
        print(f"Paying {amount} using UPI.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paying {amount} using Paypal.")


payments = [CardPayment(), CashPayment(), PayPalPayment()]

for p in payments:
    p.make_payment(500)