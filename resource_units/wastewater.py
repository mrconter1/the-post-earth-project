from resource_entity import ResourceEntity

class Wastewater(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('Wastewater', quantity)