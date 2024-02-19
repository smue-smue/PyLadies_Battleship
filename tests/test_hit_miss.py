import pytest
from hit_miss import check_hit_or_miss
from grid import Grid

@pytest.fixture
def setup_grid():
    grid = Grid() 
    # Setup grid with a ship at certain location, 'S' represents a ship
    grid.grid[1][1] = 'S' # 'B2' is the location of the ship
    return grid

def test_hit_detection(setup_grid):
    grid = setup_grid
    # Assuming 'B2' translates to grid coordinates [1][1]
    assert check_hit_or_miss('B2', grid) == 'hit', "Expected a hit at 'B2', but it was missed."

def test_miss_detection(setup_grid):
    grid = setup_grid
    # Assuming 'C3' translates to grid coordinates that do not have a ship
    assert check_hit_or_miss('C3', grid) == 'miss', "Expected a miss at 'C3', but it was marked as a hit."



