#Base Item
class Item(object):
    def __init__(self, name, inInventory):
        self.name = name
        self.inInventory = inInventory

#Health
class Health(Item):
    def __init__(self, name, inInventory, amount, health, value):
        Item.__init__(self, name, inInventory)
        self.amount = amount
        self.health = health
        self.value = value

life_bottle = Health("Life Bottle", False, 0, 100, 100)

energy_vile = Health("Energy Vile", False, 0, 50, 50)

#Keys
class Key(Item):
    def __init__(self, name, inInventory):
        Item.__init__(self, name, inInventory)

crypt_key = Key("Crypt Key", False)

skull_key = Key("Skull Key", False)

graveyard_key = Key("Graveyard Key", False)

#Shields
class Shield(Item):
    def __init__(self, name, inInventory, durability, value):
        Item.__init__(self, name, inInventory)
        self.durability = durability
        self.value = value

copper_shield = Shield("Copper Shield", False, 50, 25)

silver_shield = Shield("Silver Shield", False, 100, 50)

#Weapons
class Weapon(Item):
    def __init__(self, name, inInventory, damage, value):
        Item.__init__(self, name, inInventory)
        self.damage = damage
        self.value = value

arm = Weapon("Arm", 5, True, 0)

small_sword = Weapon("Small Sword", False, 10, 50)

club = Weapon("Club", False, 15, 100)

war_hammer = Weapon("War Hammer", False, 20, 200)
