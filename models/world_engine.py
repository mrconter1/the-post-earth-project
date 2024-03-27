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