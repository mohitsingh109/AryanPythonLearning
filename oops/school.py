# Super is used to call or interact with the parent class

class Person:
    def __init__(self, name, email, phone_number, address, country="unknown"):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.country = country

    def print_details(self):
        print(f"My name is {self.name}. Email id: [{self.email}], Phone Number: [{self.phone_number}]")


class Student(Person):
    def __init__(self, name, email, phone_number, address, grade, student_id, class_number):
        # how to call the __init__ of Person class
        super().__init__(name, email, phone_number, address) # I am calling parent constructor
        self.grade = grade
        self.student_id = student_id
        self.class_number = class_number

    # Overwrite a function
    def print_details(self):
        super().print_details()
        print(f"Hi My name is {self.name}. I am studying in {self.class_number} with grades: {self.grade}")


class Teacher(Person):
    def __init__(self, name, email, phone_number, address, teacher_id, salary, subjects):
        super().__init__(name, email, phone_number, address)  # I am calling parent constructor
        self.teacher_id = teacher_id
        self.salary = salary
        self.subjects = subjects

    def print_details(self, bonus):
        print(f"Inside the teacher {bonus}. I've teacher id: [{self.teacher_id}]")



# Student(name, email, phone_number, address, grade, sid, class_number)

s1 = Student("Aryan", "aryan@gmail.com", "1234567890", "USA", 100, "STU_1", "8th")

print(s1.name, s1.email, s1.address, s1.phone_number, s1.grade, s1.student_id, s1.class_number, s1.country)

s1.print_details()

t1 = Teacher("Mohit", "mohit@gmail.com", "1234567890", "INDIA", 10, 1000, ["Java", "C++"])

# t1.print_details() because in child we've the function with the same name
t1.print_details(10.67)
