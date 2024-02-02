
# Structure of grid and its coordinates
grid = [[" ","A","B","C","D","E","F","G","H","I","J"],
        ["0",".",".",".",".",".",".",".",".",".","."],
        ["1",".",".",".",".",".",".",".",".",".","."],
        ["2",".",".",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".",".",".","."],
        ]

coordinates_x = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
coordinates_y = {'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10}

# Game functions

def player_ships():
    '''This function asks the player where to place their ships.'''
    choice = input("Please enter the coordinates of your ship: ")
    return choice

def position_ships(grid, coordinates_x, coordinates_y, choice):
    '''This function places the players ships on the grid.'''
    coord_1 = coordinates_x[choice[0]]
    coord_2 = coordinates_y[choice[1]]
    grid[coord_2][coord_1] = "X"
    return grid

def print_grid(grid):
    '''This function prints the grid in its current state.'''
    print()
    for x in grid:
        for y in x:
            print(f"{y} ", end="")
        print()
    print()

# Main Script

print("\n This is the clear grid:")
print_grid(grid)

choice = player_ships()
grid = position_ships(grid, coordinates_x, coordinates_y, choice)
choice = player_ships()
grid = position_ships(grid, coordinates_x, coordinates_y, choice)
print_grid(grid)
