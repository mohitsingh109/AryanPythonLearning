class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance for {self.account_holder}: ₹{self.balance}")

# Child class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} added. New balance: ₹{self.balance:.2f}")

    def account_summary(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance:.2f}")
        print(f"Interest Rate: {self.interest_rate * 100}%")

# Usage
acc1 = SavingsAccount("Riya", 1000)
acc1.check_balance()
acc1.deposit(500)
acc1.withdraw(200)
acc1.add_interest()
acc1.account_summary()
