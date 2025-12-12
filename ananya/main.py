
def time_to_min(T):
    h = T[0:2] 
    m = T[3:5]
    H = int(h)
    return (H * 60) + int(m)

def min_to_time(total_min):

    H = total_min // 60
    M = total_min % 60

    h = str(H)
    m = str(M)
    return h + ":" + m

def metro_data(data_file):
    stations_map = {}
    current_line = None
    try:
        with open(data_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or '---' in line or line.startswith("Station"): continue
                
                
                if "DELHI METRO DATA:BLUE LINE" in line:
                    current_line = "Blue"
                    continue
                if "DELHI METRO DATA:MAGENTA LINE" in line:
                    current_line = "Magenta"
                    continue
                
            
                if current_line:
                    parts = [p.strip() for p in line.split('  ') if p.strip()]
                    
                    if len(parts) >= 4:
                        station, next_station, travel_min, interchange = parts[0], parts[1], parts[2], parts[3]
                        
                        if current_line not in stations_map:
                            stations_map[current_line] = []
                        
                        stations_map[current_line].append({
                            'station': station,
                            'next': next_station,
                            'time': int(travel_min.replace('min', '').strip()),
                            'interchange': interchange
                        })
        return stations_map
    except:
        return None

def get_time_from_start(line, target_station, stations_map):
    time_sum = 0
    
    for stop_info in stations_map .get(line, []):
        if stop_info['station'] == target_station:
            return time_sum
        time_sum += stop_info['time']
    return -1

def get_time_between(line, start, end, stations_map):
    time_sum = 0
    counting = False
    
    for stop_info in stations_map[line]:
        if stop_info['station'] == start:
            counting = True
        
        if counting:
            time_sum += stop_info['time']
        
        
        if stop_info['next'] == end:
            return time_sum
    return 0

def calculate_next_metro_time(line, station, time_now, stations_map):
    current_time_min = time_to_min(time_now)
    

    if current_time_min < 360 or current_time_min > 1380:
        print(f"Next metro at {station}: No service available at {time_now}")
        return None

    #frequency
    H = current_time_min // 60
    busy_hours = (8 <= H < 10) or (17 <= H < 19)
    frequency = 4 if busy_hours else 8
        
    station_travel_time = get_time_from_start(line, station, stations_map)
    if station_travel_time == -1: return None
        
    
    next_metro_time = 360 + station_travel_time 
    
    
    while next_metro_time < current_time_min:
        next_metro_time += frequency
        
    if next_metro_time > 1380:
        print(f"Service already ended for the day.")
        return None
        
    print(f"Next metro at {min_to_time(next_metro_time)}")
    

    print(f"Subsequent metros at {min_to_time(next_metro_time + frequency)}, {min_to_time(next_metro_time + 2 * frequency)}")
    
    return next_metro_time

def plan_journey(source, destination, start_time, stations_map):
    start_time_min = time_to_min(start_time)
    

    starting_line = next((ln for ln, data in stations_map.items() if any(s['station'] == source for s in data)), None)
    ending_line = next((ln for ln, data in stations_map.items() if any(s['station'] == destination for s in data)), None)

    if starting_line or not ending_line:
        print("Error: Source or Destination station not found.")
        return

    print(f"\nJourney Plan:\nStart at {source} ({starting_line} Line)")
    
   
    if starting_line == ending_line:
        total_time = get_time_between(starting_line, source, destination, stations_map)
        next_metro_start_min = calculate_next_metro_time(starting_line, source, start_time, stations_map)
        
        if next_metro_start_min is None: return
        
        final_arrival_min = next_metro_start_min + total_time
        
        print(f"Final arrival time at {destination}: {min_to_time(final_arrival_min)}")
        print(f"Total travel time: {total_time} minutes")
        return

    
    INTERCHANGE_DELAY = 3 

    if starting_line == 'Blue':
        interchange_station = "Janakpuri West" 
        next_line = 'Magenta'
    else: 
        interchange_station = "Botanical Garden"
        next_line = 'Blue'
        
    
    time_to_transfer = get_time_between(starting_line, source, interchange_station, stations_map)
    next_metro_min = calculate_next_metro_time(starting_line, source, start_time, stations_map)
    
    if next_metro_min is None: return

    arrival_at_transfer = next_metro_min + time_to_transfer
    print(f"Arrive at {interchange_station} at {min_to_time(arrival_at_transfer)}")
    
    
    departure_from_transfer = arrival_at_transfer + INTERCHANGE_DELAY
    print(f"Transfer to {next_line} Line")
    print(f"Next {next_line} metro departs at {min_to_time(departure_from_transfer)}")
    

    time_from_transfer = get_time_between(ending_line, interchange_station, destination, stations_map)
    final_arrival_min = departure_from_transfer + time_from_transfer
    total_trip_time = final_arrival_min - start_time_min
    
    print(f"Arrive at {destination} at {min_to_time(final_arrival_min)}")
    print(f"Total travel time: {total_trip_time} minutes")
    

def main():
    DATA_FILE = "metro_data.txt"
    metro_info = metro_data(DATA_FILE)
    if not metro_info: 
        print("Error: Could not load metro data. Check 'metro_data.txt'.")
        return
    
    print("\n-------------------------------------------")
    print("         DELHI METRO SIMULATOR V2          ")
    print("-------------------------------------------\n")

    # 1. METRO TIMING TEST
    print("--- 1. METRO TIMINGS TEST ---")
    print(f"Current Time: 09:18 | Line: Blue | Station: Rajiv Chowk")
    calculate_next_metro_time("Blue", "Rajiv Chowk", "09:18", metro_info)
    
    # 2. JOURNEY PLANNER TEST 
    print("\n--- 2. JOURNEY PLANNER TEST (Interchange) ---")
    print(f"Start Time: 08:22 | Source: Dwarka | Destination: Botanical Garden")
    plan_journey("Dwarka", "Botanical Garden", "08:22", metro_info)

    # 3. Additional Test Case: Single Line
    print("\n--- 3. Single Line Journey Test ---")
    print(f"Start Time: 12:00 | Source: Kirti Nagar | Destination: Rajiv Chowk")
    plan_journey("Kirti Nagar", "Rajiv Chowk", "12:00", metro_info)
    
    # 4. Service Restriction Test (23:15)
    print("\n--- 4. Service Restriction Test ---")
    calculate_next_metro_time("Blue", "Dwarka Sector 21", "23:15", metro_info)

if __name__ == "__main__":
    main()