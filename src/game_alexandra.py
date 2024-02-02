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
    for row in grid: 
        for cell in row:  
            print(cell, end=' ')  
        print()

create_grid = initialize_grid()  
print_grid(create_grid)

