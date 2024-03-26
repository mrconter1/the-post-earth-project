from stations.habitat_station import HabitatStation
from stations.farming_station import FarmingStation
from stations.water_mining_station import WaterMiningStation
from stations.waste_facility_station import WasteFacilityStation

from models.world_engine import WorldEngine

world_engine = WorldEngine()

habitat = HabitatStation()
farming_station = FarmingStation()
water_mining_station = WaterMiningStation()
waste_facility_station = WasteFacilityStation()

world_engine.add_entity(habitat)
world_engine.add_entity(farming_station)
world_engine.add_entity(water_mining_station)
world_engine.add_entity(waste_facility_station)

farming_station.create_resource_route('oxygen', habitat)
farming_station.create_resource_route('calories', habitat)

habitat.create_resource_route('co2', farming_station)

habitat.create_resource_route('organic_waste', waste_facility_station)
farming_station.create_resource_route('organic_waste', waste_facility_station)
waste_facility_station.create_resource_route('nutrients', farming_station)

water_mining_station.create_resource_route('water', habitat)
water_mining_station.create_resource_route('water', farming_station)

num_of_days = 35
for day in range(num_of_days):
    print(f"Day {day}:")
    habitat.list_stockpile()
    world_engine.tick()
    print("-" * 20)  # Separator for readability