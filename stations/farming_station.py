from models.resource_entity import ResourceEntity
from entities.aeroponics_plant import AeroponicsPlant

class FarmingStation(ResourceEntity):
    def __init__(self):
        super().__init__('FarmingStation')

        number_of_plants = 250000
        for _ in range(number_of_plants):
            self.add_entity(AeroponicsPlant())

        # Start with an initial stock of seven days
        days_to_stock = 7
        self.stock_resources_for_time_period(days_to_stock)

        # Set recycle efficiences for each resource
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

        # Farming space station would be 50 x 50 x 50 meters
        self.add_capacity("volume", 50 * 50 * 50)