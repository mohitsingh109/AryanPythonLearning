# What is abstraction?
from abc import abstractmethod, ABC

# Showing the important details and hiding the complex part from the user

# Hiding complex part and showing only the features

print("Hello")
import random

dice_roll = random.randint(1, 6)
print(dice_roll)

# In Python about abstraction:
# 1. Creating a template of what something should do (but not how)
# 2. Forcing other parts of the program to fill in the details
# 3. you can say abstraction is a way to define the requirement

# Break, Driving wheel, acc, gear, UI, speed, gas, electric...

# How to Achieve Abstraction in python?

# Abstract class, Abstract Function

# Real life payment system:

# To make Payment class as template I need to extend ABC
class Payment(ABC):
    @abstractmethod  # We are telling this is a mandatory function
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
    p.make_payment(500) # Tv Button


# Animal
# sound, eat

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

    def eat(self):
        print("Vegetables, chicken, etc..")

class Cat(Animal):

    def make_sound(self):
        print("Meow")

    def eat(self):
        print("Vegetables, chicken, etc..")


dog = Dog()
dog.make_sound()
dog.eat()

cat = Cat()
cat.make_sound()
cat.eat()


class Phone(ABC):

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def click_photo(self):
        pass

    @abstractmethod
    def storage(self):
        pass

    @abstractmethod
    def home(self):
        pass


class Samsung(Phone):

    def power_on(self):
        pass

    def power_off(self):
        print("send signal to circuit to stop all app and shutdown the phone")

    def display(self):
        pass

    def call(self):
        pass

    def click_photo(self):
        pass

    def storage(self):
        pass

    def home(self):
        pass