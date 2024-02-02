# Initialize Grid ## Original Alexandra, Adapt Sandra
def initialize_grid(size=10):
    # Create an empty grid with headers
    grid = []
    for _ in range(size + 1): 
        row = [] 
        for _ in range(size + 1):
            row.append('.')  
        grid.append(row) 
    
    # Fill in column headers
    column_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:size]
    for column, label in enumerate(column_labels):
        grid[0][column + 1] = label

    # Fill in row headers
    for row in range(1, size + 1):
        grid[row][0] = str(row)
    
    return grid

# print grid ## Original Sandra, Adapt Alexandra
def print_grid(grid):
    '''This function prints the grid in its current state.'''
    print()
    for row in grid:
        for cell in row:
            print(f"{cell:<2} ", end="")
        print()
    print()