class ResourceEntity:
    def __init__(self, label, quantity=0):
        self.label = label
        self.quantity = quantity  # Used when the entity itself is treated as a resource
        self.requires = {}  # Could be ResourceEntity instances or {label: quantity}
        self.provides = {}  # Similarly, could be ResourceEntity instances or {label: quantity}

    def add_requirement(self, resource_instance):
        # Assuming resource_instance is always a ResourceEntity for simplicity
        if resource_instance.label in self.requires:
            # Aggregate quantities if the resource already exists
            self.requires[resource_instance.label].quantity += resource_instance.quantity
        else:
            self.requires[resource_instance.label] = resource_instance

    def add_provision(self, resource_instance):
        # Similar logic to add_requirement, but for provisions
        if resource_instance.label in self.provides:
            self.provides[resource_instance.label].quantity += resource_instance.quantity
        else:
            self.provides[resource_instance.label] = resource_instance

    def summarize_requirements(self, level=0):
        indent = "  " * level
        print(f"{indent}Requirements for {self.label}:")
        for _, resource in self.requires.items():
            if isinstance(resource, ResourceEntity):
                resource.summarize_requirements(level + 1)
            else:
                print(f"{indent}  {resource.label}: {resource.quantity}")

    def summarize_provisions(self, level=0):
        indent = "  " * level
        print(f"{indent}Provisions by {self.label}:")
        for _, resource in self.provides.items():
            if isinstance(resource, ResourceEntity):
                resource.summarize_provisions(level + 1)
            else:
                print(f"{indent}  {resource.label}: {resource.quantity}")