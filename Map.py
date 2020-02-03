class area(object):

    def enter(self):
        print("Empty")
        exit(1)

class Map(object):

    rooms = {
        'intro': Intro()
    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)
