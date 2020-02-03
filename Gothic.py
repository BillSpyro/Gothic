from sys import exit
from random import randint
from textwrap import dedent
from Items import *
from Characters import *

#   Gothic          #
#   Max Crandall    #
#   1/31/2020       #

class area(object):

    def enter(self):
        print("Empty")
        exit(1)

class Engine(object):

    def __init__(self, area_map):
        self.area_map = area_map

    def play(self):
        current_area = self.area_map.opening_area()
        last_area = self.area_map.next_area('finished')

        while current_area != last_area:
            next_area_name = current_area.enter()
            current_area = self.area_map.next_area(next_area_name)

        current_area.enter()

class Death(area):

    def enter(self):
        print(dedent("""
            You have died
            """))

        exit(1)

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
                    print(dedent(f"""
                        Your attempt at destorying the statue was to no avail.
                        """))
                    return 'statue_crypt'
                else:
                    print(dedent(f"""
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
            print(dedent(f"""

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
                    print(dedent(f"""
                        Your attempt at destorying the statue was to no avail.
                        """))
                    return 'statue_crypt'
                else:
                    print(dedent(f"""
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
                print(dedent(f"""
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
                    print(dedent(f"""
                        You find nothing.
                        """))
                    return 'waterway_crypt'
                else:
                    print(dedent(f"""
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
            print(dedent(f"""

                What do you do?
                1. Go for a swim.
                2. Look for more things in the water.
                3. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
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
                    print(dedent(f"""
                        You find nothing.
                        """))
                    return 'waterway_crypt'
                else:
                    print(dedent(f"""
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

            print(dedent(f"""

                What do you do?
                1. Leave the crypt.
                2. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
                    You exit the crypt
                    """))
                return 'crypt_graveyard'
            elif choice == "2":
                print(dedent(f"""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent(f"""
                    You just stare at the lock.
                    """))
                return 'gate_crypt'
        else:
            print(dedent(f"""

                What do you do?
                1. Try to open the lock.
                2. Use your head.
                3. Go back.
                """))

            choice = input("> ")

            if choice == "1":
                print(dedent(f"""
                    You try to fiddle with the lock to no avail.
                    """))
                return 'gate_crypt'
            elif choice == "2":
                print(dedent(f"""
                    You bang your skull on the lock to no avail.
                    fustrated and determined you continuosly bang
                    your skull on the lock. After banging too many
                    times your skull has exploded into a million
                    tiny pieces.
                    """))
                return 'death'
            elif choice == "3":
                print(dedent(f"""
                    You go back to the main crypt.
                    """))
                return 'main_crypt'
            else:
                print(dedent(f"""
                    You just stare at the lock.
                    """))
                return 'gate_crypt'

class Map(object):

    areas = {
        'intro': Intro(),
        'death': Death(),
        'main_crypt': MainCrypt(),
        'statue_crypt': StatueCrypt(),
        'waterway_crypt': WaterwayCrypt(),
        'gate_crypt': GateCrypt()
    }

    def __init__(self, start_area):
        self.start_area = start_area

    def next_area(self, area_name):
        val = Map.areas.get(area_name)
        return val

    def opening_area(self):
        return self.next_area(self.start_area)

area = Map('intro')
Gothic = Engine(area)
Gothic.play()
