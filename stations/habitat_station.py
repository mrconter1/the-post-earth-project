from models.resource_entity import ResourceEntity
from entities.human import Human 
import math

class HabitatStation(ResourceEntity):
    def __init__(self):
        super().__init__('HabitatStation')

        # This habitat hosts 700 people
        for i in range(700):
            self.add_entity(Human())

        # Add initial stock of resources
        self.add_to_stockpile('oxygen', 550 * 30 * 700)      # 550 liters/day * 30 days * 700 people
        self.add_to_stockpile('water', 3.7 * 30 * 700)       # 3.7 liters/day * 30 days * 700 people
        self.add_to_stockpile('calories', 2500 * 30 * 700)   # 2500 kcal/day * 30 days * 700 people

        # Set recycle efficiences for each resource
        self.set_recycling_efficiency('water', 0.95)  # 95% recycling efficiency
        self.set_recycling_efficiency('oxygen', 0.85)  # 85% recycling efficiency

        self.add_capacity("volume", self.calculate_station_volume())

    def calculate_station_volume(self):
        # Dimensions in meters
        outer_diameter = 263
        inner_diameter = 250
        width = 15

        # Calculate radii
        outer_radius = outer_diameter / 2
        inner_radius = inner_diameter / 2

        # Volume of the cylindrical shell
        volume_outer_cylinder = math.pi * (outer_radius ** 2) * width
        volume_inner_cylinder = math.pi * (inner_radius ** 2) * width

        # Calculate the volume of the ring structure
        volume_ring_structure = volume_outer_cylinder - volume_inner_cylinder

        return volume_ring_structure