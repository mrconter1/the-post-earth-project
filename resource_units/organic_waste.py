from resource_entity import ResourceEntity

class OrganicWaste(ResourceEntity):
    def __init__(self, quantity):
        super().__init__('OrganicWaste', quantity)