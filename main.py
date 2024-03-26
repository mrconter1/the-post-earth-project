from habitat_station import HabitatStation
from world_engine import WorldEngine

def generate_habitat_station_instance():

    # Create the habitat station instance
    habitat = HabitatStation()

    # Adding monthly requirements for 700 people

    # Oxygen: 550 liters/day * 30 days * 700 people
    habitat.add_to_stockpile('oxygen', 550 * 30 * 700)

    # Water: 3.7 liters/day * 30 days * 700 people
    habitat.add_to_stockpile('water', 3.7 * 30 * 700)

    # Calories: 2500 kcal/day * 30 days * 700 people
    habitat.add_to_stockpile('calories', 2500 * 30 * 700)

    return habitat

world_engine = WorldEngine()

habitat = generate_habitat_station_instance()
world_engine.add_entity(habitat)

world_engine.tick()