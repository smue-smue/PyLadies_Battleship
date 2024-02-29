'''
Unit tests for game setup processes including player initialization, 
grid setup, and fleet population.
'''
from unittest.mock import patch
from game_setup import (
    initialize_players,
    initialize_grids,
    populate_fleets,
    initialize_fleets,
    coin_flip,
    setup_game
)
from grid import Grid

class MockPlayer:
    """Mock class for Player to simulate player behaviors without actual game logic."""
    def __init__(self, name):
        self.name = name

    def player_placing_ships(self, ships, grid, opponent_board=None):
        """Simulate the player placing ships on the grid."""

    def random_placing_ships(self, ships, grid):
        """Simulate the computer player randomly placing ships on the grid."""

class MockGrid:
    """Mock class for Grid to simulate grid behaviors without actual game logic."""
    def print_grid(self):
        """Simulate printing the grid to the console."""

class MockFleet:
    """Mock class for Fleet to simulate fleet behaviors without actual game logic."""
    def __init__(self, name):
        self.name = name
        self.ships = {}

    def add_ship(self, ship):
        """Simulate adding a ship to the fleet."""
        self.ships[ship.name] = ship

class MockShip:
    """Mock class for Ship to simulate ship behaviors without actual game logic."""
    def __init__(self, name):
        self.name = name
        self.size = 3

@patch('game_setup.Player.prompt_for_player_name', return_value='Test Player')
def test_initialize_players(_mock_prompt):
    # pylint: disable=unused-argument
    """Test the initialization of player objects."""
    player, computer = initialize_players()
    assert player.name == 'Test Player'
    assert computer.name == 'Computer'

def test_initialize_grids():
    """Test the initialization of game grids."""
    board_player, board_computer, board_computer_players_view = initialize_grids()
    assert isinstance(board_player, Grid)
    assert isinstance(board_computer, Grid)
    assert isinstance(board_computer_players_view, Grid)

def test_populate_fleets():
    """Test the population of fleets with ships."""
    fleet_player = MockFleet('Player Fleet')
    fleet_computer = MockFleet('Computer Fleet')
    ship_counts = populate_fleets(fleet_player, fleet_computer, 'Test Player')
    assert ship_counts == {"Destroyer": 2, "Cruiser": 1, "Battleship": 1, "AircraftCarrier": 1}

def test_initialize_fleets():
    """Test the initialization of fleets for both players."""
    fleet_player, fleet_computer = initialize_fleets('Test Player')
    assert fleet_player.name == 'Test Player'
    assert fleet_computer.name == "Computer's Fleet"

def test_coin_flip():
    """Test the coin flip to decide the starting player."""
    player = MockPlayer('Test Player')
    computer = MockPlayer('Computer')
    beginner = coin_flip(player, computer)
    assert beginner in [player, computer]

@patch(
        'game_setup.initialize_players',
        return_value=(
            MockPlayer('Test Player'),
            MockPlayer('Computer')
        )
)
@patch('game_setup.initialize_grids', return_value=(MockGrid(), MockGrid(), MockGrid()))
@patch(
    'game_setup.initialize_fleets',
    return_value=(
        MockFleet('Player Fleet'),
        MockFleet('Computer Fleet')
    )
)
def test_setup_game(_mock_initialize_players, _mock_initialize_grids, _mock_initialize_fleets):
    # pylint: disable=unused-argument
    """Test the complete setup of the game, including players, grids, and fleets."""
    game_setup = setup_game()
    assert len(game_setup) == 8
