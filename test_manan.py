import sys
import os

# Change to manan directory and load module without triggering main
os.chdir('manan')
exec(open('metro_simulator.py').read().replace('if __name__ == "__main__":', 'if False:'))

# Load data
data = loadmetro("metro_data.txt")
stations_by_line, station_lines, interchanges, line_map, station_map = data

print("=" * 60)
print("TESTING MANAN'S METRO SIMULATOR")
print("=" * 60)

# Test 1: Metro Timings
print("\n--- TEST 1: Metro Timings ---")
print("Line: Blue, Station: Rajiv Chowk, Time: 09:18")
trains = nexttrains("Blue", "Rajiv Chowk", "09:18", stations_by_line)
if trains:
    print(f"Next metro at {trains[0]}")
    if len(trains) > 1:
        print(f"Following metros: {', '.join(trains[1:])}")
else:
    print("No trains available")

# Test 2: Journey Planner - Interchange
print("\n--- TEST 2: Journey Planner (Interchange) ---")
print("Source: Dwarka, Destination: Botanical Garden, Time: 08:22")
result = planjourney("Dwarka", "Botanical Garden", "08:22", data)
printjourney(result)

# Test 3: Journey Planner - Same Line
print("\n--- TEST 3: Journey Planner (Same Line) ---")
print("Source: Kirti Nagar, Destination: Rajiv Chowk, Time: 12:00")
result = planjourney("Kirti Nagar", "Rajiv Chowk", "12:00", data)
printjourney(result)

# Test 4: Service Hours
print("\n--- TEST 4: Service Hours Test ---")
print("Line: Blue, Station: Dwarka Sector 21, Time: 23:15")
trains = nexttrains("Blue", "Dwarka Sector 21", "23:15", stations_by_line)
if trains:
    print(f"Next metro at {trains[0]}")
else:
    print("No service available at 23:15")

# Check data completeness
print("\n--- DATA COMPLETENESS ---")
print(f"Lines loaded: {', '.join(stations_by_line.keys())}")
print(f"Blue Line stations: {len(stations_by_line.get('Blue', {}))}")
print(f"Magenta Line stations: {len(stations_by_line.get('Magenta', {}))}")
if 'Airport Express' in stations_by_line:
    print(f"Airport Express stations: {len(stations_by_line.get('Airport Express', {}))}")
print(f"Total interchange points: {len(interchanges)}")
print(f"Interchanges: {', '.join(sorted(interchanges))}")
