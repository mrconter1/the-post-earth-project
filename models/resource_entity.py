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

    def get_provisions(self):
        if self.value > 0: # If this is a fundamental resource
            return {self.label: self.value}
        else: # If this is a composed resource, get provisions from all entities
            total_provisions = self.provides.copy() # Start with own provisions
            for entity in self.entities:
                entity_provisions = entity.get_provisions()
                for label, value in entity_provisions.items():
                    if label in total_provisions:
                        total_provisions[label] += value
                    else:
                        total_provisions[label] = value
            return total_provisions

    def list_stockpile(self):
        # Improved method to list all resources in the stockpile with better formatting
        print(f"Stockpile for {self.label}:")

        if not self.available_resources:
            print("  No resources in the stockpile.")
            return

        # Calculate the length of the longest label for alignment
        longest_label_length = max(len(label) for label in self.available_resources.keys())

        for label, value in sorted(self.available_resources.items()):
            # Right-align the labels and format the value with proper units
            print(f"  {label.rjust(longest_label_length)}: {value} units")

    def update_resources(self):
        """
        Adjusts the entity's stockpile by adding provisions and then consuming resources
        for one operational cycle. Allows resource values to temporarily go negative,
        anticipating future adjustments within the cycle.
        """
        # Add provisions to the stockpile
        for label, value in self.get_provisions().items():
            self.add_to_stockpile(label, value)

        # Subtract required resources, permitting negative values
        for label, value in self.get_requirements().items():
            self.available_resources[label] = self.available_resources.get(label, 0) - value
