'''
* With Python closure, we don’t need to use global values. This is because they let us refer to nonlocal variables. 
  A closure then provides some form of data hiding.
* When we have only a few Python methods (usually, only one), we may use a Python3 closure instead of implementing a class for that.
  This makes it easier on the programmer.
* A closure, lets us implement a Python decorator.
* A closure lets us invoke Python function outside its scope.
'''

def outer(x):
    result=0
    print(x)
    
    def inner(n):
        print(x)
        print(n)
        nonlocal result
        while n>0:
            result+=x*n
            n-=1
        return result
    return inner

myfunc=outer(7) # out x=7
print(myfunc(3)) # n=3
