import random

def place_ships_randomly(board_computer, fleet_computer):
    for shipname, shipdetails in fleet_computer.ships.items():
        placed = False
        while not placed:
            # Randomly choose an orientation
            orientation = random.choice(['H', 'V'])

            # Generate a random starting coordinate based on orientation and ship size
            if orientation == 'H':
                start_row = random.randint(0, board_computer.size - 1)
                start_col = random.randint(0, board_computer.size - shipdetails['size'])
            else:
                start_row = random.randint(0, board_computer.size - shipdetails['size'])
                start_col = random.randint(0, board_computer.size - 1)

            # Convert starting row and column to grid coordinate (e.g., "A1")
            start_coordinate = board_computer._convert_indices_to_coordinate(start_col, start_row)

            # Attempt to place the ship using the update_grid_fleet method
            if board_computer.update_grid_fleet(start_coordinate, orientation, fleet_computer.ships, shipdetails['size'], shipname):
                placed = True
