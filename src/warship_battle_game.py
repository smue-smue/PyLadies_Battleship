'''
This module is the entry point for a battleship-style game. It orchestrates the game setup, 
ship placement, and execution of the main game loop.

Functions:
    setup_game:     Initializes the game, setting up players, grids, and fleets, and decides 
                    who starts the game.
    place_ships:    Handles the placement of ships on the grid for both the human player 
                    and the computer.
    main_game_loop: Runs the main loop of the game where players take turns to attack each 
                    other's fleet.

The game starts by setting up the players, ships, and boards. 
It then allows the human player and computer to place their ships. 
Once the setup is complete, the main game loop begins, processing turns until the game concludes.

Example:
    Run this module directly to start the game:
        python warship_battle_game.py
'''

# Main execution

from game_loop import setup_game, place_ships, main_game_loop

if __name__ == "__main__":
    # Setup game
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

    # Place ships for both player and computer
    place_ships(player, fleet_player, board_player, board_computer_players_view)
    board_player.print_grid()  # Show player's grid after placing ships

    place_ships(computer, fleet_computer, board_computer)

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
