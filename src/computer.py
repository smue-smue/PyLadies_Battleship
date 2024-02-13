# Description: This file contains the computer's logic for placing ships on the grid.

import random

def random_coordinate(grid_size):
    '''
    Returns a random coordinate within the grid bounds.
    '''
    
    column_label = random.choice('ABCDEFGHIJ'[0:grid_size]) 
    row_number = str(random.randint(1, grid_size))
    return column_label + row_number

def random_direction():
    '''
    Returns a random direction: 'H' for horizontal or 'V' for vertical.
    '''
    
    return random.choice(['H', 'V'])

def place_ships_randomly(fleet, grid):
    '''
    Places the ships in the fleet randomly on the grid.
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
