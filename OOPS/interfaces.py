'''
Interface allow us to define common behavior that can be implemented by any class. 
It is something like a skeleton of the class.

Class which inherit interface need to implement all methods described in the interface (method overriding).

'''


class SpaceShip: # interface
    def attack(self):
        raise NotImplementedError("Attack method must be implemented")


class LightSpaceShip(SpaceShip):
    dmg = 5

    def attack(self):
        print(f'Light attack: {self.dmg} dmg')


class HeavySpaceShip(SpaceShip):
    dmg = 10

    def attack(self):
        print(f'Heavy attack: {self.dmg} dmg')


class MagicSpaceShip(SpaceShip):
    dmg = 15

    def attack(self):
        print(f'Magic attack: {self.dmg} dmg')


class TankSpaceShip(SpaceShip):
    dmg = 20

    def attack(self):
        print(f'Tank attack: {self.dmg} dmg')


light_ship = LightSpaceShip()
heavy_ship = HeavySpaceShip()
magic_ship = MagicSpaceShip()
tank_ship = TankSpaceShip()

space_ships_array = [light_ship, heavy_ship, magic_ship, tank_ship]

for space_ship in space_ships_array:
    space_ship.attack()


print("----- example 2 -----")
class PublicTransportInterface:
    def transport_people(self):
        raise NotImplementedError('This method must be implemented in subclass')

    def display_info(self):
        raise NotImplementedError('This method must be implemented in subclass')


class Tram(PublicTransportInterface):
    def __init__(self, tram_type, capacity, max_speed):
        self.tram_type = tram_type
        self.capacity = capacity
        self. max_speed = max_speed

    def transport_people(self):
        print(f'{self.__class__.__name__} transported {self.capacity} people')

    def display_info(self):
        print(f'Tram type: {self.tram_type}\nCapacity: {self.capacity}\nMax speed: {self.max_speed}')


class Bus(PublicTransportInterface):
    def __init__(self, brand, capacity, color):
        self.brand = brand
        self.capacity = capacity
        self.color = color

    def transport_people(self):
        print(f'{self.__class__.__name__} transported {self.capacity} people')

    def display_info(self):
        print(f'Bus brand: {self.brand}\nCapacity: {self.capacity}\nColor: {self.color}')


class MercedesBenzBus(Bus):
    def __init__(self, air_conditioning, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.air_conditioning = air_conditioning

    def display_info(self):
        super().display_info()
        print(f'Air conditioning: {self.air_conditioning}')


avenio_tram = Tram('Avenio', 240, 80)
volvo_bus = Bus('Volvo', 30, 'white')
mercedes_benz_bus = MercedesBenzBus(True, 'Mercedes-Benz', 40, 'black')

for public_transport in [avenio_tram, volvo_bus, mercedes_benz_bus]:
    public_transport.transport_people()
    public_transport.display_info()
    print('-------------------')