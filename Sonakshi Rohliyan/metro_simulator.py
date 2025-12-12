# The following code simulates the Delhi Metro system, providing metro timings and a journey planner.
# The first part of the code, reads the data and splits it into lists for each line, and one nested list containing all the stations
# the first function of the code metro_sim(linee, station, timee) finds out the time when the next metro reaches any station
# The second function plan() creates a journey plan when you want to go from one station to another on the basis of minimum travel time.
# The third function user_input() takes user input to either use the metro timings module or the journey planner.


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


import datetime 

def metro_sim(linee, station, timee):
    # Metro starts at all end points at 6 am

    # the first metro arrives at any station at time it takes to go from the first metro to the station.
    t = 0

    if linee == "blue":
        index = blue.index(station)
        for i in range(1,index,2):
            t = t + blue[i]

    if linee == "blue2":
        index = blue2.index(station) 
        for i in range(1,index,2):
            t = t + blue2[i]

    if linee == "magenta":
        index = magenta.index(station) 
        for i in range(1,index,2):
            t = t + magenta[i]

    if linee == "airport":
        index = airport.index(station) 
        for i in range(1,index,2):
            t = t + airport[i]
        
    if linee == "gray":
        index = gray.index(station) 
        for i in range(1,index,2):
            t = t + gray[i]

    if linee == "green":
        index = green.index(station) 
        for i in range(1,index,2):
            t = t + green[i]

    # t is the total time it takes for a metro to reach a station from the starting point

    first_metro = datetime.datetime.strptime("06:00", "%H:%M") + datetime.timedelta(minutes=t)
    last_metro = datetime.datetime.strptime("23:00", "%H:%M") + datetime.timedelta(minutes=t)
    
    # first_metro is the time the first metro arrives at the station
    # last_metro is the time the last metro arrives at the station

    # first we find out all the metro timings between the first metro arriving and 8:00, frequency 8 minutes 
    start_time = first_metro
    end_time = datetime.datetime.strptime("08:00", "%H:%M")
    times = []
    while start_time <= end_time:
        times.append(start_time.strftime("%H:%M"))
        start_time = start_time + datetime.timedelta(minutes=8)

    # then we find out all the metro timings between 8:00 and 10:00, frequency 4 minutes

    start_time = datetime.datetime.strptime("08:00", "%H:%M")
    end_time = datetime.datetime.strptime("10:00", "%H:%M")
    while start_time <= end_time:
        times.append(start_time.strftime("%H:%M"))
        start_time = start_time + datetime.timedelta(minutes=4)

    # then we find out all the metro timings between 10:00 and 17:00, frequency 8 minutes

    start_time = datetime.datetime.strptime("10:08", "%H:%M")
    end_time = datetime.datetime.strptime("17:00", "%H:%M")
    while start_time <= end_time:
        times.append(start_time.strftime("%H:%M"))
        start_time = start_time + datetime.timedelta(minutes=8)    

    # then we find out all the metro timings between 17:00 and 19:00, frequency 4 minutes

    start_time = datetime.datetime.strptime("17:04", "%H:%M")
    end_time = datetime.datetime.strptime("19:00", "%H:%M")
    while start_time <= end_time:
        times.append(start_time.strftime("%H:%M"))
        start_time = start_time + datetime.timedelta(minutes=4)

    # then we find out all the metro timings between 19:00 and last metro, frequency 8 minutes

    start_time = datetime.datetime.strptime("19:08", "%H:%M")
    end_time = last_metro
    while start_time <= end_time:
        times.append(start_time.strftime("%H:%M"))
        start_time = start_time + datetime.timedelta(minutes=8)


    for i in range(0, len(times)):
        if times[i] >= timee:
            return times[i], times[i+1:i+6] #times[i] gives us the next metro, and times[i+1:i+6] gives us a list of the next 5 metros

def plan():

    start = input("Starting station: ").strip()
    end = input("Destination: ").strip()
    start_time = input("The starting time of the journey: ")

    if len(start_time) != 5:
        print("Wrong Time Format. Please give time in hh:mm format (eg 6am as 06:00, 1pm as 13:00)")
        return
    elif start_time[2] != ":":
        print("Wrong Time Format. Please give time in hh:mm format (eg 6am as 06:00, 1pm as 13:00")
        return
    elif 6 > int(start_time[0:2]) or int(start_time[0:2]) > 23:
        print("Time out of range. Please give a time in between 06:00 to 23:00")
        return
    elif 0 > int(start_time[3:5]) or int(start_time[3:5]) > 59:
        print("Minutes out of range. Please give minutes in between 00 to 59")
        return

    start_timee = datetime.datetime.strptime(start_time, "%H:%M")
    #Since the input time can not be before the first metro which starts at 6:00
    if start_timee < datetime.datetime.strptime("06:00", "%H:%M"):
        print("Metro starts at 6 am")
        return

    if start == end:
        print("Start and Final station can not be same") 
        return

    start_info = [start] #a list to contain all the info about the start station
    end_info = [end] # A list to contain all the info about the end station

    for i in range(0, len(stations)):
        if stations[i][0] == start:
            start_index = i 
            line1 = stations[i][1] 
            start_info.append(start_index)
            start_info.append(line1)
        if stations[i][0] == end:
            end_index = i 
            line2 = stations[i][1]
            end_info.append(end_index)
            end_info.append(line2)

    if len(start_info) == 1:
        print("Invalid start station Name. Please make sure the first letter of each word is capital, and the name is in the same format as given on DMRC website.")
        return
    if len(end_info) == 1:
        print("Invalid destination station Name. Please make sure the first letter of each word is capital, and the name is in the same format as given on DMRC website.")
        return
    # start_info and end_info contains all the information about the start and the end statiions

    def same(line, Start, End): #here line is a string which is the line name, start is the starting station for the function and end is the final station for the function input
        t = 0 #temperory variable
        for i in range(0, len(stations)):
            if stations[i][0] == Start and stations[i][1] == line:
                Start_index = i #index of the start station in stations list
            if stations[i][0] == End and stations[i][1] == line:
                End_index = i #index of the end station in stations list

        if Start_index > End_index:
            Start_index, End_index = End_index, Start_index # If we want to go backwards on the line, we can just swap the indices, because the time taken to go from one station to another is same in both directions
        for i in range(Start_index, End_index):
            t = t + int(stations[i][2]) + 0.5 # +0.5 because the metro stops for half a minute at every station
        return t
    
    for i in range(0, len(end_info)):
        for j in range(0, len(start_info)):
            if end_info[i] == start_info[j]: #we're basically checking if there is a common line between start and end station. we use looping in case the end/start point is a transfer station
                LINE1 = start_info[j]
                if start == "Janakpuri West" and end == "Botanical Garden" or  start == "Botanical Garden" and end == "Janakpuri West":
                    LINE1 = "magenta" #since janakpuri west and botanical garden both lie on blue line and magenta line, we prefer magenta line.
                print("Your journey plan is: ")
                print(f"Start at {start}: {LINE1} Line")
                a, b= metro_sim(LINE1, start, start_time) # a gives us the time when the next metro arrives at the start station
                print("Next metro at:", a)
                print("No transfer needed")
                time = same(LINE1, start, end) # time is the time taken to go from start to end station 
                print(f"Arrive at {end} at: {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=time)).strftime("%H:%M")}")
                print(f"Total travel time : {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=time) - datetime.datetime.strptime(start_time, "%H:%M")).seconds // 60} minutes")
                return #return statement so no other case is tested.

    def transfer(Line1, Line2, Start, End):
        tf = [] #an empty list to contain all the transfer stations information
        times = []
        for i in range(0, len(stations)):
            for j in range(0, len(stations)):
                if stations[i][0] == stations[j][0] and stations[i][1] == Line1 and stations[j][1] == Line2:
                    tf.append([stations[i][0], stations[i][1], i])
                    tf.append([stations[i][0], stations[j][1], j])
        # now tf has the info of all possible transfer stations with their names, line and index
        # for eg if line1 = blue, line2 = magenta, tf = [[janakpuri west, blue, i][janakpuri west, magenta, i][botanical garden...]] 

        t = 0 #temperory variable

        t1 = same(Line1, Start, tf[0][0]) #time taken to go from start to first transfer station on line1
        t2 = same(Line2, tf[1][0], End) #time taken to go from first transfer station on line2 to end station

        t = t1 + t2 + 2 # 2 minutes cos it takes avg of 2 minutes to transfer 
        times.append([t, tf[0][0]])

        if len(tf)>3: #this case will only be implemented in case of magenta line where are two possible transfer station. this case will check for botanical
            t1 = same(Line1, Start, tf[2][0])
            t2 = same(Line2, tf[3][0], End)
            times.append([t1+t2+2, tf[2][0]]) # takes about 2 minutes to change at botanical 
        
        times.sort()
        return times[0][1] 
    

    if start_info[2] == "blue" and end_info[2] != "blue": # since all the lines have at least one transfer station to blue line, to get from any line to blue line we need only one transfer and vice versa
        x = line2
        transfer = transfer("blue", x, start, end)
        print(f"Start at {start}: blue Line")
        a, b = metro_sim("blue", start, start_time)
        print("Next metro at:", a)
        t1 = same("blue",start, transfer)
        print(f"Arrive at {transfer} at: {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print(f"Transfer to {x} Line at {transfer}")
        a,b = metro_sim(x, transfer,(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=(t1+ 2))).strftime("%H:%M"))
        print(f"Next {x} line metro departs at:", a)
        t1 = same(x, transfer, end)
        print(f"Arrive at {end} at: {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print(f"Total travel time : {((datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)) - datetime.datetime.strptime(start_time, "%H:%M")).seconds // 60} minutes")
        return
    if end_info[2] == "blue" and start_info[2] != "blue":
        x = line1
        transfer = transfer(x, "blue", start, end)
        print(f"Start at {start}: {x} Line")
        a, b = metro_sim(x, start, start_time)
        print("Next metro at:", a)
        t1 = same(x,start, transfer)
        print(f"Arrive at {transfer} at: {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print(f"Transfer to blue Line at {transfer}")
        a,b = metro_sim("blue", transfer,(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=(t1+ 2))).strftime("%H:%M"))
        print(f"Next Blue line metro departs at:", a)
        t1 = same("blue", transfer, end)
        print(f"Arrive at {end} at: {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print(f"Total travel time : {((datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)) - datetime.datetime.strptime(start_time, "%H:%M")).seconds // 60} minutes")
        return

    # now we have to look at the case in which we have to transfer twice, ie first trasfer from line1 to blue line then blue line to line2
    def two_transfer(line1, line2):
        # first go from line1 to blue line, then from blue line to line2
        tf1 = [] #contains the names of the transfer stations from line1 to blue line
        tf2 = [] # names of transfer stations from blu line to line2
        times = []
        for i in range(0, len(stations)):
            for j in range(0, len(stations)):
                if stations[i][0] == stations[j][0] and stations[i][1] == line1 and stations[j][1] == "blue":
                    tf1.append(stations[i][0])

        for i in range(0, len(stations)):
            for j in range(0, len(stations)):
                if stations[i][0] == stations[j][0] and stations[i][1] == "blue" and stations[j][1] == line2:
                    tf2.append(stations[i][0])

        for i in range(0, len(tf1)):
            for j in range(0, len(tf2)): #finds all possible combinations of trannsfer station
                t1 = same(line1, start, tf1[i]) 
                t2 = same("blue", tf1[i], tf2[j])
                t3 = same(line2, tf2[j], end)
                times.append([t1 + t2 + t3 + 4, tf1[i], tf2[j]])

        times.sort()
        return times[0][1], times[0][2]
    
    if len(end_info) > 3:
        line2 = end_info[4]
    else:
        line2 = end_info[2]    

    if len(start_info) > 3:
        line1 = start_info[4]
    else:
        line1 = start_info[2]


    if line1 != "blue" and line2 != "blue": #since we would only need one transfer from any line to blue line, we would only consider cases where neither lines are blue.
        tf1, tf2 = two_transfer(line1, line2)
        print("Your journey plan is: ")
        print(f"Start at {start} : {line1} Line")
        a, b = metro_sim(line1, start, start_time)
        print("Next Metro at", a)
        t1 = same(line1, start, tf1)
        print(f"Arrive at {tf1} at: {(datetime.datetime.strptime(a, "%H:%M")+datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print("Transfer to the main blue Line")
        a, b = metro_sim("blue", tf1 ,(datetime.datetime.strptime(a, "%H:%M")+datetime.timedelta(minutes=t1+1)).strftime("%H:%M"))
        print(f"Next Metro at blue line arrives at: {a}")
        t1 = same("blue", tf1, tf2)
        print(f"Arrive at {tf2} at: {(datetime.datetime.strptime(a, "%H:%M")+datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print(f"Transfer to {line2} line at {tf2}")
        a, b = metro_sim(line2, tf2,(datetime.datetime.strptime(a, "%H:%M")+datetime.timedelta(minutes=t1+2)).strftime("%H:%M"))
        print(f"Next {line2} metro departs at:", a)
        t1 = same(line2, tf2, end)
        print(f"Arrive at {end} at: {(datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)).strftime("%H:%M")}")
        print(f"Total travel time : {((datetime.datetime.strptime(a, "%H:%M") + datetime.timedelta(minutes=t1)) - datetime.datetime.strptime(start_time, "%H:%M")).seconds // 60} minutes")


def user_input():
    print("Welcome to Delhi Metro Route and Schedule Simulator")
    inp = input("Would you like to user Metro Timings Module or Ride journey planner: ")

    if inp == "Metro Timings Module":
        linee = input("Line (blue, blue2, magenta, airport, gray, green): ").strip()
        if linee not in ["blue", "blue2", "magenta", "airport", "gray", "green"]:
            print("Invalid Line Name")
            return
        invalidity_check = []
        station = input("Station: ").strip()
        for i in range(0, len(stations)):
            if stations[i][0] == station and stations[i][1] == linee:
                invalidity_check.append(station)
        if len(invalidity_check) == 0:
            print("Invalid Station Name for the given line. Please make sure the station is in the given line and the station name is written correctly.")
            return
                
        timee = input("Current Time (in hh:mm format in 24 hour clock)= ")
        if len(timee) != 5:
            print("Wrong Time Format. Please give time in hh:mm format (eg 6am as 06:00, 1pm as 13:00)")
            return
        elif timee[2] != ":":
            print("Wrong Time Format. Please give time in hh:mm format (eg 6am as 06:00, 1pm as 13:00")
            return
        elif 6 > int(timee[0:2]) or int(timee[0:2]) > 23:
            print("Time out of range. Please give a time in between 06:00 to 23:00")
            return
        elif 0 > int(timee[3:5]) or int(timee[3:5]) > 59:
            print("Minutes out of range. Please give minutes in between 00 to 59")
            return


        a,b = metro_sim(linee, station, timee)
        print(f"Next Metro at : {a}")
        b = ", ".join(b)
        print(f"Subsequent Metros at : {b}")

    if inp == "Ride journey planner":
        plan()
        
    if inp not in ["Ride journey planner", "Metro Timings Module"]:
        print("Please enter Ride journey planner or Metro Timings Module exactly as asked")

user_input()