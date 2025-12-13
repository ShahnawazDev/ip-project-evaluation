import datetime
import os

# Change to Sonakshi's directory
os.chdir('D:/py/ip-project/Sonakshi Rohliyan')

# Load data
blue = []
blue2 = []
magenta = []
airport = []
gray = []
green = []
stations = []

f = open("metro_data.txt", 'r')
for line in f.readlines():
    stripped_line = line.strip()
    if not stripped_line or stripped_line.startswith('Line,'):
        continue
    Line, Current_station, Time_for_next_station = stripped_line.split(", ")

    if Line == "Blue_common":
        blue.append(Current_station)
        blue.append(int(Time_for_next_station))
        stations.append([Current_station, "blue", int(Time_for_next_station)])

    if Line == "Blue_Vaishali":
        blue2.append(Current_station)
        blue2.append(int(Time_for_next_station))    
        stations.append([Current_station, "blue2", int(Time_for_next_station)])

    if Line == "Magenta":
        magenta.append(Current_station)
        magenta.append(int(Time_for_next_station))
        stations.append([Current_station, "magenta", int(Time_for_next_station)])
        
    if Line == "Airport_express":
        airport.append(Current_station)
        airport.append(int(Time_for_next_station))
        stations.append([Current_station, "airport", int(Time_for_next_station)])
        
    if Line == "Gray":
        gray.append(Current_station)
        gray.append(int(Time_for_next_station))
        stations.append([Current_station, "gray", int(Time_for_next_station)])
        
    if Line == "Green_main":
        green.append(Current_station)
        green.append(int(Time_for_next_station))
        stations.append([Current_station, "green", int(Time_for_next_station)])
f.close()

print(f"Data loaded:")
print(f"Blue line stations: {len([x for x in blue if isinstance(x, str)])}")
print(f"Blue2 (Vaishali) stations: {len([x for x in blue2 if isinstance(x, str)])}")
print(f"Magenta stations: {len([x for x in magenta if isinstance(x, str)])}")
print(f"Airport stations: {len([x for x in airport if isinstance(x, str)])}")
print(f"Gray stations: {len([x for x in gray if isinstance(x, str)])}")
print(f"Green stations: {len([x for x in green if isinstance(x, str)])}")
print(f"\nTotal station entries: {len(stations)}")

# Test journey: Dwarka to Botanical Garden (same line)
print("\n=== TEST 1: Same-line journey (Blue) ===")
start = "Dwarka Sector 21"
end = "Botanical Garden"

start_info = [start]
end_info = [end]

for i in range(0, len(stations)):
    if stations[i][0] == start:
        start_info.append(i)
        start_info.append(stations[i][1])
    if stations[i][0] == end:
        end_info.append(i)
        end_info.append(stations[i][1])

print(f"Start: {start} on line {start_info[2]}")
print(f"End: {end} on line {end_info[2]}")

# Check if same line
for i in range(0, len(end_info)):
    for j in range(0, len(start_info)):
        if end_info[i] == start_info[j]:
            print(f"Same line journey detected: {start_info[j]}")
            break

# Test journey: Janakpuri West to Terminal 1 - IGI Airport (different lines)
print("\n=== TEST 2: Interchange journey ===")
start2 = "Janakpuri West"
end2 = "Terminal 1 - IGI Airport"

start_info2 = [start2]
end_info2 = [end2]

for i in range(0, len(stations)):
    if stations[i][0] == start2:
        start_info2.append(i)
        start_info2.append(stations[i][1])
    if stations[i][0] == end2:
        end_info2.append(i)
        end_info2.append(stations[i][1])

print(f"Start: {start2} - appears on lines: ", end='')
for s in stations:
    if s[0] == start2:
        print(s[1], end=' ')
print(f"\nEnd: {end2} on line {end_info2[2]}")

# Count total lines
lines_covered = set()
for s in stations:
    lines_covered.add(s[1])
print(f"\n=== TOTAL LINES IN DATA: {len(lines_covered)} ===")
print(f"Lines: {sorted(lines_covered)}")
