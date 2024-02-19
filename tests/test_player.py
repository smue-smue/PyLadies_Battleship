import pytest
from unittest.mock import patch
"""
`patch` is used to temporarily replace the real objects in your code with mock objects during testing. 
It allows you to simulate different behaviors and responses of these objects, making it easier to test 
functions or methods that depend on external systems or user input. For example, `patch` can be used to 
mock the behavior of the `input()` function to simulate user inputs without requiring actual keyboard input 
during tests. This is particularly useful for testing functions that involve user interaction or depend on 
external resources.

"""

from player import Player
from fleet import Fleet
from grid import Grid 

@pytest.fixture
def player():
    """
    A pytest fixture that creates a new Player instance for testing.
    
    This fixture sets up a Player with a default name 'Test Player' and returns it for use in test functions.
    
    Returns:
        Player: An instance of the Player class.
    """
    return Player("Test Player")

def test_init(player):
    """
    Tests the initialization of the Player class.
    
    Verifies that a Player instance can be created with the correct name attribute.
    """
    assert player.name == "Test Player", "Player name should be initialized correctly."

@patch('builtins.input', return_value='John Doe')
def test_prompt_for_player_name(mock_input):
    """
    Tests the static method prompt_for_player_name of the Player class.
    
    This test simulates user input 'John Doe' for the player's name and verifies the method returns this input correctly.
    """
    name = Player.prompt_for_player_name()
    assert name == 'John Doe', "The prompt_for_player_name method should return the user input as the player's name."

# Example test for player_coordinate with mocking input and output
@patch('builtins.print')
@patch('builtins.input', side_effect=['A1', 'H'])
def test_player_coordinate(mock_input, mock_print, player):
    """
    Tests the player_coordinate method of the Player class.
    
    This test simulates user inputs for ship coordinates and verifies that the method returns the first valid coordinate.
    """
    fleet = {'TestShip': {'size': 3}}  # Simulated fleet dictionary
    coordinate = player.player_coordinate(fleet, 'TestShip')
    assert coordinate == 'A1', "The player_coordinate method should return the first valid coordinate input by the user."

# Example test for player_direction with mocking input
@patch('builtins.input', return_value='H')
def test_player_direction(mock_input, player):
    """
    Tests the player_direction method of the Player class.
    
    This test simulates user input 'H' for the ship's direction and verifies that the method returns this input correctly.
    """
    direction = player.player_direction()
    assert direction == 'H', "The player_direction method should return the user input for the ship's direction."


