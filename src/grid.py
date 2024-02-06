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

    # Initialize Grid ## Original Alexandra, Adapt Sandra

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
    
    def update_grid(self, coordinates=None, direction=None):
        '''
        This method updates the grid after changes to it.
        '''
        if coordinates is None:
            return ### We should insert a raise error here
        
        # Extract colum letter and row number from the coordinates
        column_letter = coordinates[0]
        row_number = coordinates[1:]

        # Convert to 0-based grid indices
        column_index = self.coordinates_x[column_letter]
        row_index = int(row_number) 

        if row_index < 0 or row_index >= len(self.grid) or column_index < 0 or column_index >= len(self.grid[0]):
            print("Error: Coordinates are out of the grid bounds.")
            return
        
        # Update the grid cell

        self.grid[row_index][column_index] = "X"

    # print grid ## Original Sandra, Adapt Alexandra
    def print_grid(self):
        '''
        This method prints the grid in its current state.
        '''
        print()
        for row in self.grid:
            print(' '.join(f"{cell:<2}" for cell in row))
        print()

