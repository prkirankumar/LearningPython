class Teacher:
    def __init__(self,first_name,last_name,students):
        self.first_name=first_name
        self.last_name=last_name
        self.number_of_students=students
    
    def show_information(self):
        print(f'Full Name : {self.first_name} {self.last_name} \n'
              f'Number of students : {self.number_of_students}')

class Mathematics(Teacher):
    def __init__(self, number, *args, **kwargs):
        self.favorite_number = number
        super().__init__(*args, **kwargs) # invokes the base class constructor


teacher = Teacher('Kiran', 'Kumar', 30)
print(f'First name: {teacher.first_name}')
teacher.show_information()

print('------------------------')

mathematics = Mathematics(first_name='KiranKumar', last_name='PR', students=35, number=10)
print(f'First name: {mathematics.first_name}')
mathematics.show_information()
print(f'Favorite number: {mathematics.favorite_number}')    

print("\n\n")


class OrcRace:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def deal_damage(self):
        print(f'Unit {self.name} dealt {self.damage} damage!')

    def go_to(self, x, y):
        print(f'Unit {self.name} is going to {x}, {y}')


class Troll(OrcRace):
    def throw_spear(self):
        print(f'Unit {self.name} threw a spear')
        super().deal_damage()


class Tauren(OrcRace):
    def __init__(self, name, damage, health, special_totem=False):
        self.special_totem = special_totem
        super().__init__(name, damage, health)

    def use_totem(self):
        print(f'Unit {self.name} attacked with totem')
        super().deal_damage()
        if self.special_totem:
            print(f'Unit {self.name} used a special totem. Additionally  dealt 20 damage')


orc = OrcRace('orc', 15, 10)
troll = Troll('troll', 20, 15)
tauren = Tauren('tauren', 30, 25, True)

orc.deal_damage()
troll.deal_damage()
tauren.deal_damage()
print('----------')
troll.throw_spear()
print('----------')
tauren.use_totem()

print(f'Is tauren an instance of OrcRace: {isinstance(tauren, OrcRace)}')
print(f'Is tauren an instance of Troll: {isinstance(tauren, Troll)}')
print(f'Is tauren an instance of Tauren: {isinstance(tauren, Tauren)}')

print(f'Is Tauren class a subclass of OrcRace: {issubclass(Tauren, OrcRace)}')
print(f'Is Tauren class a subclass of Troll: {issubclass(Tauren, Troll)}')
print(f'Is Tauren class a subclass of Tauren: {issubclass(Tauren, Tauren)}')

