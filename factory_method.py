from abc import ABC, abstractmethod

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

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def __init__(self, name):
        self.name = name
        self.category = "truck"
    
    def deliver(self):
        result = (f"{self.category} preparado para a entrega: {self.name}",
                  "Transporte térreo...")
        return result


class Ship(Transport):
    def __init__(self, name):
        self.name = name
        self.category = "ship"
    
    def deliver(self):
        result = (f"{self.category} preparado para a entrega: {self.name}",
                  "Transporte marítimo...")
        return result




