from resource_entity import ResourceEntity

class Oxygen(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('Oxygen', quantity)
