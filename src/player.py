# Player Setup - handles Player interactions and decisions

from fleet import *
from grid import Grid

class Player():
    '''

    '''
    def __init__(self, name=None):
         self.name = name

    @staticmethod
    def prompt_for_player_name():
        '''
        Static method to prompt the user for their name.
        This method does not require access to the instance (self)
        or the class (cls).

        Returns:
            str: The name entered by the user.
        '''

        return input("Ready, Player? What's your name?\n")
    
    
    def player_coordinate(self, fleet_player, shipname, attacking=False):
        '''
        Asks the player where to place their ships.
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
        Asks the player in which direction to place their ships.
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
        Asks the player where to place their ships. Repeats for invalid placements.
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
