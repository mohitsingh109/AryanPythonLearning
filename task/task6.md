
# 📚 Python Assignment: Student Database & Report Generator

Welcome to your 10-part Python challenge! This assignment helps you learn how to use **lists**, **tuples**, and **dictionaries (maps)** in real-world-like situations.

---

## 🧩 Part 1: Create Student Records
Create a list of **tuples**, where each tuple contains the following:
- (Student Name, Roll Number, Class)

Example:
```python
students = [("Amit", 101, "8A"), ("Riya", 102, "8B"), ("Ayaan", 103, "8A")]
```

---

## 🧩 Part 2: Add Marks to Students
Now, create a **dictionary** that maps each student’s roll number to their marks in 3 subjects:
```python
marks = {
    101: [78, 85, 90],
    102: [88, 79, 95],
    103: [92, 90, 85]
}
```

---

## 🧩 Part 3: Print Report Cards
Write a loop that prints each student’s name and their marks.

📝 Hint: Use the `students` list to get name & roll number, and then find marks from the `marks` dictionary.

---

## 🧩 Part 4: Calculate Total and Average Marks
For each student, calculate their total and average marks and print them neatly.

---

## 🧩 Part 5: Search by Roll Number
Take a roll number as input from user and print:
- Student name
- Class
- Marks
- Average

✅ Use a loop + conditional to find the student.

---

## 🧩 Part 6: Topper Finder
Find the student who scored the **highest average marks** and print their name and average.

---

## 🧩 Part 7: Students by Class
Write a function to show all students of a particular class (e.g., "8A") along with their marks.

---

## 🧩 Part 8: Convert to Dictionary by Name
Make a new dictionary where student names are keys and their total marks are values.

```python
name_total_marks = {
    "Amit": 253,
    "Riya": 262,
    ...
}
```

---

## 🧩 Part 9: Sort by Total Marks
Sort and display students in descending order based on total marks.

📝 Use `sorted()` and a lambda function.

---
` ++

## 🧩 Part 10: Save Report to File
Write the full student report (name, roll, class, total, average) to a `.txt` file line by line.

---

