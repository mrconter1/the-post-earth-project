from resource_container import ResourceContainer
from ResourceUnits import *

class Plant(ResourceContainer):
    def __init__(self):
        super().__init__()

        # Requirements (what a plant needs to grow and produce food)
        self.add_requirement(CO2(0.85))      # Amount of CO2 absorbed by the plant per day, placeholder value
        self.add_requirement(Nutrients(0.02)) # Nutrients needed per day in kilograms, placeholder value
        self.add_requirement(Water(1))       # Water used by the plant per day in liters, placeholder value
        self.add_requirement(Light(1000))    # Light needed per day in some units, placeholder value

        # Provisions (what a plant produces)
        self.add_provision(Oxygen(0.7))      # Amount of O2 produced by the plant, placeholder value
        self.add_provision(OrganicMatter(0.1)) # Edible or usable biomass produced, placeholder value