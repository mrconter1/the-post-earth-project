from resource import Resource

class Oxygen(Resource):
    def __init__(self, quantity):
        super().__init__('oxygen', quantity)