class ResourceEntity:
    def __init__(self, label, quantity=0):
        self.label = label
        self.quantity = quantity  # Used when the entity itself is treated as a resource
        self.requires = []
        self.provides = []

    def add_requirement(self, resource_instance):
        self.requires.append(resource_instance)

    def add_provision(self, resource_instance):
        self.provides.append(resource_instance)

    def get_requirements(self):
        # Base case: if the instance represents a fundamental entity with a set quantity
        if self.quantity > 0 or not self.requires:
            return [self]
        else:
            # Recursive case: for composite entities, get the requirements of each
            all_requirements = []
            for required_entity in self.requires:
                all_requirements.extend(required_entity.get_requirements())
            return all_requirements