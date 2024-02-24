'''
This module holds the main loop that controls the game flow.
    
Alternates turns between the player and the computer, allowing each to attack the other's grid.
Continues until one player's fleet is completely sunk, declaring the other player the winner.
'''

import time
import colorama
from colorama import Fore, Style
from hit_miss import check_hit_or_miss, get_hit_ship, record_hit, get_adjacent_cells

colorama.init(autoreset=True)

def main_game_loop(
        player,
        computer,
        board_player,
        board_computer,
        board_computer_players_view,
        fleet_player,
        fleet_computer,
        beginner
):

    game_over = False
    # Set the current turn to the beginner
    current_turn = player if beginner == player else computer

    while not game_over:
        if current_turn == player:
            # Pass an empty string for 'shipname'
            coordinate = player.player_coordinate(
                fleet_player.ships,
                ' ', 
                board_computer,
                attacking=True
            )

            outcome = check_hit_or_miss(coordinate, board_computer)
            print(f"Attack on {coordinate} resulted in a {outcome}.")

            column_index, row_index = board_computer.convert_coordinate_to_indices(coordinate)

            if outcome == 'hit':
                board_computer.grid[row_index][column_index] = 'X'
                board_computer_players_view.grid[row_index][column_index] = 'X'
                hit_ship_name = get_hit_ship(fleet_computer, coordinate)

                if hit_ship_name is not None:
                    record_hit(fleet_computer, hit_ship_name, coordinate)
                    print(f"{Fore.MAGENTA}*** Hit registered on {hit_ship_name}! ***")
                    fleet_computer.update_ship_statuses()

            elif outcome == 'repeat':
                print("You've already hit this coordinate. Try another one.")
                continue  # Skip the rest of the loop and let the player choose another coordinate

            else: # Mark the miss on the grid
                board_computer.grid[row_index][column_index] = '~'
                board_computer_players_view.grid[row_index][column_index] = '~'

            print("\nComputer's grid after player's attack:")
            board_computer_players_view.print_grid()
            board_computer.print_grid() # TODO: only for WINNING
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
                    print(f"{Fore.CYAN}*** Hit registered on {hit_ship_name}! ***")
                    fleet_player.update_ship_statuses()

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
