#FUNCTIONS
def minutes(time):
    hours,mint=map(int, time.split(':'))
    return hours*60+mint
def minute_back(minutes):
    hours=minutes//60
    mint=minutes%60
    return f"{hours:02d}:{mint:02d}"
def peak(minutes):
    if (480 <= minutes < 600) or (1020 <= minutes < 1140):
        return True
    else:
        return False
def calculate_fare(num_stations):
    if num_stations <= 2:
        return 10
    elif num_stations <= 5:
        return 20
    elif num_stations <= 12:
        return 30
    elif num_stations <= 21:
        return 40
    elif num_stations <= 32:
        return 50
    else:
        return 60

def process_journey(line_data, start_st, end_st, user_time, metro_start, metro_end, freq):
    index_start = -1
    index_end = -1
    
    for x in range(len(line_data)):
        station_current = line_data[x][1].replace("_", " ").lower()
        station_next = line_data[x][2].replace("_", " ").lower()
        
        if station_current == start_st.lower():
            index_start = x
        if station_next == end_st.lower():
            index_end = x
    if index_end == -1 and line_data[-1][2].replace("_", " ").lower() == end_st.lower():
         index_end = len(line_data) - 1

    if index_start == -1 or index_end == -1:
        return None

    duration = 0
    if index_start < index_end:
        for i in range(index_start, index_end + 1):
             if i < len(line_data): 
                 duration = duration + int(line_data[i][3])

        next_train = metro_start + int(line_data[0][3])
    else:

        for i in range(index_end, index_start):
             if i < len(line_data): 
                 duration = duration + int(line_data[i][3])

        next_train = metro_start + int(line_data[-1][3])

    next_train = next_train + (freq * index_start)
    

    while next_train <= user_time:
        next_train = next_train + freq
        
    arrival_time = next_train + duration
    return (next_train, arrival_time, duration)

def get_station_count(line_data, start_st, end_st):
    index_start = -1
    index_end = -1
    
    for x in range(len(line_data)):
        station_current = line_data[x][1].replace("_", " ").lower()
        station_next = line_data[x][2].replace("_", " ").lower()
        
        if station_current == start_st.lower():
            index_start = x
        if station_next == end_st.lower():
            index_end = x
            
    if index_end == -1 and line_data[-1][2].replace("_", " ").lower() == end_st.lower():
         index_end = len(line_data) - 1

    if index_start != -1 and index_end != -1:
        if index_start > index_end:
            return index_start - index_end
        else:
            return index_end - index_start
            
    return None


#DATA OPENING
f = open("metro_data.txt", "r")
all_lines = f.readlines()
f.close()

blue = []
blue_vaishali = []
magenta = []
interchange = []
magenta_time= []

for line in all_lines:
    line = line.strip()
    if line[0] == "#":  
        continue
    
    data = line.split()
    if data[0] == "Blue":
        blue.append(data)
    elif data[0] == "Blue-Vaishali":
        blue_vaishali.append(data)
    elif data[0] == "Magenta":
        magenta.append(data)
    

    if data[6].startswith("Yes"):
        interchange.append(data)

# USER INPUT
metro_start=60*6
metro_end=60*23+30
print("\n--------DELHI METRO SIMULATOR--------")
while True:
    print("1. Find Next Train")
    print("2. Plan Route")
    print("3. Check Fare")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "4":
        print("Thank you for using Delhi Metro Simulator!")
        break
    elif choice == "1":
        index_start=0
        index_end=0
        metro_line=input("Enter Metro Line(blue/blue-vaishali/magenta):")
        current_station=input("Enter Current Station:")
        time=input("Enter Time (HH:MM):")
        towards=input("Next station:")
        usertime=minutes(time)
        if usertime<metro_start:
            print( "Metro start from 06:00 AM")
        if usertime>metro_end:
            print( "Metro service ends at 11:30 PM")
        if peak(usertime):
            frequency = 4  
        else:
            frequency = 8 

        
        if metro_line.lower()=="magenta":
            for x in range(len(magenta)):
                station_current = magenta[x][1].replace("_", " ").lower()
                station_next = magenta[x][2].replace("_", " ").lower()
                if station_current == current_station.lower():
                    index_start = x
                if station_next == towards.lower():
                    index_end = x
                if index_start < index_end:
                    terminal = magenta[-1][2].replace("_", " ")
                    next_train=metro_start+int(magenta[0][3])
                else:
                    terminal = magenta[0][1].replace("_", " ")
                    next_train=metro_start+int(magenta[23][3])
                next_train=next_train+(frequency*index_start)
                train_times = [next_train]
                temp_time = next_train
                for i in range(3):
                    temp_time = temp_time + frequency 
                    if temp_time < metro_end:
                        train_times.append(temp_time)
                print("\nOutput:")
                print("Next metro at " + minute_back(next_train))
                if len(train_times) > 1:
                    subsequent = ""
                    for i in range(1, len(train_times)):
                        subsequent = subsequent + minute_back(train_times[i])
                        if i < len(train_times) - 1:
                            subsequent = subsequent + ", "
        
                    print("Subsequent metros at " + subsequent + ", ...")

        elif metro_line.lower() == "blue-vaishali":
            for x in range(len(blue_vaishali)):
                station_current = blue_vaishali[x][1].replace("_", " ").lower()
                station_next = blue_vaishali[x][2].replace("_", " ").lower()
                
                if station_current == current_station.lower():
                    index_start = x
                if station_next == towards.lower():
                    index_end = x
                
                # Logic for calculating the next train
                if index_start < index_end:
                    terminal = blue_vaishali[-1][2].replace("_", " ")
                    next_train = metro_start + int(blue_vaishali[0][3])
                else:
                    terminal = blue_vaishali[0][1].replace("_", " ")
                    next_train = metro_start + int(blue_vaishali[-1][3])
                
                next_train = next_train + (frequency * index_start)
                train_times = [next_train]
                temp_time = next_train
                
                for i in range(3):
                    temp_time = temp_time + frequency 
                    if temp_time < metro_end:
                        train_times.append(temp_time)
                
                print("\nOutput:")
                print("Next metro at " + minute_back(next_train))
                
                if len(train_times) > 1:
                    subsequent = ""
                    for i in range(1, len(train_times)):
                        subsequent = subsequent + minute_back(train_times[i])
                        if i < len(train_times) - 1:
                            subsequent = subsequent + ", "
        
                    print("Subsequent metros at " + subsequent + ", ...")
                elif metro_line.lower() == "blue":
                    for x in range(len(blue)):
                        station_current = blue[x][1].replace("_", " ").lower()
                        station_next = blue[x][2].replace("_", " ").lower()
                        if station_current == current_station.lower():
                            index_start = x
                        if station_next == towards.lower():
                            index_end = x
                    
                    if index_start != -1 and index_end != -1:
                        if index_start < index_end:
                            terminal = blue[-1][2].replace("_", " ")
                            next_train = metro_start + int(blue[0][3])
                        else:
                            terminal = blue[0][1].replace("_", " ")
                            next_train = metro_start + int(blue[-1][3])
                        
                        next_train = next_train + (frequency * index_start)

                        while next_train <= usertime:
                            next_train += frequency

                        train_times = [next_train]
                        temp_time = next_train
                        for i in range(3):
                            temp_time = temp_time + frequency 
                            if temp_time < metro_end:
                                train_times.append(temp_time)
                        
                        print("\nOutput:")
                        print("Next metro at " + minute_back(next_train))
                        if len(train_times) > 1:
                            subsequent = ""
                            for i in range(1, len(train_times)):
                                subsequent = subsequent + minute_back(train_times[i])
                                if i < len(train_times) - 1:
                                    subsequent = subsequent + ", "
                            print("Subsequent metros at " + subsequent + ", ...")
                    else:
                        print("Station or direction not found in Blue Line.")

    elif choice == "2":
        print("\n--- Plan Route ---")
        start_st = input("Enter Start Station: ").strip()
        end_st = input("Enter Destination: ").strip()
        time_input = input("Enter Time (HH:MM): ")
        usertime = minutes(time_input)

        if usertime < metro_start or usertime > metro_end:
            print("Metro is closed.")
            continue
            
        if peak(usertime):
            freq = 4
        else:
            freq = 8

        all_routes = [("Blue", blue), ("Blue-Vaishali", blue_vaishali), ("Magenta", magenta)]
        
        route_found = False

        for line_name, line_data in all_routes:
            res = process_journey(line_data, start_st, end_st, usertime, metro_start, metro_end, freq)
            
            if res:
                dept, arr, dur = res
                print("\nJourney Plan: Direct - " + line_name + " Line")
                print("Depart " + start_st + ": " + minute_back(dept))
                print("Arrive " + end_st + ": " + minute_back(arr))
                print("Total Time: " + str(dur) + " mins")
                route_found = True
                break
        
        if not route_found:
            interchanges = ["Janakpuri West", "Botanical Garden", "Yamuna Bank"]
            
            for hub in interchanges:
                leg1_info = None
                leg1_name = ""
                
                for line_name, line_data in all_routes:
                    res = process_journey(line_data, start_st, hub, usertime, metro_start, metro_end, freq)
                    if res:
                        leg1_info = res
                        leg1_name = line_name
                        break 
                
                if not leg1_info:
                    continue 

                dept1, arr1, dur1 = leg1_info
                transfer_time = arr1 + 10 
                
                leg2_info = None
                leg2_name = ""
                
                for line_name, line_data in all_routes:
                    res = process_journey(line_data, hub, end_st, transfer_time, metro_start, metro_end, freq)
                    if res:
                        leg2_info = res
                        leg2_name = line_name
                        break 
                
                if leg1_info and leg2_info:
                    dept2, arr2, dur2 = leg2_info
                    print("\nJourney Plan: Interchange at " + hub)
                    print("1. " + leg1_name + " Line: " + start_st + " -> " + hub)
                    print("   Depart: " + minute_back(dept1) + " | Arrive: " + minute_back(arr1))
                    print("   -- Transfer (10 mins) --")
                    print("2. " + leg2_name + " Line: " + hub + " -> " + end_st)
                    print("   Depart: " + minute_back(dept2) + " | Arrive: " + minute_back(arr2))
                    print("Total Time: " + str(arr2 - dept1) + " mins")
                    route_found = True
                    break
        
        if not route_found:
            print("No route found between these stations.")

    elif choice == "3":
        print("\n--- Check Fare ---")
        start_st = input("Enter Start Station: ").strip()
        end_st = input("Enter Destination: ").strip()
        
        all_routes = [("Blue", blue), ("Blue-Vaishali", blue_vaishali), ("Magenta", magenta)]
        fare_found = False
        total_stations = 0

        for line_name, line_data in all_routes:
             dist = get_station_count(line_data, start_st, end_st)
             if dist is not None:
                 total_stations = dist
                 fare_found = True
                 break

        if not fare_found:
             interchanges = ["Janakpuri West", "Botanical Garden", "Yamuna Bank"]
             for hub in interchanges:
                 leg1 = None
                 for line_name, line_data in all_routes:
                     d = get_station_count(line_data, start_st, hub)
                     if d is not None:
                         leg1 = d
                         break
                 if leg1 is None: continue 

                 leg2 = None
                 for line_name, line_data in all_routes:
                     d = get_station_count(line_data, hub, end_st)
                     if d is not None:
                         leg2 = d
                         break
                 
                 if leg1 is not None and leg2 is not None:
                     total_stations = leg1 + leg2
                     fare_found = True
                     break

        if fare_found:
            fare = calculate_fare(total_stations)
            print("Total Stations: " + str(total_stations))
            print("Estimated Fare: " + str(fare) + " Rupees")
        else:
            print("Could not calculate fare (Route not found).")
            
    else:
        print("Invalid choice! Please try again.")