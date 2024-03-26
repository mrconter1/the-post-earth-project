from models.resource_entity import ResourceEntity

class Human(ResourceEntity):
    def __init__(self):
        super().__init__('Human')

        # Consumption (what a human needs to consume)
        self.consumes['oxygen'] = 550           # 550 liters of oxygen
        self.consumes['water'] = 3.7            # 3.7 liters of water
        self.consumes['calories'] = 2500        # 2500 kcal

        # Requirements (what a human needs to survive)
        self.requires['volume'] = 100           # 100 cubic meters of living space

        # Provisions (what a human produces as waste)
        self.provides['co2'] = 1                # produces 1 kg of CO2
        self.provides['organic_waste'] = 0.5    # produces 0.5 kg of organic waste
        self.provides['wastewater'] = 2.5       # produces 2.5 liters of wastewater