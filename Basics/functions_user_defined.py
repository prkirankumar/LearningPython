'''
We follow the same rules when naming a function as we do when naming a variable.

It can begin with either of the following: A-Z, a-z, and underscore(_).
The rest of it can contain either of the following: A-Z, a-z, digits(0-9), and underscore(_).
A reserved keyword may not be chosen as an identifier.

'''

def my_func1():
    '''
        comments
    '''
    print("Hello Python!")
    
my_func1()
print(my_func1.__doc__) # can access docstring using the __doc__ attribute of the function.
print(type(my_func1.__doc__)) # <class 'str'>

def my_func2():
    add = 10 + 20
    print(add)
    
my_func2()

'''
If you don’t yet know what to put in the function, then you should put the pass statement in its body. 
If you leave its body empty, you get an error “Expected an indented block”.
'''
def hello():
    pass

hello()


def my_func3(x):
    return x * 10

print(my_func3(7))


def my_func4(x, y):
    return x / y

print(my_func4(38,19))


def my_func5(x,y,z):
    return x ** y + z # 3**3 + 3   ---> 27+3

print(my_func5(3,3,3))



def my_func6(x):
    my_new_list = []
    for i in range(5): # 0 1 2 3 4
        my_new_list.append(i * x)
    return my_new_list

result = my_func6(2)
print(result)

def my_func7(x):
    return x.upper()

result = my_func7("Python Programming")
print(result)

def my_func8(x):
    return list(set(x))

result = my_func8([11, 12, 13, 11, 15, 18, 18, 22, 20, 16, 12])
print(result)

def my_func9(x):
    my_new_list = []
    for i in x:
        if i > 4:
            my_new_list.append(i ** 2)
    return my_new_list

result = my_func9((2, 3, 5, 6, 4, 8, 9))
print(result)


def my_func10(x):
    return len(x) * sorted(x.keys())[-1]

result = my_func10({1: 3, 2: 3, 4: 5, 5: 9, 6: 8, 3: 7, 7: 0})
print(result)

# default parameter value
def my_func11(x, y = 10):
    return x * y

result = my_func11(5)
print(result)

def my_func12(x, y = 100, z = 200):
    return x + y + z

result = my_func12(50)
print(result)
################


def my_func13(x, y):
    return x[y]

result = my_func13(list(range(2,25,2)), 4)
print(result)

def my_func14(x, *args): # 5, 10 20 30 50
    print(args) # 10 20 30 50
    print(args[1]) # 20
    print(x) # 5
    return x * args[1] # 100

result = my_func14(5, 10, 20, 30, 50)
print(result)

def my_func(x, **kwargs):
    return x * sorted(kwargs.values())[-1]

result = my_func(10, val1 = 10, val2 = 15, val3 = 20, val4 = 25, val5 = 30)
print(result) # 300


##### variable scope in functions
 
var = 10

def my_func20(x):
	print(x * var)
	
my_func20(20)


var = 10

def my_func21(x):
    var = 5
    print(x * var)
	
my_func21(20)



def my_func22(x):
    var = 12
    print(x * var)
	
my_func22(10)


var = 8

def my_func23(x):
    global var # take the value from global variable
    print(x * var)
    var = 12

my_func23(10)

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg
test_var_args('C#','Python','Go','Scala')
   