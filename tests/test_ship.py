'''
Unit tests for Ship class and its subclasses, 
verifying correct initialization and inheritance.
'''

from ship import Ship, Destroyer, Cruiser, Battleship, AircraftCarrier

def test_ship_initialization():
    """
    Tests the initialization of the Ship class.
    
    Verifies that a Ship instance can be created with the correct name, style, and size attributes.
    """
    ship = Ship("Generic Ship", "Style", 3)
    assert ship.name == "Generic Ship", "Ship name should be initialized correctly."
    assert ship.style == "Style", "Ship style should be initialized correctly."
    assert ship.size == 3, "Ship size should be initialized correctly."

def test_destroyer_initialization():
    """
    Tests the initialization of the Destroyer subclass.
    
    Ensures that a Destroyer instance inherits from Ship and is initialized with the correct name, 
    fixed style 'Destroyer', and fixed size 2.
    """
    destroyer = Destroyer("Destroyer 1")
    assert destroyer.name == "Destroyer 1", "Destroyer name should be initialized correctly."
    assert destroyer.style == "Destroyer", "Destroyer style should be 'Destroyer'."
    assert destroyer.size == 2, "Destroyer size should be 2."

def test_cruiser_initialization():
    """
    Tests the initialization of the Cruiser subclass.
    
    Checks that a Cruiser instance inherits from Ship and has the correct name, 
    fixed style 'Cruiser', and fixed size 3.
    """
    cruiser = Cruiser("Cruiser 1")
    assert cruiser.name == "Cruiser 1", "Cruiser name should be initialized correctly."
    assert cruiser.style == "Cruiser", "Cruiser style should be 'Cruiser'."
    assert cruiser.size == 3, "Cruiser size should be 3."

def test_battleship_initialization():
    """
    Tests the initialization of the Battleship subclass.
    
    Verifies that a Battleship instance inherits from Ship and is correctly initialized 
    with a given name, fixed style 'Battleship', and fixed size 4.
    """
    battleship = Battleship("Battleship 1")
    assert battleship.name == "Battleship 1", "Battleship name should be initialized correctly."
    assert battleship.style == "Battleship", "Battleship style should be 'Battleship'."
    assert battleship.size == 4, "Battleship size should be 4."

def test_aircraft_carrier_initialization():
    """
    Tests the initialization of the AircraftCarrier subclass.
    
    Confirms that an AircraftCarrier instance inherits from Ship and is initialized 
    with the correct name, fixed style 'Aircraft Carrier', and fixed size 5.
    """
    aircraft_carrier = AircraftCarrier("Aircraft Carrier 1")
    assert aircraft_carrier.name == (
        "Aircraft Carrier 1", "Aircraft Carrier name should be initialized correctly."
    )
    assert aircraft_carrier.style == (
        "Aircraft Carrier", "Aircraft Carrier style should be 'Aircraft Carrier'."
    )
    assert aircraft_carrier.size == 5, "Aircraft Carrier size should be 5."
