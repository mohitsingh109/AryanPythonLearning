# PCEP Practice MCQs (Set 2)

---

## 1. Computer Programming and Python Fundamentals (18%)

**Q31.** Which of the following is a valid Python identifier?

* A) 123name
* B) name\_123
* C) name-123
* D) @name

**Q32.** What is the purpose of indentation in Python?

* A) Improves readability only
* B) Defines blocks of code
* C) Has no effect
* D) Used for comments

**Q33.** Which of the following represents a hexadecimal literal in Python?

* A) `0x1F`
* B) `0o17`
* C) `0b1010`
* D) `17H`

**Q34.** Which operator is used for integer division in Python?

* A) /
* B) //
* C) %
* D) \*\*

**Q35.** What is the output of the following?

```python
print(bool(""))
```

* A) True
* B) False
* C) None
* D) Error

---

## 2. Control Flow -- Conditional Blocks and Loops (29%)

**Q36.** Which statement is equivalent to `if not (x > 10)`?

* A) if x < 10
* B) if x <= 10
* C) if x != 10
* D) if x >= 10

**Q37.** Which of the following correctly describes a `for` loop in Python?

* A) Iterates until a condition is False
* B) Iterates over items of a sequence
* C) Works only with integers
* D) Always executes at least once

**Q38.** Which keyword exits from the innermost loop immediately?

* A) exit
* B) break
* C) stop
* D) end

**Q39.** What will the following code print?

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Finished")
```

* A) 0 1 2
* B) 0 1 2 Finished
* C) Finished
* D) Infinite loop

**Q40.** What is the result of the following code?

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

* A) (0,0) (1,1)
* B) (0,0) (0,1) (1,0) (1,1)
* C) (0,1) (1,0)
* D) (0,0) (1,0)

**Q41.** Which statement about `range(5, 1, -1)` is true?

* A) Produces \[5,4,3,2]
* B) Produces \[5,4,3,2,1]
* C) Produces \[5,1]
* D) Produces an empty list

**Q42.** Which of the following is valid syntax for a one-line if statement?

* A) `if x > 0 print("Positive")`
* B) `print("Positive") if x > 0 else print("Negative")`
* C) `if (x > 0): print("Positive")`
* D) Both B and C

**Q43.** Which statement about nested loops is correct?

* A) Only `for` loops can be nested
* B) Only `while` loops can be nested
* C) Both for and while loops can be nested
* D) Nesting is not allowed

---

## 3. Data Collections -- Tuples, Dictionaries, Lists, and Strings (25%)

**Q44.** Which of the following removes the last element from a list?

* A) pop()
* B) remove()
* C) del list\[-1]
* D) Both A and C

**Q45.** Which of the following creates a tuple with a single element?

* A) `(5)`
* B) `(5,)`
* C) `tuple(5)`
* D) `(5.0)`

**Q46.** What will be the result?

```python
letters = ['a','b','c']
letters[1] = 'z'
print(letters)
```

* A) \['a','b','c']
* B) \['a','z','c']
* C) \['z','b','c']
* D) Error

**Q47.** Which of the following string methods returns the number of occurrences of a substring?

* A) index()
* B) find()
* C) count()
* D) contains()

**Q48.** What is the result?

```python
d = {"a":1, "b":2}
print("c" in d)
```

* A) True
* B) False
* C) Error
* D) None

**Q49.** Which of the following list comprehensions produces `[1,4,9]`?

* A) `[x^2 for x in [1,2,3]]`
* B) `[x**2 for x in [1,2,3]]`
* C) `[square(x) for x in [1,2,3]]`
* D) None of the above

**Q50.** Which operation is invalid on a tuple?

* A) Concatenation
* B) Repetition
* C) Indexing
* D) Item assignment

**Q51.** What is the result of:

```python
"hello".upper()
```

* A) hello
* B) HELLO
* C) Error
* D) None

**Q52.** Which of the following correctly retrieves all values from a dictionary?

* A) d.items()
* B) d.values()
* C) d.keys()
* D) list(d)

**Q53.** What is the result?

```python
s = "Python"
print(s[-1])
```

* A) P
* B) y
* C) n
* D) Error

---

## 4. Functions and Exceptions (28%)

**Q54.** Which of the following defines a recursive function correctly?

* A)

```python
def fact(n):
    return n * fact(n-1)
```

* B)

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
```

* C)

```python
def fact(n):
    while n > 0:
        return n * fact(n-1)
```

* D) None

**Q55.** What is the scope of a variable defined inside a function?

* A) Global
* B) Local
* C) Static
* D) Dynamic

**Q56.** Which of the following statements about `None` is true?

* A) `None` is equivalent to 0
* B) `None` is a keyword representing no value
* C) `None` is the same as False
* D) `None` can be used in arithmetic operations

**Q57.** What will be printed?

```python
def func(a, b=5):
    print(a+b)
func(3)
```

* A) 3
* B) 5
* C) 8
* D) Error

**Q58.** Which of the following exceptions is raised when accessing a list index out of range?

* A) ValueError
* B) IndexError
* C) LookupError
* D) KeyError

**Q59.** Which statement is true about exception handling?

* A) Only one except block is allowed
* B) Multiple except blocks can handle different exceptions
* C) An except block cannot be used without a try block
* D) Both B and C

**Q60.** What will be the result of the following?

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error")
```

* A) Error
* B) Error message printed
* C) Program stops
* D) None

**Q61.** Which exception type is the base of all built-in exceptions in Python?

* A) Exception
* B) BaseException
* C) RuntimeError
* D) Error

**Q62.** Which keyword can be used to re-raise an exception inside an except block?

* A) throw
* B) raise
* C) rethrow
* D) continue

**Q63.** What happens if an exception is caught and no code is provided in the except block?

* A) Exception is ignored
* B) Exception is re-raised
* C) Program crashes
* D) None of the above

---
