class ResourceContainer:
    def __init__(self):
        self.requires = {}
        self.provides = {}

    def add_requirement(self, resource, quantity):
        if resource in self.requires:
            self.requires[resource] += quantity
        else:
            self.requires[resource] = quantity

    def add_provision(self, resource, quantity):
        if resource in self.provides:
            self.provides[resource] += quantity
        else:
            self.provides[resource] = quantity

    def get_requirements(self):
        return self.requires

    def get_provisions(self):
        return self.provides