'''
Unit tests for Player class methods, ensuring random coordinate and direction 
generation and ship placement behave as expected.
'''

from player import Player

def test_random_coordinate():
    """
    Test that the random_coordinate method returns a valid coordinate.
    """
    player = Player()
    for _ in range(100):  # repeat the test 100 times to ensure randomness
        coordinate = player.random_coordinate(10)
        assert 2 <= len(coordinate) <= 3
        assert coordinate[0] in 'ABCDEFGHIJ'
        assert 1 <= int(coordinate[1:]) <= 10

def test_random_direction():
    """
    Test that the random_direction method returns a valid direction.
    """
    player = Player()
    for _ in range(100):  # repeat the test 100 times to ensure randomness
        direction = player.random_direction()
        assert direction in ['H', 'V']

def test_random_placing_ships():
    """
    Test that the random_placing_ships method correctly places ships in the fleet.
    """
    player = Player()
    fleet = {
        'ship1': {'size': 2, 'coordinates': []},
        'ship2': {'size': 3, 'coordinates': []},
    }
    grid = StubGrid(10)

    player.random_placing_ships(fleet, grid)

    # Check that each ship in the fleet has been placed
    for ship in fleet.values():
        assert len(ship['coordinates']) == ship['size']

class StubGrid:
    """
    A stub class for the Grid class, used for testing the Player class.
    """
    def __init__(self, size):
        self.size = size

    def is_valid_placement(self, start_coordinate, direction, ship_size):
        """
        Always returns True, indicating that the placement is valid.
        """
        return True

    def update_grid_fleet(
            self,
            start_coordinate,
            direction,
            fleet,
            ship_size,
            ship_name,
            show_errors=False
        ):
        """
        Updates the fleet dictionary to reflect the placement of the ship.
        """
        fleet[ship_name]['coordinates'] = [start_coordinate] * ship_size
        return True
