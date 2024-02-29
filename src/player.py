"""
This module defines the Player class for a battleship game, handling interactions
and decisions for both human and computer players. It includes functionalities
for prompting player names, processing player inputs for ship placement and
attack coordinates, and automating random ship placements for computer players.

Classes:
- Player: Manages ship placements, attack coordinates, and player-specific
  attributes such as name and game state (e.g., hunt mode, last hit, potential targets).
"""
import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Player():
    '''
    Represents a player in a game, handling ship placements for human and computer players.

    Attributes:
    -----------
        name    (str):  The name of the player.

    Methods:
    --------
        prompt_for_player_name()
        player_coordinate(self, fleet_player, shipname, attacking=False)
        player_direction(self)
        player_placing_ships(self, fleet_player, board_player)
        random_coordinate(self, grid_size)
        random_direction(self)
        random_placing_ships(self, fleet, grid)

    '''
    def __init__(self, name=None):
        '''
        Initializes a new player instance.

        Parameters:
            name    (str, optional): The name of the player. Defaults to None.

        '''

        self.name = name
        self.hunt_mode = False  # Indicates whether the computer is in hunt mode
        self.last_hit = None  # Stores the last hit coordinate
        self.potential_targets = []  # Stores potential targets for the next move in hunt mode
        self.first_hit = None
        self.second_hit = None
        self.discovered_ship_direction = None # None, 'horizontal, 'verticel'
        self.past_targets = []
        self.safe_cells = [] # Attribute to store safe cells for the computer player

    @staticmethod
    def prompt_for_player_name():
        '''
        Static method to prompt the user for their name.
        This method does not require access to the instance (self) or the class (cls).

        Returns:
            str: The name entered by the user.
        '''

        return input(f"{Fore.GREEN}Ready, Captain? What's your name?{Style.RESET_ALL}\n")

    def player_coordinate(self, fleet_player, shipname, grid_instance, attacking=False):
        '''
        Asks the player for coordinates to place their ships or to perform attacks.

        Parameters:
            fleet_player    (dict): The player's fleet, containing ship names and properties.
            shipname        (str):  The name of the ship to place.
            attacking       (bool): Flag indicating whether the player is attacking.

        Returns:
            str: The valid coordinate entered by the player.

        Notes:
            This method loops until a valid coordinate is input by the user. It checks for
            valid row and column inputs based on predefined grid coordinates.
        '''

        while True: # Use a loop to keep asking until a valid input is received
            if attacking:
                prompt_message = (
                    f"{Fore.GREEN}Captain, it's your turn! Call out the coordinate "
                    f"for your strike: {Style.RESET_ALL}\n"
                )
            else:
                prompt_message = (
                    f"{Fore.GREEN}Captain, mark the starting coordinate of your "
                    f"{shipname} (total size: {fleet_player[shipname]['size']} "
                    f"squares):\n{Style.RESET_ALL}"
                )

            coordinate = input(prompt_message).strip().upper()

            if len(coordinate) <2 or not coordinate[0].isalpha() or not coordinate[1:].isdigit():
                print(
                    f"{Fore.RED}Invalid input. please enter a valid coordinate "
                    f"(e.g. 'B1').{Style.RESET_ALL}\n"
                    )
                continue

            try:
            # Attempt to validate the attack, this may raise a ValueError if invalid
            # Check if the attack is valid within the grid bounds
                if not grid_instance.is_valid_attack(coordinate):
                    print(
                        f"{Fore.RED}Coordinate is out of grid bounds. "
                        f"Please try again.{Style.RESET_ALL}\n"
                        )
                    continue
            except ValueError as e:
                # Handle the ValueError raised from the grid validation
                print(f"{Fore.RED}{e}{Style.RESET_ALL}\n")
                continue

            return coordinate

    def player_direction(self):
        '''
        Asks the player in which direction to place their ships on the grid.

        Returns:
            str: The direction ('H' for horizontal or 'V' for vertical) for ship placement.

        Notes:
            This method loops until a valid direction is input by the user.
        '''

        while True:  # Use a loop to keep asking until a valid input is received
            # Convert to upper case

            direction = input(
                f"{Fore.GREEN}Choose 'H' for a grand horizontal or 'V' for "
                f"a majestic vertical positioning. {Style.RESET_ALL}\n"
                ).upper()

            if direction in ['H', 'V']:
                return direction  # Return the direction if it's valid
            # Notify the user and ask again
            else:
                print(
                    f"{Fore.RED}Invalid input. Please enter 'H' for horizontal "
                    f"or 'V' for vertical.{Style.RESET_ALL}\n"
                    )

    def random_coordinate(self, grid_size):
        '''
        Generates a random coordinate within the specified grid size.

        Parameters:
            grid_size   (int): The size of the grid (number of rows/columns).

        Returns:
            str: A string representing a random coordinate within the grid, 
                combining a column letter and a row number.
        '''

        column_label = random.choice('ABCDEFGHIJKLMNOPQRSTUVXYZ'[0:grid_size])
        row_number = str(random.randint(1, grid_size))
        return column_label + row_number

    def random_direction(self):
        '''
        Selects a random direction.

        Returns:
            str: A single character 'H' or 'V', representing horizontal or
                vertical direction, respectively.
        '''

        return random.choice(['H', 'V'])

    def random_placing_ships(self, fleet, grid):
        '''
        Places each ship in the fleet at a random location on the grid.

        This function iterates through all ships in the fleet and attempts to place them
        randomly on the grid. It repeats the process for a ship until a valid placement
        is found.

        Parameters:
            fleet   (dict):     A dictionary representing the fleet, with ship names as keys
                                and ship details (including size) as values.
            grid    (object):   An object representing the game grid.

        Notes:
            The function does not return a value but updates the `fleet` and
            `grid` objects directly to reflect the placement of ships.
        '''

        for shipname, shipdetails in fleet.items():
            placed = False
            while not placed:
                start_coordinate = self.random_coordinate(grid.size)
                direction = self.random_direction()

                # Check if the placement is valid before attempting to update the grid
                if grid.is_valid_placement(start_coordinate, direction, shipdetails['size']):
                    if grid.update_grid_fleet(
                        start_coordinate,
                        direction, fleet,
                        shipdetails['size'],
                        shipname,
                        show_errors=False
                        ):
                        placed = True  # Ship placed successfully

    def player_placing_ships(self, fleet_player, board_player, board_computer):
        '''
        Guides the player through placing all their ships on the game board.

        Parameters:
            fleet_player (dict): The player's fleet, containing ship names and properties.
            board_player (Board): The game board on which ships will be placed.

        Notes:
            This method iterates over each ship in the player's fleet, prompting for
            placement until all ships are validly placed. It checks for valid placements
            and updates the game board accordingly.
        '''
        for shipname in fleet_player.keys():
            self.place_single_ship(fleet_player, shipname, board_player, board_computer)

    def place_single_ship(self, fleet_player, shipname, board_player, board_computer):
        '''
        Attempts to place a single ship on the game board, prompting the player for input until
        a valid placement is made.

        Parameters:
            fleet_player (dict): The player's fleet, containing ship names and properties.
            shipname (str): The name of the ship to be placed.
            board_player (Board): The player's game board.
            board_computer (Board): The computer's game board, used for validating coordinates.
        '''
        if fleet_player[shipname]['coordinates']:
            return  # Ship already has coordinates, no need to place it again.

        while True:
            coordinate = self.player_coordinate(fleet_player, shipname, board_computer)
            direction = self.player_direction()

            if board_player.is_valid_placement(
                coordinate, direction,
                fleet_player[shipname]['size']
                ):
                if board_player.update_grid_fleet(
                    coordinate,
                    direction,
                    fleet_player,
                    fleet_player[shipname]['size'],
                    shipname
                    ):
                    board_player.print_grid()
                    return  # Ship placed successfully, exit the loop.
            else:
                print(f"{Fore.RED}Invalid ship placement, please try again.{Style.RESET_ALL}")
