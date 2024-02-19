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
