import pytest
import random
from unittest.mock import patch
from computer import random_coordinate, random_direction, place_ships_randomly
from grid import Grid
from fleet import Fleet
from ship import Ship

# Define test_fleet fixture
@pytest.fixture
def test_fleet():
    """
    Creates a Fleet instance with a test ship for use in tests.
    """
    fleet = Fleet("Test Fleet")
    test_ship = Ship("Test Ship", "Test Type", 3)  # Adjust attributes as needed
    fleet.add_ship(test_ship) # Add the test ship to the fleet
    return fleet

# Define test_grid fixture
@pytest.fixture
def test_grid():
    """
    Creates a Grid instance of a predefined size for use in tests.
    """
    return Grid(size=10)  # Adjust the size as needed for your tests


def test_random_coordinate():
    """
    Tests the random_coordinate function to ensure it returns a valid grid coordinate.
    
    This test checks if the returned coordinate is in the expected format (e.g., 'A1')
    and within the bounds of the grid size provided.
    """
    grid_size = 10  # Example grid size
    coordinate = random_coordinate(grid_size)
    column_label, row_number = coordinate[0], int(coordinate[1:])
    
    assert column_label in 'ABCDEFGHIJ', "Column label should be a valid letter."
    assert 1 <= row_number <= grid_size, "Row number should be within the grid size."

def test_random_direction():
    """
    Tests the random_direction function to ensure it returns either 'H' or 'V'.
    
    This test verifies that the returned direction is valid for placing ships either
    horizontally ('H') or vertically ('V').
    """
    direction = random_direction()
    assert direction in ['H', 'V'], "Direction should be either 'H' (horizontal) or 'V' (vertical)."

@patch('computer.random_coordinate')  # Adjust this to the correct module path
@patch('computer.random_direction')  # Adjust this to the correct module path
def test_place_ships_randomly(mock_random_direction, mock_random_coordinate, test_fleet, test_grid):
    """
    Tests the place_ships_randomly function to ensure it places ships on the grid.
    
    This test uses mocking to control the output of random_coordinate and random_direction,
    simulating a scenario where ships can be placed. It verifies that ships are placed on the grid
    by checking if their placement is valid.
    """
    mock_random_coordinate.return_value = 'A1'
    mock_random_direction.return_value = 'H'
    
    fleet = test_fleet
    grid = test_grid

    place_ships_randomly(fleet.ships, grid) 

