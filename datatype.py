# Python dynamic datatype

# Data type
num = 10
print(type(num))
num = "Arun"
print(type(num))
num = 45.78
print(type(num))
num = True
print(type(num))

# Type Conversion
# String to float
price = "49.99"
price = float(price)
print(price, type(price))

# String to int
price = "55.67"
price = int(float(price))
print(price)

# int to str
age = 100
age = str(age)
print(age, type(age))

# string to int
# ValueError
wrong = "I am not int"
wrong = len(wrong)
print(wrong, type(wrong))
