from resource_entity import ResourceEntity

class Human(ResourceEntity):
    def __init__(self):
        super().__init__('Human')

        # Requirements (what a human needs to survive)
        self.requires['oxygen'] = 550       # 550 liters of oxygen
        self.requires['water'] = 3.7        # 3.7 liters of water
        self.requires['calories'] = 2500    # 2500 kcal
        self.requires['space'] = 100        # 100 cubic meters of living space

        # Provisions (what a human produces as waste)
        self.provides['co2'] = 1            # produces 1 kg of CO2
        self.provides['organic_waste'] = 0.5  # produces 0.5 kg of organic waste
        self.provides['wastewater'] = 2.5   # produces 2.5 liters of wastewater