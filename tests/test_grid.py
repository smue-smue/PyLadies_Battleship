import pytest
from grid import Grid

@pytest.fixture
def test_grid():
    """
    A pytest fixture that initializes a new Grid instance.
    This fixture is used to provide a fresh Grid instance for each test function that needs it.
    """
    return Grid()

def test_initialize_grid(test_grid):
    """
    Test to ensure that the grid initializes correctly.
    Checks that the grid has the default size of 10x10 and that all cells are initialized properly.
    """
    assert len(test_grid.grid) == 10  # Default grid size is 10x10
    assert all(len(row) == 10 for row in test_grid.grid), "All rows in the grid should have a length of 10."

def test_convert_coordinate_to_indices(test_grid):
    """
    Test the conversion of a board coordinate (e.g., 'A1') into its corresponding 0-based grid indices.
    Verifies that the coordinate 'A1' correctly converts to (0, 0) indices.
    """
    column_index, row_index = test_grid._convert_coordinate_to_indices('A1')
    assert column_index == 0 and row_index == 0, "The coordinate 'A1' should convert to indices (0, 0)."

def test_is_valid_placement(test_grid):
    """
    Test to check the validity of ship placement on the grid.
    Ensures that placing a ship of size 3 at 'A1' horizontally is considered a valid placement when the grid is empty.
    """
    assert test_grid.is_valid_placement('A1', 'H', 3), "Placing a ship of size 3 at 'A1' horizontally should be valid on an empty grid."

def test_update_grid_fleet(test_grid):
    """
    Test the functionality of updating the grid with a new ship placement.
    Checks that placing a ship of size 3 starting at 'A1' horizontally results in the correct grid update, 
    with the first three cells of the first row marked as 'S' to represent the ship.
    """
    test_grid.update_grid_fleet('A1', 'H', {'TestShip': {'coordinates': []}}, 3, 'TestShip')
    assert test_grid.grid[0][:3] == ['S', 'S', 'S'], "The first three cells of the first row should be marked as 'S' after placing a ship of size 3 at 'A1' horizontally."
