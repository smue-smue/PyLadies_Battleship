from grid import Grid
from fleet import Fleet

def check_hit_or_miss(coordinate, grid):
    column_index, row_index = grid._convert_coordinate_to_indices(coordinate)
    cell = grid.grid[row_index][column_index]
    if cell == 'S':
        return 'hit'
    else:
        return 'miss'
    
def get_hit_coordinate(coordinate, grid):
    column_index, row_index = grid._convert_coordinate_to_indices(coordinate)
    cell = grid.grid[row_index][column_index]
    if cell == 'S':
        return coordinate
    return None # Explicitly return None if there's no hit