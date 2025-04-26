# Read a file in python

# r ==> Reading a file (Read Mode)
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)


# Write a data to file
# w ==> Writing Mode
with open("hello1.txt", "w") as file:
    file.write("Hi, This is a write example 😀")