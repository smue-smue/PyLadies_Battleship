import pytest
from fleet import Fleet
from ship import Destroyer

@pytest.fixture
def test_fleet():
    """
    A pytest fixture that creates a new Fleet instance for testing.
    
    This fixture sets up a Fleet with a predefined name "Test Fleet" and returns it for use in test functions.
    
    Returns:
        Fleet: An instance of the Fleet class named "Test Fleet".
    """
    return Fleet("Test Fleet")

def test_add_ship(test_fleet):
    """
    Tests the ability of the Fleet class to add a ship.
    
    This test creates a Destroyer instance and adds it to the fleet. It then checks if the ship
    has been successfully added by verifying its presence in the fleet's ships dictionary.
    """
    destroyer = Destroyer("Test Destroyer")
    test_fleet.add_ship(destroyer)
    assert "Test Destroyer" in test_fleet.ships, "The destroyer should be added to the fleet."

def test_get_fleet_size(test_fleet):
    """
    Tests the Fleet class's ability to report the correct fleet size.
    
    After adding a single Destroyer to the fleet, this test verifies that the fleet's size 
    is reported as 1, indicating that the ship count is accurately maintained.
    """
    destroyer = Destroyer("Test Destroyer")
    test_fleet.add_ship(destroyer)
    assert test_fleet.get_fleet_size() == 1, "The fleet size should be 1 after adding one ship."

def test_update_ship_statuses(test_fleet):
    """
    Tests the update_ship_statuses method of the Fleet class.
    
    This test adds a Destroyer to the fleet, simulates a hit on this ship, and then calls 
    update_ship_statuses to update the fleet. The test checks that the method correctly 
    identifies that not all ships are sunk (since only one hit was recorded).
    """
    destroyer = Destroyer("Test Destroyer")
    test_fleet.add_ship(destroyer)
    test_fleet.ships["Test Destroyer"]['hits'].append('A1')
    all_sunk = test_fleet.update_ship_statuses()
    assert not all_sunk, "With only one hit, the ship should not be considered sunk."
