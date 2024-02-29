'''
This module manages the Grid setup, the state and rules of the game board.
'''
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

class Grid:
    '''
    A class used to represent a 2D grid for grid-based games, such as battleship.

    Parameters:
    -----------
        size    (int, optional):    The size of the grid (default is 10). 
                                    This size is used to determine the grid's dimensions.
    
    Attributes:
    ----------- 
        grid            (list):     Matrix representing the game grid, where each cell can 
                                    hold a value indicating a ship part, hit/miss, or empty.
        coordinates_x   (dict):     Dictionary mapping column labels (A, B, C, ...) 
                                    to their respective 1-based numerical indices.
        coordinates_y   (dict):     Dictionary mapping row labels ('1', '2', '3', ...) 
                                    to their respective 1-based numerical indices.

    Methods:
    --------    
        initialize_grid(size=10)
        _convert_coordinate_to_indices(coordinate)
        _convert_indices_to_coordinate(column_index, row_index)
        _mark_water_around_ship(self, row_index, column_index)
        is_valid_placement(grid, start_coordinate, direction, size)
        is_valid_attack(grid, coordinate)
        update_grid_fleet(start_coordinate, direction, fleet, size, shipname)
        print_grid()
   '''

    coordinates_x = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
        'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19
        }

    coordinates_y = {
        '1': 0, '2': 1, '3': 2, '4': 3, '5': 4,
        '6': 5, '7': 6, '8': 7, '9': 8, '10': 9,
        '11': 10, '12': 11, '13': 12, '14': 13, '15': 14,
        '16': 15, '17': 16, '18': 17, '19': 18, '20': 19
        }

    def __init__(self, size=10):
        self.size = size
        self.grid = self.initialize_grid(size)

    def initialize_grid(self, size=10):
        '''
        Initializes the grid as a list of lists (matrix) to a specified size, 
        with '.' indicating empty cells.

        Parameters:
            size    (int, optional):    The size of the grid, defaults to 10. 
                                        Determines both the width and height of the grid.

        Returns:
            list:   A 2D list (matrix) representing the initialized game grid.
        '''
        grid = []
        for _ in range(size):
            row = ['.'] * (size)
            grid.append(row)

        return grid

    def convert_coordinate_to_indices(self, coordinate):
        '''
        Converts a coordinate (e.g., 'A1') into 0-based grid indices.

        Parameters:
            coordinate  (str):  A string representing the grid coordinate, e.g., 'A1'.

        Returns:
            tuple:  A tuple containing two integers (column_index, row_index) 
                    representing 0-based grid indices.
        '''

        coordinate = coordinate.upper()
        # Extract colum letter and row number from the coordinates
        column_letter = coordinate[0]
        row_number = coordinate[1:]

        if column_letter not in self.coordinates_x:
            raise ValueError(
                f"{Fore.RED}Invalid column letter: {column_letter}. "
                f"Please enter a valid column.{Style.RESET_ALL}"
            )

        # Convert to 0-based grid indices
        column_index = self.coordinates_x[column_letter]
        row_index = int(row_number) - 1 # Convert row to 0-based

        return column_index, row_index

    def _convert_indices_to_coordinate(self, column_index, row_index):
        '''
        Converts 0-based grid indices back into a coordinate (e.g., 'A1').

        Parameters:
            column_index    (int):  The 0-based column index.
            row_index       (int):  The 0-based row index.

        Returns:
            str:    A string representing the coordinate (e.g., 'A1') corresponding 
                    to the given indices.
        '''

        # Find the letter corresponding to the 0-based column index
        column_letter = [
            key for key, value in self.coordinates_x.items()
            if value == column_index
            ][0]

        # Adjust row_index to 1-based for display
        coordinate = f"{column_letter}{row_index + 1}"
        return coordinate

    def _mark_water_around_ship(self, row_index, column_index):
        '''
        Modifies the grid attribute of the Grid class instance by marking adjacent cells 
        around the specified ship part as water ("~"). It is used to visually distinguish 
        ship parts from the surrounding area and to prevent other ships from being placed too close.

        Parameters:
            row_index       (int):  The 0-based row index.
            column_index    (int):  The 0-based column index.

        Returns:
            None: This method does not return a value but modifies the grid in place.
        '''
        for r in range(-1, 2):  # From -1 to 1, covering above, same, and below rows
            for c in range(-1, 2):  # From -1 to 1, covering left, same, and right columns
                new_row, new_col = row_index + r, column_index + c
                # Check boundaries and avoid marking the ship cell itself as water
                if (0 <= new_row < len(self.grid) and
                    0 <= new_col < len(self.grid[0]) and
                    self.grid[new_row][new_col] == "."):
                    self.grid[new_row][new_col] = "~"

    def is_valid_placement(self, start_coordinate, direction, size):
        '''
        Determines the validity of a proposed ship placement.
        Firstly, if the placement exceeds grid bounds based on the direction and size of the ship.
        Secondly, if any of the cells intended for the ship's placement are already occupied.
        '''

        column_label, row_number = start_coordinate[0], int(start_coordinate[1:])
        column_index = self.coordinates_x[column_label]
        row_index = row_number -1 # Convert to 0-based indexing

        if direction == 'H':
            if column_index + size > self.size:
                return False  # Exceeds grid bounds horizontally
            for i in range(size):
                if self.grid[row_index][column_index + i] != '.':
                    return False  # Occupied cell found
        elif direction == 'V':
            if row_index + size > self.size:
                return False  # Exceeds grid bounds vertically
            for i in range(size):
                if self.grid[row_index + i][column_index] != '.':
                    return False  # Occupied cell found

        return True  # Valid placement

    def is_valid_attack(self, coordinate):
        '''
        Checks if an attack at a given coordinate is within the bounds of the grid.

        The function first converts the alphanumeric coordinate (e.g., 'A1') into
        0-based numeric indices. It then checks if these indices are within the
        grid size defined by the `self.size` attribute. The grid is assumed to be
        square, so the same size applies to both dimensions.

        Parameters:
            coordinate (str): The coordinate to check, in alphanumeric format (e.g., 'A1').

        Returns:
            bool: True if the attack is within the bounds of the grid, False otherwise.
        '''
        column_index, row_index = self.convert_coordinate_to_indices(coordinate)

        # Check horizontal bounds
        if column_index >= self.size or column_index < 0:
            return False

        # Check vertical bounds
        if row_index >= self.size or row_index < 0:
            return False

        return True  # Attack is within grid bounds


    def update_grid_fleet(
            self,
            start_coordinate,
            direction,
            fleet,
            size,
            shipname,
            show_errors=True
            ):
        '''
        Updates the grid with a new ship placement based on the given parameters.

        Parameters:
            start_coordinate    (str):  The starting coordinate of the ship placement, e.g., 'A1'.
            direction           (str):  The direction of the ship placement, 
                                        'V' for vertical or 'H' for horizontal.
            fleet               (dict): A dictionary containing the fleet information, 
                                        updated with the ship's coordinates.
            size                (int):  The size (length) of the ship being placed.
            shipname            (str):  The name of the ship being placed.
            show_errors         (bool): If True, prints error messages when placement fails.

        Returns:
            bool:   True if the ship was successfully placed, 
                    False otherwise.
        '''

        if start_coordinate is None and show_errors:
            print("Error: Coordinate cannot be None.")
            return False

        column_index, row_index = self.convert_coordinate_to_indices(start_coordinate)

        for i in range(size):

            if direction == "V":
                self.grid[row_index + i][column_index] = "S" # Vertical placement
                coordinate = self._convert_indices_to_coordinate(column_index, row_index + i)
                fleet[shipname]['coordinates'].append(coordinate)
                self._mark_water_around_ship(row_index + i, column_index)
            elif direction == "H":
                self.grid[row_index][column_index + i] = "S" # Horizontal
                coordinate = self._convert_indices_to_coordinate(column_index + i, row_index)
                fleet[shipname]['coordinates'].append(coordinate)
                self._mark_water_around_ship(row_index, column_index + i)

        return True

    def print_grid(self):
        '''
        Prints the current state of the grid to the console, showing all ships, hits, 
        misses, and empty spaces. Uses colorama to colorize specific characters.

        Returns:
            None:   This method does not return a value but outputs the grid state to the console.
        '''
        # Display column headers
        print()
        column_labels = '     ' + ' '.join('ABCDEFGHIJKLMNOPQRSTUVXYZ'[:self.size])
        print(column_labels)

        # Display each row with its row number
        for index, row in enumerate(self.grid, start=1):
            row_str = f"{index:<2} "
            for cell in row:
                if cell == 'X':
                    row_str += Fore.RED + cell + Style.RESET_ALL + ' '
                elif cell == '~':
                    row_str += Fore.CYAN + cell + Style.RESET_ALL + ' '
                else:
                    row_str += cell + ' '
            print(' ', row_str)
        print()
