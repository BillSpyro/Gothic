class Item(object):
    def __init__(self, name, inInventory):
        self.name = name
        self.inInventory = inInventory

#Health
class Health(Item):
    def __init__(self, name, amount, health):
        self.name = name
        self.amount = amount
        self.health = health

life_bottle = Health("Life Bottle", 0, 100)

energy_vile = Health("Energy Vile", 0, 50)

#Keys
class Key(Item):
    def __init__(self, name, inInventory):
        self.name = name
        self.inInventory = inInventory

crypt_key = Key("Crypt Key", False)

skull_key = Key("Skull Key", False)

graveyard_key = Key("Graveyard Key", False)

#Shields
class Shield(Item):
    def __init__(self, name, inInventory, durability):
        self.name = name
        self.inInventory = inInventory
        self.durability = durability

copper_shield = Shield("Copper Shield", False, 50)

silver_shield = Shield("Silver Shield", False, 100)

#Weapons
class Weapon(Item):
    def __init__(self, name, damage, inInventory):
        self.name = name
        self.damage = damage
        self.inInventory = inInventory

small_sword = Weapon("Small Sword", 10, False)

club = Weapon("Club", 15, False)

hammer = Weapon("Hammer", 20, False)
