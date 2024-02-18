from ship import Destroyer, Cruiser, Battleship, AircraftCarrier
from grid import Grid

class Fleet:
    '''
    A class to represent a fleet of ships.

    Class Attributes:
        max_size    (int):  Class attribute to define the maximum size of the fleet. Default is 16.

    Attributes:
        name        (str):      Name of the fleet.
        ships       (dict):     Dictionary to store ship instances, with ship names as keys and
                                nested dictionaries containing 'size' and 'coordinates' as values.

    Methods:
        __init__(self, name, *ships): Constructor for Fleet class.
        add_ship(self, ship): Adds a ship instance to the fleet.
        get_fleet_size(self): Returns the current size of the fleet.

    Example:
        >>> fleet_player = Fleet("Fleet Player", destroyer_1_pl, destroyer_2_pl, cruiser_1_pl, battleship_1_pl, aircraft_carrier_1_pl)
    '''

    max_size = 16

    def __init__(self, name, *ships): # '*ships' stands for a variable number of ship instances
        '''
        Initialize a Fleet instance.
        
        Parameters:
            name    (str):      Name of the fleet.
            *ships  (Ship):     Variable number of ship instances to be added to the fleet.
        '''

        # TODO: Raise ValueError: If the number of ships provided exceeds the max_size.

        self.name = name
        self.ships = {}
        for ship in ships:
            self.add_ship(ship)

    def add_ship(self, ship): # Attribute ship is an instance of an Ship object
        '''
        Adds a ship instance to the fleet. If a ship with the same name already exists, its details are updated.

        Parameters:
            ship    (Ship):     Instance of Ship object to be added to the fleet. 
                                The ship must have 'name' and 'size' attributes. 
        
        Updates:
            self.ships: Updates the ships dictionary with the new ship's name as key
                        and a dictionary containing 'size' and 'coordinates'
                        (initially empty) as value.
        
        Return:
            None        
        '''

        # TODO: Raises: ValueError: If adding the ship would exceed the fleet's max_size.
        
        self.ships[ship.name] = {'size': ship.size, 'coordinates': [], 'hits': []} # Adds instance of Ship object to the fleet where it is called on

    def get_fleet_size(self):
        '''
        Return the current size of the fleet (the number of ships it contains.)
        
        Returns:
            int: Number of ships currently in the fleet.
        '''

        return len(self.ships)
    

        





