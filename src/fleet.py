from ship import Destroyer, Cruiser, Battleship, AircraftCarrier

class Fleet:
    max_size = 16 # Class attribute
    def __init__(self, name, *ships): # '*ships' stands for a variable number of ship instances
        self.name = name
        self.ships = {}
        for ship in ships:
            self.add_ship(ship)

    def add_ship(self, ship): # Attribute ship is an instance of an Ship object
        self.ships[ship.name] = {'size': ship.size, 'coordinates': []} # Adds instance of Ship object to the fleet where it is called on

    def get_fleet_size(self):
        pass

    #### TODO update ship instances or fleet instances, not sure what and how yet, when placing ships on grid with coordinates ####

# Creating ship instances

destroyer_1_pl = Destroyer("Destroyer 1")
destroyer_2_pl = Destroyer("Destroyer 2")
cruiser_1_pl = Cruiser("Cruiser 1")
battleship_1_pl = Battleship("Battleship 1")
aircraft_carrier_1_pl = AircraftCarrier("Aircraft Carrier 1")

destroyer_1_pc = Destroyer("Destroyer 1")
destroyer_2_pc = Destroyer("Destroyer 2")
cruiser_1_pc = Cruiser("Cruiser 1")
battleship_1_pc= Battleship("Battleship 1")
aircraft_carrier_1_pc = AircraftCarrier("Aircraft Carrier 1")

# Creating Fleet instances and adding the ship instances to it

fleet_player = Fleet("Fleet Player", destroyer_1_pl, destroyer_2_pl, cruiser_1_pl, battleship_1_pl, aircraft_carrier_1_pl)
fleet_computer = Fleet("Fleet Computer", destroyer_1_pc, destroyer_2_pc, cruiser_1_pc, battleship_1_pc, aircraft_carrier_1_pc)

# print(f"The Player's Fleet: {fleet_player.ships}")
# print(f"The Computer's Fleet: {fleet_computer.ships}")