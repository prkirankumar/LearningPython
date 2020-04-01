import config
'''
Global keyword is a keyword that allows a user to modify a variable outside of the current scope. It is used to create global variables from a non-global scope i.e inside a function. Global keyword is used inside a function only when we want to do assignments or when we want to change a variable. Global is not needed for printing and accessing.

Rules of global keyword:

If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
Variables that are only referenced inside a function are implicitly global.
We Use global keyword to use a global variable inside a function.
There is no need to use global keyword outside a function.


'''
# global variable
a = 15
b = 10
  
def add(): 
    c = a + b 
    print(c) 
  
add() 

##############

a = 15 
  
def change(): 
    #a = a + 5 # get below error
    global a 
    a=a+15
    print(a) 
  
change() # UnboundLocalError: local variable 'a' referenced before assignment,

############## sharing global variables

# # 1 Create a config.py file to store global variables:
# x = 0
# y = 0
# z ="none"
# # 2 Create a modify.py file to modify global variables:
# import config 
# config.x = 1
# config.y = 2
# config.z ="demo"
# # 3  Create a main.py file to modify global variables:
# # Here we have modified the value of x, y, and z. These variables were defined in the module config.py, hence we have to import 
# # config module and we can use config.variable_name to access these variables.
# import config 
# import modify 
# print(config.x) 
# print(config.y) 
# print(config.z) 

