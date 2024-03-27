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

class FarmingModule(ResourceEntity):
    def __init__(self):
        super().__init__('FarmingModule')

        # Populate the farming module with plants
        self.populate(Plant, 2000)

        # Set max capacity for this module based on consumption and production
        days_for_capacity = 14
        self.set_stock_capacity(days_for_capacity)

        # Start with an initial stock of seven days
        days_to_stock = 7
        self.stock_resources_for_time_period(days_to_stock)

        # Set recycle efficiences for resources
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

        # Farming space station would be 15 x 15 x 15 meters
        self.add_capacity("volume", 15 * 15 * 15)
            
class HumanHabitat(ResourceEntity):
    def __init__(self):
        super().__init__('HumanHabitat')

        # Populate the human habitat with humans
        self.populate(Human, 10)

        # Set max capacity for this module based on consumption and production
        days_for_capacity = 14
        self.set_stock_capacity(days_for_capacity)

        # Start with an initial stock of seven days
        days_to_stock = 7
        self.stock_resources_for_time_period(days_to_stock)

        # Set recycle efficiences for resources
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

        # Habitat space station would be 10 x 10 x 10 meters
        self.add_capacity("volume", 10 * 10 * 10)

# ---------------------------------------------------
# World Simulation Setup
# ---------------------------------------------------

# Initialize the World Engine
world_engine = WorldEngine()

# Creating habitats and modules for the simulation environment
# Initialize Human Habitat
human_habitat = HumanHabitat()

# Initialize Farming Module
farming_module = FarmingModule()

# Add habitats and modules to the world engine
world_engine.add_entities(human_habitat, farming_module)

# Configure resource transfers between entities
# Farming module produces oxygen and calories for human habitat
farming_module.send_resource_up_on_generation(human_habitat, 'oxygen')
farming_module.send_resource_up_on_generation(human_habitat, 'calories')

# Human habitat produces carbon dioxide for farming module
human_habitat.send_resource_up_on_generation(farming_module, 'carbon dioxide')

# ---------------------------------------------------
# Running the Simulation
# ---------------------------------------------------

# Define the duration of the simulation
NUMBER_OF_DAYS = 10

# Start the simulation, iterating over each day
for day in range(1, NUMBER_OF_DAYS + 1):
    print(f"Day {day}: Simulation running...")
    world_engine.tick()  # Advance the simulation by one day
    world_engine.print_resources_table()  # Print current resource status in each habitat/module

print("Simulation completed.")