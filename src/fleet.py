'''
This module contains a class for fleets and methods for handling the fleets.
Unfortunately it also contains methods for updating ships, which should have 
been done at the ship module.
'''

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Fleet:
    '''
    A class to represent a fleet of ships.

    Class Attributes:
    -----------------
        max_size    (int):  Class attribute to define the maximum size of the fleet. Default is 16.

    Attributes:
    -----------
        name        (str):      Name of the fleet.
        ships       (dict):     Dictionary to store ship instances, with ship names as keys and
                                nested dictionaries containing 'size' and 'coordinates' as values.

    Methods:
    --------
        __init__(self, name, *ships): Constructor for Fleet class.
        __str__(self): Prints fleet readable
        add_ship(self, ship): Adds a ship instance to the fleet.
        get_fleet_size(self): Returns the current size of the fleet.
        update_ship_statuses(self): Updates the status ('active' or 'sunk') of each ship in the 
                                    fleet based on the hits received and returns True if all 
                                    ships are sunk, otherwise False.

    Example:
    --------
        >>> fleet_player = Fleet("Fleet Player", destroyer_1_pl, destroyer_2_pl, cruiser_1_pl, 
                                battleship_1_pl, aircraft_carrier_1_pl)
    '''

    max_size = 16

    def __init__(self, name, *ships): # '*ships' stands for a variable number of ship instances
        '''
        Initialize a Fleet instance.
        
        Parameters:
            name    (str):      Name of the fleet.
            *ships  (Ship):     Variable number of ship instances to be added to the fleet.
        '''

        self.name = name
        self.ships = {}
        for ship in ships:
            self.add_ship(ship)

    def __str__(self):
        '''
        Returns a human-readable string representation of the fleet.

        Returns:
            str: A string representation of the fleet, including the name, size, and hit count
            for each ship in the fleet.

        Example output:
            Fleet 'Fleet Player' with ships:
            Destroyer 1: (Hits: 2, Size: 3)
            Cruiser 1: (Hits: 0, Size: 4)
        '''

        fleet_str = f"Fleet '{self.name}' with ships:\n"
        for ship_name, details in self.ships.items():
            hits = len(details['hits'])
            size = details['size']
            status = details['status']
            fleet_str += f"  {ship_name}: (Hits: {hits}, Size: {size}, Status: {status})\n"
        return fleet_str

    def add_ship(self, ship): # Attribute ship is an instance of an Ship object
        '''
        Adds a Ship instance to the fleet, or updates an existing ship's details.

        Parameters:
            ship    (Ship):     The Ship instance to be added or updated in the fleet.
                                The ship must have 'name' and 'size' attributes. 
        
        Updates:
            self.ships: Updates the ships dictionary with the new ship's name as key
                        and a dictionary containing 'size' and 'coordinates'
                        (initially empty) as value.
        
        Returns:
            None        
        '''

        # === This should have been done via the Ship Class.
        # Refactoring now would mean changes to nearly every bit of code. ===

        # Adds instance of Ship object to the fleet where it is called on
        self.ships[ship.name] = {
            'size': ship.size,
            'coordinates': [],
            'hits': [],
            'status': "active"
            }

    def get_fleet_size(self):
        '''
        Return the current size of the fleet (the number of ships it contains.)
        
        Returns:
            int: Number of ships currently in the fleet.
        '''

        return len(self.ships)

    def update_ship_statuses(self):
        '''
        Updates the status of each ship in the fleet based on the hits it has received.
        Marks a ship as 'sunk' if the number of hits equals or exceeds its size. Prints a
        message for each ship that is newly marked as sunk. Determines if the entire fleet
        is sunk.

        Returns:
            bool: True if all ships in the fleet are sunk, False otherwise.
        '''

        # === This should have been done via the Ship Class. ===

        all_sunk = True
        for ship_name, ship_details in self.ships.items():
            # Determine if the ship is sunk based on hits vs. size
            if len(ship_details['hits']) >= ship_details['size']:
                # Check if this is a new update to the ship's status
                if ship_details['status'] != "sunk":
                    ship_details['status'] = "sunk"
                    print(
                        f"{Fore.RED}{Style.BRIGHT}*** "
                        f"{ship_name} is destroyed! ***{Style.RESET_ALL}")
            else:
                ship_details['status'] = "active"
                all_sunk = False  # If any ship is not sunk, the entire fleet isn't sunk
        return all_sunk  # Indicates if the entire fleet is sunk
