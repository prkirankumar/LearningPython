
'''
Python Iterator, implicitly implemented in constructs like for-loops, comprehensions, and python generators. 
The iter() and next() functions collectively form the iterator protocol.

to build an iterator we use the iter() and next() functions. 

Remember, it does not have to be a list you create an iterator on.


__next__() : traverse python iterator


creat infinite python iterators
'''
import itertools


evens=[2,4,6,8,10]
print(type(evens))

evenIterator=iter(evens)
print(next(evenIterator))
print(next(evenIterator))

iter((1,3,2))

nums=[1,2,3]
numsiterator=iter(nums)
print(numsiterator.__next__())
print(next(numsiterator))


for i in "Python" :
    print(i)

## actual implementation for above 
iter_obj=iter('Python3')
while True:
    try:
        i=next(iter_obj)
        print(i)
    except StopIteration:
        break

## userdefined iterator

class Count:
    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

c=Count()
print(next(c))
print(next(c))
print("----")
#######################################333333
print("--------")
list1 = [1, 2, 3]
list2 = [4, 5]

result = list(itertools.chain(list1, list2))

print(result)


for i in itertools.count(20, 2):
    if i < 31:
        print(i)
    else:
        break

lam = lambda x: x < 5

result = list(itertools.filterfalse(lam, range(10)))

print(result)


###################################################################333

