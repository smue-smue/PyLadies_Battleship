'''This module contains classes for warships.'''

class Ship:
    '''
    A Class to represent a general ship.

    Attributes:
    -----------
        name    (str):  Name of the ship. Unique identifier for the ship instance.
        style   (str):  Type of the ship. Defines the ship's role and capabilities.
        size    (int):  Size of the ship, representing how many grid spaces it occupies.


    Parameters:
    -----------
        name    (str):  Name of the ship.
        style   (str):  Type of the ship (e.g., Destroyer)
        size    (int):  Size of the ship, representing how many spaces of the grid it takes up.

    Example:
    --------
        >>> destroyer_2_pl = Destroyer("Destroyer 2")
        >>> cruiser_1_pl = Cruiser("Cruiser 1")
    '''

    def __init__(self, name, style, size):
        self.name = name # Attribute: Name of the ship
        self.style = style # Attribute: Type of the ship
        self.size = size # Attribute: Size of the ship

class Destroyer(Ship):
    '''
    A Subclass of Ship representing a destroyer, a smaller warship.

    Parameters:
        name    (str):  Name of the destroyer.

    Inherits from Ship with a fixed type "Destroyer" and size 2.

    '''
    def __init__(self, name):
        super().__init__(name, "Destroyer", 2)

class Cruiser(Ship):
    '''
    A subclass of Ship representing a cruiser, a medium-sized warship.

    Parameters:
        name    (str):  The name of the cruiser.

    Inherits from Ship with a fixed type "Cruiser" and size 3.
    '''
    def __init__(self, name):
        super().__init__(name, "Cruiser", 3)

class Battleship(Ship):
    '''
    A subclass of Ship representing a battleship, heavily armed and armored.

    Parameters:
        name    (str):  The name of the battleship.

    Inherits from Ship with a fixed type "Battleship" and size 4.
    '''
    def __init__(self, name):
        super().__init__(name, "Battleship", 4)

class AircraftCarrier(Ship):
    '''
    A subclass of Ship representing an aircraft carrier, a warship that serves as a airbase.

    Parameters:
        name    (str):  The name of the aircraft carrier.

    Inherits from Ship with a fixed type "Aircraft Carrier" and size 5.
    '''
    def __init__(self, name):
        super().__init__(name, "Aircraft Carrier", 5)
