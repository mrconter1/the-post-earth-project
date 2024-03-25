from resource_entity import ResourceEntity

class Water(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('Water', quantity)