import random
from grid import Grid

def random_coordinate(grid_size):
    column_label = random.choice('ABCDEFGHIJ'[0:grid_size]) 
    row_number = str(random.randint(1, grid_size))
    return column_label + row_number

def random_direction():
    return random.choice(['H', 'V'])

def is_valid_placement(grid, start_coordinate, direction, size):
    column_label, row_number = start_coordinate[0], int(start_coordinate[1:])
    column_index = grid.coordinates_x[column_label] - 1  # Adjust for 0-based index
    row_index = row_number - 1  # Adjust for 0-based index

    if direction == 'H':
        if column_index + size > grid.size:
            return False  # Exceeds grid bounds horizontally
        for i in range(size):
            if grid.grid[row_index][column_index + i] != '.':
                return False  # Occupied cell found
    elif direction == 'V':
        if row_index + size > grid.size:
            return False  # Exceeds grid bounds vertically
        for i in range(size):
            if grid.grid[row_index + i][column_index] != '.':
                return False  # Occupied cell found

    return True  # Valid placement

def place_ships_randomly(fleet, grid):
    for shipname, shipdetails in fleet.items():
        placed = False
        while not placed:
            start_coordinate = random_coordinate(grid.size)
            direction = random_direction()

            # Check if the placement is valid before attempting to update the grid
            if is_valid_placement(grid, start_coordinate, direction, shipdetails['size']):
                if grid.update_grid_fleet(start_coordinate, direction, fleet, shipdetails['size'], shipname, show_errors=False):
                    placed = True  # Ship placed successfully
