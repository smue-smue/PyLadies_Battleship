# Player Setup - handles Player interactions and decisions

import random
from fleet import *
from grid import Grid

class Player():
    '''
    Represents a player in a game, handling ship placements for human and computer players.

    Attributes:
    -----------
        name    (str):  The name of the player.

    Methods:
    --------
        prompt_for_player_name()
        player_coordinate(self, fleet_player, shipname, attacking=False)
        player_direction(self)
        player_placing_ships(self, fleet_player, board_player)
        random_coordinate(self, grid_size)
        random_direction(self)
        random_placing_ships(self, fleet, grid)

    '''
    def __init__(self, name=None):
        '''
        Initializes a new player instance.

        Parameters:
            name    (str, optional): The name of the player. Defaults to None.

        '''

        self.name = name
        self.hunt_mode = False  # Indicates whether the computer is in hunt mode
        self.last_hit = None  # Stores the last hit coordinate
        self.potential_targets = []  # Stores potential targets for the next move in hunt mode

    @staticmethod
    def prompt_for_player_name():
        '''
        Static method to prompt the user for their name.
        This method does not require access to the instance (self) or the class (cls).

        Returns:
            str: The name entered by the user.
        '''

        return input("Ready, Player? What's your name?\n")
    
    
    def player_coordinate(self, fleet_player, shipname, grid_instance, attacking=False):
        '''
        Asks the player for coordinates to place their ships or to perform attacks.

        Parameters:
            fleet_player    (dict): The player's fleet, containing ship names and properties.
            shipname        (str):  The name of the ship to place.
            attacking       (bool): Flag indicating whether the player is attacking.

        Returns:
            str: The valid coordinate entered by the player.

        Notes:
            This method loops until a valid coordinate is input by the user. It checks for
            valid row and column inputs based on predefined grid coordinates.
        '''

        while True: # Use a loop to keep asking until a valid input is received
            if attacking:
                prompt_message = "It's your turn for the attack, please enter the coordinate: "
            else:
                prompt_message = f"Please enter a start coordinate of your {shipname} (total size: {fleet_player[shipname]['size']} squares): "

            coordinate = input(prompt_message).strip().upper()
            
            if len(coordinate) <2:
                print("Invalid input. please enter a valid coordinate (e.g. 'B1').")
                continue

            # Check if the attack is valid within the grid bounds
            if not grid_instance.is_valid_attack(coordinate):
                print("Coordinate is out of grid bounds. Please try again.")
                continue

            return coordinate

            # coordinate_upper = coordinate[0].upper()
            # row_part = coordinate[1:]

            # try:
            #     row_number = int(row_part)
            #     row_key = str(row_number) # Convert row_number back to string for comparison
            #     if coordinate_upper in Grid.coordinates_x and row_key in Grid.coordinates_y:
            #         return coordinate_upper + row_key
            #     else:
            #         print("Invalid input. please enter a valid coordinate (e.g. 'B1').")
            # except ValueError:
            #     print("Invalid row number. Please enter a valid coordinate (e.g. 'B1').")
    
    def player_direction(self):
        '''
        Asks the player in which direction to place their ships on the grid.

        Returns:
            str: The direction ('H' for horizontal or 'V' for vertical) for ship placement.

        Notes:
            This method loops until a valid direction is input by the user.
        '''

        while True:  # Use a loop to keep asking until a valid input is received
            direction = input("Please enter the direction (H for horizontal, V for vertical). ").upper()  # Convert to upper case
            if direction in ['H', 'V']:
                return direction  # Return the direction if it's valid
            else:
                print("Invalid input. Please enter 'H' for horizontal or 'V' for vertical.")  # Notify the user and ask again

            return direction

    def player_placing_ships(self, fleet_player, board_player, board_computer):
        '''
        Guides the player through placing all their ships on the game board.

        Parameters:
            fleet_player (dict): The player's fleet, containing ship names and properties.
            board_player (Board): The game board on which ships will be placed.

        Notes:
            This method iterates over each ship in the player's fleet, prompting for
            placement until all ships are validly placed. It checks for valid placements
            and updates the game board accordingly.
        '''

        while True:
            all_ships_processed = True # Assume all ships are processed until proven otherwise
            
            for shipname in fleet_player.keys():
                if not fleet_player[shipname]['coordinates']: # Check if ship lacks coordinates
                    while True:
                        coordinate = self.player_coordinate(fleet_player, shipname, board_computer)
                        direction = self.player_direction()

                        # Check if the placement is valid before attempting to update the grid
                        if board_player.is_valid_placement(coordinate, direction, fleet_player[shipname]['size']):
                            if board_player.update_grid_fleet(coordinate, direction, fleet_player, fleet_player[shipname]['size'], shipname): # update_grid_fleet returns True
                                # print(fleet_player)
                                board_player.print_grid()
                                break # Valid placement, break out of the inner loop.
                        else:
                            print("Invalid ship placement, please try again.")

                    all_ships_processed = False # A ship was processed, so not all were done
                    break # Break after processing each ship to recheck the condition

            if all_ships_processed:
                break # Exit the while loop if all ships have been processed

    def random_coordinate(self, grid_size):
        '''
        Generates a random coordinate within the specified grid size.

        Parameters:
            grid_size   (int): The size of the grid (number of rows/columns).

        Returns:
            str: A string representing a random coordinate within the grid, 
                combining a column letter and a row number.
        '''

        column_label = random.choice('ABCDEFGHIJKLMNOPQRST'[0:grid_size])
        row_number = str(random.randint(1, grid_size))
        return column_label + row_number
    
    def random_direction(self):
        '''
        Selects a random direction.

        Returns:
            str: A single character 'H' or 'V', representing horizontal or
                vertical direction, respectively.
        '''

        return random.choice(['H', 'V'])
    
    def random_placing_ships(self, fleet, grid):
        '''
        Places each ship in the fleet at a random location on the grid.

        This function iterates through all ships in the fleet and attempts to place them
        randomly on the grid. It repeats the process for a ship until a valid placement
        is found.

        Parameters:
            fleet   (dict):     A dictionary representing the fleet, with ship names as keys
                                and ship details (including size) as values.
            grid    (object):   An object representing the game grid.

        Notes:
            The function does not return a value but updates the `fleet` and
            `grid` objects directly to reflect the placement of ships.
        '''

        for shipname, shipdetails in fleet.items():
            placed = False
            while not placed:
                start_coordinate = self.random_coordinate(grid.size)
                direction = self.random_direction()

                # Check if the placement is valid before attempting to update the grid
                if grid.is_valid_placement(start_coordinate, direction, shipdetails['size']):
                    if grid.update_grid_fleet(start_coordinate, direction, fleet, shipdetails['size'], shipname, show_errors=False):
                        placed = True  # Ship placed successfully