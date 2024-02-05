from ship import Destroyer, Cruiser, Battleship, AircraftCarrier

class Fleet:
    '''
    A class to represent a fleet of ships.

    Class Attributes:
        max_size (int): Class attribute to define the maximum size of the fleet. Default is 16.

    Attributes:
        name (str): Name of the fleet.
        ships (dict): Dictionary to store ship instances, with ship names as keys and
                      nested dictionaries containing 'size' and 'coordinates' as values.

    Methods:
        __init__(self, name, *ships): Constructor for Fleet class.
        add_ship(self, ship): Adds a ship instance to the fleet.
        get_fleet_size(self): Returns the current size of the fleet.
    '''

    max_size = 16

    def __init__(self, name, *ships): # '*ships' stands for a variable number of ship instances
        '''
        Initialize a Fleet instance.
        
        Parameters:
            name(str): Name of the fleet.
            *ships (Ship): Variable number of ship instances to be added to the fleet.
        '''

        self.name = name
        self.ships = {}
        for ship in ships:
            self.add_ship(ship)

    def add_ship(self, ship): # Attribute ship is an instance of an Ship object
        '''
        Adds a ship instance to the fleet.

        Parameters:
            ship (Ship): Instance of Ship object to be added to the fleet. 
                         The ship must have 'name' and 'size' attributes. 
        
        Updates:
            self.ships: Updates the ships dictionary with the new ship's name as key
                        and a dictionary containing 'size' and 'coordinates'
                        (initially empty) as value.
        
        Return:
            None        
        '''
        
        self.ships[ship.name] = {'size': ship.size, 'coordinates': []} # Adds instance of Ship object to the fleet where it is called on

    def get_fleet_size(self):
        '''
        Return the current size of the fleet.
        
        Returns:
            int: Number of ships currently in the fleet.
        '''

        return len(self.ships)

    #### TODO update ship instances or fleet instances, not sure what and how yet, when placing ships on grid with coordinates ####

#print(f"The Player's Fleet: {fleet_player.ships}")
#print(f"The Computer's Fleet: {fleet_computer.ships}")