'''
Polymorphism is the ability of an object to take many forms. It allows us to use different objects in the same way.

Duck typing : object usability for a particular purpose is determined not based on type of the object,
but by the presence of certain methods and properties in the object.
This technique comes from the pharse " If it looks like a duck and quacks like a duck, it's duck"
In duck typing we dont have to check the type of the obect to call method

'''

class Duck:

    def quack(self):
        print('I am a Duck!')

    def fly(self):
        print('Duck can fly')


class Human:

    def quack(self):
        print('I am a Human!')

    def fly(self):
        print("Human can't fly")


duck = Duck()
human = Human()

# for obj in [duck, human]:
#     if hasattr(obj, 'quack'):
#         obj.quack()
#     if hasattr(obj, 'fly'):
#         obj.fly()

for obj in [duck, human]:  # polymorphism
    try:
        obj.quack()
        obj.fly()
        obj.eat()
    except AttributeError as exc:
        print(f'Attribute error: {exc}')
