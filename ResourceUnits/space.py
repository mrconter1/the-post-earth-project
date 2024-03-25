from resource import Resource

class Space(Resource):
    def __init__(self, quantity):
        super().__init__('space', quantity)