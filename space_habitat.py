from resource_container import ResourceContainer
from human import Human 

class Habitat(ResourceContainer):
    def __init__(self):
        super().__init__(
            provides ={
                'living_area': 500
            }
        )

# Create 'Human' instances
human1 = Human()
human2 = Human()

# Create a 'Habitat' instance and add humans
space_habitat = Habitat()
space_habitat.add_container(human1)
space_habitat.add_container(human2)
