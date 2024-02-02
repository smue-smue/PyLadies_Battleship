# Player Setup
player1 = input("Ready, Player? What's your name?\n")
player2 = "Computer-Player"

# Coin Flip who starts:
from random import randrange
coin = randrange(2)

if coin == 0:
    beginner = player1
    print(beginner, "starts.")
else:
    beginner = player2
    print(beginner, "starts.")
 

# Initialize Grid
def initialize_grid(size=10):
    grid = []
    for _ in range(size): 
        row = [] 
        for _ in range(size):  
            row.append('.')  
        grid.append(row) 
    return grid

# Print Grid 
def print_grid(grid):
    column_labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(grid[0])]

    # Print the column labels with additional space for a "square grid"
    print("   ", end='')
    for label in column_labels:
        print(label + ' ', end=' ') 
    print()

    # Initialize a counter for the row numbers
    row_number = 1

    # Loop through each row in the grid
    for row in grid:
        # Print the row number followed by two spaces, aligned to 2 characters wide
        print(f"{row_number:<2} ", end='')

        # Loop through each cell in the row
        for cell in row:            
            print(cell + ' ', end=' ')
        
        # Print a newline after each row
        print()

        # Increment the row number counter
        row_number += 1

# Create a grid by calling initialize_grid
create_grid = initialize_grid()

# Pass the created grid to print_grid
print_grid(create_grid)

# Player Ship Placement

# Computer Ship Placement

# Gameplay Loop

# Hit/Miss Check

# Game End Condition

