import pytest
from ship import Ship, Destroyer, Cruiser, Battleship, AircraftCarrier

def test_ship_initialization():
    """
    Tests the initialization of the Ship class.
    
    Verifies that a Ship instance can be created with the correct name, type, and size attributes.
    """
    ship = Ship("Generic Ship", "Type", 3)
    assert ship.name == "Generic Ship", "Ship name should be initialized correctly."
    assert ship.type == "Type", "Ship type should be initialized correctly."
    assert ship.size == 3, "Ship size should be initialized correctly."

def test_destroyer_initialization():
    """
    Tests the initialization of the Destroyer subclass.
    
    Ensures that a Destroyer instance inherits from Ship and is initialized with the correct name, fixed type 'Destroyer', and fixed size 2.
    """
    destroyer = Destroyer("Destroyer 1")
    assert destroyer.name == "Destroyer 1", "Destroyer name should be initialized correctly."
    assert destroyer.type == "Destroyer", "Destroyer type should be 'Destroyer'."
    assert destroyer.size == 2, "Destroyer size should be 2."

def test_cruiser_initialization():
    """
    Tests the initialization of the Cruiser subclass.
    
    Checks that a Cruiser instance inherits from Ship and has the correct name, fixed type 'Cruiser', and fixed size 3.
    """
    cruiser = Cruiser("Cruiser 1")
    assert cruiser.name == "Cruiser 1", "Cruiser name should be initialized correctly."
    assert cruiser.type == "Cruiser", "Cruiser type should be 'Cruiser'."
    assert cruiser.size == 3, "Cruiser size should be 3."

def test_battleship_initialization():
    """
    Tests the initialization of the Battleship subclass.
    
    Verifies that a Battleship instance inherits from Ship and is correctly initialized with a given name, fixed type 'Battleship', and fixed size 4.
    """
    battleship = Battleship("Battleship 1")
    assert battleship.name == "Battleship 1", "Battleship name should be initialized correctly."
    assert battleship.type == "Battleship", "Battleship type should be 'Battleship'."
    assert battleship.size == 4, "Battleship size should be 4."

def test_aircraft_carrier_initialization():
    """
    Tests the initialization of the AircraftCarrier subclass.
    
    Confirms that an AircraftCarrier instance inherits from Ship and is initialized with the correct name, fixed type 'Aircraft Carrier', and fixed size 5.
    """
    aircraft_carrier = AircraftCarrier("Aircraft Carrier 1")
    assert aircraft_carrier.name == "Aircraft Carrier 1", "Aircraft Carrier name should be initialized correctly."
    assert aircraft_carrier.type == "Aircraft Carrier", "Aircraft Carrier type should be 'Aircraft Carrier'."
    assert aircraft_carrier.size == 5, "Aircraft Carrier size should be 5."