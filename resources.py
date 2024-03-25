from resource_container import ResourceContainer

class Resource(ResourceContainer):
    def __init__(self, label, quantity):
        super().__init__()
        self.label = label
        self.quantity = quantity  
        self.add_requirement(self.label, self.quantity)
        self.add_provision(self.label, self.quantity)