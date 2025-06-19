class BankAccount:
    def __init__(self, account_holder, balance=0, minimum_balance=100):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction = []
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
            self.transaction.append(f"Deposited {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > self.balance - self.minimum_balance:
            print(f"Cannot withdraw. Balance would fall below minimum required {self.minimum_balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")
            self.transaction.append(f"Withdrew {amount}")

    def check_balance(self):
        print(f"Current balance for {self.account_holder}: ₹{self.balance}")
        
    def show_transactions(self):
        print("Transaction History:")
        for action in self.transaction:
            print(action)
        
# Child class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05, minimum_balance=100):
        super().__init__(account_holder, balance, minimum_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} added. New balance: ₹{self.balance:.2f}")
        self.transaction.append(f"Interest  {interest:.2f}")

    def account_summary(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance:.2f}")
        print(f"Interest Rate: {self.interest_rate * 100}%")

def data_summary(account_list):
    for account in account_list:
        print(f"{account.account_holder} - {account.balance} - {len(account.transaction)} Transactions")

# Usage
acc1 = SavingsAccount("Riya", 1000)
acc2 = SavingsAccount("Aryan", 1000000)
acc3 = SavingsAccount("Mohit", 1000001)
account_list = [acc1, acc2, acc3]

acc1.deposit(300)
acc1.withdraw(75)

acc2.add_interest()
acc2.withdraw(10.785676543454)
acc2.deposit(10.325434567656)

acc3.withdraw(100000.98)

data_summary(account_list)
