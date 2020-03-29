'''                                                             ***** Tuples *****
Tuples are like a list. It can hold a sequence of items. The difference is that it is immutable.
you must type a list of items separated by commas, inside parentheses.


tuple without parentheses is called "tuple packing." 
tuple unpacking is when you assign values from a tuple to a sequence of variables
FAQ tuples vs lists
'''
my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Hungary","Zurich")
last = max(my_tup)

print(last) #should return Slovenia

b= 1, 2.0, 'three' # tuple packing
print(b)

# unpacking
percentages=(99,95,90,89,93,96)
a,b,c,d,e,f=percentages
print(b)
print(percentages[3]) # accessing single item from tuple

my_tup = ("Romania", "Poland", "Estonia", "Bulgaria", "Slovakia", "Slovenia", "Estonia", "Romania", "Hungary", "Slovenia")

print(my_tup.count("Estonia"))
print(my_tup[-5:])
print(my_tup[:-3])
print(my_tup[3:])
print(my_tup[:3])

# del percentages[4] # TypeError: ‘tuple’ object doesn’t support item deletion 
# del percentages[2:4] # same as above
del percentages # deletes
'''             tuple functions
len() max() min() sum() any() all() sorted() tuple()

                tuple methods
index() count() 

                membership
in, not in

                contacenation
(1,2,3)+(4,5,6)
                logical
>,>=,==,<,<=    
                identity
is, not
'''
# nested tuples
a=((1,2,3),(4,(5,6)))
print(a[1][1][1])