'''
Tests for Fleet and Ship classes, including initialization, ship addition, 
status updates, and string representation.
'''
from fleet import Fleet

class Ship:
    '''
    Represents a ship with a name and size, to be used within a Fleet.
    '''
    def __init__(self, name, size):
        self.name = name
        self.size = size

def test_fleet_initialization():
    '''
    Test the initialization of a Fleet class.
    The fleet should be correctly initialized with the provided name and ships.
    '''
    ship1 = Ship("Ship1", 3)
    ship2 = Ship("Ship2", 4)
    fleet = Fleet("Test Fleet", ship1, ship2)
    assert fleet.name == "Test Fleet"
    assert fleet.get_fleet_size() == 2

def test_add_ship():
    '''
    Test the add_ship method of the Fleet class.
    The method should correctly add a ship to the fleet.
    '''
    ship1 = Ship("Ship1", 3)
    fleet = Fleet("Test Fleet")
    fleet.add_ship(ship1)
    assert fleet.get_fleet_size() == 1

def test_update_ship_statuses():
    '''
    Test the update_ship_statuses method of the Fleet class.
    The method should correctly update the status of each ship in the fleet 
    based on the hits received.
    '''
    ship1 = Ship("Ship1", 3)
    fleet = Fleet("Test Fleet", ship1)
    fleet.ships[ship1.name]['hits'] = [1, 2, 3]  # Simulate 3 hits
    assert fleet.update_ship_statuses() is True  # All ships should be sunk

def test_str_representation():
    '''
    Test the __str__ method of the Fleet class.
    The method should correctly return a human-readable string representation of the fleet.
    '''
    ship1 = Ship("Ship1", 3)
    fleet = Fleet("Test Fleet", ship1)
    expected_str = "Fleet 'Test Fleet' with ships:\n  Ship1: (Hits: 0, Size: 3, Status: active)\n"
    assert str(fleet) == expected_str
