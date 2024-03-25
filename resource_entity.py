class ResourceEntity:
    def __init__(self, label, quantity=0):
        self.label = label
        self.quantity = quantity  # This represents the quantity when the entity itself is used as a resource
        self.requires = {}  # Resources this entity requires, stored as {label: quantity}
        self.provides = {}  # Resources this entity provides, stored as {label: quantity}

    def add_requirement(self, resource_instance):
        # Extract label and quantity from the resource instance
        resource_label = resource_instance.label
        quantity = resource_instance.quantity
        if resource_label in self.requires:
            self.requires[resource_label] += quantity
        else:
            self.requires[resource_label] = quantity

    def add_provision(self, resource_instance):
        # Extract label and quantity from the resource instance
        resource_label = resource_instance.label
        quantity = resource_instance.quantity
        if resource_label in self.provides:
            self.provides[resource_label] += quantity
        else:
            self.provides[resource_label] = quantity