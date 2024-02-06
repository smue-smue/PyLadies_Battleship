from main import board_player

def player_placing_ships(fleet_player):
    '''This function asks the player where to place their ships.'''

    while True:
        all_ships_processed = True # Assume all ships are processed until proven otherwise
        for shipname in fleet_player.keys():
            if not fleet_player[shipname]['coordinates']: # Check if ship lacks coordinates
                coordinate = input(f"Please enter a start coordinate of your {shipname} (total size: {fleet_player[shipname]['size']} squares). ")
                fleet_player[shipname]['coordinates'].append(coordinate)
                board_player.update_grid(coordinate)
                board_player.print_grid()
                all_ships_processed = False # A ship was processed, so not all were done
                break # Break after processing each ship to check the condition again

            # Hier sicherstellen, dass c1 bei c2 etc. anschließt
            # print grid for overview after each ship
        if all_ships_processed:
            break # Exit the while loop if all ships have been processed

    print(fleet_player)
    # return fleet_player