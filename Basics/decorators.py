# Python Decorator function is a function that adds functionality to another, but does not modify it.
# wraps another function.

def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$$$$$$$$")
  
    return wrap

def sayhello():
    print("Hello")

newfunc=decor(sayhello)
newfunc()


print("\n")

@decor
def sayhello1():
    print("Hello")

sayhello1()

# Closure

#When we call func, it remembers the value of func from the argument to the function decorator(). This is called closure in Python

msg="Hello"
def func1(msg):
    def func2():
        print(msg)
        func2()
print(func1(msg))