# Arithmetic Operator (Math cal)
# +, -, *, /, //(Floor Division), % (Modules), ** (Power)

a = 10
b = 3
# + (Add)
print(a + b) # 13

# - (Sub)
print(a - b) # 7

# * (Mul)
print(a * b) # 30

# / (Divide)
print(a / b) # 3.3333333333

# // (Floor Divide)
print(a // b) # 3

# % (Mod)
print(a % b) # 1 (Reminder)

# ** (pow) (Exponentation)
print(a ** b) # a^b ==> 10^3 ==> 10 * 10 * 10 ==> 1000

# Relational Operator (Compare value)
# ==, !=, >, <, >=, <=
x = 50
y = 20

# == (equal value)
print(x == y) # False
print(x == 50) # True

str1 = "123"
str2 = "Aryan"
print(len(str1) == len(str2))
print(int(str1) == 123)
print(True == True)
print(False == False)

# != (Not equal to)
print(10.5 != 20.5) # True
print("Aryan" != "Aryan") # False
print(True != True) # False
print(True != False) # True

# > (Always used with number values)

age = 10
print(age > 5) # True
print(age > 10) # False
print(age > 50) # False
print(10.5 > 5.5) # True

# < (Always used with number values)
age = 20
print(age < 30) # True
print(age < 20) # False
print(age < 5) # False

# >= (Always used with number values)
age = 10
print(age >= 10) # True

# <= (Always used with number values)
age = 20
print(age <= 20) # True