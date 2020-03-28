'''                                                     ***** Slicing *****

Slicing is similar to indexing but returns a sequence of items instead of a single item. The indices used for slicing are also zero-based.
There are two variants of the slicing syntax: sequence[start:stop] and sequence[start:stop:step]. 

When you use the syntax sequence[start:stop], you’ll get the new sequence. 
It will start with the item that has the index start (inclusive) and end before the item with the index stop. 
In other words, the statement sequence[start:stop] returns the items sequence[start], sequence[stop-1], and all the items between them:
'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(my_string[3:7]) # 2010
print(my_string[-23:-16]) # Bitcoin
print(my_string[:12]) # In 2010, som
print(my_string[-9:])
print(my_string[::-1])
print(my_string[::7])
print(my_string[10:]) # omeone paid 10k Bitcoin for two pizzas.
print(my_string[:-4]) # In 2010, someone paid 10k Bitcoin for two piz

my_tuple = (1, 2, 4, 8, 16, 32, 64, 128)
print(my_tuple[:]) # (1, 2, 4, 8, 16, 32, 64, 128)
print(my_tuple[:-1]) # (1, 2, 4, 8, 16, 32, 64)
print(my_tuple[1:5:2]) # (2, 8)
'''
step is 2, so you start with the item that has the index 1 (the item 2), collect every second item, 
and stop before you reach the item with the index 5 (32). You take the item 2, skip 4, and take 8.
'''
print(my_tuple[1:5:]) # (2, 4, 8, 16) 
print(my_tuple[4:1:-1]) # (16, 8, 4)


 '''
 A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. 
 You can also specify the step, which allows you to e.g. slice only every other item.
 '''
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x]) # ('a', 'b')
x = slice(3, 5)
print(a[x]) # ('d', 'e')
x = slice(0, 8, 3)
print(a[x]) # ('a', 'd', 'g') 
