from resource_container import ResourceContainer
from ResourceUnits import *

class FarmStation(ResourceContainer):
    def __init__(self):
        super().__init__()

        # This habitat hosts 700 people
        for i in range(700):
            self.add_requirement(Plant())

        self.add_provision(Space(100))

class Plant(ResourceContainer):
    def __init__(self):
        super().__init__()

        # Let's assume these requirements based on a daily cycle for simplicity:
        self.add_requirement(CO2(0.85))           # 0.85 kg of CO2 per day, placeholder value
        self.add_requirement(Fertilizer(0.02))    # 0.02 kg of fertilizer per day, placeholder value
        self.add_requirement(Water(1))            # 1 liter of water per day, placeholder value
        self.add_requirement(Space(1))            # 1 cubic meter of space per plant

        # And these provisions based on the same daily cycle:
        self.add_provision(Oxygen(0.7))           # 0.7 kg of O2 per day, placeholder value
        self.add_provision(Calories(500))         # 500 kilocalories per day, placeholder value