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
