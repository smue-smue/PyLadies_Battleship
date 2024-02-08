# Grid setup - manages the state and rules of the game board.

class Grid:
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
        This method creates an empty grid with headers for columns
        and rows. It sets up the grid as a list of lists (matrix),
        where each cell is initialized to '.'.
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

        # Extract colum letter and row number from the coordinates
        column_letter = coordinate[0]
        row_number = coordinate[1:]

        # Convert to 0-based grid indices
        column_index = self.coordinates_x[column_letter]
        row_index = int(row_number)

        return column_index, row_index
    
    def _convert_indices_to_coordinate(self, column_index, row_index):

        column_letter = chr(64 + column_index) # 64 is 'A' in ASCII code
        coordinate = column_letter + str(row_index) # coordinate string, e.g. A3

        return coordinate

    def update_grid_fleet(self, start_coordinate, direction, fleet, size): # Input from player_placing_ships
        '''
        Updates the grid after each placed ship by player and computer.
        Returns True if the ship was successfully placed, False otherwise.
        '''

        # TODO: umliegende Felder sperren und zu "w" machen
        
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
                coordinate = self._convert_indices_to_coordinate(row_index + 1, column_index)
                fleet[shipname]['coordinates'].append(coordinate) # ================================= BLÖDSINN?

            elif direction == "H":
                self.grid[row_index][column_index + i] = "X" # Horizontal
            
        return True


        




    def update_grid_attacks(self, coordinate=None): # TODO: redo for different kind of attacks (hits and misses)
        '''
        This method updates the grid after changes to it.
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
        This method prints the grid in its current state.
        '''
        print()
        for row in self.grid:
            print(' '.join(f"{cell:<2}" for cell in row))
        print()

