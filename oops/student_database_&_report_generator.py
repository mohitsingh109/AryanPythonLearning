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
# search()

def topper_finder():
    avg_scores = []
    for student in students:
        average, _ = calculate_average_total(marks[student[1]])
        avg_scores.append(average)
    # for i in range(len(avg_scores)):
    #     if avg_scores[i] > avg_scores[i + 1]:
    #         print("libidy")
topper_finder()


number_list = [97, 79, 88, 87, 100, 10, 99]

b = number_list[0]
index = 0
for i in range(1, len(number_list)):
    if number_list[i] > b:
        b = number_list[i]
        index = i

print(b, index)