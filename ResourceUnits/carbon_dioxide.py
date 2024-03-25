from resource import Resource

class CO2(Resource):
    def __init__(self, quantity):
        super().__init__('co2', quantity)