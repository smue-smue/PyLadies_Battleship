'''
Unit tests for hit/miss logic and target management in a battleship game.
'''

from hit_miss import (
    check_hit_or_miss,
    get_hit_ship,
    record_hit,
    get_adjacent_cells,
    collect_hits_misses,
    refine_targets,
    get_surrounding_cells
)

class GridMock:
    """
    A mock Grid class for testing purposes. 
    Mimics the behavior of the actual Grid class used in the game.
    
    Attributes:
        grid (list): A 2D list representing the game grid.
    """
    def __init__(self, grid):
        self.grid = grid

    def convert_coordinate_to_indices(self, coordinate):
        """
        Converts a grid coordinate into its corresponding row and column indices.
        
        Args:
            coordinate (str): The grid coordinate, e.g., 'A1'.
            
        Returns:
            tuple: A tuple containing row and column indices.
        """
        return ord(coordinate[0]) - ord('A'), int(coordinate[1:]) - 1

class FleetMock:
    """
    A mock Fleet class for testing purposes. 
    Mimics the behavior of the actual Fleet class used in the game.
    
    Attributes:
        ships (dict): A dictionary representing the fleet; keys: ship names, values: ship details.
    """
    def __init__(self, ships):
        self.ships = ships

def test_check_hit_or_miss():
    """
    Tests the check_hit_or_miss function with different scenarios including hit, repeat, and miss.
    """
    grid = GridMock([['S', '.'], ['X', '.']])
    assert check_hit_or_miss('A1', grid) == 'hit'
    assert check_hit_or_miss('A2', grid) == 'repeat'
    assert check_hit_or_miss('B1', grid) == 'miss'

def test_get_hit_ship():
    """
    Tests the get_hit_ship function to ensure it correctly identifies the ship hit at a 
    given coordinate, and returns None when no ship is hit.
    """
    fleet = FleetMock({'Destroyer': {'coordinates': ['A1']}})
    assert get_hit_ship(fleet, 'A1') == 'Destroyer'
    assert get_hit_ship(fleet, 'B1') is None

def test_record_hit():
    """
    Tests the record_hit function to ensure it correctly records a hit on a ship 
    by adding the hit coordinate to the ship's 'hits' list.
    """
    fleet = FleetMock({'Destroyer': {'hits': []}})
    record_hit(fleet, 'Destroyer', 'A1')
    assert 'A1' in fleet.ships['Destroyer']['hits']

def test_get_adjacent_cells():
    """
    Tests the get_adjacent_cells function to ensure it correctly returns 
    a list of valid adjacent cells around a given coordinate.
    """
    assert get_adjacent_cells('B2', 3) == ['A2', 'C2', 'B1', 'B3']

def test_collect_hits_misses():
    """
    Tests the collect_hits_misses function to ensure it correctly 
    adds a coordinate to the list of past targets.
    """
    past_targets = []
    collect_hits_misses(past_targets, 'A1')
    assert 'A1' in past_targets

def test_refine_targets():
    """
    Tests the refine_targets function to ensure it generates a list 
    of potential targets based on the first and second hits and the ship's direction.
    """
    assert refine_targets('A1', 'A2', 'vertical', 3) == ['A3']

def test_get_surrounding_cells():
    """
    Tests the get_surrounding_cells function to ensure it correctly returns 
    a list of all surrounding cells for a given coordinate, including diagonally adjacent ones.
    """
    assert get_surrounding_cells('B2', 3) == ['A1', 'B1', 'C1', 'A2', 'C2', 'A3', 'B3', 'C3']
