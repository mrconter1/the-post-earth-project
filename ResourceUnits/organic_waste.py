from resource import Resource

class OrganicWaste(Resource):
    def __init__(self, quantity):
        super().__init__('organic waste', quantity)