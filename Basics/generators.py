'''
Generator is a kind of iterable like list and tuple. It generates a sequence of values 
that can be iterated, but can't index it

* generators vs list,tuple
 -   A list holds a number of values at once. But a Python generator holds only one value at a time, the value to yield. 
     This is why it needs much less space compared to a list. 
     With a generator, we also don’t need to wait until all the values are rendered.

a generator may contain more than one Python yield statement
'''


def counter():
    i=1
    while (i<=10):
        yield i
        i+=1

for i in counter():
    print(i)

def even_squares(x):
    for i in range(x):
        if i**2%2==0:
            yield i**2

print(list(even_squares(10)))
# If you apply the list() function to the call to the Python generator, it will return a list of the yielded values, in the order in which they are yielded.




