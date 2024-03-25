from resource import Resource

class Water(Resource):
    def __init__(self, quantity):
        super().__init__('water', quantity)