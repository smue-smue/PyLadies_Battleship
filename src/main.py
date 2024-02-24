import time
from random import randrange
import colorama
from colorama import Fore, Style
from grid import Grid
from fleet import Fleet
from ship import Destroyer, Cruiser, Battleship, AircraftCarrier
from player import Player
from hit_miss import check_hit_or_miss, get_hit_ship, record_hit, get_adjacent_cells

# Setup game

colorama.init(autoreset=True)

def setup_game():
    """
    Initializes the game setup including players, grids, and fleets.

    - Prompts for the human player's name and initializes Player instances for both the human and the computer.
    - Sets up separate Grid instances for the human player, the computer, and the human player's view of the computer's grid.
    - Initializes Fleet instances for both players and populates them with ships.
    - Determines the starting player with a coin flip.

    Returns:
        A collection of game setup components comprising the human player instance, the computer player instance, the human player's grid, the computer's grid, the human player's view of the computer's grid, the human player's fleet, the computer's fleet, and the player who will start the game. Although not explicitly returned as a tuple, Python packages these multiple return values into a tuple automatically.
    """

    # Create player and computer instances
    print("A fleet captain has been invited to the battle against the computer.")
    time.sleep(1)
    player_name = Player.prompt_for_player_name()
    player = Player(player_name)
    computer = Player("Computer")
    time.sleep(1)

    # Initialize grids
    board_player = Grid()
    board_computer = Grid()
    board_computer_players_view = Grid()    
    print("Clearing the seas for an upcoming epic battle.")
    time.sleep(2)

    # Initialize fleets
    fleet_player = Fleet(player_name)
    fleet_computer = Fleet("Computer's Fleet")
    print("Summoning the fleet, captains at the ready - the time for battle is nigh.")
    time.sleep(2)

    # Add ships to fleets
    ship_classes = {
    "Destroyer": Destroyer,
    "Cruiser": Cruiser,
    "Battleship": Battleship,
    "AircraftCarrier": AircraftCarrier
    }

    for name in ["Destroyer", "Cruiser", "Battleship", "AircraftCarrier"]:
        if name == "Destroyer":
            fleet_player.add_ship(Destroyer(f"{name} 1 {player_name}"))
            fleet_player.add_ship(Destroyer(f"{name} 2 {player_name}"))
            fleet_computer.add_ship(Destroyer(f"{name} 1 Computer"))
            fleet_computer.add_ship(Destroyer(f"{name} 2 Computer"))
        else:
            ship_class = ship_classes[name]  # Look up the class constructor
            fleet_player.add_ship(ship_class(f"{name} {player_name}"))
            fleet_computer.add_ship(ship_class(f"{name} Computer"))
    
    time.sleep(1)

    def coin_flip(player, computer):
        '''
        Coin flip to determine who starts.
        '''
        coin = randrange(2)
        if coin == 0:
            beginner = player
        else:
            beginner = computer
        return beginner

    beginner = coin_flip(player, computer)
    print(f"The coin of destiny has been tossed, and the tides have chosen: {beginner.name} shall lead the first assault.")
    time.sleep(2)

    return player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner

# Place ships
def place_ships(player):
    """
    Places the ships for the given player on the given grid.
    
    If the player is a computer, ships are placed randomly.
    If the player is human, prompts for ship placement are displayed.
    """

    print("Captains, to your battle stations! It's time to position your vessels for the impending maritime showdown.")
    if player.name == "Computer":
        player.random_placing_ships(fleet_computer.ships, board_computer)
        print("Computer ships placed randomly.")

    else:
        board_player.print_grid()
        player.player_placing_ships(fleet_player.ships, board_player, board_computer)
        print(f"{player.name}'s ships placed.")

def main_game_loop(player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner):
    """
    The main loop that controls the game flow.
    
    Alternates turns between the player and the computer, allowing each to attack the other's grid.
    Continues until one player's fleet is completely sunk, declaring the other player the winner.
    """

    game_over = False
    # Set the current turn to the beginner
    current_turn = player if beginner == player else computer

    while not game_over:
        if current_turn == player:
            # Pass an empty string for 'shipname'
            coordinate = player.player_coordinate(fleet_player.ships, ' ', board_computer, attacking=True)

            outcome = check_hit_or_miss(coordinate, board_computer)
            print(f"Attack on {coordinate} resulted in a {outcome}.")

            column_index, row_index = board_computer.convert_coordinate_to_indices(coordinate)

            if outcome == 'hit':
                board_computer.grid[row_index][column_index] = 'X'
                board_computer_players_view.grid[row_index][column_index] = 'X'
                hit_ship_name = get_hit_ship(fleet_computer, coordinate)

                if hit_ship_name is not None:
                    record_hit(fleet_computer, hit_ship_name, coordinate)
                    fleet_computer.update_ship_statuses()
                    print(f"{Fore.MAGENTA}*** Hit registered on {hit_ship_name}! ***")

            elif outcome == 'repeat':
                print(f"You've already hit this coordinate. Try another one.")
                continue  # Skip the rest of the loop and let the player choose another coordinate

            else: # Mark the miss on the grid
                board_computer.grid[row_index][column_index] = '~'
                board_computer_players_view.grid[row_index][column_index] = '~'

            print("\nComputer's grid after player's attack:")
            board_computer_players_view.print_grid()
            board_computer.print_grid() # TODO: only for WINNING :D
            # print(fleet_computer) # debugging

            if fleet_computer.update_ship_statuses():
                print(f"{Fore.MAGENTA}{Style.BRIGHT}\nGame Over! {player.name} wins!\n")
                break  # Break out of the loop immediately if the computer's fleet is sunk

            time.sleep(2)

            current_turn = computer  # Switch turn to computer only if the game is not over

        else:
            if computer.hunt_mode and computer.potential_targets:
                # If in hunt mode, choose the next target from the list of potential targets.
                coordinate = computer.potential_targets.pop(0)
            else:
                # Otherwise, select a random coordinate to attack.
                coordinate = player.random_coordinate(board_player.size)

            outcome = check_hit_or_miss(coordinate, board_player)
            print(f"\nComputer attacked {coordinate} and it was a {outcome}.")

            column_index, row_index = board_player.convert_coordinate_to_indices(coordinate)

            if outcome == 'hit':
                board_player.grid[row_index][column_index] = 'X'
                hit_ship_name = get_hit_ship(fleet_player, coordinate)


                if hit_ship_name is not None:
                    record_hit(fleet_player, hit_ship_name, coordinate)
                    fleet_player.update_ship_statuses()
                    print(f"{Fore.CYAN}*** Hit registered on {hit_ship_name}! ***")

                if not computer.hunt_mode:
                    computer.hunt_mode = True
                    computer.last_hit = coordinate
                    computer.potential_targets = get_adjacent_cells(coordinate, board_player.size)
                    print(f"{Fore.CYAN}*** Switching to hunt mode! ***")
            else:
                board_player.grid[row_index][column_index] = '~'
                if not computer.potential_targets:
                    computer.hunt_mode = False
                    computer.last_hit = None

            print("\nPlayer's grid after computer's attack:")
            board_player.print_grid()
            # print(fleet_player) # debugging

            if fleet_player.update_ship_statuses():
                print(f"{Fore.CYAN}{Style.BRIGHT}\nGame Over! {computer.name} wins!\n")
                break  # Break out of the loop immediately if the player's fleet is sunk

            current_turn = player  # Switch turn back to player only if the game is not over
            time.sleep(1)

        if game_over:
            print(f"\nGame Over! {current_turn.name} wins!\n")

# Main execution
if __name__ == "__main__":
    # Setup game
    player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner = setup_game()

    # Place ships for both player and computer
    place_ships(player)
    board_player.print_grid()  # Show player's grid after placing ships

    place_ships(computer)

    main_game_loop(player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner)
