f=open("metro_data.txt", "r")
data = f.readlines()
f.close()

list=[]
for i in range(len(data)):
    new_data=data[i].strip().split(",")
    list.append(new_data)

#Phase 2- Part A

line=input("Line= ")
station=input("Station= ")
time=input("Current Time= ")

h, m = map(int, time.split(":")) #we convert(HH:MM) to minutes
minutes = h * 60 + m

if minutes>1380:
    print("No service available") #no metro can come after 11:00
    quit()
        
peakA = 8 * 60 #1st peak starts
peakAx = 10 * 60 #1st peak ends
peakB = 17 * 60 #2nd peak starts 
peakBx = 19 * 60 #3rd peak ends

if(peakA<=minutes<=peakAx): #peak frequency is 4(given)
    frequency=4
elif(peakB<=minutes<=peakBx): 
    frequency=4
else:
    frequency=8 #non peak frequency is 8(given)

exist = False
for row in list:
    if row[0].strip() == line:
        if row[1].strip() == station:
            exist = True
            break

if not exist:
    print("Station or Line not found")
    quit()

open_time = 6 * 60  

if minutes <= open_time:
    next_metro = open_time 
else:
    extra_time = minutes - open_time #how much time has it been since metro station opened
    last_metro = extra_time % frequency #how much time as it been since the last metro arrived
    if last_metro == 0:  #if last metro arrived 0 mins ago that means the metro will come now
        next_metro = minutes
    else:
        next_metro = minutes + (frequency - last_metro) #in how many mins will the next metro arrives+current time

def normal_time(minutes): #we convert it back to readable time
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

print("Next metro at: ", normal_time(next_metro)) #print our outputs
print("Subsequent metro at:", end="")
for i in range(1, 4):
    print(normal_time(next_metro + i * frequency),end=",") #print our outputs

#Phase 2- Part B

source=input("Source: ")
destination=input('Destination: ')
time_travel=input("Time of travel: ")

h, m = map(int, time_travel.split(":")) #we convert(HH:MM) to minutes
start_minutes = h * 60 + m

if start_minutes>1380:
    print("No service available") #no metro can come after 11:00
    quit()

def line_identifier(station): #we define a fn to check if the line exist
    lines = []
    for row in list: #list referers to the original list of all the data from metro_data.txt
        if row[1].strip() == station:
            if row[0].strip() not in lines:
                lines.append(row[0].strip())
    return lines

source_lines = line_identifier(source) 
destination_lines = line_identifier(destination) #these functions will return the list lines which will give us which lines do the stations belong to

if len(source_lines) == 0: #error checker for wrong input
    print("Station not found in any line.")
elif len(destination_lines) == 0:
    print("Station not found in any line.")
    quit()

def get_order_for_line(line_name):
    edges = []
    for row in list:
        if row[0].strip() == line_name:#this logic has been used to find the correct order of stations from the source to the destination
            a = row[1].strip()
            b = row[2].strip()

            if b != "None":
                if a not in edges:
                    edges[a] = []
                if b not in edges:
                    edges[b] = []

                edges[a].append(b)
                edges[b].append(a)

    start = None
    for st in edges:
        if len(edges[st]) == 1:
            start = st
            break

    order = [start]
    visited = {start}

    while True:
        curr = order[-1]
        next_stations = [s for s in edges[curr] if s not in visited]
        if not next_stations:
            break
        nxt = next_stations[0]
        order.append(nxt)
        visited.add(nxt)

    return order

same_line = None

for line_name in source_lines:
    station_order = get_order_for_line(line_name)
    if (source in station_order) and (destination in station_order):
        same_line = line_name
        break

peakA = 8 * 60 #1st peak starts
peakAx = 10 * 60 #1st peak ends
peakB = 17 * 60 #2nd peak starts 
peakBx = 19 * 60 #3rd peak ends

if(peakA<=start_minutes<=peakAx): #peak frequency is 4(given)
    freq=4
elif(peakB<=start_minutes<=peakBx): 
    freq=4
else:
    freq=8 #non peak frequency is 8(given)

open_time = 6 * 60 

if start_minutes <= open_time:#we can find the next metro using the saem logic we used in part A
    next_train_source = open_time
else:
    diff = start_minutes - open_time
    remndr = diff % freq
    if remndr == 0:
        next_train_source = start_minutes
    else:
        next_train_source = start_minutes + (freq - remndr)

if same_line is not None:  # output if both source and destination are on the same line
    print("Journey Plan :")
    print(f"Start at {source} ({same_line})")
    print("Line:", same_line)
    print("Next metro at", normal_time(next_train_source))

    station_order = get_order_for_line(same_line)

    index1 = station_order.index(source)       # index for source station
    index2 = station_order.index(destination)  # index for destination station

    total_time = 0

    step = 1 if index1 < index2 else -1

    current_time = next_train_source
    i = index1

    while i != index2:
        source_st = station_order[i]
        destination_st = station_order[i + step]
        segment_time = None
        for row in list:
            if row[0].strip() == same_line:
                station1 = row[1].strip()
                station2 = row[2].strip()
                if (station1 == source_st and station2 == destination_st) or \
                   (station1 == destination_st and station2 == source_st):
                    segment_time = int(row[3])
                    break
        
        current_time += segment_time
        total_time += segment_time
        i += step

    print("Arrive at", destination, "at", normal_time(current_time))
    print("\nTotal travel time:", total_time, "minutes")
    quit()

#this was the code for same line now we write the code for interchange
def get_frequency(t):
    if (8*60 <= t <= 10*60) or (17*60 <= t <= 19*60):
        return 4
    return 8

print("\nJourney Plan:")
print(f"Start at {source} ({source_lines})")
print("Next metro at", normal_time(next_train_source))

source_line = source_lines[0]
dest_line = destination_lines[0]

interchange_station = ["Janakpuri West", "Janak Puri West", "Botanical Garden"] #interchanging stations

interchange = None

source_order = get_order_for_line(source_line)
destination_order = get_order_for_line(dest_line)

for x in interchange_station: # we find if there is a interchange station
    if x in source_order and x in destination_order:
        interchange = x
        break

if interchange is None: #interchange non-exist output
    print("No interchange possible.")
    quit()

def compute_arrival(line, start_station, end_station, depart_time): 
    order = get_order_for_line(line)
    i1 = order.index(start_station)
    i2 = order.index(end_station)
    step = 1 if i1 < i2 else -1
    current = depart_time
    while i1 != i2:
        a = order[i1]
        b = order[i1 + step]
        for row in list:
            if row[0].strip() == line:
                st1 = row[1].strip()
                st2 = row[2].strip()
                if (st1 == a and st2 == b) or (st1 == b and st2 == a):
                    current += int(row[3])
                    break
        i1 += step
    return current

arrival_interchange = compute_arrival(source_line, source, interchange, next_train_source)

print(f"Arrive at {interchange} at {normal_time(arrival_interchange)}")
print("Transfer to Magenta Line")

freq2 = get_frequency(arrival_interchange)

if arrival_interchange <= open_time:
    next_train_inter = open_time
else:
    diff = arrival_interchange - open_time #(VERY IMPORTANT) i have added arrival_interchnage as reflective to the actual app we have assumed 5 mins as interchange time 
    rem = diff % freq2
    if rem == 0:
        next_train_inter = arrival_interchange
    else:
        next_train_inter = arrival_interchange + (freq2 - rem)

print("Next Magenta metro departs at", normal_time(next_train_inter))

final_time = compute_arrival(dest_line, interchange, destination, next_train_inter)

print("Arrive at", destination, "at", normal_time(final_time))

total_time = final_time - start_minutes
print("Total travel time:", total_time, "minutes")
