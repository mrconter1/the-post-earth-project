class WorldEngine:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_entities(self, *entities):
        """
        Adds multiple entities to the world. Entities can be passed as separate arguments.
        """
        for entity in entities:
            self.add_entity(entity)
        return self

    def tick(self):
        # Update resources for each entity
        for entity in self.entities:
            entity.update_resources()

        # After updating all entities, check for negative stockpile values
        for entity in self.entities:
            for resource_label, quantity in entity.available_resources.items():
                if quantity < 0:
                    print(f"Warning: Negative stockpile of {resource_label} in entity {entity.label}. Adjusting...")

    def print_resources_table(self):
        # Collect all unique resources from all entities
        all_resources = set()
        for entity in self.entities:
            all_resources.update(entity.available_resources.keys())

        # Start with the header row
        table = "Resource".ljust(20) + "".join(entity.label.ljust(20) for entity in self.entities) + "\n"

        # For each resource, create a row
        for resource in sorted(all_resources):
            row = resource.ljust(20)  # Resource name
            for entity in self.entities:
                # Add resource amount or "-" if the entity doesn't have it
                row += str(entity.available_resources.get(resource, "-")).ljust(20)
            table += row + "\n"

        print(table)