x = 10  # Global variable

def fun1():
    y = 5 # Local variable
    print(y)

def fun2():
    x = 15 # Local variable
    print("Inside f2", x) # 15

def fun3():
    global x
    x = 15 # It;s going to change the global value of x to 15
    print("Inside f3", x)

fun2() # 15
print("main", x) # 10
fun3() # 15
print("main", x) # 15