# to hide the internal details of how something works
# Why we use encapsulation?
# keep data safe from outside interface
# Control how data is accessed or changed

class BankAccount:
    def __init__(self, owner, balance):
        # Private variable
        self.__owner = owner
        # Private variable
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        # I ve send the otp to your mobile phone
        # User end the otp
        # Opt is valid
        self.__owner = name

    def print_details(self):
        print(f"Owner: {self.__owner}, Balance: {self.__balance}")


def hack_me(account):
    account.__owner = "hacker"
    account.__balance = 0 # it;s adding new variable inside the object

# I am loading this from some database
account1 = BankAccount("Aryan", 12345)

# Before hack
account1.print_details()

account1.set_name("Mohit")

account1.print_details()
account1.get_balance()

hack_me(account1)

# After hack
account1.print_details()
