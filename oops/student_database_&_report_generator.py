students = [("Mohit", 101, "8A"), ("Aryan", 113, "8C"), ("Steve", 123, "8G")]

marks = {
    101: [87, 95, 90],
    113: [102, 101, 103],
    123: [82, 90, 85]
}

for student in students:
    name = student[0]
    roll_number = student[1]
    class_number = student[2]
    student_scores = marks[roll_number]
    print(f"Student {roll_number}, {name}, scored {student_scores} in his English, History, and Math tests respectively.")

for student in students:
    roll_number = student[1]
    student_scores = marks[roll_number]
    total = sum(student_scores)
    average = total/len(student_scores)
    print(f"{student[0]} scored {total} in total. They scored {average:.2f} on average.")