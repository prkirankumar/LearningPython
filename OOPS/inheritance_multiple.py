'''
Multiple inheritance is a feature in which a class can inherit attributes and method from more than one parent class

Method Resolution Order (MRO ) : shows the order in which base classes are searched for a method or attribute
 syntax : classname.mro()
'''

class Dancer:
    def dance(self):
        print('I am a Dancer!')


class FitnessCoach:
    def coach(self):
        print(f'I am a Fitness Coach!')


class Student(Dancer, FitnessCoach):
    pass


student = Student()
student.dance()
student.coach()

print("----- MRO-----")
print(Student.mro())

class A:
    def which_class(self):
        print("A")

class B(A):
    def which_class(self):
        print("B")

class C(B, A):  # for class C(A,B  getting method inconsistency resolution order)
    def which_class(self):
        B.which_class(self)
        A.which_class(self)
        print("C")

print(C.mro())
c=C()
print(c.which_class())

 # 
class AA:
    id=1            
class BB:
    id=2             
class CC:
    id=3              
class M(AA,CC,BB):
    pass

print(M.id) # 1 as base class is being called first
print(M.mro())
