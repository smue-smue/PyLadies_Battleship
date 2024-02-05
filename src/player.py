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

# The Player's Fleet: {'Destroyer 1': {'size': 2, 'coordinates': []}, 'Destroyer 2': {'size': 2, 'coordinates': []}, 'Cruiser 1': {'size': 3, 'coordinates': []}, 'Battleship 1': {'size': 4, 'coordinates': []}, 'Aircraft Carrier 1': {'size': 5, 'coordinates': []}}
# The Computer's Fleet: {'Destroyer 1': {'size': 2, 'coordinates': []}, 'Destroyer 2': {'size': 2, 'coordinates': []}, 'Cruiser 1': {'size': 3, 'coordinates': []}, 'Battleship 1': {'size': 4, 'coordinates': []}, 'Aircraft Carrier 1': {'size': 5, 'coordinates': []}}


        while True:
            for shipname in fleet_player.keys():
                    for key, values in fleet_player[shipname].items():
                            coordinate = input(f"Please enter a coordinate of your {shipname} (total size: {values} squares). ")
                            fleet_player[shipname][key[1]].append(coordinate)
                            # Hier sicherstellen, dass c1 bei c2 etc. anschließt
                    # print grid for overview after each ship
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



