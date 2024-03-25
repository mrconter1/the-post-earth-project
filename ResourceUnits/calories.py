from resource import Resource

class Calories(Resource):
    def __init__(self, quantity):
        super().__init__('calories', quantity)