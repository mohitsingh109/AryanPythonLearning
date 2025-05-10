
"""
Parent
  |
  |
Child
"""

class Parent:
    def say_hello(self):
        print("Hello from Parent")


class Child(Parent): # I am inherent all my parent property
    def say_hello_2(self):
        print("Hello from Child")


# What is this line?
parent = Parent()
parent.say_hello()

# What is this line?
child = Child()
child.say_hello()
child.say_hello_2()