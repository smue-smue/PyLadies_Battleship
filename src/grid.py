# Grid setup - manages the state and rules of the game board.

class Grid:
    '''
    A class used to represent a grid for grid-based games, such as battleship.

    Parameters:
    -----------
    size    (int, optional):    The size of the grid (default is 10). This size is used to determine the grid's dimensions (size x size).
    
    Attributes:
    -----------
    grid            (list):     A matrix representing the game grid, where each cell can hold a value indicating a ship part, a hit, a miss, or empty.
    coordinates_x   (dict):     A dictionary mapping column labels (A, B, C, ...) to their respective 1-based numerical indices.
    coordinates_y   (dict):     A dictionary mapping row labels ('1', '2', '3', ...) to their respective 1-based numerical indices.

    Methods:
    --------
    initialize_grid(size=10)      
    _convert_coordinate_to_indices(coordinate) 
    _convert_indices_to_coordinate(column_index, row_index)
    _mark_water_around_ship(self, row_index, column_index)
    update_grid_fleet(start_coordinate, direction, fleet, size, shipname)   
    update_grid_attacks(coordinate=None)
    print_grid()
    
    Notes:
    ------
    This class is designed for grid-based games where tracking positions on a 2D grid is necessary. 
    It includes methods for initializing the grid, updating it with ship placements or attack results, and converting 
    between different coordinate systems. The class requires further implementation to fully handle game logic, such as 
    checking for overlapping ships, handling different attack types, and fixing coordinate conversion methods.
   ''' 
    
    def __init__(self, size=10):
        self.grid = self.initialize_grid(size)
    
        self.coordinates_x = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20
            }

        self.coordinates_y = {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            '11': 11, '12': 12, '13': 13, '14': 14, '15': 15,
            '16': 16, '17': 17, '18': 18, '19': 19, '20': 20
            }

    def initialize_grid(self, size=10):
        '''
        Initializes the grid as a list of lists (matrix) to a specified size, 
        with '.' indicating empty cells, and sets up row and column headers.

        Parameters:
            size    (int, optional):    The size of the grid, defaults to 10. 
                                        Determines both the width and height of the grid.

        Returns:
            list:   A 2D list (matrix) representing the initialized game grid.
        '''
        grid = []
        for _ in range(size + 1): 
            row = ['.'] * (size + 1) 
            grid.append(row) 
        
        # Fill in column headers
        column_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:size]
        for column, label in enumerate(column_labels, start=1):
            grid[0][column] = label

        # Fill in row headers
        for row in range(1, size + 1):
            grid[row][0] = str(row)
        
        return grid
    
    def _convert_coordinate_to_indices(self, coordinate):
        '''
        Converts a coordinate (e.g., 'A1') into 0-based grid indices.

        Parameters:
            coordinate  (str):  A string representing the grid coordinate, e.g., 'A1'.

        Returns:
            tuple:  A tuple containing two integers (column_index, row_index) 
                    representing 0-based grid indices.
        '''

        # Extract colum letter and row number from the coordinates
        column_letter = coordinate[0]
        row_number = coordinate[1:]

        # Convert to 0-based grid indices
        column_index = self.coordinates_x[column_letter]
        row_index = int(row_number)

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

        column_letter = chr(64 + column_index) # 64 is 'A' in ASCII code
        coordinate = column_letter + str(row_index) # coordinate string, e.g. A3

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
                if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]) and self.grid[new_row][new_col] == ".":
                    self.grid[new_row][new_col] = "~"

    def update_grid_fleet(self, start_coordinate, direction, fleet, size, shipname): # Input from player_placing_ships
        '''
        Updates the grid with a new ship placement based on the given parameters. It checks for valid placement 
        and updates the fleet's information with the ship's coordinates.

        Parameters:
            start_coordinate    (str):  The starting coordinate of the ship placement, e.g., 'A1'.
            direction           (str):  The direction of the ship placement, 'V' for vertical or 'H' for horizontal.
            fleet               (dict): A dictionary containing the fleet information, updated with the ship's coordinates.
            size                (int):  The size (length) of the ship being placed.
            shipname            (str):  The name of the ship being placed.

        Returns:
            bool:   True if the ship was successfully placed, 
                    False otherwise.
        '''
        
        if start_coordinate is None:
            print("Error: Coordinate cannot be None.")
            return False
        
        column_index, row_index = self._convert_coordinate_to_indices(start_coordinate)

        # Check if the starting coordinate is out of bounds.
        if row_index < 0 or row_index >= len(self.grid) or column_index < 0 or column_index >= len(self.grid[0]):
            print("Error: Coordinates are out of the grid bounds.")
            return False
        
        # Check if the ship placement exceed grid bounds
        if direction == "V" and row_index + size > len(self.grid):
            print("Error: Ship placement exceeds grid bounds vertically.") 
            return False
        if direction == "H" and column_index + size > len(self.grid[0]):
            print("Error: Ship placement exceeds grid bounds horizontally.")
            return False
        
        # Check if the spaces are free

        for i in range(size):
            if direction == "V":
                if self.grid[row_index + i][column_index] != ".": # Vertical checking
                    print("Error: Space is occupied by another ship.")
                    return False
            
            elif direction == "H":
                if self.grid[row_index][column_index + i] != ".": # Horizontal checking
                    print("Error: Space is occupied by another ship.")
                    return False

        # Place the ship 

        for i in range(size):

            if direction == "V":
                self.grid[row_index + i][column_index] = "X" # Vertical placement
                coordinate = self._convert_indices_to_coordinate(column_index, row_index + i)
                fleet[shipname]['coordinates'].append(coordinate)
                self._mark_water_around_ship(row_index + i, column_index)
            elif direction == "H":
                self.grid[row_index][column_index + i] = "X" # Horizontal
                coordinate = self._convert_indices_to_coordinate(column_index + i, row_index)
                fleet[shipname]['coordinates'].append(coordinate)
                self._mark_water_around_ship(row_index, column_index + i)
     
        return True

    def update_grid_attacks(self, coordinate=None): # TODO: redo for different kind of attacks (hits and misses)
        '''
        Updates the grid to reflect the result of an attack at the given coordinate.

        Parameters:

        Returns:
            
        
        '''
        if coordinate is None:
            return # TODO: We should insert a raise error here
    
        column_index, row_index = self._convert_coordinate_to_indices(coordinate)

        if row_index < 0 or row_index >= len(self.grid) or column_index < 0 or column_index >= len(self.grid[0]):
            print("Error: Coordinates are out of the grid bounds.")
            return
        
        # Update the grid cell

        self.grid[row_index][column_index] = "O"

    def print_grid(self):
        '''
        Prints the current state of the grid to the console, showing all ships, hits, 
        misses, and empty spaces.

        Returns:
            None:   This method does not return a value but outputs the grid state to the console.
        '''
        print()
        for row in self.grid:
            print(' '.join(f"{cell:<2}" for cell in row))
        print()

