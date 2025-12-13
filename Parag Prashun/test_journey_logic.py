metro_lines={}
n_line=None
with open("metro_data.txt", "r") as f:
    for li in f:
        li=li.strip()
        if li == "":
            continue
        if li.startswith("/"):
            n_line = li[1:]
            metro_lines[n_line] =[]
            continue
        if n_line:
            try:
                parts = [p.strip() for p in li.split(",")]
                station = parts[0]
                time_min = parts[1] if len(parts) >= 2 else "0"
                metro_lines[n_line].append([station, int(time_min)])
            except Exception:
                pass

magenta = metro_lines.get("magenta",[])
blue = metro_lines.get("blue",[])
blue1 = metro_lines.get("blue1",[])

print(f"Loaded: Blue={len(blue)} stations, Blue1={len(blue1)} stations, Magenta={len(magenta)} stations\n")

# Test 1: Same line journey on Blue
print("=== Test 1: Same line journey (Dwarka to Rajiv Chowk on Blue) ===")
source = "Dwarka"
dest = "Rajiv Chowk"

# Find stations in blue line
source_found = False
dest_found = False
source_idx = -1
dest_idx = -1

for idx, (station, time) in enumerate(blue):
    if station == source:
        source_found = True
        source_idx = idx
    if station == dest:
        dest_found = True
        dest_idx = idx

if source_found and dest_found:
    print(f"✓ Both stations found in Blue line")
    print(f"  Source '{source}' at index {source_idx}")
    print(f"  Destination '{dest}' at index {dest_idx}")
    
    # Calculate travel time
    total_time = 0
    if dest_idx > source_idx:
        for i in range(source_idx, dest_idx):
            total_time += blue[i][1]
        print(f"  Travel time: {total_time} minutes")
    else:
        print(f"  ERROR: Destination comes before source")
else:
    print(f"✗ Stations not found: source_found={source_found}, dest_found={dest_found}")

# Test 2: Interchange journey (Blue to Magenta)
print("\n=== Test 2: Interchange journey (Dwarka to Botanical Garden) ===")
source2 = "Dwarka"
dest2 = "Botanical Garden"

source_in_blue = any(s[0] == source2 for s in blue)
dest_in_magenta = any(s[0] == dest2 for s in magenta)

print(f"Source '{source2}' in Blue: {source_in_blue}")
print(f"Destination '{dest2}' in Magenta: {dest_in_magenta}")

if source_in_blue and dest_in_magenta:
    print("✓ This is an interchange journey (Blue → Magenta)")
    print("  Interchange point: Janakpuri West or Botanical Garden")
else:
    print("✗ Cannot determine route")

# Test 3: Check if the actual q2() function would work with print
print("\n=== Test 3: Checking blue2, blue3, blue4, blue5 ===")
blue2 = metro_lines.get("blue2",[])
blue3 = metro_lines.get("blue3",[])
blue4 = metro_lines.get("blue4",[])
blue5 = metro_lines.get("blue5",[])

print(f"blue2: {len(blue2)} stations (should be 0 - NOT IN DATA)")
print(f"blue3: {len(blue3)} stations (should be 0 - NOT IN DATA)")
print(f"blue4: {len(blue4)} stations (should be 0 - NOT IN DATA)")
print(f"blue5: {len(blue5)} stations (should be 0 - NOT IN DATA)")

if len(blue2) == 0 and len(blue3) == 0 and len(blue4) == 0 and len(blue5) == 0:
    print("\n⚠️  CRITICAL: Code references blue2-5 but they don't exist in data!")
    print("   Most journey planner routes will return 'Route not found'")
