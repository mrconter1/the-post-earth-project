from models.resource_entity import ResourceEntity

class AeroponicsPlant(ResourceEntity):
    def __init__(self):
        super().__init__('AeroponicsPlant')

        # Requirements (what a plant needs to grow)
        self.requires['water'] = 0.75           # Average 0.75 liters of water per day per plant
        self.requires['nutrients'] = 0.0001875  # Average of 187.5 mg per plant per day
        self.requires['co2'] = 34               # Average of 34 liters of CO2 needed per day
        self.requires['volume'] = 0.1           # Average 0.1 cubic meters of space per plant

        # Provisions (what a plant produces)
        self.provides['oxygen'] = 0.04          # Approx. 0.04 kg of oxygen per day per square meter of plant area
        self.provides['calories'] = 14          # Approx. 14 calories/day from various plant types.
        self.provides['water'] = 0.5            # Approx. 0.5 liters of water released through transpiration per day