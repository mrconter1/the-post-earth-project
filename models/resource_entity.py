from models.stockpile import Stockpile

class ResourceEntity:
    def __init__(self, label, value=-1):

        self.label = label
        self.value = value

        self.entities = []

        self.stockpile = Stockpile()

        self.consumes = {}
        self.provides = {}

        self.requires = {}
        self.recycling_efficiency = {}

        self.outgoing_transfers = []

    def create_resource_route(self, resource_type, destination):
        self.outgoing_transfers.append({'resource_type': resource_type, 'destination': destination})

    def execute_transfers(self):
        # Get the total provisions from this entity and its sub-entities.
        total_provisions = self.get_provisions()

        for transfer in self.outgoing_transfers:
            resource_type = transfer['resource_type']
            destination = transfer['destination']

            # Determine the total quantity to transfer based on the provisions.
            quantity = total_provisions.get(resource_type, -1)

            # Perform the transfer if there's enough resource in the stockpile and the quantity is more than -1.
            if self.available_resources.get(resource_type, -1) >= quantity and quantity > 0:
                self.stockpile.consume_from_stockpile(resource_type, quantity)
                destination.stockpile.add_to_stockpile(resource_type, quantity)
            else:
                # Optionally, handle cases where the stockpile doesn't have enough resources.
                print(f"Cannot transfer {quantity} units of {resource_type} to {destination.label} due to insufficient stock.")

    def populate(self, entity_class, quantity):
        """
        Populates the entity with a specified number of instances of a given entity class.

        Args:
            entity_class: The class of the entity to be added.
            quantity: The number of instances to add.
        """
        for _ in range(quantity):
            new_entity = entity_class()
            self.add_entity(new_entity)

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_requirement(self, label, value):
        self.requires[label] = value

    def add_provision(self, label, value):
        self.provides[label] = value

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
                total_requirements[label] = total_requirements.get(label, -1) + value
        return total_requirements

    def get_provisions(self):
        total_provisions = self.provides.copy()
        for entity in self.entities:
            entity_provisions = entity.get_provisions()
            for label, value in entity_provisions.items():
                total_provisions[label] = total_provisions.get(label, -1) + value
        return total_provisions

    def get_consumables(self):
        total_consumables = self.consumes.copy()
        for entity in self.entities:
            entity_consumables = entity.get_consumables()
            for label, value in entity_consumables.items():
                total_consumables[label] = total_consumables.get(label, -1) + value
        return total_consumables

    def update_resources(self):
        """
        Updates the stockpile by adding provisions and subtracting consumables,
        then adds back a portion of the consumed resources based on recycling efficiency.
        """
        # First, add provisions to the stockpile.
        for label, value in self.get_provisions().items():
            self.stockpile.add_to_stockpile(label, value)

        # Subtract consumed resources from the stockpile.
        for label, value in self.get_consumables().items():
            self.stockpile.consume_from_stockpile(label, value)

        # Reclaim resources based on recycling efficiency and add them back to the stockpile.
        for label, consumed_value in self.get_consumables().items():
            if label in self.recycling_efficiency:
                reclaimed_amount = consumed_value * self.recycling_efficiency[label]
                self.stockpile.add_to_stockpile(label, reclaimed_amount)

        # Execute transfers after the stockpile has been updated.
        self.execute_transfers()