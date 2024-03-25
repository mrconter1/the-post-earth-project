from resource_container import ResourceContainer
from human import Human 

class Habitat(ResourceContainer):
    def __init__(self):
        super().__init__()

        self.add_requirement(Human())

        self.add_provision(Space(100))