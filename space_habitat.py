from resource_container import ResourceContainer
from human import Human 

class Habitat(ResourceContainer):
    pass

# Create 'Human' instances
human1 = Human()
human2 = Human()

# Create a 'Habitat' instance and add humans
space_habitat = Habitat()
space_habitat.add_container(human1)
space_habitat.add_container(human2)

# Create a nested container if needed
nested_habitat = Habitat()
nested_habitat.add_container(space_habitat)  

# Get a summary of total daily resources for the habitat
print(f"Total daily consumption for the habitat: {nested_habitat.get_total_consumption()}")
print(f"Total daily production for the habitat: {nested_habitat.get_total_production()}")
