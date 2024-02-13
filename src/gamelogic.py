from grid import Grid
from player import Player
from fleet import Fleet
from ship import Destroyer, Cruiser, Battleship, AircraftCarrier 
from hit_miss import check_hit_or_miss

def initialize_game(player_name):
    """
    Initializes the game by setting up grids for the player and the computer,
    creating player and computer instances, and optionally placing ships on the grid.

    Parameters:
    - player_name (str): The name of the human player.

    Returns:
    - player (Player): The human player object.
    - computer (Player): The computer player object.
    - player_grid (Grid): The human player's grid.
    - computer_grid (Grid): The computer's grid.
    - fleet_player (Fleet): The fleet for the human player.
    - fleet_computer (Fleet): The fleet for the computer.
    """
    player_grid = Grid()  # Default size is used
    computer_grid = Grid()

    player = Player(player_name)
    computer = Player("Computer")

    # Initialize fleets using consistent variable names
    fleet_player = Fleet(f"{player.name}'s Fleet")
    fleet_computer = Fleet(f"{computer.name}'s Fleet")

    # Further initialization like placing ships can be added here

    return player, computer, player_grid, computer_grid, fleet_player, fleet_computer

def player_turn(player_grid):
    """
    Handles the player's turn in the game.

    Parameters:
    - player_grid (Grid): The grid for the human player.

    Returns:
    - coordinate (str): The coordinate entered by the player.
    """
    # Example: Ask the player for a coordinate
    coordinate = input("Enter a coordinate to attack: ")
    return coordinate

def computer_turn(computer_grid):
    """
    Handles the computer's turn in the game.

    Parameters:
    - computer_grid (Grid): The grid for the computer.

    Returns:
    - coordinate (str): The coordinate chosen by the computer.
    """
    # Example: Choose a random coordinate
    coordinate = "A1"  # Replace with actual logic
    return coordinate

def check_game_over(fleet_player, fleet_computer):
    """
    Checks if the game is over by determining if one of the fleets has no remaining ships.

    Parameters:
    - fleet_player (Fleet): The fleet for the human player.
    - fleet_computer (Fleet): The fleet for the computer.

    Returns:
    - bool: True if the game is over, False otherwise.
    """
    if fleet_player.is_defeated() or fleet_computer.is_defeated():
        return True
    else:
        return False

