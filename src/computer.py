# Contains the computer's logic for placing ships on the grid.

import random

def random_coordinate(grid_size):
    '''
    Generates a random coordinate within the specified grid size.

    Parameters:
        grid_size   (int): The size of the grid (number of rows/columns).

    Returns:
        str: A string representing a random coordinate within the grid, 
             combining a column letter and a row number.
    '''
    
    column_label = random.choice('ABCDEFGHIJ'[0:grid_size]) 
    row_number = str(random.randint(1, grid_size))
    return column_label + row_number

def random_direction():
    '''
    Selects a random direction.

    Returns:
        str: A single character 'H' or 'V', representing horizontal or vertical direction, respectively.
    '''
    
    return random.choice(['H', 'V'])

def place_ships_randomly(fleet, grid):
    '''
    Places each ship in the fleet at a random location on the grid.

    This function iterates through all ships in the fleet and attempts to place them
    randomly on the grid. It repeats the process for a ship until a valid placement
    is found.

    Parameters:
        fleet   (dict):     A dictionary representing the fleet, with ship names as keys and ship details (including size) as values.
        grid    (object):   An object representing the game grid.

    Notes:
        The function does not return a value but updates the `fleet` and `grid` objects directly to reflect the placement of ships.
    '''
    
    for shipname, shipdetails in fleet.items():
        placed = False
        while not placed:
            start_coordinate = random_coordinate(grid.size)
            direction = random_direction()

            # Check if the placement is valid before attempting to update the grid
            if grid.is_valid_placement(start_coordinate, direction, shipdetails['size']):
                if grid.update_grid_fleet(start_coordinate, direction, fleet, shipdetails['size'], shipname, show_errors=False):
                    placed = True  # Ship placed successfully

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
    