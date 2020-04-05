class Employee:
    count=0
    
    def __init__(self,firstname,lastname,email,monthlysalary):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.monthlysalary=monthlysalary
        Employee.count+=1    

    def getannualsalary(self):
        return self.monthlysalary*12

    def showemployeeinformation(self):        
        fullname=f'{self.firstname} {self.lastname}'
        print(f' Name : {fullname} \n email : {self.email} \n Annual Salary : {self.getannualsalary()}')

emp1=Employee("kiran","kumar","reddykkp@hotmail.com",10000)
emp2=Employee("kiran","kumar","reddykkp@hotmail.com",10000)
emp1.showemployeeinformation()
emp2.showemployeeinformation()
print(f'No of employees {Employee.count}')



class ClassOne(object):
    myattribute="this is class attribute"
    def __init__(self, p1, p2):     # constructor
        self.p1 = p1 # instance attribute
        self.p2 = p2
    
    def square(self, p3): # instance method
        print(p3 ** 2)

p = ClassOne(1, 2)
print(type(p)) # <class '__main__.ClassOne'>

print(p.p1)
p.square(10)

p.p3="new attribute" # adding new attribute
p.p2=10
print(p.p2)
print(p.p3)
print(dir(p)) # to get the attributess of the object
print(ClassOne.myattribute)  # accessing class attributes


setattr(p, 'p2', 50)
print(getattr(p, 'p2'))

print(hasattr(p, 'p2'))

print(isinstance(p, ClassOne))

class ClassTwo(ClassOne):
    def times10(self, x):
        print(x * 10)
        
y = ClassTwo(10, 20)
print(y.p1)

obj = ClassTwo(15, 25)
print(obj.times10(45))

print(issubclass(ClassTwo, ClassOne))

# del classname
# del obj.attribute
# del obj