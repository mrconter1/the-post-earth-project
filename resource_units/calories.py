from resource_entity import ResourceEntity

class Calories(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('Calories', quantity)