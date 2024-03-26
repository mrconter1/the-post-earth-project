from models.resource_entity import ResourceEntity

class WasteFacilityStation(ResourceEntity):
    def __init__(self):
        super().__init__('WasteFacilityStation')

        self.consumes['organic_waste'] = 0.5 * 700

        self.provides['nutrients'] = self.consumes['organic_waste'] * 0.008

        self.add_capacity("volume", 500)