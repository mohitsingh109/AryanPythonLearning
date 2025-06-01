
# 🏦 Python OOP Assignment: Bank Account System

In this assignment, you'll use **Object-Oriented Programming** in Python to build a simple **banking system** using **inheritance** and **multiple methods**.

---

## 🎯 Task Overview

You will create:
- A **Parent Class**: `BankAccount`
- A **Child Class**: `SavingsAccount` that inherits from `BankAccount`

---

## 🧩 Part 1: BankAccount Class

Create a class `BankAccount` with:

### 🔸 Attributes:
- `account_holder` (name of the person)
- `balance` (default should be ₹0)

### 🔸 Methods:
1. `deposit(amount)` – adds money to balance
   - Show error if amount is zero or negative
2. `withdraw(amount)` – subtracts money
   - Show error if insufficient balance or negative amount
3. `check_balance()` – prints current balance

---

## 🧩 Part 2: SavingsAccount Class (Child)

Create a class `SavingsAccount` that inherits from `BankAccount`.

### 🔸 Additional Attributes:
- `interest_rate` (default 0.05 or 5%)

### 🔸 New Methods:
1. `add_interest()` – adds interest to balance based on `interest_rate`
2. `account_summary()` – prints:
   - Account Holder name
   - Balance
   - Interest Rate

---

## 📌 Instructions

1. Create an object of `SavingsAccount`
2. Perform:
   - Deposit of some money
   - Withdraw some money
   - Add interest
   - Show account summary
3. Use proper conditionals inside each function to handle errors or logic.

---

## ✅ Sample Output (for reference)

```
Current balance for Riya: ₹1000
₹500 deposited. New balance: ₹1500
₹200 withdrawn. Remaining balance: ₹1300
Interest ₹65.00 added. New balance: ₹1365.00
Account Holder: Riya
Balance: ₹1365.00
Interest Rate: 5.0%
```


---

## 🧩 Part 3: Transaction History 📜

Enhance your `BankAccount` class to **track the history of all transactions**.

### 🔸 What to do:
- Add a list called `transactions` in the constructor.
- Every time `deposit()` or `withdraw()` is called, **append a message** to this list like:
  - `"Deposited ₹500"`
  - `"Withdrew ₹200"`
- Add a method `show_transactions()` that prints each transaction on a new line.

### 🧪 Example:

```
Transaction History:
Deposited ₹500
Withdrew ₹200
Interest ₹50.0 added
```

---

## 🧩 Part 4: Minimum Balance Rule 🚫

Update your `SavingsAccount` to **enforce a minimum balance rule**.

### 🔸 What to do:
- Set a `minimum_balance` attribute (e.g., ₹100).
- In `withdraw()`, check if the balance **after withdrawal** will go **below the minimum**.
- If yes, print a warning: `"Cannot withdraw. Balance would fall below minimum required ₹100."`

---

## 🧩 Part 5: Create Multiple Accounts & Summary 📊

Let the user create **multiple savings accounts** and get a report.

### 🔸 What to do:
- Create a list of 3 `SavingsAccount` objects.
- For each account, perform a few deposits, withdrawals, and interest additions.
- Add a function outside the class to:
  - Print a summary of all accounts:
    - Account Holder
    - Final Balance
    - Number of transactions

### 📌 Sample Output

```
Account Summary:
Riya - ₹1365.0 - 4 transactions
Aman - ₹980.0 - 3 transactions
Sneha - ₹1200.0 - 5 transactions
```


