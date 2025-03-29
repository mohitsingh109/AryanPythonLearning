def fun1():
    print("Fun1()")

def fun2(arg):
    print(f"Arg: {arg}")
    fun1()

def fun3():
    print("Fun3()")
    fun2("I am fun 3")
    return 100  # return is used to exit the function call as well

def call_me_get_multiple_response():
    return "Aryan", 15, "USA", 9.8

result = fun3()
print(result)

name, age, address, _  = call_me_get_multiple_response() # unboxing
print(name)
print(age)
print(address)
"""
Fun3()
Arg: I am fun 3
Fun1()
100
"""