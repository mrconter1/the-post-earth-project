from resource_entity import ResourceEntity

from resource_units.space import Space
from human import Human 

class HabitatStation(ResourceEntity):
    def __init__(self):
        super().__init__('HabitatStation')

        # This habitat hosts 700 people
        for i in range(700):
            self.add_requirement(Human())

        self.add_requirement(Space(self.calculate_station_volume()))

    def calculate_station_volume(self):
        return 100