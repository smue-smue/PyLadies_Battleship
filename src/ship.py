class Ship:
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size

class Destroyer(Ship):
    def __init__(self, name):
        super().__init__(name, "Destroyer", 2)

class Cruiser(Ship):
    def __init__(self, name):
        super().__init__(name, "Cruiser", 3)

class Battleship(Ship):
    def __init__(self, name):
        super().__init__(name, "Battleship", 4)

class AircraftCarrier(Ship):
    def __init__(self, name):
        super().__init__(name, "Aircraft Carrier", 5)

