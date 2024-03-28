from models.resource_entity import ResourceEntity
from models.world_engine import WorldEngine

class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __repr__(self):
        return f"{self.amount} {self.unit}"

class Plant(ResourceEntity):
    def __init__(self):
        super().__init__('Plant')

        # Consumption (what a plant needs to grow per day)
        self.consumes = {
            'water': Quantity(0.75, 'L'),               # Average 0.75 liters of water per day per plant
            'co2': Quantity(34, 'L'),                   # Average of 34 liters of CO2 needed per day
        }

        # Requirements (what a plant needs to have)
        self.requires = {
            'volume': Quantity(0.5, 'm^3'),             # Average 0.5 cubic meters of space per plant
        }

        # Provisions (what a plant produces per day)
        self.provides = {
            'protein': Quantity(0.01, 'g'),             # Average 0.01 g of proteins per day
            'carbohydrates': Quantity(0.04, 'g'),       # Average 0.04 g of carbohydrates per day
            'fats': Quantity(0.002, 'g'),               # Average 0.002 g of fats per day
            'oxygen': Quantity(28, 'L'),                # Approx. 28 liters of oxygen per day
        }

class Human(ResourceEntity):
    def __init__(self):
        super().__init__('Human')

        # Consumption (what a human needs to consume)
        self.consumes = {
            'protein': Quantity(0.8, 'kg'),                     # 0.8 kg of proteins
            'carbohydrates': Quantity(1.3, 'kg'),               # 1.3 kg of carbohydrates
            'fats': Quantity(0.7, 'kg'),                        # 0.7 kg of fats
            'water': Quantity(3.7, 'L'),                        # 3.7 liters of water
            'oxygen': Quantity(550, 'L'),                       # 550 liters of oxygen
        }

        # Requirements (what a human needs to have)
        self.requires = {
            'volume': Quantity(100, 'm^3'),                     # 100 cubic meters of living space
        }

        # Provisions (what a human produces as waste)
        self.provides = {
            'co2': Quantity(1, 'kg'),                           # Produces 1 kg of CO2
        }

class FarmingModule(ResourceEntity):
    def __init__(self):
        super().__init__('FarmingModule')

        # Populate the farming module with plants
        self.populate(Plant, 2000)

        self.define_max_volume(Quantity(15 * 15 * 15, 'm^3'))
        self.define_max_mass(Quantity(100, 'ton'))

        # Start with an initial stock of seven days
        self.stock_for_N_time_steps(7)

        # Set recycle efficiences for resources
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency
            
class HumanHabitat(ResourceEntity):
    def __init__(self):
        super().__init__('HumanHabitat')

        # Populate the human habitat with humans
        self.populate(Human, 10)

        self.define_max_volume(Quantity(10 * 10 * 10, 'm^3'))
        self.define_max_mass(Quantity(200, 'ton'))

        # Start with an initial stock of seven days
        self.stock_for_N_time_steps(7)

        # Set recycle efficiences for resources
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

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
human_habitat.send_resource_up_on_generation(farming_module, 'co2')

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