
# 📦 Student Performance Management System

---

## 📁 Project Structure

```
student_system/
│
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── student.py
│   └── report.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── main.py
```

---

## ✅ Task 1: Create a `Student` Class (models/student.py)

- Properties:
  - name
  - roll_no
  - marks (list of 5 subjects)
- Add methods:
  - `get_average()`
  - `display_info()`

---

## ✅ Task 2: Create a `Report` Class (models/report.py)

- Takes a list of student objects
- Methods to:
  - Display all student data
  - Display top 5 students by average
  - Search by roll number
  - Delete by roll number

---

## ✅ Task 3: Create a Utility Module (utils/helpers.py)

- Function to:
  - Validate marks (0–100)
  - Generate dummy student data (5–10 students)
  - Sort student list

---

## ✅ Task 4: Create `main.py`

- Menu options:
  - 1. Add Student
  - 2. Show All Students
  - 3. Search Student by Roll No
  - 4. Delete Student by Roll No
  - 5. Show Top 5 Students
  - 6. Exit

---

## ✅ Task 5: Use Packages and Imports Properly

- Use:
```python
from models.student import Student
from models.report import Report
from utils.helpers import validate_marks
```

---

## ✅ Task 6: Add Class Variable

- In `Student`, keep a class variable to track total students created.

---

## ✅ Task 7: Use Encapsulation

- Make `marks` a private variable.
- Use getter/setter to modify it safely.

---

## ✅ Task 8: Save Data to File (Optional Challenge)

- After exiting, write all student data to a `.txt` file.

---

## ✅ Task 9: Load Data from File (Bonus)

- When the program starts, try to load student data from the saved file.

---

## ✅ Task 10: Abstract Class (Super Bonus)

- Create an abstract class `Person` with `display_info()` as an abstract method.
- Let `Student` inherit from it.

---

## 💡 Tips

- Use loops and conditions inside class methods
- Add exception handling when searching or deleting
- Keep each module focused (Single Responsibility Principle)



# 🎮 Score Tracker System

Build a **modular game scoring system** using Python OOP, Modules, and Packages.

---

## 🎯 Task Overview:

You will simulate a basic game system that:

- Tracks players and their scores
- Records top 10 high scorers
- Allows adding/removing players
- Uses multiple Python files organized into modules and packages

---

## 🧱 Project Structure

```
game_score/
│
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── player.py
│   └── scoreboard.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
└── main.py
```

---

## ✅ Task 1: Create a `Player` class (models/player.py)

- Attributes: `username`, `score`
- Use `__str__()` to display player info
- Add method to update score

---

## ✅ Task 2: Create `ScoreBoard` class (models/scoreboard.py)

- Keep a list of players
- Add methods to:
  - Add new player
  - Remove player
  - Update score
  - Show top 10 players
  - Search player by username

---

## ✅ Task 3: Helpers Module (utils/helpers.py)

- Function to sort players by score
- Function to validate that score is integer and ≥ 0

---

## ✅ Task 4: Main Menu (main.py)

Create a CLI menu:

```
1. Add Player
2. Remove Player
3. Update Score
4. Show All Players
5. Show Top 10 Players
6. Search Player
7. Exit
```

---

## ✅ Task 5: Use Encapsulation and Class Variables

- Make `score` private in `Player`
- Track total number of players with a class variable

---

## ✅ Task 6: Use Abstraction

- Create an abstract base class `GameMember`
  - Method: `display_profile()`
  - Inherit `Player` from `GameMember`

---

## 🧠 BONUS:

- Auto-save all player scores to a `.txt` file when exiting.
- Load from that file on start.

---

## 💡 Tip for Students

> Try adding simple features like "levels", "badges", or "player ranks" later as practice!

---

## ✅ Task 11: Add Game Levels and Categories

- Add a new attribute `level` to the `Player` class
- Add method to promote level based on score:
  - `score > 1000` → Level 2
  - `score > 2000` → Level 3
- Add player category: "Beginner", "Intermediate", "Pro" based on level

---

## ✅ Task 12: Prevent Duplicate Usernames

- Ensure no duplicate usernames are allowed when adding a new player

---

## ✅ Task 13: Implement Leaderboard Persistence

- Save top 10 players to `leaderboard.txt` every time a score is updated
- Load leaderboard from the file when the app starts

---

## ✅ Task 14: Add Admin Password for Sensitive Actions

- Protect "Remove Player" and "Reset Score" operations with a simple password (e.g., "admin123")

---

## ✅ Task 15: Add Team Functionality

- Let players belong to teams (e.g., Red, Blue)
- Add a class `Team`:
  - Keep a list of players
  - Calculate total team score
  - Show team leaderboard (based on total team scores)

---

## ✅ Task 16: Export Player Statistics

- Allow exporting all player data to a `.csv` file using Python's `csv` module

---

## ✅ Task 17: Add Search Filters

- Allow player search by:
  - Username
  - Level
  - Team
  - Score greater than a value

---

## ✅ Task 18: Create a Simple Game Simulation

- Simulate a random game round:
  - Pick 2 random players
  - Randomly increase their scores
  - Update their levels and rankings

---

## ✅ Task 19: Add Logging

- Log every major action to a file:
  - Adding, removing, updating players
  - Saving leaderboard
  - Exporting stats

---

## ✅ Task 20: Add Sorting Options

- Allow sorting players by:
  - Score
  - Level
  - Username
  - Team name

Use a menu system to choose sort type.

---
