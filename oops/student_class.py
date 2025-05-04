class Student:
    # Constructor: initialize the instance variable
    # Self refer to Current object (single object)
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Operation on instance variable + function of student class
    def print_details(self):
        print(f"Hi I am {self.name} and I've scored {self.marks} marks")

    def has_passed(self):
        return self.marks >= 40


#Task-1: we need to create list of 3 students (Aryan 85, Mohit 33, Arjun 58)
#Task-2: Any having marks >= 40 passed (True) the exam else failed (False)
#Task-3 I want to call has_passed on all the object and print (Aryan - Passed) or (Mohit - Failed) with name

# Hi I am Aryan and I've scored 85 marks
students = [
    Student("Aryan", 85), # Always and always we are calling the constructor (__init__)
    Student("Mohit", 33),
    Student("Arjun", 58)
]

# Calling a function
students[0].print_details()
students[1].print_details()

# Accessing the property of the object
# I want to access the name property from here how I can do that?
print(students[2].name, students[2].marks)

for stu in students:
    # Ternary Operator
    result = "Passed" if stu.has_passed() else "Failed"
    print(f"{stu.name} - {result}")

