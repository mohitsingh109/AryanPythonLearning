# Oops (Object-Oriented Programming)
# It's a way of writing code where we think of real
# life things as object - like car, animal, students

# Opps helps us?
# Organize code
# Reuse it easily
# Make it easy to understand

# Opps Concept:
# 1) Class & Object
# 2) Inheritance
# 3) Polymorphism
# 4) Abstraction

# Let's talk about student

# Class: We call it as a blueprint (we define what all things student should have & it's operation)
# name, age, school name, email, ....

class Student:
    # Initialize the instance variable
    # Constructor: it's job is to initialize the instance variable
    # self: refer to current object
    def __init__(self, name, age, school_name, email): # Constructor in python
        self.name = name  # self.name is the instance variable (Object variable)
        self.age = age
        self.school_name = school_name
        self.email = email
        self.points = 100

    def greet(self):
        print(f"Hello, I am {self.name}, I am {self.age} years old.")


# Object: Existence of class is an object
# Instance == Object
s1 = Student("Aryan", 15, "ABC", "allaryan@xyz.com")
s2 = Student("Mohit", 25, "XYZ", "mohit@xyz.com")
s3 = Student("Karan", 45, "JP", "k@xyz.com")
s4 = Student("Aman", 22, "AP", "a@xyz.com")

# Array of object
# Array of student object
students = [s1, s2, s3, s4]

# s1.name == self.name
print(s1.name, s1.school_name, s1.email, s1.age, s1.points)
print(s2.name, s2.school_name, s2.email, s2.age, s2.points)

s1.points = s1.points - 10

print(s1.name, s1.school_name, s1.email, s1.age, s1.points) # 90
print(s2.name, s2.school_name, s2.email, s2.age, s2.points) # 100


print("===============================")

for student in students:
    student.greet()

print("===============================")

# Class is like a recipe
# Object when the recipe is actually created
# instance variable belong to an object

# Opps Concept:
# 1) Class & Object
# 2) Inheritance
# 3) Polymorphism
# 4) Abstraction