from resource_container import ResourceContainer
from ResourceUnits import *

class Human(ResourceContainer):
    def __init__(self):
        super().__init__()

        # Requirements (what a human needs to survive)
        self.add_requirement(Oxygen(550))      # 550 liters of oxygen per day
        self.add_requirement(Calories(2500))   # 2500 kcal per day
        self.add_requirement(Water(3.7))       # 3.7 liters of water per day
        self.add_requirement(Space(100))       # 100 cubic meters of living space

        # Provisions (what a human produces as waste)
        self.add_provision(CO2(1))             # produces 1 kg of CO2 per day
        self.add_provision(OrganicWaste(0.5))  # produces 0.5 kg of organic waste per day
        self.add_provision(Wastewater(2.5))    # produces 2.5 liters of wastewater per day