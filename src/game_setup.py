'''
This module orchestrates the setup and execution of a battleship-style game.
It includes functions for initializing players, grids, fleets, and the game itself,
as well as determining the starting player with a coin flip.

Functions:
    initialize_players: Set up player instances for the game.
    initialize_grids: Prepare the game grids for both players.
    initialize_fleets: Create and populate fleets with ships for both players.
    populate_fleets: Add ships to the players' fleets.
    coin_flip: Randomly decide which player starts the game.
    setup_game: Conduct the complete setup of the game before starting the main loop.
'''
import time
from random import randrange
import colorama
from colorama import Fore, Style
from grid import Grid
from fleet import Fleet
from ship import Destroyer, Cruiser, Battleship, AircraftCarrier
from player import Player

colorama.init(autoreset=True)

def initialize_players():
    '''
    Create player instances for the game, one for the human player based on input name
    and one for the computer with a default name.

    Returns:
        tuple: Two Player instances for the human and the computer.
    '''

    print(f"{Fore.GREEN}\nA fleet captain has been invited to the battle against the computer.")
    time.sleep(2)
    player_name = Player.prompt_for_player_name()
    player = Player(player_name)
    computer = Player("Computer")
    time.sleep(2)
    return player, computer

def initialize_grids():
    '''
    Initialize game grids for the player and the computer, including a view for the player
    to track shots against the computer's fleet.

    Returns:
        tuple: Three Grid instances for the player, computer, and player's view.
    '''

    board_player = Grid()
    board_computer = Grid()
    board_computer_players_view = Grid()
    print(f"{Fore.GREEN}Clearing the seas for an upcoming epic battle.")
    time.sleep(2)
    return board_player, board_computer, board_computer_players_view

def initialize_fleets(player_name):
    '''
    Create fleets for the human player and the computer, and invoke the ship placement function.

    Arguments:
        player_name (str): The name of the human player to label their fleet.

    Returns:
        tuple: Two Fleet instances for the human player and the computer.
    '''

    fleet_player = Fleet(player_name)
    fleet_computer = Fleet("Computer's Fleet")
    print(f"{Fore.GREEN}Summoning the fleet, captains at the ready - the time for battle is nigh.")
    time.sleep(2)
    populate_fleets(fleet_player, fleet_computer, player_name)
    return fleet_player, fleet_computer

def populate_fleets(fleet_player, fleet_computer, player_name):
    '''
    Add ships to both the human player's and the computer's fleets.

    Arguments:
        fleet_player (Fleet): The human player's fleet to add ships to.
        fleet_computer (Fleet): The computer's fleet to add ships to.
        player_name (str): The name of the human player for naming ships.

    Returns:
        None
    '''
    ship_classes = {
        "Destroyer": Destroyer,
        "Cruiser": Cruiser,
        "Battleship": Battleship,
        "AircraftCarrier": AircraftCarrier
    }

    for name in ship_classes:
        if name == "Destroyer":
            fleet_player.add_ship(Destroyer(f"{name} 1 {player_name}"))
            fleet_player.add_ship(Destroyer(f"{name} 2 {player_name}"))
            fleet_computer.add_ship(Destroyer(f"{name} 1 Computer"))
            fleet_computer.add_ship(Destroyer(f"{name} 2 Computer"))
        else:
            ship_class = ship_classes[name]
            fleet_player.add_ship(ship_class(f"{name} {player_name}"))
            fleet_computer.add_ship(ship_class(f"{name} Computer"))
    time.sleep(2)

def coin_flip(player, computer):
    '''
    Perform a coin flip to determine who will start the game.

    Arguments:
        player (Player): The human player's instance.
        computer (Player): The computer player's instance.

    Returns:
        Player: The instance of the player who will begin the game.
    '''
    coin = randrange(2)
    if coin == 0:
        beginner = player
    else:
        beginner = computer
    return beginner

def setup_game():
    '''
    Conduct the complete setup of the game, including player initialization,
    grid setup, fleet creation, and deciding the starting player.

    Returns:
        tuple: Collection of all game-related instances needed to start the game loop.
    '''
    player, computer = initialize_players()
    board_player, board_computer, board_computer_players_view = initialize_grids()
    fleet_player, fleet_computer = initialize_fleets(player.name)
    beginner = coin_flip(player, computer)
    print(
        f"{Fore.GREEN}The coin of destiny has been tossed, "
        f"{Fore.GREEN}and the tides have chosen: {Style.BRIGHT}{beginner.name}{Style.RESET_ALL} "
        f"{Fore.GREEN}shall lead the first assault."
        )
    time.sleep(2)

    return (
        player,
        computer,
        board_player,
        board_computer,
        board_computer_players_view,
        fleet_player,
        fleet_computer,
        beginner
    )

def place_ships(player, fleet, board, opponent_board=None):
    """
    Places the ships for the given player on the given grid.
    
    If the player is a computer, ships are placed randomly.
    If the player is human, prompts for ship placement are displayed.
    """

    print(f"{Fore.GREEN}Captains, to your battle stations! "
          f"{Fore.GREEN}It's time to position your vessels for the impending maritime showdown.")
    if player.name == "Computer":
        player.random_placing_ships(fleet.ships, board)
        print("Computer ships placed randomly.")

    else:
        board.print_grid()
        player.player_placing_ships(fleet.ships, board, opponent_board)
        print(f"{player.name}'s ships placed.")
