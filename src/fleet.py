from ship import Destroyer, Cruiser, Battleship, AircraftCarrier

# Creating ship instances
destroyer_1 = Destroyer("Destroyer 1")
destroyer_2 = Destroyer("Destroyer 2")
cruiser_1 = Cruiser("Cruiser 1")
battleship_1 = Battleship("Battleship 1")
aircraft_carrier_1 = AircraftCarrier("Aircraft Carrier 1")

# Create a dictionary to store the fleet
fleet = {}

# Manually add Destroyer instances to the fleet
fleet['Destroyer'] = {}
fleet['Destroyer'][destroyer_1.name] = {'size': destroyer_1.size, 'coordinates': []}
fleet['Destroyer'][destroyer_2.name] = {'size': destroyer_2.size, 'coordinates': []}

# Manually add Cruiser instance to the fleet
fleet['Cruiser'] = {}
fleet['Cruiser'][cruiser_1.name] = {'size': cruiser_1.size, 'coordinates': []}

# Manually add Battleship instance to the fleet
fleet['Battleship'] = {}
fleet['Battleship'][battleship_1.name] = {'size': battleship_1.size, 'coordinates': []}

# Manually add Aircraft Carrier instance to the fleet
fleet['Aircraft Carrier'] = {}
fleet['Aircraft Carrier'][aircraft_carrier_1.name] = {'size': aircraft_carrier_1.size, 'coordinates': []}

print(fleet)


# fleet = {
#     2: {"1st destroyer": [], "2nd destroyer": []},
#     3: {"Cruiser": []},
#     4: {"Battleship": []},
#     5: {"Aircraft Carrier": []}
#     }