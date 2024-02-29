from game_setup import setup_game
from game_loop import main_game_loop

def main():
    (
        player,
        computer,
        board_player,
        board_computer,
        board_computer_players_view,
        fleet_player,
        fleet_computer,
        beginner
    ) = setup_game()

    board_player.print_grid()  # Show player's grid after placing ships

    main_game_loop(
        player,
        computer,
        board_player,
        board_computer,
        board_computer_players_view,
        fleet_player,
        fleet_computer,
        beginner
        )

if __name__ == "__main__":
    main()