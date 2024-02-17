from random import randrange
from grid import Grid
from fleet import Fleet
from ship import Destroyer, Cruiser, Battleship, AircraftCarrier
from player import Player
from computer import place_ships_randomly
from computer import random_coordinate
from hit_miss import check_hit_or_miss

# Setup game

def setup_game():
    """
    Initializes the game by setting up players, grids, and fleets.
    
    - Prompts for the player's name and creates Player instances for the human player and the computer.
    - Initializes grids for both players.
    - Creates fleets for both players and adds ships to them.
    - Determines who will start the game by a coin flip.
    
    Returns:
        Tuple containing player, computer, player's board, computer's board, player's fleet, computer's fleet, and the beginner.
    """
     
    # Create player and computer instances
    player_name = Player.prompt_for_player_name()
    player = Player(player_name)
    computer = Player("Computer")

    print(f"Player name: {player.name}") #TODO: löschen, nur für Testzwecke
    print(f"Computer name: {computer.name}") #TODO: löschen, nur für Testzwecke


    # Initialize grids
    board_player = Grid()
    print("Player grid initialized.")
    print("Computer grid initialized.")
    board_computer = Grid()
    board_computer_players_view = Grid()

    # Initialize fleets
    fleet_player = Fleet(player_name)
    fleet_computer = Fleet("Computer's Fleet")

    print("Player and computer fleets created.")

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
    print(f"The game will start with {beginner.name}.")

    return player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner

# Place ships
def place_ships(player):
    """
    Places the ships for the given player on the given grid.
    
    If the player is a computer, ships are placed randomly.
    If the player is human, prompts for ship placement are displayed.
    """

    print(f"Placing ships for {player.name}...")
    if player.name == "Computer":
        place_ships_randomly(fleet_computer.ships, board_computer) 
        print("Computer ships placed randomly.")
        
    else:
        board_player.print_grid()
        player.player_placing_ships(fleet_player.ships, board_player)
        print(f"{player.name}'s ships placed.")

def is_fleet_sunk(fleet, grid):
    """
    Checks if all ships in a fleet are sunk.
    
    Returns:
        True if all ships are sunk, False otherwise.
    """
    
    # for shipname, shipdetails in fleet.items(): # TODO: Testing new one
    for shipdetails in fleet.values():
        # Check if all coordinates of the ship have been hit
        for coordinate in shipdetails['coordinates']:
            column_index, row_index = grid._convert_coordinate_to_indices(coordinate)
            if grid.grid[row_index][column_index] != 'X':  # If any part of the ship is not hit ('X'), the ship is not sunk
                return False  # Fleet is not sunk
    return True  # All ships in the fleet are sunk


def main_game_loop(player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner, record_hit):
    """
    The main loop that controls the game flow.
    
    Alternates turns between the player and the computer, allowing each to attack the other's grid.
    Continues until one player's fleet is completely sunk, declaring the other player the winner.
    """

    game_over = False
    current_turn = player if beginner == player else computer  # Set the current turn to the beginner

    while not game_over:
        if current_turn == player:
                        
            coordinate = player.player_coordinate(fleet_player.ships, '', attacking=True)  # Pass an empty string for 'shipname'

            outcome = check_hit_or_miss(coordinate, board_computer)
            print(f"Attack on {coordinate} resulted in a {outcome}.")

            column_index, row_index = board_computer._convert_coordinate_to_indices(coordinate)
            if outcome == 'hit':
                board_computer.grid[row_index][column_index] = 'X'
                board_computer_players_view.grid[row_index][column_index] = 'X'
                record_hit(self, fleet, shipname, coordinate, grid) #TODO: einbauen, dass wenn Hit, dann wird es in der fleet beim ship aufgezeichnet
            else:
                board_computer.grid[row_index][column_index] = '~'
                board_computer_players_view.grid[row_index][column_index] = '~'

            print("Computer's grid after player's attack:")
            board_computer_players_view.print_grid()

            if is_fleet_sunk(fleet_computer.ships, board_computer):
                print(f"\nGame Over! {player.name} wins!")
                break  # Break out of the loop immediately if the computer's fleet is sunk

            current_turn = computer  # Switch turn to computer only if the game is not over

        else:
            coordinate = random_coordinate(board_player.size)
            outcome = check_hit_or_miss(coordinate, board_player)
            print(f"Computer attacked {coordinate} and it was a {outcome}.")

            column_index, row_index = board_player._convert_coordinate_to_indices(coordinate)
            if outcome == 'hit':
                board_player.grid[row_index][column_index] = 'X'
            else:
                board_player.grid[row_index][column_index] = '~'

            print("Player's grid after computer's attack:")
            board_player.print_grid()

            if is_fleet_sunk(fleet_player.ships, board_player):
                print(f"\nGame Over! {computer.name} wins!")
                break  # Break out of the loop immediately if the player's fleet is sunk

            current_turn = player  # Switch turn back to player only if the game is not over

        if game_over:
            print(f"\nGame Over! {current_turn.name} wins!")


# Main execution
if __name__ == "__main__":
    # Setup game
    player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner = setup_game()

    # Place ships for both player and computer
    place_ships(player)
    board_player.print_grid()  # Show player's grid after placing ships

    place_ships(computer)

    main_game_loop(player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner)
