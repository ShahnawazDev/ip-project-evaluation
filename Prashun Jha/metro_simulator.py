f = open("/Users/prashunjha/Downloads/delhi_metro/metro_data.txt", "r")
lines = f.readlines()
f.close()

#i am  creating lines 1 as the first word is the line itself 
# i am not adding shortest route funtion as the blue line is always the shortest if i dont have to go to magenta statio
lines1 = lines[1:] 

metro_schedule = []
metro_schedule2 = []

start_station = input("Enter current station: ").strip()
end_station = input("Enter station where you want to go: ").strip()
time1 = input("enter current_time1: ")
ampm = input("enter am or pm: ")

for line in lines1:
    cs = line.strip().split(",")
    #now i will store all of them into nested list thats why i have created a csv file. 
    #i can just use split in csv file and everything is in list
      
    line_name = cs[0].strip()
    station = cs[1].strip()
    next_station = cs[2].strip()
    travel_time = int(cs[3].strip())
    interchange = cs[4].strip()
    
    if interchange.endswith("Yes"):
        interchange = "Yes"
    else:
        interchange = "No"
    #stored them into list   
    metro_schedule.append([station, next_station, travel_time, line_name, interchange])
#i have created this to make a reverse list 
#so that when we go in end_stationackward direction we dont have to accces first one and it would end_statione easier
for i in metro_schedule:
    metro_schedule2.append([i[1], i[0], i[2], i[3], i[4]])   

all_data = metro_schedule + metro_schedule2

def check_gap(h, ampm):
    h24 = h
    if ampm == "pm" and h != 12:
        h24 = h + 12
    if ampm == "am" and h == 12:
        h24 = 0
    # a 24 hour clock will make it easier and this function will handle the gap timings end_stationetween metro
    if (8 <= h24 < 10) or (17 <= h24 < 19):
        return 4
    else:
        return 8

def add_minutes(h, m, val):
    m = m + val
    while m >= 60:
        m = m - 60
        h = h + 1
    if h > 12:
        h = h - 12
    return h, m

def metro_simulator(start_station, end_station, time, am_pm):
    t_split = time.split(":")
    current_hour = int(t_split[0])
    current_minute = int(t_split[1])
    path = []
    path.append(start_station)
    
    curr = start_station
    visited = []
    visited.append(start_station)
    
    
    while curr != end_station:
        
        
        neighbors = []
        for x in all_data:
            if x[0] == curr:
                already_visited = False
                for v in visited:
                    if v == x[1]:
                        already_visited = True
                
                if already_visited == False:
                    neighbors.append(x[1])
        
        if len(neighbors) == 0:
            
            break

        
        next_stop = ""
        
        
        for n in neighbors:
            if n == end_station:
                next_stop = n
                break
        
        
        if next_stop == "":
            for n in neighbors:
                
                can_reach = False
                
                
                check_list = [n]
                
                temp_visited = []
                for v in visited:
                    temp_visited.append(v)
                temp_visited.append(n)
                for k in range(50):
                    new_check_list = []
                    found_in_inner = False
                    
                    for item in check_list:
                        if item == end_station:
                            found_in_inner = True
                            break
                        for y in all_data:
                            if y[0] == item:
                                is_seen = False
                                for tv in temp_visited:
                                    if tv == y[1]:
                                        is_seen = True
                                
                                if is_seen == False:
                                    new_check_list.append(y[1])
                                    temp_visited.append(y[1])
                    
                    if found_in_inner == True:
                        can_reach = True
                        break
                    
                    check_list = new_check_list
                    if len(check_list) == 0:
                        break
                
                if can_reach == True:
                    next_stop = n
                    break
        
       
        if next_stop != "":
            path.append(next_stop)
            visited.append(next_stop)
            curr = next_stop
        else:
            print("No path found.")
            return

    if len(path) == 0:
        print("No route available.")
        return

    print("Journey Plan:")
    
    first_line_name = ""
    for x in all_data:
        if x[0] == path[0] and x[1] == path[1]:
            first_line_name = x[3]
            break
            
    print(f"Start at {start_station} ({first_line_name} Line)")
    
    gap = check_gap(current_hour, am_pm)
    rem = current_minute % gap
    wait = 0
    if rem != 0:
        wait = gap - rem
    
    current_hour, current_minute = add_minutes(current_hour, current_minute, wait)
    print(f"Next metro at {current_hour:02d}:{current_minute:02d}")
    
    current_line = first_line_name
    
    start_h = int(t_split[0])
    start_m = int(t_split[1])
    start_total = start_h * 60 + start_m
    if am_pm == "pm" and start_h != 12:
        start_total += 720
        
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i+1]
        
        t_time = 0
        n_line = ""
        
        for x in all_data:
            if x[0] == u and x[1] == v:
                t_time = x[2]
                n_line = x[3]
                break
                
        if n_line != current_line:
            print(f"Arrive at {u} at {current_hour:02d}:{current_minute:02d}")
            print(f"Transfer to {n_line} Line and adding 10 mins for waliking")
            
            current_hour, current_minute = add_minutes(current_hour, current_minute, 10)
            
            gap_new = check_gap(current_hour, am_pm)
            rem_new = current_minute % gap_new
            wait_new = 0
            if rem_new != 0:
                wait_new = gap_new - rem_new
            
            current_hour, current_minute = add_minutes(current_hour, current_minute, wait_new)
            print(f"Next {n_line} metro departs at {current_hour:02d}:{current_minute:02d}")
            current_line = n_line
            
        current_hour, current_minute = add_minutes(current_hour, current_minute, t_time)
        
    print(f"Arrive at {end_station} at {current_hour:02d}:{current_minute:02d}")
    
    end_total = current_hour * 60 + current_minute
    if am_pm == "pm" and current_hour != 12:
        end_total += 720
    
    if end_total < start_total:
        end_total += 720
        
    print(f"Total travel time: {end_total - start_total} minutes")
metro_simulator(start_station, end_station, time1, ampm)