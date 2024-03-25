class ResourceContainer:
    def __init__(self, inputs=None, outputs=None):
        self.inputs = inputs or {}
        self.outputs = outputs or {}
        self.containers = []

    def add_container(self, container):
        if isinstance(container, ResourceContainer):
            self.containers.append(container)
        else:
            raise ValueError("Container must be an instance of ResourceContainer.")

    def add_resource_consumption(self, resource, amount):
        self.inputs[resource] = self.inputs.get(resource, 0) + amount

    def add_resource_production(self, resource, amount):
        self.outputs[resource] = self.outputs.get(resource, 0) + amount

    def get_total_consumption(self):
        total_consumption = self.inputs.copy()
        for container in self.containers:
            for resource, amount in container.get_total_consumption().items():
                total_consumption[resource] = total_consumption.get(resource, 0) + amount
        return total_consumption

    def get_total_production(self):
        total_production = self.outputs.copy()
        for container in self.containers:
            for resource, amount in container.get_total_production().items():
                total_production[resource] = total_production.get(resource, 0) + amount
        return total_production