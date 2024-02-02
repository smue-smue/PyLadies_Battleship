# Entry point for the game

import grid

# Player Setup
player1 = input("Ready, Player? What's your name?\n")
player2 = "Computer-Player"

# Coin Flip who starts:
from random import randrange
coin = randrange(2)

if coin == 0:
    beginner = player1
    print(beginner, "starts.")
else:
    beginner = player2
    print(beginner, "starts.")

# Create a grid by calling initialize_grid
create_grid = grid.initialize_grid()


print(grid.print_grid(create_grid))