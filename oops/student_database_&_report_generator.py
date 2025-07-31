students = [("Mohit", 101, "8A"), ("Aryan", 113, "8C"), ("Steve", 123, "8G")]

marks = {
    101: [87, 95, 90],
    113: [102, 101, 103],
    123: [82, 90, 85]
}

def calculate_average_total(scores):
    total = sum(scores)
    average = total / len(scores)
    return average, total

for student in students:
    name = student[0]
    roll_number = student[1]
    class_number = student[2]
    student_scores = marks[roll_number]
    print(f"Student {roll_number}, {name}, scored {student_scores} in his English, History, and Math tests respectively.")

for student in students:
    roll_number = student[1]
    student_scores = marks[roll_number]
    average, total = calculate_average_total(student_scores)
    print(f"{student[0]} scored {total} in total. They scored {average:.2f} on average.")

def search():
    roll_num = int(input("What is the roll number of the person you are looking for? "))
    for student in students:
        if student[1] == roll_num:
            print(student[0])
            print(student[2])
            student_marks = marks[roll_num]
            print(student_marks)
            average, _ = calculate_average_total(student_marks)
            print(f"{average:.2f}")

def topper_finder():
    avg_scores = []
    for student in students:
        average, _ = calculate_average_total(marks[student[1]])
        avg_scores.append(average)
    ti = 0
    tv = avg_scores[0]
    for i in range(1, len(avg_scores)):
        if avg_scores[i] > tv:
            tv = avg_scores[i]
            ti = i
    name_of_student = students[ti][0]
    print(f"{name_of_student} scored the highest average grade at {tv:.0f} percent.")

def class_search():
    search_holder = {}
    class_name = input("What class are you searching for?")
    for student in students:
        if student[2] == class_name:
            search_holder[student[0]] = marks[student[1]]
    print(search_holder)

def dict_creation():
    dict_of_students = {}
    for student in students:
        dict_of_students[student[0]] = sum(marks[student[1]])
    print(dict_of_students)

def sort_by_scores(dict_of_students):
    list_of_lower_students = []
    student_name = "name"
    student_marks = 90
    for key, value in dict_of_students.items():
        if value > student_marks:
            student_name = key
            student_marks = value
        else:
            list_of_lower_students.append([key, value])

def save_to_file():
    for student in students:
        print(student)
        