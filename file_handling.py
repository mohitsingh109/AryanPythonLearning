# Read a file in python
# r ==> Reading a file (Read Mode)

with open("hello.txt", "r") as file:
    content = file.read()
    print(content)


# Write a data to file
# w ==> Writing Mode
with open("hello1.txt", "w") as file:
    file.write("Hi, This is a write example 😀\nWelcome to python file handling")

# It will replace (w ==> overwrite)
with open("hello1.txt", "w") as file:
    file.write("Will is replace all the previous files 🧐?\n")

# Append mode
with open("hello1.txt", "a") as file:
    file.write("Yhaaa... I am going to append 😎...\n")


# Fun Activity
# Hi Mohit 🥳
# Hi Aditya 🥳

def write_to_file(students):
    with open("student.txt", "w") as student_file:
        for student in students:
            result_str = f"Hi {student} 🥳\n"
            student_file.write(result_str)


def add_new_student(new_students):
    # First you need to get the student list from the file
    existing_student = get_all_students()
    with open("student.txt", "a") as update_student_file:
        for student in new_students:
            if student not in existing_student:
                result_str = f"Hi {student} 🥳\n"
                update_student_file.write(result_str)

def get_all_students():
    stu = []
    with open("student.txt", "r") as student_file:
        for line in student_file: # [Hi, Mohit, 🥳]
            words = line.split() # Hi Jack 🥳 ==> [Hi,Jack,🥳]
            stu.append(words[1])
    return stu

def delete_student(student):
    existing_student = get_all_students()
    if student in existing_student:
        existing_student.remove(student)
        write_to_file(existing_student)


#write_to_file(["Mohit", "Aditya", "Arun", "Aryan", "Karan"])
#add_new_student(["Alex", "Cody", "Jack", "Hack"])
#delete_student("Alex")
#get_all_students()