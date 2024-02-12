def is_valid_placement(grid, start_coordinate, direction, size):
    '''
    Checks if the ship placement is valid.
    '''

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