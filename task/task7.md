
# 🧠 Python OOP Assignment: Smart School Management System

This assignment will test your understanding of **Class Variables**, **Encapsulation**, and **Abstraction** using a real-world scenario.

Imagine you are building a system for a smart school to manage students, teachers, and their data securely.

---

## 📌 Part 1: Create an Abstract Class `Person`

- It should contain the abstract method `display_info()`.
- Add a class variable `school_name = "Greenwood High"`

---

## 📌 Part 2: Create `Student` and `Teacher` Classes (Inherit from `Person`)

- `Student` should store name, roll number, grade, and marks.
- `Teacher` should store name, employee ID, subject.

Use **encapsulation** (private variables) to protect personal data.

---

## 📌 Part 3: Add Getter and Setter Methods

- Add `get_` and `set_` methods for private attributes.
- Do not allow negative marks.

---

## 📌 Part 4: Count Total Students and Teachers

- Use class variables to count how many `Student` and `Teacher` objects are created.

---

## 📌 Part 5: Implement `display_info()` in Both Classes

- Print all public data and use getter for private ones.

---

## 📌 Part 6: Maintain a List of All Students and Teachers

- Create a list `all_students` and `all_teachers` to store objects.

---

## 📌 Part 7: Add a Method to Search Student by Roll Number

- Take input from user and return full student info.

---

## 📌 Part 8: Add a Method to Search Teacher by Subject

- Return list of teachers teaching the given subject.

---

## 📌 Part 9: Ensure Roll Numbers Are Unique

- While creating a new student, check if roll number already exists.

---

## 📌 Part 10: Add a Class Method to Change School Name

- This should update `school_name` for all objects.

---

## 📌 Part 11: Add Method to Calculate Average Marks

- Store and return average marks of a student using their marks list.

---

## 📌 Part 12: Add Teacher Assignment Feature

- Each student can have one assigned teacher.
- Store teacher ID inside student object.

---

## 📌 Part 13: Show Students with Average Marks Above 80

- Loop through all students and print those who scored well.

---

## 📌 Part 14: Save All Student and Teacher Info to File

- Write all data (name, roll/id, subject/marks, average) to a `.txt` file.

---

## 📌 Part 15: Create a Menu-Driven Interface

- Allow user to:
  - Add student/teacher
  - Search student/teacher
  - Update school name
  - Show high performers
  - Save to file

---

💡 **BONUS**: Add a password system for teachers to secure their profiles.
