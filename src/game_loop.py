'''
This module holds the main loop that controls the game flow.
    
Alternates turns between the player and the computer, allowing each to attack the other's grid.
Continues until one player's fleet is completely sunk, declaring the other player the winner.
'''

import time
import colorama
from colorama import Fore, Style
from hit_miss import (
    check_hit_or_miss,
    get_hit_ship,
    record_hit,
    get_adjacent_cells,
    collect_hits_misses,
    refine_targets,
    get_surrounding_cells
)

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
    '''
    This function represents the main game loop for a game of Battleship.

    Parameters:
        player (Player): The human player.
        computer (Computer): The computer player.
        board_player (Board): The game board for the human player.
        board_computer (Board): The game board for the computer player.
        board_computer_players_view (Board): The game board for the computer player 
                                            as viewed by the human player.
        fleet_player (Fleet): The fleet of ships for the human player.
        fleet_computer (Fleet): The fleet of ships for the computer player.
        beginner (Player or Computer): The player who begins the game.

    The function alternates turns between the human player and the computer. On each turn, 
    the current player chooses a coordinate to attack on the opponent's board. The function 
    checks if the attack is a hit or a miss and updates the game boards accordingly. If a 
    ship is hit, the function also updates the status of the ship in the fleet. The game 
    continues until all the ships in a player's fleet have been sunk, at which point the 
    game ends and the other player is declared the winner.
    '''

    game_over = False
    # Set the current turn to the beginner
    current_turn = player if beginner == player else computer

    # Initialize round counter and turn counter
    round_counter = 0
    turn_counter = 0

    while not game_over:

        # Increment round counter and print it when both players have had their turn
        if turn_counter % 2 == 0:
            round_counter += 1
            print(f"\n{Fore.YELLOW}*** Round {round_counter}! ***{Style.RESET_ALL}")

# ================= HUMAN PLAYER =============================================

        if current_turn == player:
            # Pass an empty string for 'shipname'
            coordinate = player.player_coordinate(
                fleet_player.ships,
                ' ', 
                board_computer,
                attacking=True
            )

            outcome = check_hit_or_miss(coordinate, board_computer)

            if outcome != 'repeat':
                print(
                    f"\n{Fore.GREEN}Your daring attack on {coordinate} "
                    f"turned out a {Style.BRIGHT}{outcome}.{Style.RESET_ALL}"
                )

            column_index, row_index = board_computer.convert_coordinate_to_indices(coordinate)

            if outcome == 'hit':
                board_computer.grid[row_index][column_index] = 'X'
                board_computer_players_view.grid[row_index][column_index] = 'X'
                hit_ship_name = get_hit_ship(fleet_computer, coordinate)

                if hit_ship_name is not None:
                    record_hit(fleet_computer, hit_ship_name, coordinate)
                    print(f"\n{Fore.MAGENTA}*** Hit registered on {hit_ship_name}! ***")
                    fleet_computer.update_ship_statuses()

            elif outcome == 'miss':
                if board_computer.grid[row_index][column_index] == '.':
                    board_computer.grid[row_index][column_index] = '~'
                if board_computer_players_view.grid[row_index][column_index] == '.':
                    board_computer_players_view.grid[row_index][column_index] = '~'

            elif outcome == 'repeat':
                print(
                    f"{Fore.GREEN}You've already fired a cannonball here. "
                    f"Set your sights on new coordinates, Captain.{Style.RESET_ALL}"
                )
                continue  # Skip the rest of the loop and let the player choose another coordinate

            else: # Mark the miss on the grid
                board_computer.grid[row_index][column_index] = '~'
                board_computer_players_view.grid[row_index][column_index] = '~'

            print(
                f"\n{Fore.GREEN}The status of the enemy's fleet after "
                f" your attack:{Style.RESET_ALL}"
            )
            board_computer_players_view.print_grid()
            #board_computer.print_grid() # Print the computer's grid for debugging
            #print(fleet_computer) # debugging

            if fleet_computer.update_ship_statuses():
                print(
                    f"{Fore.MAGENTA}{Style.BRIGHT}\nGame Over! Captain {current_turn.name} "
                    f"triumphs over the seas and claims the title of supreme commander! "
                    f"{Style.RESET_ALL}\n"
                )
                game_over = True
                break  # Break out of the loop immediately if the computer's fleet is sunk
            else:
                turn_counter += 1
                current_turn = computer  # Switch turn to computer only if the game is not over
                time.sleep(1)

# ================= COMPUTER ======================================================================

        else:
            if computer.hunt_mode and computer.potential_targets:
                # Keep popping coordinates until one not in past_targets is found
                # or potential_targets is empty.
                coordinate = None
                while computer.potential_targets:
                    # If in hunt mode, choose the next target from the list of potential targets.
                    next_potential_target = computer.potential_targets.pop()
                    if (next_potential_target is not None and
                                next_potential_target not in computer.past_targets):
                        # Found a coordinate not in past_targets, use this one.
                        coordinate = next_potential_target
                        break # Exit the loop once a valid coordinate is found.

            else:
                # Otherwise, select a random coordinate to attack, but consider past targets.
                coordinate = None
                while not coordinate:
                    coordinate_test = player.random_coordinate(board_player.size)
                    if coordinate_test not in computer.past_targets:
                        coordinate = coordinate_test
                        break

            # Add a check here to ensure coordinate is not None
            if coordinate is None:
                print("No valid coordinate found, skipping to the next turn.")
                continue  # Skip the rest of the loop and try again

            collect_hits_misses(computer.past_targets, coordinate)
            # Print statement for debugging
            #print(f"Next attack at: {coordinate}")
            computer.past_targets.sort()
            # Print statement for debbuging
            #print(computer.past_targets)

            outcome = check_hit_or_miss(coordinate, board_player)

            column_index, row_index = board_player.convert_coordinate_to_indices(coordinate)

            if outcome == 'hit':

                computer.hunt_mode = True

                # Print the outcome of the computer's attack
                print(
                    f"\n{Fore.GREEN}Computer attacked {coordinate} and it was "
                    f"a {outcome}.{Style.RESET_ALL}\n"
                )

                board_player.grid[row_index][column_index] = 'X'
                hit_ship_name = get_hit_ship(fleet_player, coordinate)

                if hit_ship_name is not None:
                    record_hit(fleet_player, hit_ship_name, coordinate)
                    print(f"{Fore.CYAN}*** Hit registered on {hit_ship_name}! ***")

                previously_active_ships = [
                    name for name, details in fleet_player.ships.items()
                    if details['status'] == "active"
                ]
                # Print statement for debugging
                #print("Active before status update:", previously_active_ships)

                fleet_player.update_ship_statuses()

                newly_sunk_ships = [
                    name for name, details in fleet_player.ships.items()
                    if details['status'] == "sunk" and name in previously_active_ships
                ]
                # Print statement for debugging
                #print("Newly sunk ships:", newly_sunk_ships)

                if newly_sunk_ships:
                    print(
                        f"{Fore.CYAN}*** {', '.join(newly_sunk_ships)} has been sunk! "
                        f"Exiting hunt mode. ***"
                    )
                    computer.hunt_mode = False
                    computer.first_hit = None
                    computer.second_hit = None
                    computer.last_hit = None
                    computer.discovered_ship_direction = None
                    computer.potential_targets.clear()  # This clears the list of potential targets

                    # After a ship is sunk
                    for ship_name in newly_sunk_ships:
                        safe_cells = set()
                        ship_coordinates = fleet_player.ships[ship_name]['coordinates']
                        for coordinate in ship_coordinates:
                            surrounding_cells = get_surrounding_cells(coordinate, board_player.size)
                            safe_cells.update(surrounding_cells)

                        # Extend the safe cells list with the new safe cells
                        computer.safe_cells.extend(
                            cell for cell in safe_cells if cell not in computer.safe_cells
                            )

                        # Transfer safe cells to past targets
                        for cell in safe_cells:
                            if cell not in computer.past_targets:
                                computer.past_targets.append(cell)

                        # Print statements for debugging
                        #print(f"Safe cells around sunken ship are: {sorted(computer.safe_cells)}")
                        #print(f"Past targets with safe cells: {sorted(computer.past_targets)}")

                else:
                    print(f"{Fore.CYAN}*** Hunt mode! ***")
                    if not computer.first_hit:
                        computer.first_hit = coordinate
                        # Record the first hit if it's the very first successful hit
                        new_targets = get_adjacent_cells(coordinate, board_player.size)
                        # Get the adjacent cells of the hit cell
                        computer.potential_targets.extend(new_targets)

                    elif not computer.second_hit:
                        # Check if second_hit is not set
                        computer.second_hit = coordinate
                        if computer.first_hit[0] == computer.second_hit[0]:
                            # Same column, different row
                            computer.discovered_ship_direction = 'vertical'
                        elif computer.first_hit[1] == computer.second_hit[1]:
                            # Same row, different column
                            computer.discovered_ship_direction = 'horizontal'

                        # Focus future attacks based on direction // Debugging print statements
                        #print(computer.first_hit)
                        #print(computer.second_hit)
                        #print(computer.discovered_ship_direction)

                        computer.potential_targets = refine_targets(
                            computer.first_hit,
                            computer.second_hit,
                            computer.discovered_ship_direction,
                            board_player.size
                        )

                    else:
                        # Extend the potential targets along the discovered direction
                        if computer.discovered_ship_direction:
                            computer.last_hit = coordinate
                            computer.potential_targets = refine_targets(
                                computer.first_hit,
                                computer.last_hit,
                                computer.discovered_ship_direction,
                                board_player.size
                            )
                        else:
                        # If no direction has been established, revert to hunt mode logic.
                            computer.last_hit = coordinate
                            new_targets = get_adjacent_cells(coordinate, board_player.size)
                            computer.potential_targets.extend(new_targets)

            elif outcome == 'miss':
                if board_player.grid[row_index][column_index] == '.':
                    board_player.grid[row_index][column_index] = '~'
                # Print the outcome of the computer's attack
                print(
                    f"{Fore.GREEN}The enemy attacked {coordinate} and it was "
                    f"a {Style.BRIGHT}{outcome}.{Style.RESET_ALL}"
                )

            elif outcome == 'repeat':
                continue

            else:
                # Mark a miss with '~' only if the cell was not previously targeted
                if board_player.grid[row_index][column_index] == '.':
                    board_player.grid[row_index][column_index] = '~'
                if not computer.potential_targets:
                    computer.hunt_mode = False
                    computer.last_hit = None

            print(f"\n{Fore.GREEN}Your fleet's status after the enemy's attack:{Style.RESET_ALL}")
            board_player.print_grid()
            # print(fleet_player) # debugging

            if fleet_player.update_ship_statuses():
                print(
                    f"{Fore.MAGENTA}{Style.BRIGHT}\nGame Over! Captain "
                    f"{current_turn.name} triumphs over the seas and claims the title of "
                    f"supreme commander!{Style.RESET_ALL}\n"
                )
                game_over = True
                break  # Break out of the loop immediately if the player's fleet is sunk
            else:
                turn_counter += 1
                current_turn = player  # Switch turn back to player only if the game is not over
                time.sleep(1)
