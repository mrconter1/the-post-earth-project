from resource_entity import ResourceEntity

from resource_units.oxygen import Oxygen
from resource_units.carbon_dioxide import CO2

class Human(ResourceEntity):
    def __init__(self):
        super().__init__('Human')

        # Requirements (what a human needs to survive)
        self.add_requirement(Oxygen(550))      # 550 liters of oxygen per day

        # Provisions (what a human produces as waste)
        self.add_provision(CO2(1))             # Produces 1 kg of CO2 per day
