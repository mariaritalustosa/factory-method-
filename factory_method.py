class Logistics:
    def createTransport(self):
        pass

    def planDelivery(self):
        pass

class RoadLogistics(Logistics):
    def __init__(self, name):
        self.name = name

    def createTransport(self):
        return Truck(self.name)

class SeaLogistics(Logistics):
    def __init__(self, name):
        self.name = name

    def createTransport(self):
        return Ship(self.name)