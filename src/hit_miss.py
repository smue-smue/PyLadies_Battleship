from grid import Grid
from fleet import Fleet

def check_hit_or_miss(coordinate, grid):
    column_index, row_index = grid._convert_coordinate_to_indices(coordinate)
    cell = grid.grid[row_index][column_index]
    if cell == 'S':
        return 'hit'
    else:
        return 'miss'
    
# def get_hit_coordinate(coordinate, grid): # not really needed, but for easier reading
#     column_index, row_index = grid._convert_coordinate_to_indices(coordinate)
#     cell = grid.grid[row_index][column_index]
#     if cell == 'S':
#         hit_coordinate = coordinate
#         return hit_coordinate
    
def get_hit_ship(fleet, hit_coordinate):
    for ship_name, ship_details in fleet.ships.items(): # Iterates over ship keys and values
        if hit_coordinate in ship_details['coordinates']:
            return ship_name
    return None

def record_hit(fleet, hit_ship_name, hit_coordinate):

    # Access the 'ships' dictionary within the 'fleet' object to update the 'hits' list for the specified ship.
    if hit_ship_name in fleet.ships:
        fleet.ships[hit_ship_name]['hits'].append(hit_coordinate)
    else:
        print(f"Ship name {hit_ship_name} not found in fleet.")



