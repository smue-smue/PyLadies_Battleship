'''
This module manages the hits and misses placed by
computer and player.
'''

def check_hit_or_miss(coordinate, grid):
    '''
    Determines if the given coordinate on the grid is a hit ('S') or a miss ('.').
    
    Arguments:
        coordinate: A string or tuple representing the grid coordinate to check.
        grid: The grid object containing the game board.
    
    Returns:
        A string 'hit' if the coordinate hits a ship ('S'), otherwise 'miss'.
    '''

    column_index, row_index = grid.convert_coordinate_to_indices(coordinate)
    cell = grid.grid[row_index][column_index]
    if cell == 'S':
        return 'hit'
    return 'miss'

def get_hit_ship(fleet, hit_coordinate):
    '''
    Identifies which ship, if any, has been hit at the given coordinate.
    
    Arguments:
        fleet: The fleet object containing all ships and their details.
        hit_coordinate: The coordinate where a hit has been recorded.
    
    Returns:
        The name of the ship that was hit at the given coordinate, 
        or None if no ship was hit.
    '''
    # Iterates over ship keys and values
    for ship_name, ship_details in fleet.ships.items():
        if hit_coordinate in ship_details['coordinates']:
            return ship_name
    return None

def record_hit(fleet, hit_ship_name, hit_coordinate):
    '''
    Records a hit at the specified coordinate for the given ship in the fleet.
    
    Args:
        fleet: The fleet object containing all ships.
        hit_ship_name: The name of the ship that was hit.
        hit_coordinate: The coordinate where the ship was hit.
    
    Returns:
        None. Updates the 'hits' list for the specified ship within the fleet object.
    '''

    # Access the 'ships' dictionary within the 'fleet' object
    # to update the 'hits' list for the specified ship.
    if hit_ship_name in fleet.ships:
        fleet.ships[hit_ship_name]['hits'].append(hit_coordinate)
    else:
        print(f"Ship name {hit_ship_name} not found in fleet.")
