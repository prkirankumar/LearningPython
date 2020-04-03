'''
range() - returns an immutable sequence of numbers between the given start integer to the stop integer.
range() takes mainly three arguments having the same use in both definitions:

start(optional) - integer starting from which the sequence of integers is to be returned
stop(required) - integer before which the sequence of integers is to be returned.
The range of integers end at stop - 1.
step (Optional) - integer value which determines the increment between each integer in the sequence



'''

my_range = range(10)
print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(0, 10)
print(list(my_range)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(-25, 139, 30)
print(list(my_range)) #[-25, 5, 35, 65, 95, 125]

my_range = range(-10,-9)
print(list(my_range)) #[-10]


# zip() is a built-in Python function that gives us an iterator of tuples. 
for i in zip([1,2,3],['a','b','c','d']):
    print(i)

print(set(zip([1,2],[3,4,5]))) # {(2, 4), (1, 3)}

''' 
eval() in Python is a built-in function or method, to which we pass an expression. 
It parses this expression and runs it as we execute the program. 
eval(expression, globals=None, locals=None)

Expression in Python eval()- This is the string to parse and evaluate

Globals in eval()- This is a dictionary that holds available global methods and variables, and is an optional parameter
Python eval Locals- This is a mapping object that holds available local methods and variables, and is an optional parameter.
We know that the standard mapping type in Python is a dictionary.

Vulnerabilities :
* Call a dangerous function
* Expose hidden values


Protecting Python Eval from exploitation

'''


''' exec()
We use exec() to dynamically execute Python code- this can be a string or some object code. When it is a string, 
Python parses it as a set of statements and executes it if there is no syntax error. When it is object code, Python executes it. 
But exec() doesn’t return a value; it returns None. Hence, we cannot use return and yield statements outside function definitions.
'''
code='a=7\nprint("a*17=",a*17)'
exec(code)

'''
repr()
repr() returns a string that holds a printable representation of an object.

FAQ 
str() vs repr() in Python
The __str__() and __repr__() methods both give us strings in return. So what sets them apart?

The goal of __repr__ is to be unambiguous and that of __str__ is to be readable.
__repr__ is kind of official and __str__ is somewhat informal.
'''