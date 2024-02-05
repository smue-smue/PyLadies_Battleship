# Entry point for the game
from random import randrange

import grid
import fleet
from player import Player

# Set up Player
player_name = Player.prompt_for_player_name() # Calls the static method on the class
player = Player(player_name) # Creates a new Player instance with the provided name

# Set up Computer?

# Coin Flip who starts:

coin = randrange(2)

if coin == 0:
    beginner = player
    print(beginner, "starts.")
else:
    #beginner = computer
    #print(computer, "starts.")

# Create a grid by calling initialize_grid
create_grid = grid.initialize_grid()
grid.print_grid(create_grid)

# Game logic

#choice = player_ships() # old
#updated_grid = position_ships(create_grid, grid.coordinates_x, grid.coordinates_y, choice)

#grid.print_grid(updated_grid)