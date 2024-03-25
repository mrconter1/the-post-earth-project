from resource_container import ResourceContainer
from human import Human 

class HabitatStation(ResourceContainer):
    def __init__(self):
        super().__init__()

        # This habitat hosts 700 people
        for i in range(700):
            self.add_requirement(Human())

        self.add_provision(Space(100))