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
    # Create player and computer instances
    player_name = Player.prompt_for_player_name()
    player = Player(player_name)
    computer = Player("Computer")

    print(f"Player name: {player.name}") #TODO: löschen, nur für Testzwecke
    print(f"Computer name: {computer.name}") #TODO: löschen, nur für Testzwecke


    # Initialize grids
    board_player = Grid()
    print("Player grid initialized.")
    board_player.print_grid() #TODO: löschen, nur für Testzwecke
    print("Computer grid initialized.")
    board_computer = Grid()
    board_computer.print_grid() #TODO: löschen, nur für Testzwecke
   
    # Initialize fleets
    fleet_player = Fleet(player_name)
    fleet_computer = Fleet("Computer's Fleet")

    print("Player and computer fleets created.")


    # Add ships to fleets
    for name in ["Destroyer", "Cruiser", "Battleship", "AircraftCarrier"]:
        if name == "Destroyer":
            fleet_player.add_ship(Destroyer(f"{name} 1 {player_name}"))
            fleet_player.add_ship(Destroyer(f"{name} 2 {player_name}"))
            fleet_computer.add_ship(Destroyer(f"{name} 1 Computer"))
            fleet_computer.add_ship(Destroyer(f"{name} 2 Computer"))
        else:
            fleet_player.add_ship(eval(f"{name}('{name} {player_name}')"))
            fleet_computer.add_ship(eval(f"{name}('{name} Computer')"))

    print(f"{player.name}'s fleet: {[ship for ship in fleet_player.ships]}") #TODO: löschen, nur für Testzwecke
    print(f"{computer.name}'s fleet: {[ship for ship in fleet_computer.ships]}") #TODO: löschen, nur für Testzwecke
    
    def coin_flip(player, computer):
        '''
        Coin flip to determine who starts.
        '''
        coin = randrange(2)
        print(f"Coinflip was", coin) #TODO: löschen, nur für Testzwecke
        if coin == 0:
            beginner = player
        else:
            beginner = computer       
        return beginner

    beginner = coin_flip(player, computer)
    print(f"The game will start with {beginner.name}.")

    return player, computer, board_player, board_computer, fleet_player, fleet_computer, beginner

# Place ships

def place_ships(player, grid, fleet):
    print(f"Placing ships for {player.name}...")
    if player.name == "Computer":
        place_ships_randomly(fleet_computer.ships, board_computer) 
        print("Computer ships placed randomly.")
        
    else:
        board_player.print_grid()
        player.player_placing_ships(fleet_player.ships, board_player)
        print(f"{player.name}'s ships placed.")

def is_fleet_sunk(fleet, grid):
    for shipname, shipdetails in fleet.items():
        # Check if all coordinates of the ship have been hit
        for coordinate in shipdetails['coordinates']:
            column_index, row_index = grid._convert_coordinate_to_indices(coordinate)
            if grid.grid[row_index][column_index] != 'H':  # If any part of the ship is not hit ('H'), the ship is not sunk
                return False  # Fleet is not sunk
    return True  # All ships in the fleet are sunk


def main_game_loop(player, computer, board_player, board_computer, fleet_player, fleet_computer, beginner):
    
    game_over = False
    current_turn = player if beginner == player else computer  # Set the current turn to the beginner

    while not game_over:
        if current_turn == player:
            print(f"\n{player.name}'s turn")
            
            valid_shipname_for_input = list(fleet_player.ships.keys())[0]
            coordinate = player.player_coordinate(fleet_player.ships, valid_shipname_for_input)

            outcome = check_hit_or_miss(coordinate, board_computer)
            print(f"Attack on {coordinate} resulted in a {outcome}.")

            column_index, row_index = board_computer._convert_coordinate_to_indices(coordinate)
            if outcome == 'hit':
                board_computer.grid[row_index][column_index] = 'H'
            else:
                board_computer.grid[row_index][column_index] = 'M'

            print("Computer's grid after player's attack:")
            board_computer.print_grid()

            if is_fleet_sunk(fleet_computer.ships, board_computer):
                print(f"\nGame Over! {player.name} wins!")
                break  # Break out of the loop immediately if the computer's fleet is sunk

            current_turn = computer  # Switch turn to computer only if the game is not over

        else:
            print(f"\n{computer.name}'s turn")
            coordinate = random_coordinate(board_player.size)
            outcome = check_hit_or_miss(coordinate, board_player)
            print(f"Computer attacked {coordinate} and it was a {outcome}.")

            column_index, row_index = board_player._convert_coordinate_to_indices(coordinate)
            if outcome == 'hit':
                board_player.grid[row_index][column_index] = 'H'
            else:
                board_player.grid[row_index][column_index] = 'M'

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
    player, computer, board_player, board_computer, fleet_player, fleet_computer, beginner = setup_game()

    # Place ships for both player and computer
    place_ships(player, board_player, fleet_player)
    board_player.print_grid()  # Show player's grid after placing ships

    place_ships(computer, board_computer, fleet_computer)
    board_computer.print_grid()  #TODO: löschen, nur für Testzwecke

    main_game_loop(player, computer, board_player, board_computer, fleet_player, fleet_computer, beginner)
