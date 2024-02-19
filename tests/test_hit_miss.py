import pytest
from grid import Grid
from fleet import Fleet
from ship import Ship
from hit_miss import check_hit_or_miss, get_hit_ship, record_hit

@pytest.fixture
def setup_grid():
    """
    Fixture to initialize a grid and place a ship at a specific location.
    
    This fixture sets up a grid with a single 'ship' placed at the 'B2' coordinate 
    (which translates to grid coordinates [1][1]). It is used to test hit or miss detection.
    
    Returns:
        Grid: An instance of the Grid class with a ship placed at 'B2'.
    """
    grid = Grid() 
    grid.grid[1][1] = 'S'  # 'B2' is the location of the ship
    return grid

@pytest.fixture
def setup_fleet():
    """
    Creates a Fleet instance and adds a single ship to the fleet.
    
    This fixture also updates the ship's coordinates to simulate a placed ship. It is used 
    to test the functionality of recording hits on ships within the fleet.
    
    Returns:
        tuple: A tuple containing the Fleet instance and the name of the added ship.
    """
    fleet = Fleet("Test Fleet")
    ship = Ship("TestShip", "Destroyer", 3)
    fleet.add_ship(ship)
    fleet.ships["TestShip"]['coordinates'] = ['A1', 'A2', 'A3']
    return fleet, "TestShip"

def test_hit_detection(setup_grid):
    """
    Tests if a hit is correctly detected on a ship's location.
    
    This test verifies that the check_hit_or_miss function identifies a hit when a ship 
    is present at the specified grid coordinate ('B2').
    """
    grid = setup_grid
    assert check_hit_or_miss('B2', grid) == 'hit', "Expected a hit at 'B2', but it was missed."

def test_miss_detection(setup_grid):
    """
    Tests if a miss is correctly identified on an empty grid location.
    
    This test checks that the check_hit_or_miss function returns 'miss' for a grid coordinate 
    ('C3') where no ship is placed, ensuring accurate miss detection.
    """
    grid = setup_grid
    assert check_hit_or_miss('C3', grid) == 'miss', "Expected a miss at 'C3', but it was marked as a hit."

def test_record_hit(setup_fleet):
    """
    Tests the record_hit function's ability to correctly log a hit on a ship.
    
    This test ensures that when a hit is recorded against a ship ('TestShip') at a specific 
    coordinate ('A1'), it is accurately reflected in the fleet's ship details.
    """
    fleet, ship_name = setup_fleet
    record_hit(fleet, ship_name, 'A1')
    assert 'A1' in fleet.ships[ship_name]['hits'], "Expected 'A1' to be recorded as a hit for 'TestShip'."
