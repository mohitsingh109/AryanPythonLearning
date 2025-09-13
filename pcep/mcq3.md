# PCEP Practice MCQs (Set 3)

---

## 1. Computer Programming and Python Fundamentals (18%)

**Q64.** Which of the following is a valid comment in Python?

* A) `// comment`
* B) `# comment`
* C) `/* comment */`
* D) `<!-- comment -->`

**Q65.** Which operator is used for exponentiation in Python?

* A) ^
* B) \*\*
* C) exp()
* D) \*

**Q66.** What will be printed?

```python
x = 10
y = 3
print(x % y)
```

* A) 3
* B) 1
* C) 0
* D) 10

**Q67.** Which function converts a string into an integer?

* A) str()
* B) int()
* C) float()
* D) bool()

**Q68.** Which of the following literals is a float?

* A) 10
* B) 10.0
* C) "10"
* D) '10'

---

## 2. Control Flow -- Conditional Blocks and Loops (29%)

**Q69.** What will the following print?

```python
x = 5
y = 7
if x and y:
    print("Yes")
else:
    print("No")
```

* A) Yes
* B) No
* C) Error
* D) None

**Q70.** Which of the following is the correct syntax for an `if/else` block?

* A) `if x > 5 print("Hi") else print("Bye")`
* B)

```python
if x > 5:
    print("Hi")
else:
    print("Bye")
```

* C) `if (x > 5): print("Hi") else: print("Bye")`
* D) Both B and C

**Q71.** Which of the following correctly represents a loop that executes 4 times?

* A) `for i in range(4):`
* B) `for i in range(1,5):`
* C) Both A and B
* D) None

**Q72.** What does the following code print?

```python
for i in range(3):
    if i == 1:
        break
    print(i)
```

* A) 0 1 2
* B) 0
* C) 0 1
* D) Nothing

**Q73.** What is the output of:

```python
for i in range(2):
    pass
print("Done")
```

* A) Done
* B) 0 1 Done
* C) Nothing
* D) Error

**Q74.** Which statement about `else` with loops is correct?

* A) Runs only if loop terminates normally
* B) Runs only if loop breaks
* C) Runs always
* D) Runs only in while loops

**Q75.** Which operator is used to check multiple conditions inside an `if`?

* A) &&
* B) and
* C) &
* D) both && and and

**Q76.** What is the output?

```python
n = 0
while n < 2:
    print(n)
    n += 1
else:
    print("End")
```

* A) 0 1
* B) 0 1 End
* C) End
* D) Infinite loop

---

## 3. Data Collections -- Tuples, Dictionaries, Lists, and Strings (25%)

**Q77.** Which of these methods adds multiple elements to a list?

* A) append()
* B) extend()
* C) insert()
* D) push()

**Q78.** What will be printed?

```python
nums = [1,2,3,4]
print(nums[::2])
```

* A) \[1,2]
* B) \[1,3]
* C) \[2,4]
* D) Error

**Q79.** Which of the following is true about tuples?

* A) They are mutable
* B) They are immutable
* C) They allow item assignment
* D) They cannot be compared

**Q80.** What is the result?

```python
s = "abcd"
print(s[::-1])
```

* A) abcd
* B) dcba
* C) Error
* D) None

**Q81.** What will be the result of:

```python
{'x':1, 'y':2}.get('z', 100)
```

* A) None
* B) Error
* C) 100
* D) z

**Q82.** Which of the following methods removes all elements from a list?

* A) clear()
* B) remove()
* C) del list
* D) pop()

**Q83.** Which of the following string methods returns True if all characters are alphabetic?

* A) isdigit()
* B) isalpha()
* C) isalnum()
* D) isspace()

**Q84.** Which of the following is the correct syntax for a multi-line string?

* A) `'''text'''`
* B) `"""text"""`
* C) Both A and B
* D) None

**Q85.** What is the output?

```python
t = (1,2,3)
print(len(t))
```

* A) 2
* B) 3
* C) Error
* D) None

**Q86.** Which dictionary method returns a view of all keys?

* A) values()
* B) items()
* C) keys()
* D) get()

---

## 4. Functions and Exceptions (28%)

**Q87.** Which of the following defines a function correctly?

* A) `def myfunc: print("Hi")`
* B) `def myfunc(): print("Hi")`
* C) `func myfunc(): print("Hi")`
* D) `define myfunc(): print("Hi")`

**Q88.** Which keyword is used to return a value from a function?

* A) yield
* B) return
* C) pass
* D) break

**Q89.** Which of the following represents keyword arguments?

* A) `func(1,2)`
* B) `func(a=1,b=2)`
* C) `func(1, b=2)`
* D) Both B and C

**Q90.** What will the following code print?

```python
def add(x,y=2):
    return x+y
print(add(3))
```

* A) 2
* B) 3
* C) 5
* D) Error

**Q91.** What will be printed?

```python
def fun():
    global x
    x = 5
fun()
print(x)
```

* A) Error
* B) None
* C) 5
* D) 0

**Q92.** Which of the following exceptions occurs when converting a non-numeric string to int?

* A) ValueError
* B) TypeError
* C) IndexError
* D) ArithmeticError

**Q93.** Which exception occurs when trying to open a file that doesn’t exist?

* A) FileError
* B) FileNotFoundError
* C) IOError
* D) OSError

**Q94.** Which of the following is true about exception propagation?

* A) Exception stops only current function
* B) Exception moves up the call stack
* C) Exception always terminates program
* D) Exception cannot be propagated

**Q95.** Which block is always executed regardless of exception?

* A) try
* B) except
* C) else
* D) finally

**Q96.** Which exception is raised when you try to access a dictionary key that doesn’t exist?

* A) ValueError
* B) IndexError
* C) KeyError
* D) LookupError

**Q97.** What happens if you put `return` without a value inside a function?

* A) Returns 0
* B) Returns None
* C) Returns Error
* D) Returns False

**Q98.** Which of the following is true about recursion?

* A) Every recursive function must have a base case
* B) Recursion always leads to infinite loops
* C) Recursion cannot be used in Python
* D) Recursion replaces loops entirely

**Q99.** Which keyword allows handling of multiple exceptions in one block?

* A) and
* B) or
* C) as
* D) tuple form `(Exception1, Exception2)`

**Q100.** What is the output of the following code?

```python
try:
    print(1/0)
except ZeroDivisionError as e:
    print("Error:", e)
```

* A) Error
* B) Error: division by zero
* C) ZeroDivisionError
* D) None

**Q101.** Which statement about `raise` is correct?

* A) Used to define new exceptions
* B) Used to trigger exceptions
* C) Used to stop the program
* D) Used to continue the program

**Q102.** Which of the following is true about the `else` block in exception handling?

* A) Executes only if no exception occurs
* B) Executes always
* C) Executes only if exception occurs
* D) Never executes

---
