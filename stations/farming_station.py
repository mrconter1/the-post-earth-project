from models.resource_entity import ResourceEntity
from entities.aeroponics_plant import AeroponicsPlant

class FarmingStation(ResourceEntity):
    def __init__(self):
        super().__init__('FarmingStation')

        number_of_plants = 500
        for _ in range(number_of_plants):
            self.add_entity(AeroponicsPlant())

        # Set recycle efficiences for each resource
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

        self.add_capacity("volume", 500)