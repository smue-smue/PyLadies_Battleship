'''
This module manages the hits and misses placed by
computer and player.
'''

def check_hit_or_miss(coordinate, grid):
    '''
    Determines if the given coordinate on the grid is a hit, a miss, or a repeated hit.
    
    Arguments:
        coordinate: A string representing the grid coordinate to check, e.g., 'A2'.
        grid: The grid object containing the game board.
    
    Returns:
        A string 'hit' if the coordinate hits a ship ('S'), 'repeat' if the coordinate was 
        already hit before, otherwise 'miss'.
    '''

    column_index, row_index = grid.convert_coordinate_to_indices(coordinate)
    cell = grid.grid[row_index][column_index]

    if cell == 'S':  # Ship part
        return 'hit'
    if cell == 'X':  # Already hit
        return 'repeat'
    #else: Water or missed shot
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

def get_adjacent_cells(coordinate, grid_size):
    """
    Generates a list of valid adjacent cells around a given coordinate on the grid.

    Parameters:
    - coordinate (str): The current grid coordinate in the format 'LetterNumber' (e.g., 'A1').
    - grid_size (int): The size of the grid (the number of rows/columns).

    Returns:
    - list: A list of strings representing valid adjacent coordinates on the grid.

    The function calculates adjacent cells in all four cardinal directions (left, right, up, down)
    from the given coordinate, ensuring they fall within the grid boundaries defined by grid_size.
    """
    adjacent_cells = []
    letters = 'ABCDEFGHIJ'[:grid_size]  # Adjust the string based on grid size
    column, row = coordinate[0], int(coordinate[1:])

    index = letters.find(column)  # Find the index of the column letter to navigate left and right

    if index > 0:  # Left
        adjacent_cells.append(f"{letters[index - 1]}{row}")
    if index < grid_size - 1:  # Right
        adjacent_cells.append(f"{letters[index + 1]}{row}")
    if row > 1:  # Up
        adjacent_cells.append(f"{column}{row - 1}")
    if row < grid_size:  # Down
        adjacent_cells.append(f"{column}{row + 1}")

    print("Potential targets:", adjacent_cells)
    return adjacent_cells
