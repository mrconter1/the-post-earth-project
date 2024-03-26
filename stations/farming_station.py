from models.resource_entity import ResourceEntity
from entities.aeroponics_plant import AeroponicsPlant

class FarmingStation(ResourceEntity):
    def __init__(self):
        super().__init__('FarmingStation')

        number_of_plants = 500
        for _ in range(number_of_plants):
            self.add_entity(AeroponicsPlant())

        self.add_capacity("volume", 500)