# PCEP Practice MCQs (Set 1)

---

## 1. Computer Programming and Python Fundamentals (18%)

**Q1.** Which of the following best describes an interpreter?

* A) Translates the entire program into machine code before execution
* B) Executes code line by line
* C) Optimizes code into bytecode
* D) Converts Python code into C++ code

**Q2.** Which of the following is **not** a Python keyword?

* A) elif
* B) lambda
* C) include
* D) pass

**Q3.** What will be the output of the following code?

```python
print("5" + "3")
```

* A) 8
* B) 53
* C) Error
* D) 5 3

**Q4.** Which numeral system does the prefix `0b` represent in Python?

* A) Octal
* B) Binary
* C) Hexadecimal
* D) Decimal

**Q5.** What is the correct way to take user input and convert it into an integer?

* A) `num = int(input())`
* B) `num = input(int())`
* C) `num = input(); int(num)`
* D) `num = int(get())`

---

## 2. Control Flow -- Conditional Blocks and Loops (29%)

**Q6.** What is the output of the following code?

```python
x = 5
if x > 10:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
```

* A) A
* B) B
* C) C
* D) Nothing

**Q7.** Which of the following loops will run exactly 5 times?

* A) `for i in range(1,6):`
* B) `for i in range(5):`
* C) Both A and B
* D) None of the above

**Q8.** What does the `continue` statement do?

* A) Ends the loop immediately
* B) Skips the current iteration
* C) Stops the loop and moves to else
* D) Restarts the loop from the beginning

**Q9.** What is the output of the following code?

```python
for i in range(3):
    print(i)
else:
    print("Done")
```

* A) 0 1 2
* B) 0 1 2 Done
* C) Done
* D) Error

**Q10.** Which keyword is used to create an empty block in Python?

* A) skip
* B) empty
* C) pass
* D) none

**Q11.** Which of the following is the correct syntax for a nested if statement?

* A)

```python
if x > 0
    if x < 10:
        print("Valid")
```

* B)

```python
if x > 0:
    if x < 10:
        print("Valid")
```

* C)

```python
if (x > 0)
    if (x < 10)
        print("Valid")
```

* D) None of the above

**Q12.** What is the result of `range(2,10,2)`?

* A) \[2, 4, 6, 8, 10]
* B) \[2, 4, 6, 8]
* C) \[2, 3, 4, 5, 6, 7, 8, 9]
* D) \[2, 6, 10]

**Q13.** In a `while` loop, what happens if the condition is always True and no break is used?

* A) Loop executes once
* B) Loop never runs
* C) Infinite loop
* D) Error

---

## 3. Data Collections -- Tuples, Dictionaries, Lists, and Strings (25%)

**Q14.** Which of the following data structures is immutable?

* A) List
* B) Tuple
* C) Dictionary
* D) String and Tuple

**Q15.** What is the output of the following?

```python
my_list = [1,2,3]
print(my_list[1:])
```

* A) \[1]
* B) \[2, 3]
* C) \[1, 2]
* D) Error

**Q16.** Which of the following methods adds an element to a list?

* A) insert()
* B) append()
* C) extend()
* D) All of the above

**Q17.** What will be the result of the following?

```python
x = (1,2,3)
y = (1,2,3)
print(x == y)
```

* A) True
* B) False
* C) Error
* D) None

**Q18.** What will be printed?

```python
s = "Python"
print(s[1:4])
```

* A) Pyt
* B) yth
* C) ytho
* D) thon

**Q19.** Which of the following correctly creates a dictionary?

* A) `d = {}`
* B) `d = {"a":1, "b":2}`
* C) `d = dict(a=1, b=2)`
* D) All of the above

**Q20.** Which statement about strings in Python is true?

* A) Strings are mutable
* B) Strings can be modified using indexing
* C) Strings are immutable
* D) Strings cannot be sliced

**Q21.** What is the output of the following?

```python
text = "Hello\nWorld"
print(text)
```

* A) Hello World
* B) Hello\nWorld
* C) Hello
  World
* D) Error

**Q22.** What does the `items()` method of a dictionary return?

* A) Keys only
* B) Values only
* C) List of tuples (key, value)
* D) None of the above

---

## 4. Functions and Exceptions (28%)

**Q23.** What is the default return value of a function without a `return` statement?

* A) 0
* B) False
* C) None
* D) Empty string

**Q24.** Which of the following is the correct way to define a function with a default argument?

* A) `def func(x=10):`
* B) `def func(default x=10):`
* C) `func def(x:10)`
* D) `def func(x:default=10):`

**Q25.** Which keyword is used to access a variable defined outside a function inside it?

* A) static
* B) nonlocal
* C) global
* D) external

**Q26.** What will be the result?

```python
def test():
    return
print(test())
```

* A) 0
* B) None
* C) Empty string
* D) Error

**Q27.** Which of the following is **not** part of Python’s exception hierarchy?

* A) BaseException
* B) SystemExit
* C) NullPointerException
* D) ArithmeticError

**Q28.** Which of the following exception types is raised when you try to divide by zero?

* A) ValueError
* B) ArithmeticError
* C) ZeroDivisionError
* D) OverflowError

**Q29.** Which of the following is the correct structure of exception handling in Python?

* A)

```python
try:
    # code
catch Exception:
    # handle
```

* B)

```python
try:
    # code
except Exception:
    # handle
```

* C)

```python
catch:
    # code
except:
    # handle
```

* D) None of the above

**Q30.** What happens when an exception is raised but not handled in Python?

* A) Program ignores it and continues
* B) Program stops execution and prints traceback
* C) Program retries the code
* D) Program automatically resolves the error

---

**End of MCQ Set**
