from resource_container import ResourceContainer

class Human(ResourceContainer):
    def __init__(self):
        super().__init__(
            inputs={'oxygen': 550, 'calories': 2500, 'water': 3.7},
            outputs={'co2': 1, 'organic_waste': 0.5, 'wastewater': 2.5}
        )
