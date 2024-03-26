class ResourceEntity:
    def __init__(self, label, value=0):
        self.label = label
        self.value = value # Used when the entity itself is treated as a resource
        self.requires = {}
        self.provides = {}
        self.available_resources = {} # Stockpile of ResourceEntity instances

    def add_requirement(self, label, value):
        self.requires[label] = value

    def add_provision(self, label, value):
        self.provides[label] = value

    def add_to_stockpile(self, label, value):
        # Adds resources to the stockpile
        if label in self.available_resources:
            self.available_resources[label] += value  # Increment resource count by value
        else:  # If the resource is not found in the stockpile, add it
            self.available_resources[label] = value  # Initialize the resource with given value

    def consume_from_stockpile(self, label, value):
        # Consumes resources from the stockpile
        if label in self.available_resources and self.available_resources[label] >= value:
            self.available_resources[label] -= value  # Decrement resource count by value
        elif label not in self.available_resources:
            print(f"The resource {label} is not available in the stockpile.")
        else:
            print(f"Not enough of the resource {label} available to consume.")

    def gather_requirements(self):
        # Base case: if the instance represents a fundamental entity with a set quantity
        if self.value > 0 or not self.requires:
            return {self.label, self.value}
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
