import pytest
from unittest.mock import patch, MagicMock
from main import setup_game, main_game_loop

@patch('main.setup_game', return_value=(MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()))
@patch('main.main_game_loop')
def test_main(mock_main_game_loop, mock_setup_game):
    # Import the module under test. The import statement is inside the function
    # so it's executed after the mocks are set up.
    import main as game_module

    # Call the main function.
    game_module.main()

    # Assert that setup_game and main_game_loop were each called once.
    mock_setup_game.assert_called_once()
    mock_main_game_loop.assert_called_once()