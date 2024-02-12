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
    

    def player_coordinate(self, fleet_player, shipname):
        '''
        Asks the player where to place their ships.
        '''

        coordinate = input(f"Please enter a start coordinate of your {shipname} (total size: {fleet_player[shipname]['size']} squares). ") # TODO: ValueError for inputs like "E" or only "8"
        
        return coordinate
    
    def player_direction(self):
        '''
        Asks the player in which direction to place their ships.
        '''

        direction = input("Please enter the direction (H for horizontal, V for vertical). ")
        
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
                        while direction not in ['H', 'V']:
                            print("Invalid input. Please enter 'H' for horizontal or 'V' for vertical. ")
                            direction = input("Please enter the direction (H for horizontal, V for vertical). ")

                        if board_player.update_grid_fleet(coordinate, direction, fleet_player, fleet_player[shipname]['size'], shipname): # update_grid_fleet returns True
                            print(fleet_player)
                            board_player.print_grid()
                            break
                        else:
                            print("Invalid ship placement, please try again.")

                    all_ships_processed = False # A ship was processed, so not all were done
                    break # Break after processing each ship to recheck the condition

            if all_ships_processed:
                break # Exit the while loop if all ships have been processed 
