class WorldEngine:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def tick(self):
        total_requirements = {}
        total_provisions = {}

        # Calculate total daily requirements and provisions
        for entity in self.entities:
            entity_requirements = entity.get_requirements()
            for requirement_label, required_quantity in entity_requirements.items():
                if requirement_label not in total_requirements:
                    total_requirements[requirement_label] = required_quantity
                else:
                    total_requirements[requirement_label] += required_quantity

            entity_provisions = entity.get_provisions()
            for provision_label, provision_quantity in entity_provisions.items():
                if provision_label not in total_provisions:
                    total_provisions[provision_label] = provision_quantity
                else:
                    total_provisions[provision_label] += provision_quantity

        # Check if each requirement is met by provisions
        for entity in self.entities:
            entity_requirements = entity.get_requirements()
            entity_provisions = entity.get_provisions()
            for requirement_label, required_quantity in entity_requirements.items():
                if requirement_label in entity_provisions:
                    entity_provisions[requirement_label] -= required_quantity
                    if entity_provisions[requirement_label] < 0:
                        print(f"Warning: Shortage of {requirement_label} in entity {entity.label}")
                        entity_provisions[requirement_label] = 0
                else:
                    print(f"Warning: Shortage of {requirement_label} in entity {entity.label}")

            # Update available resources in the entity
            for provision_label, provision_quantity in entity_provisions.items():
                entity.add_to_stockpile(provision_label, provision_quantity)