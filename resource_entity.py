class ResourceEntity:
    def __init__(self, label, quantity=0):
        self.label = label
        self.quantity = quantity  # Used when the entity itself is treated as a resource
        self.requires = []
        self.provides = []
        self.available_resources = []  # Stockpile of ResourceEntity instances

    def add_requirement(self, resource_instance):
        self.requires.append(resource_instance)

    def add_provision(self, resource_instance):
        self.provides.append(resource_instance)

    def add_to_stockpile(self, resource_instance):
        # Adds resources to the stockpile
        for available_resource in self.available_resources:
            if available_resource.label == resource_instance.label:
                available_resource.quantity += resource_instance.quantity
                break
        else:  # If the resource is not found in the stockpile, add it
            self.available_resources.append(resource_instance)

    def consume_from_stockpile(self, resource_instance):
        # Consumes resources from the stockpile
        for available_resource in self.available_resources:
            if available_resource.label == resource_instance.label and available_resource.quantity >= resource_instance.quantity:
                available_resource.quantity -= resource_instance.quantity
                break
        else:
            print(f"Not enough {resource_instance.label} available to consume.")

    def gather_requirements(self):
        # Base case: if the instance represents a fundamental entity with a set quantity
        if self.quantity > 0 or not self.requires:
            return [self]
        else:
            # Recursive case: for composite entities, get the requirements of each
            all_requirements = []
            for required_entity in self.requires:
                all_requirements.extend(required_entity.get_requirements())
            return all_requirements

    def get_requirements(self):
        all_requirements = self.gather_requirements()
        consolidated = {}
        # Consolidate requirements by summing quantities for each label
        for requirement in all_requirements:
            if requirement.label in consolidated:
                consolidated[requirement.label].quantity += requirement.quantity
            else:
                consolidated[requirement.label] = ResourceEntity(requirement.label, requirement.quantity)
        return list(consolidated.values())
