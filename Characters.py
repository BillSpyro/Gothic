#Base Character
class Character(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

#Player
class Player(Character):
        def __init__(self, name, health, gold):
            Character.__init__(self, name, health)
            self.gold = gold

player = Player("Player", 100, 0)

#Enemies
class Enemy(Character):
        def __init__(self, name, health, damage):
            Character.__init__(self, name, health)
            self.damage = damage

zombie = Enemy("Zombie", 20, 10)

headless_zombie = Enemy("Headless Zombie", 30, 20)

imp = Enemy("Imp", 20, 20)

wolf = Enemy("Wolf", 25, 25)

#Bosses
class Boss(Enemy):
        def __init__(self, name, health, damage, defeated):
            Enemy.__init__(self, name, health, damage)
            self.defeated = defeated

stained_glass_demon = Boss("Stained Glass Demon", 200, 30, True)
