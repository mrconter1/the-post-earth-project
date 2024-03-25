from habitat_station import HabitatStation

habitat = HabitatStation()

l = habitat.get_requirements()

for r in l:
    print(r.label)
    print(r.quantity)
    print()