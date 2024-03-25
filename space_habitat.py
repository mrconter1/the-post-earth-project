from resource_container import ResourceContainer
from human import Human 

class Habitat(ResourceContainer):
    def __init__(self):
        super().__init__(
            outputs={
                'living_space': 500
            }
        )

# Create 'Human' instances
human1 = Human()
human2 = Human()

# Create a 'Habitat' instance and add humans
space_habitat = Habitat()
space_habitat.add_container(human1)
space_habitat.add_container(human2)

# Get a summary of total daily resources for the habitat
print(f"Total daily consumption for the habitat: {space_habitat.get_total_consumption()}")
print(f"Total daily production for the habitat: {space_habitat.get_total_production()}")
