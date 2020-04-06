'''
Method overriding : reimplementation of method inherited from the base class in the derived class
It has the same name as the method in the base class and same method signature
The implementation in the derived class replaces the implementation in the in the base class

'''


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

    def show_information(self): # method overriding
        print(f'Full Name : {self.first_name} {self.last_name} \n'
              f'Number of students : {self.number_of_students} \n'
              f'Favorite number : {self.favorite_number}')
 

teacher = Teacher('Kiran', 'Kumar', 30)
print(f'First name: {teacher.first_name}')
teacher.show_information()

print('------------------------')

mathematics = Mathematics(first_name='KiranKumar', last_name='PR', students=35, number=10)
print(f'First name: {mathematics.first_name}')
mathematics.show_information()

print("\n\n Example 2 \n\n")

class Ship:
    def __init__(self,damage):
        self.damage=damage
    
    def deal_damage(self):
        print(f"{self.__class__.__name__} dealt {self.damage} damage")

class BattleShip(Ship):
    def __init__(self,special_damage,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.special_damage=special_damage
    
    def deal_special_damage(self):
        print(f"{self.__class__.__name__} dealt {self.special_damage} damage")

class BigBattleShip(BattleShip):
    def __init__(self, bomb_damage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bomb_damage = bomb_damage

    def deal_special_damage_twice(self):
        for _ in range(2):
            super().deal_special_damage()

    def use_bomb(self):
        print(f'{self.__class__.__name__} used a bomb and dealt {self.bomb_damage} damage')

class CargoShip(Ship):
    def __init__(self,capacity,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.capacity=capacity
    
    def transport(self):
        print(f'{self.__class__.__name__} transported {self.capacity} TEU')

ship = Ship(5)
battle_ship = BattleShip(special_damage=10, damage=5)
big_battle_ship = BigBattleShip(special_damage=10, damage=5, bomb_damage=20)
cargo_ship = CargoShip(capacity=10000, damage=0)

ship.deal_damage()
print('---------')
battle_ship.deal_damage()
battle_ship.deal_special_damage()
print('---------')

big_battle_ship.deal_damage()
big_battle_ship.deal_special_damage_twice()
big_battle_ship.use_bomb()
print('---------')
cargo_ship.deal_damage()
cargo_ship.transport()

