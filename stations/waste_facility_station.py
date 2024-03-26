from models.resource_entity import ResourceEntity

class WasteFacilityStation(ResourceEntity):
    def __init__(self):
        super().__init__('WasteFacilityStation')

        self.consumes['organic_waste'] = 500

        self.provides['nutrients'] = 500

        self.add_capacity("volume", 500)