class ResourceEntity:
    def __init__(self, label, value=0):

        self.label = label
        self.value = value

        self.entities = []

        self.consumes = {}
        self.provides = {}
        self.available_resources = {}

        self.requires = {}
        self.capacities = {}  
        self.recycling_efficiency = {}

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_requirement(self, label, value):
        self.requires[label] = value

    def add_capacity(self, label, value):
        if label in self.capacities:
            self.capacities[label] += value  # Update existing capacity value
        else:
            self.capacities[label] = value  # Add new capacity

    def add_provision(self, label, value):
        self.provides[label] = value

    def add_to_stockpile(self, label, value):
        if label in self.available_resources:
            self.available_resources[label] += value
        else:
            self.available_resources[label] = value

    def consume_from_stockpile(self, label, value):
        if label in self.available_resources and self.available_resources[label] >= value:
            self.available_resources[label] -= value
        elif label not in self.available_resources:
            print(f"The resource {label} is not available in the stockpile.")
        else:
            print(f"Not enough of the resource {label} available to consume.")

    def set_recycling_efficiency(self, resource_label, efficiency):
        """
        Sets the recycling efficiency for a given resource.
        """
        self.recycling_efficiency[resource_label] = efficiency

    def get_requirements(self):
        total_requirements = self.requires.copy()
        for entity in self.entities:
            entity_requirements = entity.get_requirements()
            for label, value in entity_requirements.items():
                total_requirements[label] = total_requirements.get(label, 0) + value
        return total_requirements

    def get_provisions(self):
        total_provisions = self.provides.copy()
        for entity in self.entities:
            entity_provisions = entity.get_provisions()
            for label, value in entity_provisions.items():
                total_provisions[label] = total_provisions.get(label, 0) + value
        return total_provisions

    def get_consumables(self):
        total_consumables = self.consumes.copy()
        for entity in self.entities:
            entity_consumables = entity.get_consumables()
            for label, value in entity_consumables.items():
                total_consumables[label] = total_consumables.get(label, 0) + value
        return total_consumables

    def check_capacities(self):
        """
        Checks if the entity's capacities are sufficient to meet its requirements.
        """
        for label, required in self.get_requirements().items():
            if label in self.capacities and self.capacities[label] < required:
                print(f"Insufficient {label} capacity. Required: {required}, Available: {self.capacities[label]}")
                return False
        return True

    def update_resources(self):
        """
        Updates the stockpile by adding provisions and subtracting consumables,
        then adds back a portion of the consumed resources based on recycling efficiency.
        """
        if not self.check_capacities():
            print("Cannot update resources due to insufficient capacities.")
            return

        # First, add provisions to the stockpile.
        for label, value in self.get_provisions().items():
            self.add_to_stockpile(label, value)

        # Subtract consumed resources from the stockpile.
        for label, value in self.get_consumables().items():
            self.consume_from_stockpile(label, value)

        # Reclaim resources based on recycling efficiency and add them back to the stockpile.
        for label, consumed_value in self.get_consumables().items():
            if label in self.recycling_efficiency:
                reclaimed_amount = consumed_value * self.recycling_efficiency[label]
                self.add_to_stockpile(label, reclaimed_amount)

    def list_stockpile(self):
        print(f"Stockpile for {self.label}:")
        if not self.available_resources:
            print("  No resources in the stockpile.")
            return
        longest_label_length = max(len(label) for label in self.available_resources.keys())
        for label, value in sorted(self.available_resources.items()):
            value_as_int = int(value)
            print(f"  {label.rjust(longest_label_length)}: {value_as_int} units")