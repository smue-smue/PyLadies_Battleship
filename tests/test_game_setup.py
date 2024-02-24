import pytest
from unittest.mock import patch
from game_setup import setup_game, place_ships, main_game_loop
from player import Player
from grid import Grid
from fleet import Fleet

def test_setup_game():
    """
    Test the setup_game function to ensure it initializes the game with the correct components.
    """
    with patch('player.Player.prompt_for_player_name', return_value="TestPlayer"):
        player, computer, board_player, board_computer, board_computer_players_view, fleet_player, fleet_computer, beginner = setup_game()

    assert player.name == "TestPlayer", "Player name should be 'TestPlayer'"
    assert computer.name == "Computer", "Computer name should be 'Computer'"
    assert isinstance(board_player, Grid), "board_player should be an instance of Grid"
    assert isinstance(board_computer, Grid), "board_computer should be an instance of Grid"
    assert isinstance(board_computer_players_view, Grid), "board_computer_players_view should be an instance of Grid"
    assert isinstance(fleet_player, Fleet), "fleet_player should be an instance of Fleet"
    assert isinstance(fleet_computer, Fleet), "fleet_computer should be an instance of Fleet"
    assert beginner.name in ["TestPlayer", "Computer"], "Beginner should be either 'TestPlayer' or 'Computer'"

#TODO: Add test for place_ships function
#TODO: Add test for main_game_loop function
#TODO: Add test for coin_flip function

