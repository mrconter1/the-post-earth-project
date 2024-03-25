from resource_entity import ResourceEntity
from human import Human 

class HabitatStation(ResourceEntity):
    def __init__(self):
        super().__init__('HabitatStation')

        # This habitat hosts 700 people
        for i in range(700):
            self.add_requirement(Human())