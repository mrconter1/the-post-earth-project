class ResourceEntity:
    def __init__(self, label, value=0):
        self.label = label
        self.value = value # Used when the entity itself is treated as a resource
        self.entities = []
        self.requires = {}
        self.provides = {}
        self.available_resources = {} 

    def add_entity(self, entity):
        self.entities.append(entity)

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

    def get_requirements(self):
        if self.value > 0: # If this is a fundamental resource
            return {self.label: self.value}
        else: # If this is a composed resource, get requirements from all entities
            total_requirements = self.requires.copy() # Start with own requirements
            for entity in self.entities:
                entity_requirements = entity.get_requirements()
                for label, value in entity_requirements.items():
                    if label in total_requirements:
                        total_requirements[label] += value
                    else:
                        total_requirements[label] = value
            return total_requirements