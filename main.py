from stations.habitat_station import HabitatStation
from stations.farming_station import FarmingStation
from stations.water_mining_station import WaterMiningStation
from stations.waste_facility_station import WasteFacilityStation

from models.world_engine import WorldEngine

def generate_habitat_station_instance():

    # Create the habitat station instance
    habitat = HabitatStation()

    # Adding monthly requirements for 700 people
    habitat.add_to_stockpile('oxygen', 550 * 30 * 700)      # 550 liters/day * 30 days * 700 people
    habitat.add_to_stockpile('water', 3.7 * 30 * 700)       # 3.7 liters/day * 30 days * 700 people
    habitat.add_to_stockpile('calories', 2500 * 30 * 700)   # 2500 kcal/day * 30 days * 700 people

    return habitat

world_engine = WorldEngine()

habitat = generate_habitat_station_instance()
farming_station = FarmingStation()
water_mining_station = WaterMiningStation()
waste_facility_station = WasteFacilityStation()

world_engine.add_entity(habitat)
world_engine.add_entity(farming_station)
world_engine.add_entity(water_mining_station)
world_engine.add_entity(waste_facility_station)

#world_engine.create_resource_route('oxygen', farm_station, habitat)
#world_engine.create_resource_route('calories', farm_station, habitat)

#world_engine.create_resource_route('co2', habitat, farm_station)

num_of_days = 35
for day in range(num_of_days):
    print(f"Day {day}:")
    habitat.list_stockpile()
    world_engine.tick()
    print("-" * 20)  # Separator for readability