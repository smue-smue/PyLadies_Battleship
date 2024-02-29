'''
This module is the entry point for the battleship-style game.

Example:
    Run this module directly to start the game:
        python main.py
'''

from game_setup import setup_game
from game_loop import main_game_loop

def main():
    '''
    Initiates and executes the main game setup and loop for the Battleship game.

    The function starts by setting up the game environment which includes initializing the players 
    (human and computer), game boards for both players, and the fleets of ships. 
    
    It then displays the human player's grid with the placed ships.

    After the setup, it enters the main game loop where it alternates turns between the human player 
    and the computer, allowing each to attack the other's fleet. 
    The game continues in this loop until one of the fleets is completely sunk.

    Returns:
        None. The function controls the game flow and exits once the game concludes.
    '''
    (
        player,
        computer,
        board_player,
        board_computer,
        board_computer_players_view,
        fleet_player,
        fleet_computer,
        beginner
    ) = setup_game()

    board_player.print_grid()  # Show player's grid after placing ships

    main_game_loop(
        player,
        computer,
        board_player,
        board_computer,
        board_computer_players_view,
        fleet_player,
        fleet_computer,
        beginner
        )

if __name__ == "__main__":
    main()
