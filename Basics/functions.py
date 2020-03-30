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


