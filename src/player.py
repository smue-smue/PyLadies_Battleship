# Player Setup - handles Player interactions and decisions

from fleet import *
from grid import Grid

class Player():
    '''
    Represents a player in a game, handling player interactions such as name input,
    ship placement, and direction choices.

    Attributes:
    -----------
        name    (str):  The name of the player.

    Methods:
    --------
        prompt_for_player_name(): Static method to prompt the user for their name.
        player_coordinate(self, fleet_player, shipname, attacking=False): Asks the player for coordinates to place their ships or to perform attacks.
        player_direction(self): Asks the player in which direction to place their ships on the grid.
        player_placing_ships(self, fleet_player, board_player): Guides the player through placing all their ships on the game board.
    '''
    def __init__(self, name=None):
        '''
        Initializes a new player instance.

        Parameters:
            name    (str, optional): The name of the player. Defaults to None.

        '''

        self.name = name

    @staticmethod
    def prompt_for_player_name():
        '''
        Static method to prompt the user for their name.
        This method does not require access to the instance (self) or the class (cls).

        Returns:
            str: The name entered by the user.
        '''

        return input("Ready, Player? What's your name?\n")
    
    
    def player_coordinate(self, fleet_player, shipname, attacking=False):
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

            coordinate = input(prompt_message) # TODO: ValueError for inputs like "E" or only "8"
            
            column_label = coordinate[0].upper()
            try:
                row_number = int(coordinate[1:])
                row_key = str(row_number) # Convert row_number back to string for comparison
            except ValueError:
                print("Invalid row number. Please enter a valid coordinate (e.g. 'B1').")
                continue # Ensure the loop continues without attempting to check invalid input

            if column_label in Grid.coordinates_x and row_key in Grid.coordinates_y:
                return coordinate  # Return the coordinate if it's valid
            else:
                print("Invalid coordinate. Please enter a valid coordinate (e.g. 'A1').")
    
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

    def player_placing_ships(self, fleet_player, board_player):
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
                        coordinate = self.player_coordinate(fleet_player, shipname)
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
