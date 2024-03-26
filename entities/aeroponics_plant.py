from models.resource_entity import ResourceEntity

class AeroponicsPlant(ResourceEntity):
    def __init__(self):
        super().__init__('AeroponicsPlant')

        # Consumption (what a plant needs to grow)
        self.consumes['water'] = 0.75           # Average 0.75 liters of water per day per plant
        self.consumes['nutrients'] = 0.0001875  # Average of 187.5 mg per plant per day
        self.consumes['co2'] = 34               # Average of 34 liters of CO2 needed per day

        # Requirements (what a plant needs to survive)
        self.requires['volume'] = 0.5           # Average 0.5 cubic meters of space per plant

        # Provisions (what a plant produces)
        self.provides['oxygen'] = 28            # Approx. 28 liters of oxygen per day
        self.provides['calories'] = 14          # Approx. 14 calories/day from various plant types.
        self.provides['water'] = 0.5            # Approx. 0.5 liters of water released through transpiration per day
        self.provides['organic_waste'] = 0.0125 # Approx. 12.5 g of organic waste in the form of non-edible plant parts