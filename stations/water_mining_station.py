from models.resource_entity import ResourceEntity

class HabitatStation(ResourceEntity):
    def __init__(self):
        super().__init__('WaterMiningStation')

        self.add_provision("water", 50)