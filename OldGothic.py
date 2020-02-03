#   Gothic          #
#   Max Crandall    #
#   1/15/2020       #

import random

# Equipment
small_sword = 0
copper_shield = 0

# Key Items
crypt_key = 0

# Stats
gold = 0
health = 300
deaths = 0

prompt = "> "

# Intro Sequence
def Intro(deaths):
    if deaths == 0:
        print("You wake up.")
        print("You are laying on a slab.")
        print("You seem to be in some sort of crypt.")
        print("As you get up you see that you have the form of a skeleton.\n")
        Crypt_Start_Area()
    else:
        print("You wake up.")
        print("You are laying on a slab.")
        print("You seem to be in some sort of crypt.")
        print("This seems to be familiar.\n")
        Crypt_Start_Area()

# Death
def Death(how, deaths):
    ResetItems()
    deaths += 1
    print(how, "\n")
    print("You died.\n")
    print("Try again?")
    print("1. Yes")
    print("2. No")

    restart = input(prompt)

    if restart == "1":
        Intro(deaths)
    else:
        print(f"You have died {deaths} times")

# Inventory
def Inventory():
    global small_sword
    global copper_shield
    global crypt_key
    print(f"Small Sword = {small_sword}")
    print(f"Copper Shield = {copper_shield}")
    print(f"Crypt Key = {crypt_key}")

# Reseting items upon death
def ResetItems():
    global small_sword
    global copper_shield
    global crypt_key
    global gold
    global health
    small_sword = 0
    copper_shield = 0
    crypt_key = 0
    gold = 0
    health = 300

# Combat encounters
def Encounter(enemy, inventory, health):
    if enemy == "None":
        print("No enemies appeared")
    elif enemy == "Zombie":
        print("A zombie appears")

# Crypt Start
def Crypt_Start_Area():
    global copper_shield
    if copper_shield == 0:
        print("There are two hallways one to the left, and one to the right.")
        print("There is also a gate with a stairwell leading upwards.")
        print("Lying next to the slab is a copper shield.\n")
        print("What do you do?")
        print("1. Go to the left hallway")
        print("2. Go to the right hallway")
        print("3. Go to the gate")
        print("4. Take the copper shield\n")

        CryptStartArea = input(prompt)

        if CryptStartArea == "1":
            Crypt_Statue_Room()
        elif CryptStartArea == "2":
            Crypt_Key_Room()
        elif CryptStartArea == "3":
            Crypt_Gate()
        elif CryptStartArea == "4":
            print("You took the copper shield.\n")
            copper_shield = 1
            Crypt_Start_Area()
        else:
            print("You just stare into empty space.\n")
            Crypt_Start_Area()
    else:
        print("There are two hallways one to the left, and one to the right.")
        print("There is also a gate with a stairwell leading upwards.")
        print("The copper shield that once lied next to the slab is gone.\n")
        print("What do you do?")
        print("1. Go to the left hallway")
        print("2. Go to the right hallway")
        print("3. Go to the gate")
        print("4. Put the copper shield back\n")

        CryptStartArea = input(prompt)

        if CryptStartArea == "1":
            Crypt_Statue_Room()
        elif CryptStartArea == "2":
            Crypt_Key_Room()
        elif CryptStartArea == "3":
            Crypt_Gate()
        elif CryptStartArea == "4":
            print("Put the copper shield back.\n")
            copper_shield = 0
            Crypt_Start_Area()
        else:
            print("You just stare into empty space.\n")
            Crypt_Start_Area()


# Crypt Statue Room
def Crypt_Statue_Room():
    global small_sword
    if small_sword == 0:
        print("You find yourself in a room with a statue of a hero.")
        print("Below next to the statue you see a small sword.\n")
        print("What do you do?")
        print("1. Take the small sword")
        print("2. Desecrate the statue")
        print("3. Exit the area\n")

        CryptStatueRoom = input(prompt)

        if CryptStatueRoom == "1":
            if small_sword == 0:
                print("You took the small sword.\n")
                small_sword = 1
                Crypt_Statue_Room()
        elif CryptStatueRoom == "2":
            print("After attempting to dismantle the statue you tripped and fell")
            Death("landing on your skull, you explode into tiny bone fragments.", deaths)
        elif CryptStatueRoom == "3":
            print("You left the room\n")
            Crypt_Start_Area()
        else:
            print("You just stared at the statue\n")
            Crypt_Statue_Room()
    else:
        print("You find yourself in a room with a statue of a hero.")
        print("There is no longer a small sword next to the statue.\n")
        print("What do you do?")
        print("1. Put the small sword back")
        print("2. Desecrate the statue")
        print("3. Exit the area\n")

        CryptStatueRoom = input(prompt)

        if CryptStatueRoom == "1":
            print("You put the small sword back.\n")
            small_sword = 0
            Crypt_Statue_Room()
        elif CryptStatueRoom == "2":
            print("After attempting to dismantle the statue you tripped and fell")
            Death("landing on your skull, you explode into tiny bone fragments.", deaths)
        elif CryptStatueRoom == "3":
            print("You left the room.\n")
            Crypt_Start_Area()
        else:
            print("You just stared at the statue.\n")
            Crypt_Statue_Room()

# Crypt Key Room
def Crypt_Key_Room():
    global crypt_key
    if crypt_key == 0:
        print("You see a small stream of water on the ground.")
        print("Taking a closer look you see something shimmer in the water.")
        print("It seems to be a key.\n")
        print("What do you do?")
        print("1. Take the key")
        print("2. Go for a swim")
        print("3. Exit the area\n")

        CryptKeyRoom = input(prompt)

        if CryptKeyRoom == "1":
            print("You carefully grabbed the key")
            print("from the water and fished it out.\n")
            crypt_key = 1
            Crypt_Key_Room()
        elif CryptKeyRoom == "2":
            print("You jump in the water")
            print("but bouyancy is a problem if you are just bones.")
            Death("You then proceed to drown.", deaths)
        elif CryptKeyRoom == "3":
            print("You left the room.\n")
            Crypt_Start_Area()
        else:
            print("You just stared at the flowing water\n")
            Crypt_Key_Room()
    else:
        print("You see a small stream of water on the ground.")
        print("Nothing shimmers in the water.\n")
        print("What do you do?")
        print("1. Try to find something in the water")
        print("2. Go for a swim")
        print("3. Exit the area\n")

        CryptKeyRoom = input(prompt)

        if CryptKeyRoom == "1":
            print("After moving your hand around in the water you found nothing.\n")
            Crypt_Key_Room()
        elif CryptKeyRoom == "2":
            print("You jump in the water")
            print("but bouyancy is a problem if you are just bones.")
            Death("You then proceed to drown.", deaths)
        elif CryptKeyRoom == "3":
            print("You left the room.\n")
            Crypt_Start_Area()
        else:
            print("You just stared at the flowing water.\n")
            Crypt_Key_Room()

# Crypt Gate
def Crypt_Gate():
    global crypt_key
    print("You get closer to the gate.")
    print("There is a lock on the gate.\n")
    print("What do you do?")
    print("1. Open the lock")
    print("2. Use your head")
    print("3. Exit the area\n")

    CryptGate = input(prompt)

    if CryptGate == "1":
        if crypt_key == 1:
            print("You unlock the gate with the key.")
            print("You then proceed to leave the crypt.\n")
        else:
            print("You can't open it normally without a key.\n")
            Crypt_Gate()
    elif CryptGate == "2":
        print("You proceed to bang your skull against the lock to no avail.")
        Death("In desperation you keep banging until your skull falls off.", deaths)
    elif CryptGate == "3":
        print("You left the room.\n")
        Crypt_Start_Area()
    else:
        print("You just stare at the lock.\n")
        Crypt_Gate()


Intro(deaths)
