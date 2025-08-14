# Basic Try Catch
# try:
#     # Code which we feel can cause exception
#     num = int(input("Enter a number: ")) # Exception was thrown by python
#     print("You entered:", num)
# except ValueError: # Catching the exception
#     print("Oops! That was not a number.")


# Multiple except block

# try:
#     a = int(input("Enter numerator: ")) # Stop
#     b = int(input("Enter denominator: "))
#     print("Result: ", a / b)
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# Using else and finally

# try:
#     print("Trying something risky...")
#     result = 10 / 0
# except: # Generic Exception but we never know the reason
#     print("Something want wrong..")
# else: # Code that only run if no exception occurred
#     print("No error occurred.")
# finally: # Code block that run always either exception occurred or not
#     print("This will always run..")
#     print("Doing the cleanup operation")
#     print("Database connection close")
#     print("Send notification to someone")
#     print("Close the file read object")


# try:
#     result = 10 / 0
# except ValueError: # Catch the exception
#     print("Please enter a valid number")
# except Exception as e: # Generic Exception but we know the reason
#     print("Something want wrong..", e)

# Raising Custom exception
# We are learning how to throw the exception
# age = int(input("Enter your age: "))
#
# if age < 0:
#     raise ValueError("Age cannot be negative")


# Define Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is not a valid value")

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    elif age > 18:
        raise InvalidAgeError(age)

try:
    check_age(-5)
except InvalidAgeError as e:
    print("Error: ", e)