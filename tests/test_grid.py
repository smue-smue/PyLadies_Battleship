'''
Tests for Grid class functionality, including initialization, 
coordinate conversion, placement validation, and grid updates.
'''

import pytest
from grid import Grid

def test_initialize_grid_default_size():
    """
    Test that a Grid instance initializes with the default size of 10x10.
    """
    grid = Grid()
    assert len(grid.grid) == 10  # Default size
    assert all(len(row) == 10 for row in grid.grid)  # Each row has 10 columns

def test_initialize_grid_custom_size():
    """
    Test that a Grid instance initializes with a custom size correctly.
    """
    size = 5
    grid = Grid(size=size)
    assert len(grid.grid) == size
    assert all(len(row) == size for row in grid.grid)

def test_convert_coordinate_to_indices_valid():
    """
    Test that valid coordinates are correctly converted to 0-based indices.
    """
    grid = Grid()
    column_index, row_index = grid.convert_coordinate_to_indices('A1')
    assert column_index == 0
    assert row_index == 0

def test_convert_coordinate_to_indices_invalid():
    """
    Test that invalid coordinates raise a ValueError.
    """
    grid = Grid()
    with pytest.raises(ValueError):
        grid.convert_coordinate_to_indices('Z10')  # Assuming Z is out of bounds

def test_mark_water_around_ship():
    """
    Test that water is correctly marked around a ship's location on the grid.
    """
    grid = Grid(size=5)
    grid.grid[2][2] = "S"  # Place a ship at a specific location
    # pylint: disable=protected-access
    grid._mark_water_around_ship(2, 2)  # Mark water around the ship

    expected_grid = [
        ['.', '.', '.', '.', '.'],
        ['.', '~', '~', '~', '.'],
        ['.', '~', 'S', '~', '.'],
        ['.', '~', '~', '~', '.'],
        ['.', '.', '.', '.', '.']
    ]

    assert grid.grid == expected_grid, "Water should be marked around the ship correctly."

def test_is_valid_placement():
    """
    Test that ship placements are correctly validated against grid boundaries and existing ships.
    """
    grid = Grid(size=5)
    assert grid.is_valid_placement('A1', 'H', 3) is True  # Valid horizontal placement
    assert grid.is_valid_placement('A1', 'V', 6) is False  # Invalid vertical placement

def test_is_valid_attack():
    """
    Test that attacks are correctly validated as being within or outside the grid boundaries.
    """
    grid = Grid(size=5)
    assert grid.is_valid_attack('A1') is True  # Attack within bounds
    assert grid.is_valid_attack('F1') is False  # Attack out of bounds

def test_update_grid_fleet():
    """
    Test that the grid and fleet are correctly updated after placing a ship.
    """
    grid = Grid(size=5)
    fleet = {'Destroyer': {'size': 2, 'coordinates': []}}
    grid.update_grid_fleet('A1', 'H', fleet, 2, 'Destroyer')

    expected_grid = [
        ['S', 'S', '~', '.', '.'],
        ['~', '~', '~', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.']
    ]
    expected_fleet = {'Destroyer': {'size': 2, 'coordinates': ['A1', 'B1']}}

    assert grid.grid == expected_grid, "Grid should be updated with ship and surrounding water."
    assert fleet == expected_fleet, "Fleet should be updated with new ship coordinates."
