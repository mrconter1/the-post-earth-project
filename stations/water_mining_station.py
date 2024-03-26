from models.resource_entity import ResourceEntity

class WaterMiningStation(ResourceEntity):
    def __init__(self):
        super().__init__('WaterMiningStation')

        self.add_to_stockpile("water", 100000000)