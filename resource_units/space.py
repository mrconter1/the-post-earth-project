from resource_entity import ResourceEntity

class Space(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('Space', quantity)