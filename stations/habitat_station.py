from models.resource_entity import ResourceEntity
from entities.human import Human 
import math

class HabitatStation(ResourceEntity):
    def __init__(self):
        super().__init__('HabitatStation')

        # This habitat hosts 700 people
        for i in range(700):
            self.add_entity(Human())

        # Start with an initial stock of seven days
        days_to_stock = 7
        self.stock_resources_for_time_period(days_to_stock)

        # Set recycle efficiences for each resource
        self.set_recycling_efficiency('water', 0.92)  # 92% recycling efficiency

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