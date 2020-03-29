'''                                                         ***** Sets *****
A set is an unordered collection of simple objects in Python. In addition to being iterable and mutable, a set has no duplicate elements. 
Any set defined in Python is an instance of the set class.

A set is employed when the existence of an object in a collection is much more important than the order or the frequency 
(number of times it appears) of the same.


Compared to a list, a set is advantageous by virtue of having a highly optimized method for checking whether some element is contained
in the set or not. The general syntax of a set is:

some_set = {“item 1”, “item 2”, “item 3”,….., “item n”}


add () – Adds an item to the set (Note: As sets don’t have repeating values, the item that is to be added to a set must not be already a member of the set.)
clear () – Removes all items of the set
difference () – Returns a set with all elements of the invoking set but not of the second set
intersect () – Returns an intersection of two sets
union () – Returns a union of two sets

discard()
remove()
pop() - it does not take an argument. a set doesn’t support indexing, there is absolutely no way to pass an index to the pop method. 
clear()
update() - add multiple items to the set at once, which it takes as arguments.


##     functions ##
len()
min()
max()
sum()
any()
all()
sorted()


#      methods

union() - What it does is it returns all the items that are in any of those sets.
instersection() - returns the common items in all the sets.

difference() - This returns the items that are in set1, but not in set2.
symmetric_difference() - returns all the items that are unique to each set.
intersection_update() - it does not update the set on which it is called
difference_update() - Like intersection-update(), this method updates the Python set with the difference.
symmetric_difference_update() - Like the two methods we discussed before this, it updates the set on which it is called with the symmetric difference.
copy() - reates a shallow copy of the Python set.
isdisjoint() - method returns True if two sets have a null intersection.
issubset() - returns true if the set in the argument contains this set.
issuperset() - returns True if the set contains the set in the argument.



'''
my_list = [1, 2, 3, 4, 4, 5, 2, 9, 8, 8, 4, 3]
print(type(my_list)) # <class 'list'>

my_set = set(my_list)
print(type(my_set)) # <class 'set'>
print(my_set)



b={3,2,1,2}
print(b) # {1, 2, 3}

'''
A set is mutable, but may not contain mutable items like a list, set, or even a dictionary.
There is no such thing as a nested Python set.
You can also create a set with the set() function.

d=set()

Remember that if you declare an empty set as the following code, it is an empty dictionary, not an empty set. We confirm this using the type() function.

d={}
type(d)
<class ‘dict’>


FAQ                                                        discard() vs remove()
discard() vs remove()-
These two methods may appear the same to you, but there’s actually a difference. 
If you try deleting an item that doesn’t exist in the set, discard() ignores it, but remove() raises a KeyError.
'''
# d={[1,2,3],4}
# print(d) # TypeError: unhashable type: 'list'

numbers={3,2,1,4,6,5}
print(numbers.remove(4)) 
print(numbers.discard(4))
print(numbers.pop()) # removes 1
numbers.clear()
print(numbers) # set()

# in and not in 

print('p' in {'a','p','p','l','e'})
print(0 not in {'0','1'})

numbers={3,2,1,4,6,5}


for i in numbers:
    print(i)

'''                                     frozen set
A frozen set is in-effect an immutable set. You cannot change its values. Also, a set can’t be used a key for a dictionary, but a frozenset can.
'''
my_set = frozenset(my_list) # {1, 2, 3, 4, 5, 8, 9}
print(type(my_set)) # <class 'frozenset'>
