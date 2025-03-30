
## Q1: To-Do List Manager
Create a function todo_list(action: str, task: str = None) -> list that manages a to-do list.

"add" adds a task.

"remove" removes a task.

"view" returns the current list of tasks.

Use a global variable to store tasks.

### Example:

todo_list("add", "Buy groceries")

todo_list("add", "Read a book")

todo_list("view")

Output: ["Buy groceries", "Read a book"]

todo_list("remove", "Buy groceries")

todo_list("view")

Output: ["Read a book"]

---

## Q2: Contact Book
Create a function contact_book(action: str, name: str = None, number: str = None) -> dict to store contact names and phone numbers.

"add" stores a new contact.

"delete" removes a contact.

"lookup" returns a contact’s number.

"list" returns all contacts.

### Example:

contact_book("add", "Alice", "1234567890")

contact_book("add", "Bob", "9876543210")

contact_book("lookup", "Alice")

Output: "1234567890"

contact_book("list")

Output: {"Alice": "1234567890", "Bob": "9876543210"}
---

## Q3: Random Story Generator
Write a function generate_story(name: str, place: str, activity: str) -> str that takes inputs and returns a randomly generated short story.

### Example:

generate_story("John", "park", "cycling")

Output: "One day, John went to the park and enjoyed cycling under the blue sky."

---

## Q4: Sentence Word Counter
Write a function count_words(sentence: str) -> int that takes a sentence and returns the number of words in it.

### Example:

count_words(" is fun to learn!")

Output: 5

---

## Q5: ATM PIN Validator
Write a function validate_pin(pin: str) -> bool that checks if a PIN is exactly 4 digits.

### Example:

validate_pin("1234")

Output: True

validate_pin("12a4")

Output: False

---

### Q6: E-Commerce Discount Calculator
Write a function calculate_discount(price: float, discount: float) -> float that calculates the final price after applying a discount.

### Example:

calculate_discount(1000, 10)

Output: 900.0

--- 

## Q7: Text-Based Dice Game
Create a function roll_dice_game(guess: int) -> str where the user guesses a dice roll (1-6), and the function rolls a dice using random.randint().

If the guess is correct, return "You win!".

Otherwise, return "Try again.".

### Example:

roll_dice_game(3)

Output: "You win!" (if the random dice lands on 3)

---

## Q8: Word Scramble Game
Write a function scramble_word(word: str) -> str that shuffles the letters of a word randomly using random.shuffle().

### Example:

scramble_word("")

Output: "yhpnot"

---

## Q9: Simple Chatbot
Create a function chatbot(question: str) -> str that gives predefined answers.

If the question is "How are you?", return "I'm good!".

If the question is "What is your name?", return "I'm ChatBot.".

Otherwise, return "I don't understand.".

### Example:

chatbot("How are you?")

Output: "I'm good!"

chatbot("Tell me a joke")

Output: "I don't understand."

---

## Q10: File Line Counter
Write a function count_lines(filename: str) -> int that counts the number of lines in a given file.

Example:

count_lines("sample.txt")

Output: 42  

---