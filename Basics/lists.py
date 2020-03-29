'''                                                 ***** Lists *****
Unlike C++ or Java, Python Programming Language doesn’t have arrays. To hold a sequence of values, then, it provides the ‘list’ class. 
A Python list can be seen as a collection of values.

To create python list of items, you need to mention the items, separated by commas, in square brackets.

append () – Adds an element to the end of the list
clear () – Removes all elements from the list
copy () – Returns a shallow copy of the list
count () – Returns the total number of items passed as an argument
extend () – Adds all elements of a list to some other list
index () – Returns the index of an element (Note: If the same element appears multiple times in the list then the index of the very first match is returned)
insert () – Inserts an element to the list at the defined index
pop () – Eliminates and returns an element from the list
remove () – Eliminates an element from the list
reverse () – Reverses the order of all elements of the list
sort () – Sort all elements of a list in the ascending order

Time Complexity:
Append has constant time complexity i.e.,O(1).
Extend has time complexity of O(k). Where k is the length of list which need to be added.

Built-in List Functions
len()
max()
min()
sum()
sorted()
list()
any()
all()

'''
my_list = [10, 10.5, 20, 30, "Python", "Java", "Ruby"]
print(type(my_list)) # <class 'list'>
print(len(my_list))

my_list.pop(5)  # remove based on index
print(my_list)

my_list.append('C++') 
print(my_list)

my_list.remove(30) # removes the element, if the element is not there in the list throws ValueError
print(my_list)

print(my_list.index(10.5))

my_list.insert(4, 77) # insert(index,value)
print(my_list)

languages=[['English'],['Gujarati'],['Hindi'],'Romanian','Spanish']
print(languages[0])
languages=[('English','Albanian'),'Gujarati','Hindi','Romanian','Spanish']
print(languages[0])

my_list.extend([100, 101, 102])
print(my_list)
list1=[1,2,3,4,5]
list2=[1,2,3,4,5,6,7,8,9]
list1.extend(list2)
print(list1)
print(my_list.count(20))


my_list = [10, 10.5, 20, 30, 25.6, 19.25, 11.01, 29.99]
print(my_list.sort())
print(sorted(my_list)) # asc
print(sorted(my_list,reverse=True)) # desc
print(sorted(list1))

print(min(my_list))
print(max(my_list))
print(sum(my_list))
print(min(list1))
print(list1.clear()) # None
#print(my_list.clear()) # None

print((my_list + [30.01, 30.02, 30.03]) * 3) # prints my list 3 times
#my_list = [10, 10.5, 20, 30, "Python", "Java", "Ruby"]
print(my_list[2]) # 11.01
print(my_list[-2]) #29.99
print(my_list[3:6]) # [19.25, 20, 25.6]
print(my_list[-4:-1]) #[20, 25.6, 29.99]
print(my_list[3:]) # [19.25, 20, 25.6, 29.99, 30]
print(my_list[:5]) # [10, 10.5, 11.01, 19.25, 20]
print(my_list[:-4]) # [10, 10.5, 11.01, 19.25]
print(my_list[-4:]) # [20, 25.6, 29.99, 30]
print( my_list[::3]) # [10, 19.25, 29.99]
print(my_list[::-4]) # [30, 19.25]