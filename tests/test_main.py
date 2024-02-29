'''
Tests the main game flow, ensuring setup and game loop are called.
'''
from unittest.mock import patch, MagicMock

@patch('main.setup_game', return_value=(
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock(),
        MagicMock()
        )
    )
@patch('main.main_game_loop')
def test_main(mock_main_game_loop, mock_setup_game):
    '''
    Verifies the main function initiates game setup and enters the game loop exactly once.
    '''
    # Import the module under test. The import statement is inside the function
    # so it's executed after the mocks are set up.
    # pylint: disable=import-outside-toplevel
    import main as game_module

    # Call the main function.
    game_module.main()

    # Assert that setup_game and main_game_loop were each called once.
    mock_setup_game.assert_called_once()
    mock_main_game_loop.assert_called_once()
