def factorial(n):
    f=1
    while n>0:
             f*=n
             n-=1
    print(f)

factorial(5)
factorial(-2) #2 

def factorial_recursion(n):
    if n==1:
        return 1
    return n*factorial_recursion(n-1)

print(factorial_recursion(5))
#print(factorial_recursion(-2)) # throws RecursionError

