# Player Setup

from fleet import *

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

    @staticmethod
    def player_placing_ships(fleet_player):
        '''This function asks the player where to place their ships.'''

        while True:
            all_ships_processed = True # Assume all ships are processed until proven otherwise
            for shipname in fleet_player.keys():
                if not fleet_player[shipname]['coordinates']: # Check if ship lacks coordinates
                    coordinate = input(f"Please enter a start coordinate of your {shipname} (total size: {fleet_player[shipname]['size']} squares). ")
                    fleet_player[shipname]['coordinates'].append(coordinate)
                    all_ships_processed = False # A ship was processed, so not all were done
                    break # Break after processing each ship to check the condition again

                # Hier sicherstellen, dass c1 bei c2 etc. anschließt
                # print grid for overview after each ship
            if all_ships_processed:
                break # Exit the while loop if all ships have been processed

        print(fleet_player)
            #return fleet



    # def position_ships(create_grid, coordinates_x, coordinates_y, choice): # needs to be redone!
    #     '''This function places the players ships on the grid.'''
    #     coord_1 = coordinates_x[choice[0]]
    #     coord_2 = coordinates_y[choice[1]]
    #     create_grid[coord_2][coord_1] = "X"
    #     updated_grid = create_grid
    #     return updated_grid

    #################################



