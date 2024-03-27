from models.resource_entity import ResourceEntity
from models.world_engine import WorldEngine

class Plant(ResourceEntity):
    def __init__(self):
        super().__init__('Plant')

        # Consumption (what a plant needs to grow)
        self.consumes['water'] = 0.75           # Average 0.75 liters of water per day per plant
        self.consumes['co2'] = 34               # Average of 34 liters of CO2 needed per day

        # Requirements (what a plant needs to have)
        self.requires['volume'] = 0.5           # Average 0.5 cubic meters of space per plant

        # Provisions (what a plant produces)
        self.provides['oxygen'] = 28            # Approx. 28 liters of oxygen per day
        self.provides['calories'] = 14          # Approx. 14 calories/day from various plant types.
        self.provides['water'] = 0.5            # Approx. 0.5 liters of water released through transpiration per day

        # Start with an initial stock of seven days
        days_to_stock = 7
        self.stock_resources_for_time_period(days_to_stock)

        # Set recycle efficiences for resources
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

        # Farming space station would be 50 x 50 x 50 meters
        self.add_capacity("volume", 50 * 50 * 50)

class Human(ResourceEntity):
    def __init__(self):
        super().__init__('Human')

        # Consumption (what a human needs to consume)
        self.consumes['oxygen'] = 550           # 550 liters of oxygen
        self.consumes['water'] = 3.7            # 3.7 liters of water
        self.consumes['calories'] = 2500        # 2500 kcal

        # Requirements (what a human needs to have)
        self.requires['volume'] = 100           # 100 cubic meters of living space

        # Provisions (what a human produces as waste)
        self.provides['co2'] = 1                # produces 1 kg of CO2
        self.provides['wastewater'] = 2.5       # produces 2.5 liters of wastewater

        # Start with an initial stock of seven days
        days_to_stock = 7
        self.stock_resources_for_time_period(days_to_stock)

        # Set recycle efficiences for resources
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

        # Habitat space station would be 10 x 10 x 10 meters
        self.add_capacity("volume", 10 * 10 * 10 )

class FarmingModule(ResourceEntity):
    def __init__(self):
        super().__init__('FarmingModule')

        # This habitat hosts 10 people
        for i in range(10):
            self.add_entity(Plant())
            
class HumanHabitat(ResourceEntity):
    def __init__(self):
        super().__init__('HumanHabitat')

        # This habitat hosts 10 people
        for i in range(10):
            self.add_entity(Human())

world_engine = WorldEngine()

human_habitat = HumanHabitat()
farming_module = FarmingModule()

world_engine.add_entity(human_habitat)
world_engine.add_entity(farming_module)
        
farming_module.create_resource_route('oxygen', human_habitat)
farming_module.create_resource_route('calories', human_habitat)

human_habitat.create_resource_route('co2', farming_module)