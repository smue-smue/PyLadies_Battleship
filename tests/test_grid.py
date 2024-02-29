import pytest
from grid import Grid

def test_initialize_grid_default_size():
    grid = Grid()
    assert len(grid.grid) == 10  # Default size
    assert all(len(row) == 10 for row in grid.grid)  # Each row has 10 columns

def test_initialize_grid_custom_size():
    size = 5
    grid = Grid(size=size)
    assert len(grid.grid) == size
    assert all(len(row) == size for row in grid.grid)

def test_convert_coordinate_to_indices_valid():
    grid = Grid()
    column_index, row_index = grid.convert_coordinate_to_indices('A1')
    assert column_index == 0
    assert row_index == 0

def test_convert_coordinate_to_indices_invalid():
    grid = Grid()
    with pytest.raises(ValueError):
        grid.convert_coordinate_to_indices('Z10')  # Assuming Z is out of bounds

def test_mark_water_around_ship():
    # Initialize a grid
    grid = Grid(size=5)

    # Place a ship at a specific location
    grid.grid[2][2] = "S"

    # Call the method to mark water around the ship
    grid._mark_water_around_ship(2, 2)

    # Define the expected grid after marking water around the ship
    expected_grid = [
        ['.', '.', '.', '.', '.'],
        ['.', '~', '~', '~', '.'],
        ['.', '~', 'S', '~', '.'],
        ['.', '~', '~', '~', '.'],
        ['.', '.', '.', '.', '.']
    ]

    # Assert that the grid matches the expected grid
    assert grid.grid == expected_grid

def test_is_valid_placement():
    grid = Grid(size=5)
    assert grid.is_valid_placement('A1', 'H', 3) is True  # Horizontal placement within bounds
    assert grid.is_valid_placement('A1', 'V', 6) is False  # Vertical placement exceeding bounds

def test_is_valid_attack():
    grid = Grid(size=5)
    assert grid.is_valid_attack('A1') is True  # Attack within bounds
    assert grid.is_valid_attack('F1') is False  # Attack out of bounds

def test_update_grid_fleet():
    # Initialize a grid
    grid = Grid(size=5)

    # Define a fleet
    fleet = {
        'Destroyer': {
            'size': 2,
            'coordinates': []
        }
    }

    # Call the method to update the grid with the fleet
    grid.update_grid_fleet('A1', 'H', fleet, 2, 'Destroyer')

    # Define the expected grid after updating the grid with the fleet
    expected_grid = [
        ['S', 'S', '~', '.', '.'],
        ['~', '~', '~', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.']
    ]

    # Define the expected fleet after updating the grid with the fleet
    expected_fleet = {
        'Destroyer': {
            'size': 2,
            'coordinates': ['A1', 'B1']
        }
    }

    # Assert that the grid and fleet match the expected grid and fleet
    assert grid.grid == expected_grid
    assert fleet == expected_fleet
