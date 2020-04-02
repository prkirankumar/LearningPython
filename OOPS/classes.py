class ClassOne(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def square(self, p3):
        print(p3 ** 2)

p = ClassOne(1, 2)
print(type(p)) # <class '__main__.ClassOne'>

print(p.p1)
p.square(10)

p.p2=10
print(p.p2)

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