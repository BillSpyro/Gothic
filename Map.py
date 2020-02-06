from sys import exit
from random import randint
from textwrap import dedent
from Items import *
from Characters import *

#Base Area
class area(object):

    def enter(self):
        print("Empty")
        exit(1)

#Combat System
class Combat(area):
    def __init__(self, enemy, area, fought):
        self.enemy = enemy
        self.area = area
        self.fought = fought

    def enter(self):
        while player.health > 0 and combat.enemy.health > 0:
            print(dedent(f"""
                -Combat-
                A {combat.enemy.name} approaches you.
                Your health {player.health}
                {combat.enemy.name} health {combat.enemy.health}
                """))

            if silver_shield.inInventory == True:
                print(dedent(f"""
                    Your {silver_shield.name} durability {silver_shield.durability}.
                    """))

            if copper_shield.inInventory == True:
                print(dedent(f"""
                    Your {copper_shield.name} durability {copper_shield.durability}.
                    """))

            print(dedent("""
                What do you do?
                1. Attack.
                2. Use item.
                3. Nothing.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
                    Attack with what?

                    1. Your {arm.name}.
                    """))

                if small_sword.inInventory == True:
                    print(dedent(f"""
                        2. Your {small_sword.name}.
                        """))

                if club.inInventory == True:
                    print(dedent(f"""
                        3. Your {club.name}.
                        """))

                if war_hammer.inInventory == True:
                    print(dedent(f"""
                        4. Your {war_hammer.name}.
                        """))

                choice = input("> ")

                if choice == '1':
                    combat.enemy.health -= arm.damage
                    print(dedent(f"""
                        You pull off your skeletal arm and proceed
                        to smack the {combat.enemy.name} dealing {arm.damage} damage.
                        """))

                elif choice == '2' and small_sword.inInventory == True:
                    combat.enemy.health -= small_sword.damage
                    print(dedent(f"""
                        You dealt {small_sword.damage} to the {combat.enemy.name}.
                        """))

                elif choice == '3' and club.inInventory == True:
                    combat.enemy.health -= club.damage
                    print(dedent(f"""
                        You dealt {club.damage} to the {combat.enemy.name}.
                        """))

                elif choice == '4' and war_hammer.inInventory == True:
                    combat.enemy.health -= war_hammer.damage
                    print(dedent(f"""
                        You dealt {war_hammer.damage} to the {combat.enemy.name}.
                        """))

                else:
                    return 'combat'

            elif choice == "2":
                print(dedent("""
                    Use what?
                    """))

                if life_bottle.amount > 0:
                    print(dedent(f"""
                        1. Your {life_bottle.name}. {life_bottle.amount} left.
                        """))

                if energy_vile.amount > 0:
                    print(dedent(f"""
                        2. Your {energy_vile.name}. {energy_vile.amount} left.
                        """))

                choice = input("> ")

                if choice == '1' and life_bottle.amount > 0:
                    if player.health >= 100:
                        print(dedent("""
                            You are at full health.
                            """))
                    else:
                        player.health += life_bottle.health
                        life_bottle.amount -= 1
                        if player.health > 100:
                            player.health = 100
                        print(dedent(f"""
                            You used the {life_bottle.name}.
                            """))

                elif choice == '2' and energy_vile.amount > 0:
                    if player.health >= 100:
                        print(dedent("""
                            You are at full health.
                            """))
                    else:
                        player.health += energy_vile.health
                        energy_vile.amount -= 1
                        if player.health > 100:
                            player.health = 100
                        print(dedent(f"""
                            You used the {energy_vile.name}.
                            """))

                else:
                    return 'combat'

            elif choice == "3":
                print(dedent("""
                    You chose to do nothing.
                    """))

            else:
                print(dedent(f"""
                    You just stared at the {combat.enemy.name}.
                    """))
                return 'combat'

            enemy_attack = randint(1,2)

            if enemy_attack > 1 and combat.enemy.health > 0:
                print(dedent(f"""
                    The {combat.enemy.name} hits.
                    """))
                if silver_shield.inInventory == True and silver_shield.durability > 0:
                    silver_shield.durability -= combat.enemy.damage
                    print(dedent(f"""
                        Your {silver_shield.name} took {combat.enemy.damage} damage.
                        """))
                    if silver_shield.durability < 0:
                        silver_shield.durability = 0
                elif copper_shield.inInventory == True and copper_shield.durability > 0:
                    copper_shield.durability -= combat.enemy.damage
                    print(dedent(f"""
                        Your {copper_shield.name} took {combat.enemy.damage} damage.
                        """))
                    if copper_shield.durability < 0:
                        copper_shield.durability = 0
                else:
                    player.health -= combat.enemy.damage
                    print(dedent(f"""
                        You took {combat.enemy.damage} damage.
                        """))
            else:
                print(dedent(f"""
                    The {combat.enemy.name} misses.
                    """))

        if player.health <= 0:
            print(dedent(f"""
                You have been struck down by the {combat.enemy.name}.
                """))
            return 'death'
        else:
            print(dedent(f"""
                You have felled the {combat.enemy.name}.
                """))
            lootChance = randint(1,4)
            if lootChance > 3:
                print(dedent(f"""
                    You have found a {energy_vile.name}
                    """))
                energy_vile.amount += 1
            else:
                gold_yield = randint(0, 100)
                print(dedent(f"""
                    You have found {gold_yield} gold.
                    """))
                player.gold += gold_yield

        combat.fought = True
        return combat.area

combat = Combat(0, 0, 0)

#Shop System
class Gargoyle(area):
    def enter(self):
        print(dedent("""
            -Gargoyle-
            Hello Stranger. I have many useful items for sale.
            What would you like to buy?
            """))

        print(dedent(f"""
            Gold: {player.gold}
            """))

        print(dedent("""

            Category?
            1. Health
            2. Shields
            3. Weapons
            4. Go back
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent(f"""
                1. {life_bottle.name} costs {life_bottle.value}
                2. {energy_vile.name} costs {energy_vile.value}
                3. Go back
                """))

            choice = input("> ")

            if choice == "1":
                if player.gold > life_bottle.value:
                    player.gold -= life_bottle.value
                    life_bottle.amount += 1
                    print(dedent(f"""
                        You bought the {life_bottle.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford the {life_bottle.name}.
                        """))
                    return 'gargoyle'
            elif choice == "2":
                if player.gold > energy_vile.value:
                    player.gold -= energy_vile.value
                    energy_vile.amount += 1
                    print(dedent(f"""
                        You bought the {energy_vile.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford the {energy_vile.name}.
                        """))
                    return 'gargoyle'
            elif choice == "3":
                return 'gargoyle'
            else:
                print(dedent("""
                    You just stare at the gargoyle.
                    """))
                return 'gargoyle'


        elif choice == "2":

            if copper_shield.inInventory == False:
                print(dedent(f"""
                    1. buy {copper_shield.name} costs {copper_shield.value}
                    """))

            if copper_shield.inInventory == True and copper_shield.durability < 50:
                print(dedent(f"""
                    2. repair {copper_shield.name} costs {copper_shield.value}
                    """))

            if silver_shield.inInventory == False:
                print(dedent(f"""
                    3. buy {silver_shield.name} costs {silver_shield.value}
                    """))

            if silver_shield.inInventory == True and silver_shield.durability < 100:
                print(dedent(f"""
                    4. repair {silver_shield.name} costs {silver_shield.value}
                    """))

            print(dedent("""
                5. Go back
                """))

            choice = input("> ")

            if choice == "1" and copper_shield.inInventory == False:
                if player.gold > copper_shield.value:
                    player.gold -= copper_shield.value
                    copper_shield.inInventory = True
                    print(dedent(f"""
                        You bought the {copper_shield.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford the {copper_shield.name}.
                        """))
                    return 'gargoyle'
            elif choice == "2" and copper_shield.inInventory == True and copper_shield.durability < 50:
                if player.gold > copper_shield.value:
                    player.gold -= copper_shield.value
                    copper_shield.durability = 50
                    print(dedent(f"""
                        You repaired the {copper_shield.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford to repair the {copper_shield.name}.
                        """))
                    return 'gargoyle'
            elif choice == "3" and silver_shield.inInventory == False:
                if player.gold > silver_shield.value:
                    player.gold -= silver_shield.value
                    silver_shield.inInventory = True
                    print(dedent(f"""
                        You bought the {silver_shield.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford the {silver_shield.name}.
                        """))
                    return 'gargoyle'
            elif choice == "4" and silver_shield.inInventory == True and silver_shield.durability < 100:
                if player.gold > silver_shield.value:
                    player.gold -= silver_shield.value
                    silver_shield.durability = 100
                    print(dedent(f"""
                        You repaired the {silver_shield.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford to repair the {silver_shield.name}.
                        """))
                    return 'gargoyle'
            elif choice == "5":
                return 'gargoyle'
            else:
                print(dedent("""
                    You just stare at the gargoyle.
                    """))
                return 'gargoyle'
        elif choice == "3":

            if war_hammer.inInventory == False:
                print(dedent(f"""
                    1. buy {war_hammer.name} costs {war_hammer.value}
                    """))

            print(dedent("""
                2. Go back
                """))

            choice = input("> ")

            if choice == "1" and war_hammer.inInventory == False:
                if player.gold > war_hammer.value:
                    player.gold -= war_hammer.value
                    war_hammer.inInventory = True
                    print(dedent(f"""
                        You bought the {war_hammer.name}.
                        """))
                    return 'gargoyle'
                else:
                    print(dedent(f"""
                        You can't afford the {war_hammer.name}.
                        """))
                    return 'gargoyle'

            elif choice == "2":
                return 'gargoyle'
            else:
                print(dedent("""
                    You just stare at the gargoyle.
                    """))
                return 'gargoyle'
        elif choice == "4":
            print(dedent("""
                You stop talking to the gargoyle.
                """))
            return 'enterance_graveyard'
        else:
            print(dedent("""
                You just stare at the gargoyle.
                """))
            return 'gargoyle'

#Death System
class Death(area):

    def enter(self):
        print(dedent("""
            You have died
            """))

        exit(1)

#Intro Area
class Intro(area):

    def enter(self):
        print(dedent("""
            You have awakened.....
            As you get up, you look around.
            The area you are in seems to be an underground crypt.
            As you raise your hands you see skeletal fingers.
            You are in the form of an undead skeleton.
            """))

        return 'main_crypt'

class MainCrypt(area):

    def enter(self):
        print(dedent("""
            -Main Crypt-
            From where you are there are two hallways. One to
            the left and one to the right. There is also a gate
            with a stairwell behind it leading upwards.
            """))
        if copper_shield.inInventory == False:
            print(dedent(f"""
                Next to the slab that you have awoken from there is a
                {copper_shield.name}.
                """))

            print(dedent(f"""

                What do you do?
                1. Take the {copper_shield.name}.
                2. Go down the left hallway.
                3. Go down the right hallway.
                4. Go to the gate.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
                    You take the {copper_shield.name}.
                    """))
                copper_shield.inInventory = True
                return 'main_crypt'
            elif choice == "2":
                print(dedent("""
                    You head down the left hallway.
                    """))
                return 'statue_crypt'
            elif choice == "3":
                print(dedent("""
                    You head down the right hallway.
                    """))
                return 'waterway_crypt'
            elif choice == "4":
                print(dedent("""
                    You approach the gate.
                    """))
                return 'gate_crypt'
            else:
                print(dedent("""
                    You just stared into space.
                    """))
                return 'main_crypt'
        else:
            print(dedent("""

                What do you do?
                1. Go down the left hallway.
                2. Go down the right hallway.
                3. Go to the gate.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You head down the left hallway.
                    """))
                return 'statue_crypt'
            elif choice == "2":
                print(dedent("""
                    You head down the right hallway.
                    """))
                return 'waterway_crypt'
            elif choice == "3":
                print(dedent("""
                    You approach the gate.
                    """))
                return 'gate_crypt'
            else:
                print(dedent("""
                    You just stared into space.
                    """))
                return 'main_crypt'

class StatueCrypt(area):

    def enter(self):
        print(dedent("""
            -Statue Crypt-
            As you enter the room, you see a statue of a hero.
            The statue is posing heroically, a sign next to the
            statue reads 'The great hero Karl Sturnguard whom has
            slain the last of the demons.'
            """))
        if small_sword.inInventory == False:
            print(dedent(f"""
                You spot a {small_sword.name} lying next to the statue.
                """))

            print(dedent(f"""

                What do you do?
                1. Take the {small_sword.name}.
                2. Desecrate the statue.
                3. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
                    You take the {small_sword.name}.
                    """))
                small_sword.inInventory = True
                return 'statue_crypt'
            elif choice == "2":
                print(dedent("""
                    You attempt to desecrate the statue.
                    """))
                chance = randint(1,3)
                if chance == 1:
                    print(dedent(f"""
                        Your attempt at destorying the statue was to no avail,
                        but while trying, you find a {life_bottle.name} wedged
                        in the statue. You then take it for yourself.
                        """))
                    life_bottle.amount += 1
                    return 'statue_crypt'
                elif chance == 2:
                    print(dedent("""
                        Your attempt at destorying the statue was to no avail.
                        """))
                    return 'statue_crypt'
                else:
                    print(dedent("""
                        Your attempt at destorying the statue was to no avail,
                        but while trying, a piece of the statue fell of
                        and hit you smack in the skull, causing it to
                        explode into tiny pieces.
                        """))
                    return 'death'
            elif choice == "3":
                print(dedent("""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent("""
                    You just stare at the statue.
                    """))
                return 'statue_crypt'
        else:
            print(dedent("""

                What do you do?
                1. Desecrate the statue.
                2. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You attempt to desecrate the statue.
                    """))
                chance = randint(1,3)
                if chance == 1:
                    print(dedent(f"""
                        Your attempt at destorying the statue was to no avail,
                        but while trying, you find a {life_bottle.name} wedged
                        in the statue. You then take it for yourself.
                        """))
                    life_bottle.amount += 1
                    return 'statue_crypt'
                elif chance == 2:
                    print(dedent("""
                        Your attempt at destorying the statue was to no avail.
                        """))
                    return 'statue_crypt'
                else:
                    print(dedent("""
                        Your attempt at destorying the statue was to no avail,
                        but while trying, a piece of the statue fell of
                        and hit you smack in the skull, causing it to
                        explode into tiny pieces.
                        """))
                    return 'death'
            elif choice == "2":
                print(dedent("""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent("""
                    You just stare at the statue.
                    """))
                return 'statue_crypt'

class WaterwayCrypt(area):
    def enter(self):
        print(dedent("""
            -Waterway Crypt-
            As you enter the room, you can see a stream of water
            coming from a grate from one side of the room which
            flows to the other side of the room into another grate.
            """))
        if crypt_key.inInventory == False:
            print(dedent(f"""
                Taking a closer look into the stream of water, you can
                see something shimmer. It seems to be the {crypt_key.name}.
                """))

            print(dedent(f"""

                What do you do?
                1. Take the {crypt_key.name}.
                2. Go for a swim.
                3. Look for more things in the water.
                4. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
                    You carefully fish out the {crypt_key.name}.
                    """))
                crypt_key.inInventory = True
                return 'waterway_crypt'
            elif choice == "2":
                print(dedent("""
                    You jump right into the water. But have you forgotten?
                    You are only just a skeleton and bouyancy is a problem
                    for the undead. You then proceed to drown.
                    """))
                return 'death'
            elif choice == "3":
                print(dedent("""
                    You attempt find something in the water.
                    """))
                chance = randint(1,3)
                if chance == 1:
                    print(dedent(f"""
                        You manage to fish something out of the water. It
                        is an {energy_vile.name}.
                        """))
                    energy_vile.amount += 1
                    return 'waterway_crypt'
                elif chance == 2:
                    print(dedent("""
                        You find nothing.
                        """))
                    return 'waterway_crypt'
                else:
                    print(dedent("""
                        While trying to fish something out of the water,
                        something grabs your boney hand and drags you in.
                        You then proceed to drown.
                        """))
                    return 'death'
            elif choice == "4":
                print(dedent("""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent("""
                    You just stared at the stream.
                    """))
                return 'waterway_crypt'

        else:
            print(dedent("""

                What do you do?
                1. Go for a swim.
                2. Look for more things in the water.
                3. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You jump right into the water. But have you forgotten?
                    You are only just a skeleton and bouyancy is a problem
                    for the undead. You then proceed to drown.
                    """))
                return 'death'
            elif choice == "2":
                print(dedent("""
                    You attempt find something in the water.
                    """))
                chance = randint(1,3)
                if chance == 1:
                    print(dedent(f"""
                        You manage to fish something out of the water. It
                        is a {energy_vile.name}.
                        """))
                    energy_vile.amount += 1
                    return 'waterway_crypt'
                elif chance == 2:
                    print(dedent("""
                        You find nothing.
                        """))
                    return 'waterway_crypt'
                else:
                    print(dedent("""
                        While trying to fish something out of the water,
                        something grabs your boney hand and drags you in.
                        You then proceed to drown.
                        """))
                    return 'death'
            elif choice == "3":
                print(dedent("""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent("""
                    You just stared at the stream.
                    """))
                return 'waterway_crypt'

class GateCrypt(area):
    def enter(self):
        print(dedent("""
            -Gate Crypt-
            As you near the gate, there seems to be a lock attached.
            Beyond the gate it looks like freedom from this dank and
            dark crypt.
            """))
        if crypt_key.inInventory == True:
            print(dedent(f"""
                But you now have the {crypt_key.name}!
                You can now get out of here.
                """))

            print(dedent("""

                What do you do?
                1. Leave the crypt.
                2. Go back to the main area.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You exit the crypt.
                    """))
                return 'crypt_graveyard'
            elif choice == "2":
                print(dedent("""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent("""
                    You just stare at the lock.
                    """))
                return 'gate_crypt'
        else:
            print(dedent("""

                What do you do?
                1. Try to open the lock.
                2. Use your head.
                3. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You try to fiddle with the lock to no avail.
                    """))
                return 'gate_crypt'
            elif choice == "2":
                print(dedent("""
                    You bang your skull on the lock to no avail.
                    fustrated and determined you continuosly bang
                    your skull on the lock. After banging too many
                    times your skull has exploded into a million
                    tiny pieces.
                    """))
                return 'death'
            elif choice == "3":
                print(dedent("""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent("""
                    You just stare at the lock.
                    """))
                return 'gate_crypt'

class CryptGraveyard(area):
    def enter(self):
        print(dedent("""
            -Crypt Graveyard-
            You are now up a hill next to the crypt in the middle
            of a sprawling graveyard. There are graves and
            tombstones spread out across the land. It is the middle
            of the night and the sky is dark blue. In the distance
            a large mausoleum is resting upon a towering hill. From
            where you are one path leads to the graveyard enterance
            and the other leads deeper into the graveyard and towards
            the hilltop mausoleum.
            """))

        print(dedent("""

            What do you do?
            1. Go to the graveyard enterance.
            2. Go deeper into the graveyard.
            3. Go back into the crypt.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You walk towards the graveyard enterance.
                """))
            return 'enterance_graveyard'
        elif choice == "2":
            print(dedent("""
                You walk down deeper into the graveyard.
                """))
            return 'graves_graveyard'
        elif choice == "3":
            print(dedent("""
                You go back into the crypt.
                """))
            return 'gate_crypt'
        else:
            print(dedent("""
                You just start into the moonlight.
                """))
            return 'crypt_graveyard'

class EnteranceGraveyard(area):
    def __init__(self, looted):
        self.looted = looted

    def enter(self):
        print(dedent("""
            -Enerance Graveyard-
            You walk down the hill to the graveyard enterance. There
            is a large gate that is keeping you from leaving the
            graveyard. Past the gate you can see a distant village.
            The gate doesn't have a lock and seems to be stuck shut.
            There also is an object attached to the wall next to the
            gate. It seems to be a gargoyle. His eyes are glowing.
            """))

        if enterance_graveyard.looted == False:
            print(dedent("""

                What do you do?
                1. Talk to the gargoyle.
                2. Loot an open grave.
                3. Go back up the crypt hill.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You try to talk to the gargoyle.
                    """))
                return 'gargoyle'
            elif choice == "2":
                gold_yield = randint(20, 100)
                print(dedent(f"""
                    You pillage a nearby open grave.
                    The plunder has yielded you {gold_yield} gold.
                    """))
                player.gold += gold_yield
                enterance_graveyard.looted = True
                return 'enterance_graveyard'
            elif choice == "3":
                print(dedent("""
                    You go back up the crypt hill.
                    """))
                return 'crypt_graveyard'
            else:
                print(dedent("""
                    You just stare into the distant village.
                    """))
                return 'enterance_graveyard'
        else:
            print(dedent("""

                What do you do?
                1. Talk to the gargoyle.
                2. Go back up the crypt hill.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You try to talk to the gargoyle.
                    """))
                return 'gargoyle'
            elif choice == "2":
                print(dedent("""
                    You go back up the crypt hill.
                    """))
                return 'crypt_graveyard'
            else:
                print(dedent("""
                    You just stare into the distant village.
                    """))
                return 'enterance_graveyard'

enterance_graveyard = EnteranceGraveyard(False)

class GravesGraveyard(area):
    def __init__(self, looted):
        self.looted = looted

    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = zombie
            combat.area = 'graves_graveyard'
            zombie.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Graves Graveyard-
            You are now surrounded by open graves and tombstones.
            One way leads to a large wooden gate and the other
            leads to the crypt hill.
            """))

        if graves_graveyard.looted == False:

            print(dedent("""

                What do you do?
                1. Go to the large wooden gate.
                2. Loot an open grave.
                3. Go back up the crypt hill.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You go towards the large wooden gate.
                    """))
                return 'wooden_gate_graveyard'
            elif choice == "2":
                gold_yield = randint(20, 100)
                print(dedent(f"""
                    You pillage a nearby open grave.
                    The plunder has yielded you {gold_yield} gold.
                    """))
                player.gold += gold_yield
                graves_graveyard.looted = True
                combat.fought = True
                return 'graves_graveyard'
            elif choice == "3":
                print(dedent("""
                    You go back up the crypt hill.
                    """))
                return 'crypt_graveyard'
            else:
                print(dedent("""
                    You just stare at the open graves.
                    """))
                combat.fought = True
                return 'graves_graveyard'

        else:
            print(dedent("""

                What do you do?
                1. Go to the large wooden gate.
                2. Go back up the crypt hill.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent("""
                    You go towards the large wooden gate.
                    """))
                return 'wooden_gate_graveyard'
            elif choice == "2":
                print(dedent("""
                    You go back up the crypt hill.
                    """))
                return 'crypt_graveyard'
            else:
                print(dedent("""
                    You just stare at the open graves.
                    """))
                combat.fought = True
                return 'graves_graveyard'

graves_graveyard = GravesGraveyard(False)

class WoodenGateGraveyard(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = zombie
            combat.area = 'wooden_gate_graveyard'
            zombie.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Wooden Gate Graveyard-
            You have come upon a large wooden gate. It also appears to be locked.
            Passed the wooden gate you can see the Hilltop Mausoleum in the distance.
            There are also two other paths near you. One leads back to the open
            graves closer to the crypt. The other leads into another part of the
            graveyard with a small tomb that rests on a small hill.
            """))

        if graveyard_key.inInventory == True:
            print(dedent("""
                You now have the key to open the wooden gate.
                """))

        print(dedent("""

            What do you do?
            """))

        if graveyard_key.inInventory == True:
            print(dedent("""
                1. Go through the wooden gate.
                """))
        else:
            print(dedent("""
                1. Charge the wooden gate.
                """))
        print(dedent("""
            2. Go towards the tomb.
            3. Go towards the open graves.
            """))

        choice = input("> ")

        if choice == "1" and graveyard_key.inInventory == True:
            print(dedent("""
                You leave through the wooden gate.
                """))
            return 'angel_statue_graveyard'
        elif choice == "1" and graveyard_key.inInventory == False:
            print(dedent("""
                You charge at the wooden gate and upon impact....nothing happens.
                """))
            combat.fought = True
            return 'wooden_gate_graveyard'
        elif choice == "2":
            print(dedent("""
                You go towards the tomb.
                """))
            return 'tomb_graveyard'
        elif choice == "3":
            print(dedent("""
                You go back to the open graves.
                """))
            return 'graves_graveyard'
        else:
            print(dedent("""
                You just stare at wooden gate.
                """))
            combat.fought = True
            return 'wooden_gate_graveyard'

class TombGraveyard(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = zombie
            combat.area = 'tomb_graveyard'
            zombie.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Tomb Graveyard-
            Now up the hill in front of the tomb you can see
            a key attached to a coffin inside the tomb.
            """))

        print(dedent("""

            What do you do?
            """))

        if graveyard_key.inInventory == False:
            print(dedent("""
                1. Raid the tomb for the key.
                """))
        else:
            print(dedent("""
                1. Present an offering.
                """))
        print(dedent("""
            2. Go back to the wooden gate.
            """))

        choice = input("> ")

        if choice == "1" and graveyard_key.inInventory == False:
            print(dedent("""
                You forcefully take the key from the coffin. In doing so
                the coffin opens and a headless zombie emerges from the
                coffin seeking revenge for disrespecting his tomb.
                """))
            graveyard_key.inInventory = True
            combat.enemy = headless_zombie
            combat.area = 'tomb_graveyard'
            headless_zombie.health = 30
            return 'combat'
        elif choice == "1" and player.gold > 50 and graveyard_key.inInventory == True:
            print(dedent("""
                You present an offering of 50 gold to the tomb for
                stealing the key.
                """))
            player.gold -= 50
            player.health += 5
            combat.fought = True
            return 'tomb_graveyard'
        elif choice == "1" and player.gold < 50 and graveyard_key.inInventory == True:
            print(dedent("""
                You don't have enough gold.
                """))
            combat.fought = True
            return 'tomb_graveyard'
        elif choice == "2":
            print(dedent("""
                You go back to the wooden gate.
                """))
            return 'wooden_gate_graveyard'
        else:
            print(dedent("""
                You just stare at the tomb.
                """))
            combat.fought = True
            return 'tomb_graveyard'

class AngelStatueGraveyard(area):
    def __init__(self, direction, looted):
        self.direction = direction
        self.looted = looted

    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = zombie
            combat.area = 'angel_statue_graveyard'
            zombie.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Angel Statue Graveyard-
            As you enter the area a gate behind you closes.
            In front of you now is an Angel Statue. an inscription on
            the statue reads, "Nothing is hidden under the gaze of an
            angel". To the North you will come upon a monument. To the
            East is a small grave. To the West you will come upon a
            cliffside. To the South you will come upon the wooden gate.
            Each direction has a gate.
            """))

        if angel_statue_graveyard.direction == 1:
            print(dedent("""
                The Angel Statue is facing South.
                """))
        elif angel_statue_graveyard.direction == 2:
            print(dedent("""
                The Angel Statue is facing East.
                """))
        elif angel_statue_graveyard.direction == 3:
            print(dedent("""
                The Angel Statue is facing North.
                """))
        elif angel_statue_graveyard.direction == 4:
            print(dedent("""
                The Angel Statue is facing West.
                """))

        print(dedent("""

            What do you do?
            """))
        if angel_statue_graveyard.direction == 1:
            print(dedent("""
                1. Go to the wooden gate.
                """))
        elif angel_statue_graveyard.direction == 2 and angel_statue_graveyard.looted == False:
            print(dedent("""
                1. Loot the grave.
                """))
        elif angel_statue_graveyard.direction == 3:
            print(dedent("""
                1. Go to the monument.
                """))
        elif angel_statue_graveyard.direction == 4:
            print(dedent("""
                1. Go to the cliffside.
                """))
        print(dedent("""
            2. Hit the statue.
            """))

        choice = input("> ")

        if choice == "1" and angel_statue_graveyard.direction == 1:
            print(dedent("""
                You go towards the large wooden gate.
                """))
            return 'wooden_gate_graveyard'
        elif choice == "1" and angel_statue_graveyard.direction == 2 and angel_statue_graveyard.looted == False:
            gold_yield = randint(20, 100)
            print(dedent(f"""
                You pillage the grave.
                The plunder has yielded you {gold_yield} gold.
                """))
            player.gold += gold_yield
            angel_statue_graveyard.looted = True
            combat.fought = True
            return 'angel_statue_graveyard'
        elif choice == "1" and angel_statue_graveyard.direction == 3:
            print(dedent("""
                You go to the monument.
                """))
            return 'monument_graveyard'
        elif choice == "1" and angel_statue_graveyard.direction == 4:
            print(dedent("""
                You go to the cliffside.
                """))
            return 'cliffside_graveyard'
        elif choice == "2":
            print(dedent("""
                You hit the Angel Statue, causing it to rotate.
                """))
            angel_statue_graveyard.direction += 1
            if angel_statue_graveyard.direction > 4:
                angel_statue_graveyard.direction = 1
            combat.fought = True
            return 'angel_statue_graveyard'
        else:
            print(dedent("""
                You just stare at the Angel Statue.
                """))
            combat.fought = True
            return 'angel_statue_graveyard'

angel_statue_graveyard = AngelStatueGraveyard(1, False)

class MonumentGraveyard(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = zombie
            combat.area = 'monument_graveyard'
            zombie.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Monument Graveyard-
            You have come across a large monument in the middle of the graveyard.
            This seems to be the center landmark of the graveyard. From where you
            are there are three paths. One leads to the Angel Statue. Another leads
            to A Skull Gate. The last leads into a large ditch of unfilled graves.
            In the not so distance you are getting closer to the Hilltop Mausoleum.
            """))
        print(dedent("""

            What do you do?
            1. Go to the Skull Gate.
            2. Go into the ditch.
            3. Go to the Angel Statue.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You approach the Skull Gate.
                """))
            return 'skull_gate_graveyard'
        elif choice == "2":
            print(dedent("""
                You go into the ditch.
                """))
            return 'ditch_graveyard'
        elif choice == "3":
            print(dedent("""
                You go towards the angel statue.
                """))
            return 'angel_statue_graveyard'
        else:
            print(dedent("""
                You just stare at monument.
                """))
            combat.fought = True
            return 'monument_graveyard'

class SkullGateGraveyard(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = wolf
            combat.area = 'skull_gate_graveyard'
            wolf.health = 25
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Skull Gate Graveyard-
            Now infront of the Skull Gate you see that of course it is locked.
            a sign next to the gate reads, "Passed these gates lies the land
            of the living. Only those worthy enough may leave the necropolis."
            """))

        if skull_key.inInventory == True:
            print(dedent("""
                You now have the skull key and leave the Necropolis.
                """))

        print(dedent("""

            What do you do?
            """))

        if skull_key.inInventory == True:
            print(dedent("""
                1. Go through the Skull Gate.
                """))
        else:
            print(dedent("""
                1. Bang on the Skull Gate.
                """))
        print(dedent("""
            2. Go back to the monument.
            """))

        choice = input("> ")

        if choice == "1" and skull_key.inInventory == True:
            print(dedent("""
                You leave the necropolis.
                """))
            return 'completed'
        elif choice == "1" and skull_key.inInventory == False:
            print(dedent("""
                You try and bang on the Skull Gates hoping something will
                happen. But all the noise just attracted some wolves.
                """))
            combat.enemy = wolf
            combat.area = 'skull_gate_graveyard'
            wolf.health = 25
            return 'combat'
        elif choice == "2":
            print(dedent("""
                You go back to the monument.
                """))
            return 'monument_graveyard'
        else:
            print(dedent("""
                You just stare at Skull Gate.
                """))
            combat.fought = True
            return 'skull_gate_graveyard'

class CliffSideGraveyard(area):
    def __init__(self, looted):
        self.looted = looted

    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = zombie
            combat.area = 'cliffside_graveyard'
            zombie.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -CliffSide Graveyard-
            You are now on a cliff hanging above a ditch. Passed the ditch is
            the Hilltop Mausoleum. There are many graves and tombstones along
            the cliff edge. The ditch looks low enough for you to jump down
            into it.
            """))

        print(dedent("""

            What do you do?
            1. Go down in the ditch.
            """))

        if cliffside_graveyard.looted == False:
            print(dedent("""
            2. Loot an open grave.
                """))

        print(dedent("""
            3. Go to the angel statue.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You go down in the ditch.
                """))
            return 'ditch_graveyard'
        elif choice == "2" and cliffside_graveyard.looted == False:
            gold_yield = randint(20, 100)
            print(dedent(f"""
                You pillage a nearby open grave.
                The plunder has yielded you a {life_bottle.name}.
                """))
            life_bottle.amount += 1
            cliffside_graveyard.looted = True
            combat.fought = True
            return 'cliffside_graveyard'
        elif choice == "3":
            print(dedent("""
                You go to the angel statue.
                """))
            return 'angel_statue_graveyard'
        else:
            print(dedent("""
                You just stare off into the ditch.
                """))
            combat.fought = True
            return 'cliffside_graveyard'

cliffside_graveyard = CliffSideGraveyard(False)

class DitchGraveyard(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = headless_zombie
            combat.area = 'ditch_graveyard'
            headless_zombie.health = 30
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Ditch Graveyard-
            You are now in a ditch in the graveyard. There are many coffins
            lying around that haven't been placed in a proper burial. From
            one end of the ditch there is a door and passed it is the base
            of Cemetary Hill which is the foundation for the Hilltop
            Mausoleum. From the other is stairs that lead up to the monument
            which is the center of the graveyard. Up above you can see a
            cliffside that houses many tombstones.
            """))

        print(dedent("""

            What do you do?
            1. Go through the door to the base of Cemetary Hill.
            2. Go up the stairs to the monument.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You go down in the ditch.
                """))
            return 'base_cemetaryhill'
        elif choice == "2":
            print(dedent("""
                You go up to the monument.
                """))
            return 'monument_graveyard'
        else:
            print(dedent("""
                You just stare at the unfilled graves.
                """))
            combat.fought = True
            return 'ditch_graveyard'

class BaseCemetaryHill(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = headless_zombie
            combat.area = 'base_cemetaryhill'
            headless_zombie.health = 30
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Base Cemetaryhill-
            You have arrived at the base of Cemetaryhill. You could attempt
            to climb the hill but at the top there are a pair of gargoyles
            spewing boulders that are rolling down the hill. It would be
            painful to get hit by one unless if you had a shield handy.
            Off to the side is a small forest that is enclosed in the graveyard.
            There is also a door that leads to the ditch in the graveyard.
            """))

        print(dedent("""

            What do you do?
            1. Attempt to climb the hill.
            2. Go off to the forest.
            3. Go through the door.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You attempt to climb the hill. While doing so
                several boulders are rolling down.
                """))
            boulders = randint(1,3)
            chance = randint(1,3)
            damage = boulders * 30
            if chance == 1:
                print(dedent("""
                    You have evaded the boulders and took no damage.
                    """))
                return 'top_cemetaryhill'
            else:
                print(dedent(f"""
                    You have been hit by {boulders} boulders.
                    """))
                if silver_shield.inInventory == True and silver_shield.durability > 0:
                    silver_shield.durability -= damage
                    print(dedent(f"""
                        Your {silver_shield.name} took {damage} damage.
                        """))
                    if silver_shield.durability < 0:
                        silver_shield.durability = 0
                elif copper_shield.inInventory == True and copper_shield.durability > 0:
                    copper_shield.durability -= damage
                    print(dedent(f"""
                        Your {copper_shield.name} took {damage} damage.
                        """))
                    if copper_shield.durability < 0:
                        copper_shield.durability = 0
                else:
                    player.health -= damage
                    print(dedent(f"""
                        You took {damage} damage.
                        """))
                    if player.health <= 0:
                        print(dedent(f"""
                            You have been crushed by a boulder.
                            """))
                        return 'death'
                return 'top_cemetaryhill'
        elif choice == "2":
            print(dedent("""
                You go to the forest area.
                """))
            return 'forest_cemetaryhill'
        elif choice == "3":
            print(dedent("""
                You go through the door.
                """))
            return 'ditch_graveyard'
        else:
            print(dedent("""
                You just stare rolling boulders.
                """))
            combat.fought = True
            return 'base_cemetaryhill'

#WIP
class TopCemetaryHill(area):
    def enter(self):
        print(dedent("""
            -Top Cemetaryhill-
            You are now at the top of Cemetary Hill. The Hilltop Mausoleum lies
            in front of you. There are two gargoyles spewing boulders down the
            hill. You could go down the hill to enter the graveyard proper again.
            """))

        print(dedent("""

            What do you do?
            1. Enter the Hilltop Mausoleum.
            2. Go down Cemetary Hill.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You enter the Hilltop Mausoleum.
                """))
            return 'hall_hilltop_mausoleum'
        elif choice == "2":
            print(dedent("""
                You go down to the base of Cemetaryhill.
                """))
            return 'base_cemetaryhill'
        else:
            print(dedent("""
                You just stare at the Hilltop Mausoleum.
                """))
            return 'top_cemetaryhill'

class ForestCemetaryHill(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = wolf
            combat.area = 'forest_cemetaryhill'
            wolf.health = 25
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Forest Cemetaryhill-
            You are now in the forested area of the graveyard. There are many
            trees surrounding the area and not graves in sight. From where you
            are you can see a cave that is behind Cemetaryhill. There is also
            a path that leads back to the base of Cemetaryhill.
            """))

        print(dedent("""

            What do you do?
            1. Go into the cave.
            2. Go to the base of Cemetaryhill
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You go into the cave.
                """))
            return 'witches_cave_cemetaryhill'
        elif choice == "2":
            print(dedent("""
                You go to the base of Cemetaryhill.
                """))
            return 'base_cemetaryhill'
        else:
            print(dedent("""
                You just stare into the forest.
                """))
            combat.fought = True
            return 'forest_cemetaryhill'

class WitchesCaveCemetaryHill(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = imp
            combat.area = 'witches_cave_cemetaryhill'
            imp.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Witches Cave Cemetaryhill-
            You are now inside the cave. It appears to be an old witches coven
            that was abandoned. You can see weird ritualistic markings along
            the cave wall, there are a couple of bookshelves and cauldrons
            laid about the place.
            """))

        if club.inInventory == False:
            print(dedent("""
                There is a large club lying next to a bookshelf.
                """))

        print(dedent("""

            What do you do?
            """))

        if club.inInventory == False:
            print(dedent("""
                1. Take the club.
                """))

        print(dedent("""
            2. Go to the forest.
            """))

        choice = input("> ")

        if choice == "1" and club.inInventory == False:
            print(dedent("""
                You go take the club.
                """))
            club.inInventory = True
            combat.fought = True
            return 'witches_cave_cemetaryhill'
        elif choice == "2":
            print(dedent("""
                You go to the forest.
                """))
            return 'forest_cemetaryhill'
        else:
            print(dedent("""
                You just stare at the markings on the wall.
                """))
            combat.fought = True
            return 'witches_cave_cemetaryhill'

class HallHilltopMausoleum(area):
    def __init__(self, destroyed):
        self.destroyed = destroyed

    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = imp
            combat.area = 'hall_hilltop_mausoleum'
            imp.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Hall Hilltop Mausoleum-
            You have entered the main hall of the Hilltop Mausoleum. The walls are
            lined with stained glass and torches illuminating the dank Mausoleum.
            There are coffins laid in two columns along the walls. There also is
            a crack in the ground. There is a gate in front of you and beyond it
            is a large circular arena. Also you could leave the Mausoleum.
            """))

        if club.inInventory == True and hall_hilltop_mausoleum.destroyed == False:
            print(dedent("""
                You could destroy the crack in the ground.
                """))

        elif hall_hilltop_mausoleum.destroyed == True:
            print(dedent("""
                There is an opening in the ground.
                """))

        print(dedent("""

            What do you do?
            """))

        if (club.inInventory == True or war_hammer.inInventory == True) and hall_hilltop_mausoleum.destroyed == False:
            print(dedent("""
                1. Smash the crack in the ground.
                """))

        elif hall_hilltop_mausoleum.destroyed == True:
            print(dedent("""
                1. Go through the opening in the ground.
                """))

        if skull_key.inInventory == True:
            print(dedent("""
                2. Go through the gate.
                """))

        else:
            print(dedent("""
                2. Attack the gate.
                """))

        print(dedent("""
            3. Leave the Mausoleum.
            """))

        choice = input("> ")

        if choice == "1" and (club.inInventory == True or war_hammer.inInventory == True) and hall_hilltop_mausoleum.destroyed == False:
            print(dedent("""
                You destroy the crack.
                """))
            hall_hilltop_mausoleum.destroyed = True
            combat.fought = True
            return 'hall_hilltop_mausoleum'
        elif choice == "1" and hall_hilltop_mausoleum.destroyed == True:
            print(dedent("""
                You jump down into the opening.
                """))
            return 'catacombs_hilltop_mausoleum'
        elif choice == "2" and skull_key.inInventory == True:
            print(dedent("""
                You go through the gate.
                """))
            return 'boss_arena_hilltop_mausoleum'
        elif choice == "2" and skull_key.inInventory == False:
            print(dedent("""
                You try to attack the gate to no avail.
                """))
            combat.fought = True
            return 'hall_hilltop_mausoleum'
        elif choice == "3":
            print(dedent("""
                You leave the Mausoleum
                """))
            return 'top_cemetaryhill'
        else:
            print(dedent("""
                You just stare at the stained glass.
                """))
            combat.fought = True
            return 'hall_hilltop_mausoleum'

hall_hilltop_mausoleum = HallHilltopMausoleum(False)

class CatacombsHilltopMausoleum(area):
    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = imp
            combat.area = 'catacombs_hilltop_mausoleum'
            imp.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Catacombs Hilltop Mausoleum-
            You find yourself deeper inside of the Mausoleum. You seem to be
            in catacombs of the Mausoleum. There are stairs that lead upward
            and a chamber that is emitting a red light.
            """))

        print(dedent("""

            What do you do?
            1. Go up the stairs.
            2. Go to the chamber.
            """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You go up the stairs.
                """))
            return 'boss_arena_hilltop_mausoleum'
        elif choice == "2":
            print(dedent("""
                You go into the chamber.
                """))
            return 'chamber_hilltop_mausoleum'
        else:
            print(dedent("""
                You just stare at the coffins.
                """))
            combat.fought = True
            return 'catacombs_hilltop_mausoleum'

class ChamberHilltopMausoleum(area):
    def __init__(self, destroyed):
        self.destroyed = destroyed

    def enter(self):
        combat_chance = randint(1,2)
        if combat_chance > 1 and combat.fought == False:
            combat.enemy = imp
            combat.area = 'chamber_hilltop_mausoleum'
            imp.health = 20
            return 'combat'

        combat.fought = False

        print(dedent("""
            -Chamber Hilltop Mausoleum-
            You are now in a chamber withing the Mausoleum.
            """))

        if chamber_hilltop_mausoleum.destroyed == False:
            print(dedent("""
                There is a glass heart in the middle of the room.
                """))

        elif chamber_hilltop_mausoleum.destroyed == True:
            print(dedent("""
                There are pieces of glass on the ground.
                """))

        print(dedent("""

            What do you do?
            """))

        if chamber_hilltop_mausoleum.destroyed == False:
            print(dedent("""
                1. Smash the glass heart.
                """))

        print(dedent("""
            2. Leave the chamber.
            """))

        choice = input("> ")

        if choice == "1" and chamber_hilltop_mausoleum.destroyed == False:
            print(dedent("""
                You smash the glass heart into pieces.
                """))
            chamber_hilltop_mausoleum.destroyed = True
            combat.fought = True
            stained_glass_demon.defeated = False
            return 'chamber_hilltop_mausoleum'
        elif choice == "2":
            print(dedent("""
                You go back into the catacombs.
                """))
            return 'catacombs_hilltop_mausoleum'
        else:
            print(dedent("""
                You just stare into space.
                """))
            combat.fought = True
            return 'chamber_hilltop_mausoleum'

chamber_hilltop_mausoleum = ChamberHilltopMausoleum(False)

class BossArenaHilltopMausoleum(area):
    def enter(self):

        print(dedent("""
            -Boss Arena Mausoleum-
            You are now in a large circular room. There is a huge stained glass
            window on the wall. There are stairs that lead down to the catacombs
            and there is a gate that leads to the hall. The gate is locked and
            needs the Skull Key to unlock which is the same key for the Skull
            Gate back at the Graveyard.
            """))

        if stained_glass_demon.defeated == False:
            print(dedent("""
                With the glass heart destroyed you have released the demon
                within. The demon then flys into the stained glass window.
                A moment later the glass comes to life as it bursts out of
                the window. Now a lumbering Stained Glass Demon towers over
                you.
                """))
            combat.enemy = stained_glass_demon
            combat.area = 'boss_arena_hilltop_mausoleum'
            stained_glass_demon.defeated = True
            skull_key.inInventory = True
            return 'combat'
        else:
            print(dedent(f"""
                With the death of the {stained_glass_demon.name} you now have the
                {skull_key.name}. You can now make your way to the skull gates
                and leave the Necropolis.
                """))

        print(dedent("""

            What do you do?
            1. Go down the stairs.
            """))

        if skull_key.inInventory == True:
            print(dedent("""
            2. Go to the hall.
                """))

        choice = input("> ")

        if choice == "1":
            print(dedent("""
                You go down the stairs.
                """))
            return 'catacombs_hilltop_mausoleum'
        elif choice == "2" and skull_key.inInventory == True:
            print(dedent("""
                You go into hall.
                """))
            return 'hall_hilltop_mausoleum'
        else:
            print(dedent("""
                You just stare at the stained glass window.
                """))
            return 'boss_arena_hilltop_mausoleum'

#Winning the game
class Completed(area):
    def enter(self):
        print(dedent("""
            -Land of the Living-
            You have escaped the Necropolis and now that you are free
            from the imprisonment of the Graveyard you can now
            wreak havoc across the Land of the Living.
            """))
        exit(1)

#Map System
class Map(object):

    areas = {
        'intro': Intro(),
        'death': Death(),
        'gargoyle': Gargoyle(),
        'combat': Combat(0, 0, 0),
        'main_crypt': MainCrypt(),
        'statue_crypt': StatueCrypt(),
        'waterway_crypt': WaterwayCrypt(),
        'gate_crypt': GateCrypt(),
        'crypt_graveyard': CryptGraveyard(),
        'enterance_graveyard': EnteranceGraveyard(0),
        'graves_graveyard': GravesGraveyard(0),
        'wooden_gate_graveyard': WoodenGateGraveyard(),
        'tomb_graveyard': TombGraveyard(),
        'angel_statue_graveyard': AngelStatueGraveyard(0, 0),
        'monument_graveyard': MonumentGraveyard(),
        'skull_gate_graveyard': SkullGateGraveyard(),
        'cliffside_graveyard': CliffSideGraveyard(0),
        'ditch_graveyard': DitchGraveyard(),
        'base_cemetaryhill': BaseCemetaryHill(),
        'forest_cemetaryhill': ForestCemetaryHill(),
        'witches_cave_cemetaryhill': WitchesCaveCemetaryHill(),
        'top_cemetaryhill': TopCemetaryHill(),
        'hall_hilltop_mausoleum': HallHilltopMausoleum(0),
        'catacombs_hilltop_mausoleum': CatacombsHilltopMausoleum(),
        'chamber_hilltop_mausoleum': ChamberHilltopMausoleum(0),
        'boss_arena_hilltop_mausoleum': BossArenaHilltopMausoleum(),
        'completed': Completed()
    }

    def __init__(self, start_area):
        self.start_area = start_area

    def next_area(self, area_name):
        val = Map.areas.get(area_name)
        return val

    def opening_area(self):
        return self.next_area(self.start_area)
