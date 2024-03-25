from resource import Resource

class Wastewater(Resource):
    def __init__(self, quantity):
        super().__init__('wastewater', quantity)