class ResourceContainer:
    def __init__(self, requires=None, provides=None):
        self.requires = requires or {}
        self.provides = provides or {}
        self.containers = []

    def add_container(self, container):
        if isinstance(container, ResourceContainer):
            self.containers.append(container)
        else:
            raise ValueError("Container must be an instance of ResourceContainer.")

    def require_resource(self, resource, amount):
        self.requires[resource] = self.requires.get(resource, 0) + amount

    def provide_resource(self, resource, amount):
        self.provides[resource] = self.provides.get(resource, 0) + amount

    def get_total_requirements(self):
        total_requirements = self.requires.copy()
        for container in self.containers:
            for resource, amount in container.get_total_requirements().items():
                total_requirements[resource] = total_requirements.get(resource, 0) + amount
        return total_requirements

    def get_total_provisions(self):
        total_provisions = self.provides.copy()
        for container in self.containers:
            for resource, amount in container.get_total_provisions().items():
                total_provisions[resource] = total_provisions.get(resource, 0) + amount
        return total_provisions