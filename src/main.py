# Entry point for the game

import grid
from random import randrange

#### TEMPORARY PLACE ####
def ship_destroyer(coordinate_1, coordinate_2):
    return(coordinate_1, coordinate_2)


def player_ships():
    '''This function asks the player where to place their ships.'''

    fleet = {
            2: {"1st destroyer": [], "2nd destroyer": []},
            3: {"Cruiser": []},
            4: {"Battleship": []},
            5: {"Aircraft Carrier": []}
            }
 
    while True:
        for shipsize in fleet.keys():
                for shiptype in fleet[shipsize].keys():
                    for coordinate in range(shipsize):
                        coordinate = input(f"Please enter a coordinate of your {shiptype} (total size: {shipsize} squares). ")
                        fleet[shipsize][shiptype].append(coordinate)
                        # Hier sicherstellen, dass c1 bei c2 etc. anschließt
                # print grid for overview after each ship
        print(fleet)
        return fleet


# def position_ships(create_grid, coordinates_x, coordinates_y, choice): # needs to be redone!
#     '''This function places the players ships on the grid.'''
#     coord_1 = coordinates_x[choice[0]]
#     coord_2 = coordinates_y[choice[1]]
#     create_grid[coord_2][coord_1] = "X"
#     updated_grid = create_grid
#     return updated_grid

#################################

# Player Setup
player1 = input("Ready, Player? What's your name?\n")
player2 = "Computer-Player"

# Coin Flip who starts:

coin = randrange(2)

if coin == 0:
    beginner = player1
    print(beginner, "starts.")
else:
    beginner = player2
    print(beginner, "starts.")

# Create a grid by calling initialize_grid
create_grid = grid.initialize_grid()
grid.print_grid(create_grid)

# Game logic

choice = player_ships()
#updated_grid = position_ships(create_grid, grid.coordinates_x, grid.coordinates_y, choice)

#grid.print_grid(updated_grid)