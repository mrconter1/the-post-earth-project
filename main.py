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

#world_engine.create_resource_route('oxygen', farming_station, habitat)
#world_engine.create_resource_route('calories', farming_station, habitat)

#world_engine.create_resource_route('co2', habitat, farming_station)

#world_engine.create_resource_route('organic_waste', habitat, waste_facility_station)
#world_engine.create_resource_route('nutrients', waste_facility_station, farming_station)

#world_engine.create_resource_route('water', water_mining_station, habitat)
#world_engine.create_resource_route('water', water_mining_station, farming_station)

num_of_days = 35
for day in range(num_of_days):
    print(f"Day {day}:")
    habitat.list_stockpile()
    world_engine.tick()
    print("-" * 20)  # Separator for readability