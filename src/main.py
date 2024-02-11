# Entry point for the game
from random import randrange

from grid import Grid
from ship import *
from fleet import Fleet
from player import Player
from computer import place_ships_randomly


# Set up Player
player_name = Player.prompt_for_player_name() # Calls the static method on the class
player = Player(player_name) # Creates a new Player instance with the provided name

# Set up Computer?
computer = Player("Captain Computer")

# Creating ship instances

destroyer_1_pl = Destroyer("Destroyer 1")
destroyer_2_pl = Destroyer("Destroyer 2")
cruiser_1_pl = Cruiser("Cruiser 1")
battleship_1_pl = Battleship("Battleship 1")
aircraft_carrier_1_pl = AircraftCarrier("Aircraft Carrier 1")

destroyer_1_pc = Destroyer("Destroyer 1")
destroyer_2_pc = Destroyer("Destroyer 2")
cruiser_1_pc = Cruiser("Cruiser 1")
battleship_1_pc= Battleship("Battleship 1")
aircraft_carrier_1_pc = AircraftCarrier("Aircraft Carrier 1")

# Creating Fleet instances and adding the ship instances to it
#TODO: Add a Timer, that Player has like 2 Minutes for placing the ships

fleet_player = Fleet("Fleet Player", destroyer_1_pl, destroyer_2_pl, cruiser_1_pl, battleship_1_pl, aircraft_carrier_1_pl)
print(type(fleet_player))
fleet_computer = Fleet("Fleet Computer", destroyer_1_pc, destroyer_2_pc, cruiser_1_pc, battleship_1_pc, aircraft_carrier_1_pc)

# Coin Flip who starts:

coin = randrange(2)

if coin == 0:
    beginner = player
    print(beginner, "starts.")
else:
    beginner = "computer"
    print("Computer starts.")

# Create boards by calling initialize_grid
board_player = Grid()
board_player.print_grid()

board_computer = Grid()
board_computer.print_grid() # TODO: löschen

# Game logic

player.player_placing_ships(fleet_player.ships, board_player) # Parameter: dict ships of the instance fleet_player from the class Fleet
place_ships_randomly(fleet_computer.ships, board_computer)  # Parameter: dict ships of the instance fleet_computer from the class Fleet
board_computer.print_grid() # TODO: löschen, nur zum nachschauen, ob das Grid befüllt wird
