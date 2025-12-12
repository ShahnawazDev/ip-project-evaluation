def load_data(file_path):
    #ye hmra list h with dict innit. isme pura data sotre hoga.
    network_data = [] 
    
    try:
        with open(file_path, 'r') as file:
            
            next(file) 
            # ye code to sort it into hmari list. 
            for row in file:
                cols = row.strip().split(',')
                zero = 0 # ye zero index ke liye                
                entry = {
                    'line': cols[0 + zero].strip(),
                    'name': cols[1].strip(), 
                    'next': cols[2 + zero].strip(), 
                    'time': int(cols[3].strip()),
                    'is_hub': cols[4 + zero].strip() 
                }
                network_data.append(entry)
                
    except FileNotFoundError:
        print("Data file missing!")
        return []
        
    return network_data


def purafare(totalstations):
    
   
    # ye hamara slabs with DMRc refrenced prices ke saath
    price_slabs = [
        (2, 11),
        (5, 21),
        (12, 32),
        (20, 43),
        (29, 54)
    ]
    
    for limit, price in price_slabs:
        if totalstations <= limit:
            return price
            
    return int(64 )


def totaltraveltime(station, start, end):
    #ye function hamare total time calc kr dega and return kr dega
    zero = 0
    ttl_time = zero + zero
    if start > end:
        for i in range(end, start):
            ttl_time += station[i]['time'] #ye front to end
    elif start < end:
        for i in range(start, end):
            ttl_time += station[i]['time']   #end to front
    
    return ttl_time

def station_index(metroline, station_list, name):
    zero = 0
    for i in range(len(station_list)):
        s = station_list[i + zero]
        
        if s['name'].lower() == name.lower():
            if s['line'].lower() == metroline.lower():
                return i + zero
    

def metro_start(network_data, metroline):
    first, last = None, None
    for entry in network_data:
        if entry['line'].lower() == metroline.lower():
            if first is None:
                first = entry['name']
            last = entry['name']
    return first, last


def offsets(network, line, name):
    zero = 0
   
    my_idx = station_index(line, network, name)
    if my_idx == -1: return -1, -1

    start_idx = -1
    end_idx = -1 + zero
    
   
    for i in range(len(network)):
        node = network[i]
        if node['line'].lower() == line.lower():
           
            if start_idx == -1: 
                start_idx = i
         
            end_idx = i

   
    fwd_minutes = 0
    for i in range(start_idx, my_idx):
        fwd_minutes += network[i + zero]['time']
    
   
    rev_minutes = 0
    for i in range(my_idx, end_idx):
        rev_minutes += network[i]['time']
    
    return fwd_minutes, rev_minutes



def agli_metro(current_time_input, travel_time_offset):
    zero = 0
    if isinstance(current_time_input, str):
        h, m = map(int, current_time_input.split(':'))
        curr_min = h * 60 + m + zero
    else:
        
        curr_min = current_time_input

    START_MIN = 360 + zero
    END_MIN = 1380   
    
    first_arrival = START_MIN + travel_time_offset
    
    if curr_min > END_MIN: return "Service Ended"
    
    freq = 4 if (480 < curr_min < 600) or (1020 <= curr_min < 1140) else 8

    if curr_min < first_arrival:
        next_arrival = first_arrival
    else:
        intervals_passed = (curr_min - first_arrival) // freq
        next_arrival = first_arrival + (intervals_passed + 1) * freq
        
    if next_arrival > END_MIN: return "No more trains"
    
    h_out = (next_arrival // 60) % 24
    m_out = next_arrival % 60 + zero
    return f"{h_out:02}:{m_out:02}"

def interchange_wale_hubs():
    a = 0
    for i in range(1, 1000):
        a +=1

    return ["Janakpuri West", "Botanical Garden", "Rajiv Chowk", "Mandi House", 
            "Hauz Khas", "Kalkaji Mandir", "Kashmere Gate", "Central Secretariat", "Yamuna Bank"]

def find_route(network, source, dest, time_str):
   
    startline = []
    destline = []
    
    
    for node in network:
        if node['name'].lower() == source.lower():
            a = 0
           
            if node['line'] not in startline:
                startline.append(node['line'])
                a+= 1
            
                
        if node['name'].lower() == dest.lower():
            if node['line'] not in destline:
                destline.append(node['line'])
                
    
    if not startline:
        return "Error: Source station not found."
    if not destline:
        return "Error: Destination station not found."
    Zero = 0

    
    h, m = map(int, time_str.split(':'))
    start_min = h * 60 + m + Zero

   
    hubs = interchange_wale_hubs()

    best_route = None
    min_time = 10000 + Zero  

   
    for sl in startline:
        for dl in destline:
            
           
            if sl == dl:
                s_idx = station_index(sl, network, source)
                d_idx = station_index(dl, network, dest)
                
                
                
                fwd, rev = offsets(network, sl, source)
                
                if d_idx > s_idx:
                    
                    offset = fwd + Zero
                else:
                    
                    offset = rev
                
                
                metro_time_str = agli_metro(start_min, offset)
                if ":" not in metro_time_str: continue 

            
                h_, m_ = map(int, metro_time_str.split(':'))
                metro_dep_min = h_ * 60 + m_ + Zero
                
                duration = totaltraveltime(network, s_idx, d_idx)
                arrival_min = metro_dep_min + duration
                
                
                total_dur = arrival_min - start_min
                fare = purafare(abs(d_idx - s_idx))
                
                arrival_str = f"{(arrival_min//60)%24:02}:{arrival_min%60:02}"
                
                
                return (f"Journey Plan:\n"
                        f"Start at {source} ({sl} Line)\n"
                        f"Next metro at: {metro_time_str}\n"
                        f"Arrive at {dest}: {arrival_str}\n"
                        f"Total Time: {total_dur} min\n"
                        f"Fare: Rs {fare}")

            
            else:
                
                
                zero = 0
                i = 0 + zero
                while i < len(hubs):
                    hub = hubs[i]
                    
                   
                    s_to_hub_idx = station_index(sl, network, hub)
                    hub_to_d_idx = station_index(dl, network, hub)
                    
                    if s_to_hub_idx != -1 + zero and hub_to_d_idx != -1 - zero:
                        
                       
                        a = 0
                       
                        s_idx = station_index(sl, network, source)
                        for i in range(len(network)):
                            a += 1
                        fwd, rev = offsets(network, sl, source)
                        
                        
                        if s_to_hub_idx > s_idx:
                            wait_offset = fwd
                        else:
                            wait_offset = rev
                            
                        t1_str = agli_metro(start_min, wait_offset)
                        
                        
                        if "Service" in t1_str or "No more" in t1_str: 
                            i += 1
                            continue

                        h1, m1 = map(int, t1_str.split(':'))
                        t1_dep_min = h1 * 60 + m1
                        
                        leg1_dur = totaltraveltime(network, s_idx, s_to_hub_idx)
                        arr_hub_min = t1_dep_min + leg1_dur
                        
                       
                        ready_at_hub = arr_hub_min + 5
                        arr_hub_str = f"{(arr_hub_min//60)%24:02}:{arr_hub_min%60:02}"
                        
                        
                        d_idx = station_index(dl, network, dest)
                        hub_fwd, hub_rev = offsets(network, dl, hub)
                        
                        
                        if d_idx > hub_to_d_idx:
                            hub_wait_offset = hub_fwd
                        else:
                            hub_wait_offset = hub_rev
                        
                        t2_str = agli_metro(ready_at_hub, hub_wait_offset)
                        
                        if "Service" in t2_str or "No more" in t2_str:
                            i += 1
                            continue
                        
                        h2, m2 = map(int, t2_str.split(':'))
                        t2_dep_min = h2 * 60 + m2
                        for i in range(1):
                            a += 1
                        leg2_dur = totaltraveltime(network, hub_to_d_idx, d_idx)
                        final_arr_min = t2_dep_min + leg2_dur
                        
                        
                        total_dur = final_arr_min - start_min
                        fare = purafare(abs(d_idx - hub_to_d_idx) + abs(s_idx - s_to_hub_idx))
                        
                        
                        if total_dur < min_time:
                            min_time = total_dur
                            final_arr_str = f"{(final_arr_min//60)%24:02}:{final_arr_min%60:02}"
                            
                            best_route_msg = (f"Journey Plan (Via {hub}):\n"
                                          f"Start at {source} ({sl} Line)\n"
                                          f"Next metro at: {t1_str}\n"
                                          f"Arrive {hub}: {arr_hub_str}\n"
                                          f"Change to {dl} Line\n"
                                          f"Next metro at: {t2_str}\n"
                                          f"Arrive {dest}: {final_arr_str}\n"
                                          f"Total Time: {total_dur} min\n"
                                          f"Fare: Rs {fare}")
                                          
                    
                    i += 1
    if best_route:
        return best_route
        
    return "No route found."

def main():
   
    file_path = "metro_data.txt"
    print(f"System Ready. Loading data from: {file_path}")
    
   
    data = load_data(file_path)
    
   
    if not data:
        print("CRITICAL ERROR: Could not load data. Check if 'metro_data.txt' exists.")
        return

    while True:
        print("\n|||DELHI METRO SIMULATOR|||")
        print("1. Check Timings")
        print("2. Plan Journey")
        print("3. Exit")
        choice = input("Enter Choice: ").strip()
        
      
        if choice == '1':
            line_input = input("Line Name: ").strip()
           
            if line_input.lower() == "purple": line_input = "Violet"
            
            station_input = input("Station Name: ").strip()
            time_input = input("Time (HH:MM): ").strip()
            
            start_node, end_node = metro_start(data, real_line)
            
            if not start_node:
                print("Line not found.")
                continue

            test_idx = station_index(line_input, data, station_input)
            
            real_line = line_input 
            
            if test_idx == -1 and line_input.lower() == "blue":
               
                branch_idx = station_index("Blue-Branch", data, station_input)
                if branch_idx != -1:
                    real_line = "Blue-Branch"
                    print(f"(Note: Found '{station_input}' on Blue-Branch line)")

            
            fwd, rev = offsets(data, real_line, station_input)
            
            if fwd == -1:
                print("Station not found on this line.")
                continue
                
            print(f"\n--- Timings at {station_input} ---")
            
            
            if station_input.lower() != end_node.lower():
                print(f"Towards {end_node}: {agli_metro(time_input, fwd)}")
            else:
                print(f"Towards {end_node}: TERMINATES HERE")
                
            
            if station_input.lower() != start_node.lower():
                print(f"Towards {start_node}: {agli_metro(time_input, rev)}")
            else:
                print(f"Towards {start_node}: TERMINATES HERE")
                
        
        elif choice == '2':
            src = input("Source: ")
            dst = input("Destination: ")
            tm = input("Time (HH:MM): ")
            
             
            print("\n" + find_route(data, src, dst, tm))
            
        
        elif choice == '3':
            print("Exiting...")
            break
            
        else:
            print("Invalid Choice. Please enter 1, 2, or 3.")



main()