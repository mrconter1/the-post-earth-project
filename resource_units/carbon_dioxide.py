from resource_entity import ResourceEntity

class CO2(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('CO2', quantity)
