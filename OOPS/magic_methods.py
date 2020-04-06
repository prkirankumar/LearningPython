'''                             Special Methods (Magic / Dunder Methods)
* method names start and end with double underscore e.g __init__
* are called implicityly
* allow us to interact with core concepts of the python language
* thanks to them classes can behave like functions, list or numbers

__str__(self):
 The method should return a readable form of the object. This is informal text for the customer

 __repr__(self):
 The method should return a Python object in a form that could be acceptable for eval() funciton. Useful for developers while debugging

__len__(self):
This method is called when built-in function len(object) is used. It returns the number of elements of the given object

arithmetic operations
---------------------
__add__(sef,other) - addition
__sub__(self,other) - subtraction
__mul__(self,other) - multiplication
__truediv__(self,other) - division



'''

import datetime

today=datetime.datetime.now()

print(today) # implicitly calls __str__ on today 
print(str(today))
print(repr(today))

new_date=datetime.datetime(2020, 4, 6, 12, 40, 3, 110656)
print(new_date)

class Car:
    def __init__(self,color,model):
        self.color=color
        self.model=model
    
    def __str__(self):
        return f'this is a {bmw1.color} {bmw1.model}'
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.model!r})'

bmw1=Car('white','BMW') # this is a white BMW
print(bmw1) #str
print(f'{repr(bmw1)}') # Car('white', 'BMW')
#print(f'this is a {bmw1.color} {bmw1.model}') # can be included in the calls with __str__()



text="Python Programming"
print(len(text))
print(text.__len__())
 

class SomeList:
    def __init__(self):
        self.__inner_list=[]
    
    def add_element(self,element):
        self.__inner_list.append(element)
    
    def remove_element(self,element):
        self.__inner_list.remove(element)
    
    # def get_length(self):
    def __len__(self):
        return len(self.__inner_list)

some_list=SomeList()
some_list.add_element(1)
some_list.add_element(2)
some_list.add_element(3)
print(len(some_list))
print(some_list.__len__())


print("-----arithmetic operations-----")

print(5 + 5)
print(int.__add__(5, 5))
print(5 + 5 == int.__add__(5, 5))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x, y: {self.x}, {self.y}'

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            x = self.x - other.x
            y = self.y - other.y
            return Point(x, y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Point):
            x = self.x * other.x
            y = self.y * other.y
            return Point(x, y)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Point):
            x = self.x / other.x
            y = self.y / other.y
            return Point(x, y)
        return NotImplemented


point_1 = Point(5, 5)
print(f'point_1 : {repr(point_1)}')
point_2 = Point(5, 5)
print(f'point_2 : {repr(point_2)}')
point_3 = point_1 + point_2
point_4 = point_1 - point_2
point_5 = point_1 * point_2
point_6 = point_1 / point_2
print(f'__add__\t {point_3}')
print(f'__sub__\t {point_4}')
print(f'__mul__\t {point_5}')
print(f'__truediv__\t {point_6}')

# point_7 = point_1 + '5, 5'




class MineralWater:
    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other):
        return self.sodium == other.sodium and self.calcium == other.calcium

    def __lt__(self, other):
        return self.sodium < other.sodium and self.calcium < other.calcium

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self < other and not self == other

    def __ge__(self, other):
        return not self < other


mineral_water_1 = MineralWater(32.50, 124)
mineral_water_2 = MineralWater(10, 114)
mineral_water_3 = MineralWater(10, 114)

print(f'mineral_water_1 == mineral_water_2: {mineral_water_1 == mineral_water_2}')
print(f'mineral_water_1 < mineral_water_2: {mineral_water_1 < mineral_water_2}')
print(f'mineral_water_1 != mineral_water_2: {mineral_water_1 != mineral_water_2}')
print(f'mineral_water_1 <= mineral_water_2: {mineral_water_1 <= mineral_water_2}')
print(f'mineral_water_1 > mineral_water_2: {mineral_water_1 > mineral_water_2}')
print(f'mineral_water_1 >= mineral_water_2: {mineral_water_1 >= mineral_water_2}')
print('---------------')
print(f'mineral_water_2 == mineral_water_3: {mineral_water_2 == mineral_water_3}')
print(f'mineral_water_2 < mineral_water_3: {mineral_water_2 < mineral_water_3}')
print(f'mineral_water_2 != mineral_water_3: {mineral_water_2 != mineral_water_3}')
print(f'mineral_water_2 <= mineral_water_3: {mineral_water_2 <= mineral_water_3}')
print(f'mineral_water_2 > mineral_water_3: {mineral_water_2 > mineral_water_3}')
print(f'mineral_water_2 >= mineral_water_3: {mineral_water_2 >= mineral_water_3}')

