# Player Setup



class Player():
    '''

    '''
    def __init__(self, name=None):
         self.name = name

    def prompt_for_player_name():
        '''
        Static method to prompt the user for their name.
        This method does not require access to the instance (self)
        or the class (cls).

        Returns:
            str: The name entered by the user.
        '''

        return input("Ready, Player? What's your name?\n")

    def player_ships():
        '''This function asks the player where to place their ships.'''

        fleet = {
                2: {"1st destroyer": [], "2nd destroyer": []},
                3: {"Cruiser": []},
                4: {"Battleship": []},
                5: {"Aircraft Carrier": []}
                }
    
        while True:
            for shipsize in fleet.keys():
                    for shiptype in fleet[shipsize].keys():
                        for coordinate in range(shipsize):
                            coordinate = input(f"Please enter a coordinate of your {shiptype} (total size: {shipsize} squares). ")
                            fleet[shipsize][shiptype].append(coordinate)
                            # Hier sicherstellen, dass c1 bei c2 etc. anschließt
                    # print grid for overview after each ship
            print(fleet)
            return fleet


    # def position_ships(create_grid, coordinates_x, coordinates_y, choice): # needs to be redone!
    #     '''This function places the players ships on the grid.'''
    #     coord_1 = coordinates_x[choice[0]]
    #     coord_2 = coordinates_y[choice[1]]
    #     create_grid[coord_2][coord_1] = "X"
    #     updated_grid = create_grid
    #     return updated_grid

    #################################

player_name = Player.prompt_for_player_name() # Calls the static method on the class
player = Player(player_name) # Creates a new Player instance with the provided name

