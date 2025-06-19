# Create an object of SavingsAccount
# Perform:
# Deposit of some money
# Withdraw some money
# Add interest
# Show account summary
# Use proper conditionals inside each function to handle errors or logic.


print("This is a simulator that does not involve any real money or currency of any sort.")


class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Balance updated! You now have {self.balance}₹ in your account.")
        else:
            print("Invalid amount. You must enter a value above 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("You must enter a positive value above 0.")
        elif amount > self.balance:
            print(f"{amount} is more than what you have in your account. You can currently withdraw up to {self.balance} rupees.")
        else:
            self.balance = self.balance - amount
            print(f"You now have {self.balance} rupees in your account.")

    def check_balance(self):
        print(f"You currently have {self.balance} rupees in your account.")


class SavingsAccount(BankAccount):

    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_value = self.interest_rate * self.balance
        self.balance = self.balance + interest_value
        print(f"You gained {interest_value} in interest rupees. Your new balance is now {self.balance}")

    def account_summary(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance : {self.balance}")
        print(f"Interest Rate : {self.interest_rate}")

account1 = SavingsAccount("Aryan", 1000, 0.06)
account1.check_balance()
account1.deposit(400)
account1.withdraw(100)
account1.add_interest()
account1.account_summary()