
lst = []
print("***********WELCOME TO METRO STIMULATOR************")
with open("metro_data.txt", "r") as file:
    for i in file:
        i = i.strip()
        words = i.split(",")
        lst.append(words)

# input 
Source= input("source:")
desti= input("Destination:")
Current_time =list(map(int, input("current time(hh:mm)=").split(":")))
print("**********DATA************")
pop =True
# check for ststion in data
def station_check(x):
    l=[]
    try :
        for i in lst:
            l.append(i[1])
            if x in l:
                return "station found"
            else:
                print("station not found")
                pop = False
                exit()
    except:
        if ValueError:
            return "INVALID INPUT"
        if x== "":
            return "empty input"

print(station_check(Source))
# station in blue
station_blue =[]
for i in lst:
    if i[0]== "Blue":
        station_blue.append(i[1])
# station in blue1
station_blue1 =[]
for i in lst:
    if i[0]== "Blue1":
        station_blue1.append(i[1])
#station in green
station_green =[]
for i in lst:
    if i[0]== "Green":
        station_green.append(i[1])
#station in Magenta
station_magenta =[]
for i in lst:
    if i[0]== "Magenta":
        station_magenta.append(i[1])
#station in red
station_red =[]
for i in lst:
    if i[0]== "Red":
        station_red.append(i[1])
#station in Yellow
station_yellow =[]
for i in lst:
    if i[0]== "Yellow":
        station_yellow.append(i[1])

# detailed station in blue
ds_blue =[]
for i in lst:
    if i[0]== "Blue":
        ds_blue.append(i)
# detailed station in blue1
ds_blue1 =[]
for i in lst:
    if i[0]== "Blue1":
        ds_blue1.append(i)
#detailed station in green
ds_green =[]
for i in lst:
    if i[0]== "Green":
        ds_green.append(i)
#detailed in Magenta station
ds_magenta =[]
for i in lst:
    if i[0]== "Magenta":
        ds_magenta.append(i)
#detailed in red station
ds_red =[]
for i in lst:
    if i[0]== "Red":
        ds_red.append(i)
#detailed in Yellow  station
ds_yellow =[]
for i in lst:
    if i[0]== "Yellow":
        ds_yellow.append(i)

 #time checker
def time_checker(Current_time):
    if Current_time[0] not in range(0,25) and Current_time[1] not in range(0,61):
        return "STATUS :INVALID TIME"
        
    if Current_time[0]<6 or Current_time[0]>=22 :
        return "STATUS :NO SERVICE AVILABLE"
        
    else:
        return "STATUS :Metro Avilable"


print(time_checker(Current_time))
def hours_to_minutes(time_str):
    cleaned = ""
    for ch in time_str:
        if ch.isdigit() or ch == ":":
            cleaned += ch
    
    h, m = cleaned.split(":")
    return int(h) * 60 + int(m)

# next metro time calculator
def next_metro_time( k,STATION):
    minute = (Current_time[0] *60) + Current_time[1]
    if minute> 480 and minute <= 600:
        freq = 4
    elif minute> 1020 and minute <= 1140:
        freq = 4
    else:
        freq = 8
    minute1 = k[0] *60 + k[1]
    minute1+= freq
    arrival_hour = minute1 // 60
    arrival_minute = minute1 % 60
    return f"NEXT METRO ARRIVING AT {STATION} = {arrival_hour}:{arrival_minute},....."



# predictor(Current_time ):
def duration(count,Current_time):
    time = Current_time.copy()
    (time[0])= (Current_time[0])+((Current_time[1]+count)//60)
    if (Current_time[1]+count)>= 60:
        (time[1])= ((Current_time[1]+count)%60)
    else:
        (time[1])= (Current_time[1])+(count)
    return time

# metro arival time pridictor
def predictor(Current_time,station):

    minute = (Current_time[0] *60) + Current_time[1]
    if minute> 480 and minute <= 600:
        freq = 4
    elif minute> 1020 and minute <= 1140:
        freq = 4
    else:
        freq = 8
    if station in station_red:
        a = station_red.index(station)
        b = station_red.index(station) - len(station_red)
        travel_time = 0          # <-- initialize before using
        for i in range(a):
            travel_time += int(ds_red[i][3])
        first_train_time = 6*60 + travel_time                                   
        if first_train_time >= minute:
            arrival_time = first_train_time
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT RED LINE={arrival_hour}:{arrival_minute}"
        else:
            wait_time = (minute - first_train_time) % freq
            if wait_time == 0:
                arrival_time = minute
            else:
                arrival_time = minute + (freq - wait_time)
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT RED LINE={arrival_hour}:{arrival_minute}"

    elif station in station_blue:
        a = station_blue.index(station)
        b = station_blue.index(station) - len(station_blue)
        travel_time = 0
        for i in range(a):
            travel_time += int(ds_blue[i][3])
        first_train_time = 6*60 + travel_time
        if first_train_time >= minute:
            arrival_time = first_train_time
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT BLUE LINE={arrival_hour}:{arrival_minute}"
        else:
            wait_time = (minute - first_train_time) % freq
            if wait_time == 0:
                arrival_time = minute
            else:
                arrival_time = minute + (freq - wait_time)
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT BLUE LINE={arrival_hour}:{arrival_minute}"

    elif station in station_yellow:
        a = station_yellow.index(station)
        b = station_yellow.index(station) - len(station_yellow) 
        travel_time = 0
        for i in range(a):
            travel_time += int(ds_yellow[i][3]) 
        first_train_time = 6*60 + travel_time  
        if first_train_time >= minute:
            arrival_time = first_train_time
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT YELLOW LINE={arrival_hour}:{arrival_minute}"
        else:
            wait_time = (minute - first_train_time) % freq
            if wait_time == 0:
                arrival_time = minute
            else:
                arrival_time = minute + (freq - wait_time)
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT YELLOW LINE={arrival_hour}:{arrival_minute}"   
    elif station in station_magenta:
        a = station_magenta.index(station)  
        b = station_magenta.index(station) - len(station_magenta)    
        travel_time = 0   
        for i in range(a):  
            travel_time += int(ds_magenta[i][3])
        first_train_time = 6*60 + travel_time
        if first_train_time >= minute:
            arrival_time = first_train_time
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT MAGENTA LINE={arrival_hour}:{arrival_minute}"
        else:

            wait_time = (minute - first_train_time) % freq
            if wait_time == 0:
                arrival_time = minute
            else:
                arrival_time = minute + (freq - wait_time)
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT MAGENTA LINE={arrival_hour}:{arrival_minute}"
    elif station in station_blue1:
        a = station_blue1.index(station)
        b = station_blue1.index(station) - len(station_blue1) 
        travel_time = 0
        for i in range(a):
            travel_time += int(ds_blue1[i][3]) 
        first_train_time = 6*60 + travel_time  
        if first_train_time >= minute:
            arrival_time = first_train_time
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT BLUE LINE={arrival_hour}:{arrival_minute}"
        else:
            wait_time = (minute - first_train_time) % freq
            if wait_time == 0:
                arrival_time = minute
            else:
                arrival_time = minute + (freq - wait_time)
            arrival_hour = arrival_time // 60
            arrival_minute = arrival_time % 60
            Current_time = [arrival_hour, arrival_minute]
            return f"METRO ARRIVING AT BLUE LINE={arrival_hour}:{arrival_minute}"


if pop == False:
    exit()
else:
    print(predictor(Current_time,Source))

#journey pridictor

def jrny_pred(x,y):
    count = 0
    Source =x
    desti =y
    
    # FOR NO INTERCHANGE
    if x in station_blue and y in station_blue:
        print("no interchange needed")
        idx1 = station_blue.index(Source)
        idx2 = station_blue.index(desti)
        for i in range(min(idx1, idx2), max(idx1, idx2)):
            count += (int(ds_blue[i][3])+ 1)
    elif x in station_magenta and y in station_magenta:
        print("no interchange needed")
        idx1 = station_magenta.index(Source)
        idx2 = station_magenta.index(desti)
        for i in range(min(idx1, idx2), max(idx1, idx2)):
            count += (int(ds_magenta[i][3])+ 1)
    elif x in station_yellow and y in station_yellow:
        print("no interchange needed")
        idx1 = station_yellow.index(Source)
        idx2 = station_yellow.index(desti)
        for i in range(min(idx1, idx2), max(idx1, idx2)):
            count += (int(ds_yellow[i][3])+ 1)
    elif x in station_red and y in station_red:
        print("no interchange needed")
        idx1 = station_red.index(Source)
        idx2 = station_red.index(desti)
        for i in range(min(idx1, idx2), max(idx1, idx2)):
            count += int(ds_red[i][3])+ 1
    elif x in station_blue1 and y in station_blue1:
        print("no interchange needed")
        idx1 = station_blue1.index(Source)
        idx2 = station_blue1.index(desti)
        for i in range(min(idx1, idx2), max(idx1, idx2)):
            count += int(ds_blue1[i][3]) + 1
    # FOR ONE INTERCHANGE
    elif (x in station_blue and y in station_yellow) or (x in station_yellow and y in station_blue):
        print("one interchange needed at Rajiv Chowk")
        if x in station_blue:
            idx1 = station_blue.index(Source)
            idx2 = station_blue.index("Rajiv Chowk")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_blue[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx3 = station_yellow.index("Rajiv Chowk")
            idx4 = station_yellow.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3])   + 1
        else:
            idx1 = station_yellow.index(Source)
            idx2 = station_yellow.index("Rajiv Chowk")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_yellow[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            k = (duration(count,x))
            idx3 = station_blue.index("Rajiv Chowk")
            idx4 = station_blue.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_blue[j][3]) + 1
    elif (x in station_magenta and y in station_yellow) or (x in station_yellow and y in station_magenta):
        print("one interchange needed at Hauz Khas")
        if x in station_magenta:
            idx1 = station_magenta.index(Source)
            idx2 = station_magenta.index("Hauz Khas")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_magenta[i][3])+ 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
            predictor(x,"Hauz Khas")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}")
            print(next_metro_time( k," Hauz Khas"))
            idx3 = station_yellow.index("Hauz Khas")
            idx4 = station_yellow.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3]) + 1
        else:
            idx1 = station_yellow.index(Source)
            idx2 = station_yellow.index("Hauz Khas")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_yellow[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
            predictor(x,"Hauz Khas")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}")
            print(next_metro_time( k," Hauz Khas"))
            idx3 = station_magenta.index("Hauz Khas")
            idx4 = station_magenta.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_magenta[j][3]) + 1
    elif (x in station_yellow and y in station_red) or (x in station_red and y in station_yellow):
        print("one interchange needed at Kashmere Gate")
        if x in station_red:
            idx1 = station_red.index(Source)
            idx2 = station_red.index("Kashmere Gate")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_red[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx3 = station_yellow.index("Kashmere Gate")
            idx4 = station_yellow.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3]) + 1
        else:
            idx1 = station_yellow.index(Source)
            idx2 = station_yellow.index("Kashmere Gate")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_yellow[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx3 = station_red.index("Kashmere Gate")
            idx4 = station_red.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_red[j][3]) + 1
    elif (x in station_blue and y in station_blue1) or (x in station_blue1 and y in station_blue):
        print("one interchange needed at Yamuna Bank")
        if x in station_blue1:
            idx1 = station_blue1.index(Source)
            idx2 = station_blue1.index("Yamuna Bank")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_blue1[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
            predictor(x,"Yamuna Bank")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
            print(next_metro_time( k,"Yamuna Bank"))
            idx3 = station_blue.index("Yamuna Bank")
            idx4 = station_blue.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_blue[j][3]) + 1
        else:
            idx1 = station_blue.index(Source)
            idx2 = station_blue.index("Yamuna Bank")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_blue[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
            predictor(x,"Yamuna Bank")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
            print(next_metro_time( k,"Yamuna Bank"))
            idx3 = station_blue1.index("Yamuna Bank")
            idx4 = station_blue1.index(desti)
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_blue1[j][3]) + 1
    # two interchange needed
    elif (x in station_red and y in station_blue) or (x in station_blue and y in station_red)  :
        print("two interchange needed at Rajiv Chowk and Kashmere Gate")
        if x in station_red:
            idx1 = station_red.index(Source)
            idx2 = station_red.index("Kashmere Gate")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_red[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx3 = station_yellow.index("Kashmere Gate")
            idx4 = station_yellow.index("Rajiv Chowk")
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx5 = station_blue.index("Rajiv Chowk")
            idx6 = station_blue.index(desti)
            for k in range(min(idx5, idx6), max(idx5, idx6)):
                count += int(ds_blue[k][3]) + 1
        else:
            idx1 = station_blue.index(Source)
            idx2 = station_blue.index("Rajiv Chowk")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_blue[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx3 = station_yellow.index("Rajiv Chowk")
            idx4 = station_yellow.index("Kashmere Gate")
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx5 = station_red.index("Kashmere Gate")
            idx6 = station_red.index(desti)
            for k in range(min(idx5, idx6), max(idx5, idx6)):
                count += int(ds_red[k][3]) + 1
    elif (x in station_yellow and y in station_blue1) or (x in station_blue1 and y in station_yellow)  :
        print("two interchange needed at Rajiv Chowk and Yamuna Bank")
        if x in station_yellow:
            idx1 = station_yellow.index(Source)
            idx2 = station_yellow.index("Rajiv Chowk")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_yellow[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx3 = station_blue.index("Yamuna Bank")
            idx4 = station_blue.index("Rajiv Chowk")
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_blue[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
            predictor(x,"Yamuna Bank")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
            print(next_metro_time( k,"Yamuna Bank"))
            idx5 = station_blue1.index("Yamuna Bank")
            idx6 = station_blue1.index(desti)
            for k in range(min(idx5, idx6), max(idx5, idx6)):
                count += int(ds_blue1[k][3])    + 1
        else:
            idx1 = station_blue1.index(Source)
            idx2 = station_blue1.index("Yamuna Bank")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_blue1[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
            predictor(x,"Yamuna Bank")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
            print(next_metro_time( k,"Yamuna Bank"))
            idx3 = station_blue.index("Yamuna Bank")
            idx4 = station_blue.index("Rajiv Chowk")
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_blue[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx5 = station_yellow.index("Rajiv Chowk")
            idx6 = station_yellow.index(desti)
            for k in range(min(idx5, idx6), max(idx5, idx6)):
                count += int(ds_yellow[k][3]) + 1
    # three interchange needed
    elif (x in station_red and y in station_blue1) or (x in station_blue1 and y in station_red)  :
        print("three interchange needed at Kashmere Gate,Rajiv Chowk and Yamuna Bank")
        if x in station_red:
            idx1 = station_red.index(Source)
            idx2 = station_red.index("Kashmere Gate")
            for i in range (min(idx1,idx2),max(idx1,idx2)):
                count+=int(ds_red[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx3 = station_yellow.index("Kashmere Gate")
            idx4 = station_yellow.index("Rajiv Chowk")
            for j in range (min(idx3,idx4),max(idx3,idx4)):
                count+=int(ds_yellow[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx5 = station_blue.index("Rajiv Chowk")
            idx6 = station_blue.index("Yamuna Bank")
            for k in range(min(idx5,idx6),max(idx5,idx6)):
                count+=int(ds_blue[k][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
            predictor(x,"Yamuna Bank")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
            print(next_metro_time( k,"Yamuna Bank"))
            idx7 = station_blue1.index("Yamuna Bank")
            idx8 = station_blue1.index(desti)
            for l in range(min(idx7,idx8),max(idx7,idx8)):
                count+=int(ds_blue1[l][3]) + 1
        else:   
            idx1 = station_blue1.index(Source)
            idx2 = station_blue1.index("Yamuna Bank")
            for i in range (min(idx1,idx2),max(idx1,idx2)):
                count+=int(ds_blue1[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
            predictor(x,"Yamuna Bank")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
            print(next_metro_time( k,"Yamuna Bank"))
            idx3 = station_blue.index("Yamuna Bank")
            idx4 = station_blue.index("Rajiv Chowk")
            for j in range (min(idx3,idx4),max(idx3,idx4)):
                count+=int(ds_blue[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx5 = station_yellow.index("Rajiv Chowk")
            idx6 = station_yellow.index("Kashmere Gate")
            for k in range(min(idx5,idx6),max(idx5,idx6)):
                count+=int(ds_yellow[k][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx7 = station_red.index("Kashmere Gate")
            idx8 = station_red.index(desti)
            for l in range(min(idx7,idx8),max(idx7,idx8)):
                count+=int(ds_red[l][3]) + 1   


    ############## special cases################
    # red to magenta 
    elif (x in station_red and y in station_magenta) or (x in station_magenta and y in station_red):
        print("three interchange needed")
        if x in station_red:
            idx1 = station_red.index(Source)
            idx2 = station_red.index("Kashmere Gate")
            for i in range (min(idx1,idx2),max(idx1,idx2)):
                count+=int(ds_red[i][3]) + 1
            print("interchange at Kashmere Gate")
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
            predictor(x,"Kashmere Gate")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
            print(next_metro_time( k,"Kashmere Gate"))
            idx3 = station_yellow.index("Kashmere Gate")
            idx4 = station_yellow.index("Rajiv Chowk")
            for j in range (min(idx3,idx4),max(idx3,idx4)):
                count+=int(ds_yellow[j][3]) + 1
            print("interchange at Rajiv Chowk")
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            # case1
            caselist = []
            for m in range(3):
                if m==0:
                    idx5 = station_yellow.index("Rajiv Chowk")
                    idx6 = station_yellow.index("Hauz Khas")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_magenta[k][3]) + 1
                    idx7 = station_magenta.index("Hauz Khas")
                    idx8 = station_magenta.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_magenta[l][3]) + 1  
                    caselist.append(count)
                elif m==1:
                    idx5 = station_blue.index("Rajiv Chowk")
                    idx6 = station_blue.index("janakpuri West")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_blue[k][3]) + 1
                    idx7 = station_magenta.index("janakpuri West")
                    idx8 = station_magenta.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_magenta[l][3]) + 1  
                    caselist.append(count)
                elif m==2:
                    idx5 = station_blue.index("Rajiv Chowk")
                    idx6 = station_blue.index("botanical Garden")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_blue[k][3]) + 1
                    idx7 = station_magenta.index("botanical Garden")
                    idx8 = station_magenta.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_magenta[l][3]) + 1  
                    caselist.append(count)
            count = min(caselist)   
            if caselist.index(count)==0:
                print("interchange at Hauz Khas")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
                predictor(x,"Hauz Khas")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}")
                print(next_metro_time( k,"Hauz Khas"))
            elif caselist.index(count)==1:
                print("interchange at Janakpuri West")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Janakpuri West")) - minute
                predictor(x,"Janakpuri West")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Janakpuri West={k[0]}:{k[1]}")   
                print(next_metro_time( k,"Janakpuri West"))
            elif caselist.index(count)==2:
                print("interchange at Botanical Garden")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Botanical Garden")) - minute
                predictor(x,"Botanical Garden")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Botanical Garden={k[0]}:{k[1]}")
                print(next_metro_time( k,"Botanical Garden"))


        else:   
            idx1 = station_magenta.index(Source)
            idx2 = station_magenta.index("Hauz Khas")
            for i in range (min(idx1,idx2),max(idx1,idx2)):
                count+=int(ds_magenta[i][3]) + 1
            print("interchange at Hauz Khas")
            print(duration(count,Current_time))
            idx3 = station_yellow.index("Hauz Khas")
            idx4 = station_yellow.index("Rajiv Chowk")
            for j in range (min(idx3,idx4),max(idx3,idx4)):
                count+=int(ds_yellow[j][3]) + 1
            print("interchange at Rajiv Chowk")
            print(duration(count,Current_time))
            caselist = []
            for m in range(3):
                if m==0:
                    idx5 = station_yellow.index("Rajiv Chowk")
                    idx6 = station_yellow.index("Kashmere Gate")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_yellow[k][3]) + 1
                    idx7 = station_red.index("Kashmere Gate")
                    idx8 = station_red.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_red[l][3]) + 1 
                    caselist.append(count)
                elif m==1:
                    idx5 = station_blue.index("Rajiv Chowk")
                    idx6 = station_blue.index("janakpuri West")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_blue[k][3]) + 1
                    idx7 = station_red.index("janakpuri West")
                    idx8 = station_red.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_red[l][3]) + 1  
                    caselist.append(count)
                elif m==2:
                    idx5 = station_blue.index("Rajiv Chowk")
                    idx6 = station_blue.index("botanical Garden")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_blue[k][3]) + 1
                    idx7 = station_red.index("botanical Garden")
                    idx8 = station_red.index(desti)                     
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_red[l][3]) + 1      
                    caselist.append(count)
            count = min(caselist)
            if caselist.index(count)==0:
                print("interchange at Kashmere Gate")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Kashmere Gate")) - minute
                predictor(x,"Kashmere Gate")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Kashmere Gate={k[0]}:{k[1]}")
                print(next_metro_time( k,"Kashmere Gate"))
            elif caselist.index(count)==1:
                print("interchange at Janakpuri West")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Janakpuri West")) - minute
                predictor(x,"Janakpuri West")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Janakpuri West={k[0]}:{k[1]}") 
                print(next_metro_time( k,"Janakpuri West"))   
            elif caselist.index(count)==2:
                print("interchange at Botanical Garden")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Botanical Garden")) - minute
                predictor(x,"Botanical Garden")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Botanical Garden={k[0]}:{k[1]}")
                print(next_metro_time( k,"Botanical Garden"))

     #################### special case #######################
    # magenta to blue1
    # case 2
    elif (x in station_magenta and y in station_blue1) or (x in station_blue1 and y in station_magenta):
        print(" following interchange needed")
        if x in station_magenta:
            for i in range(3):
                caselist = []
                if i==0:
                    idx1 = station_magenta.index(Source)
                    idx2 = station_magenta.index("Hauz Khas")
                    for i in range (min(idx1,idx2),max(idx1,idx2)):
                        count+=int(ds_magenta[i][3]) + 1
                    # print("interchange at Hauz Khas")
                    # print(duration(count,Current_time))
                    idx3 = station_yellow.index("Hauz Khas")
                    idx4 = station_yellow.index("Rajiv Chowk")
                    for j in range (min(idx3,idx4),max(idx3,idx4)):
                        count+=int(ds_yellow[j][3]) + 1
                    # print("interchange at Rajiv Chowk")
                    # print(duration(count,Current_time))
                    idx5 = station_blue.index("Rajiv Chowk")
                    idx6 = station_blue.index("Yamuna Bank")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(station_blue[k][3]) + 1
                    # print("interchange at Yamuna Bank")
                    # print(duration(count,Current_time))
                    idx7 = station_blue1.index("Yamuna Bank")
                    idx8 = station_blue1.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(station_blue1[l][3]) + 1
                    # print(duration(count,Current_time))
                    caselist.append(count)
                elif i==1:
                    idx1 = station_magenta.index(Source)
                    idx2 = station_magenta.index("janakpuri West")
                    for i in range (min(idx1,idx2),max(idx1,idx2)):
                        count+=int(ds_magenta[i][3]) + 1
                    # print("interchange at Janakpuri West")
                    # print(duration(count,Current_time))
                    idx3 = station_blue.index("janakpuri West")
                    idx4 = station_blue.index("Yamuna Bank")
                    for j in range (min(idx3,idx4),max(idx3,idx4)):
                        count+=int(ds_blue[j][3]) + 1
                    # print("interchange at Yamuna Bank")
                    # print(duration(count,Current_time))
                    idx5 = station_blue1.index("Yamuna Bank")
                    idx6 = station_blue1.index(desti)
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(station_blue1[k][3]) + 1
                    # print(duration(count,Current_time))
                    caselist.append(count)
                elif i==2:
                    idx1 = station_magenta.index(Source)
                    idx2 = station_magenta.index("botanical Garden")
                    for i in range (min(idx1,idx2),max(idx1,idx2)):
                        count+=int(ds_magenta[i][3]) + 1
                    # print("interchange at Botanical Garden")
                    # print(duration(count,Current_time))
                    idx3 = station_blue.index("botanical Garden")
                    idx4 = station_blue.index("Yamuna Bank")
                    for j in range (min(idx3,idx4),max(idx3,idx4)):
                        count+=int(ds_blue[j][3]) + 1
                    # print("interchange at Yamuna Bank")
                    # print(duration(count,Current_time))
                    idx5 = station_blue1.index("Yamuna Bank")
                    idx6 = station_blue1.index(desti)
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(station_blue1[k][3]) + 1
                    # print(duration(count,Current_time))
                    caselist.append(count)

            count = min(caselist)   
            if caselist.index(count)==0:
                print("interchange at Hauz Khas")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
                predictor(x,"Hauz Khas")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}") 
                print(next_metro_time( k,"Hauz Khas"))
                print("interchange at Rajiv Chowk")              
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
                predictor(x,"Rajiv Chowk")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
                print(next_metro_time( k,"Rajiv Chowk"))
                print("interchange at Yamuna Bank")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
                predictor(x,"Yamuna Bank")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}") 
                print(next_metro_time( k,"Yamuna Bank"))
            elif caselist.index(count)==1:
                print("interchange at Janakpuri West")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Janakpuri West")) - minute
                predictor(x,"Janakpuri West")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Janakpuri West={k[0]}:{k[1]}")  
                print(next_metro_time( k,"Janakpuri West"))
                print("interchange at Yamuna Bank")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
                predictor(x,"Yamuna Bank")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
                print(next_metro_time( k,"Yamuna Bank"))  
            elif caselist.index(count)==2:
                print("interchange at Botanical Garden")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Botanical Garden")) - minute
                predictor(x,"Botanical Garden")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Botanical Garden={k[0]}:{k[1]}")  
                print(next_metro_time( k,"Botanical Garden"))    
                print("interchange at Yamuna Bank")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
                predictor(x,"Yamuna Bank")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
                print(next_metro_time( k,"Yamuna Bank"))
        else:                                               
            for i in range(3):
                caselist = []
                if i==0:
                    idx1 = station_blue1.index(Source)
                    idx2 = station_blue1.index("Yamuna Bank")
                    for i in range (min(idx1,idx2),max(idx1,idx2)):
                        count+=int(station_blue1[i][3]) + 1
                    # print("interchange at Yamuna Bank")
                    # print(duration(count,Current_time))
                    idx3 = station_blue.index("Yamuna Bank")
                    idx4 = station_blue.index("Rajiv Chowk")
                    for j in range (min(idx3,idx4),max(idx3,idx4)):
                        count+=int(ds_blue[j][3]) + 1
                    # print("interchange at Rajiv Chowk")
                    # print(duration(count,Current_time))
                    idx5 = station_yellow.index("Rajiv Chowk")
                    idx6 = station_yellow.index("Hauz Khas")
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_yellow[k][3]) + 1
                    # print("interchange at Hauz Khas")
                    # print(duration(count,Current_time))
                    idx7 = station_magenta.index("Hauz Khas")
                    idx8 = station_magenta.index(desti)
                    for l in range(min(idx7,idx8),max(idx7,idx8)):
                        count+=int(ds_magenta[l][3]) + 1
                    # print(duration(count,Current_time))
                    caselist.append(count)
                elif i==1:
                    idx1 = station_blue1.index(Source)
                    idx2 = station_blue1.index("Yamuna Bank")
                    for i in range (min(idx1,idx2),max(idx1,idx2)):
                        count+=int(station_blue1[i][3]) + 1
                    # print("interchange at Yamuna Bank")
                    # print(duration(count,Current_time))
                    idx3 = station_blue.index("Yamuna Bank")
                    idx4 = station_blue.index("janakpuri West")
                    for j in range (min(idx3,idx4),max(idx3,idx4)):
                        count+=int(ds_blue[j][3]) + 1
                    # print("interchange at Janakpuri West")
                    # print(duration(count,Current_time))
                    idx5 = station_magenta.index("janakpuri West")  
                    idx6 = station_magenta.index(desti)
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_magenta[k][3]) + 1

                    # print(duration(count,Current_time))
                    caselist.append(count)  
                elif i==2:
                    idx1 = station_blue1.index(Source)
                    idx2 = station_blue1.index("Yamuna Bank")
                    for i in range (min(idx1,idx2),max(idx1,idx2)):
                        count+=int(station_blue1[i][3]) + 1
                    # print("interchange at Yamuna Bank")
                    # print(duration(count,Current_time))
                    idx3 = station_blue.index("Yamuna Bank")
                    idx4 = station_blue.index("botanical Garden")
                    for j in range (min(idx3,idx4),max(idx3,idx4)):
                        count+=int(ds_blue[j][3]) + 1
                    # print("interchange at Botanical Garden")
                    # print(duration(count,Current_time))
                    idx5 = station_magenta.index("botanical Garden")  
                    idx6 = station_magenta.index(desti)
                    for k in range(min(idx5,idx6),max(idx5,idx6)):
                        count+=int(ds_magenta[k][3]) + 1

                    # print(duration(count,Current_time))
                    caselist.append(count)
            count = min(caselist)
            if caselist.index(count)==0:
                print("interchange at Yamuna Bank")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
                predictor(x,"Yamuna Bank")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")
                print(next_metro_time( k,"Yamuna Bank"))
                print("interchange at Rajiv Chowk")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
                predictor(x,"Rajiv Chowk")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
                print(next_metro_time( k,"Rajiv Chowk"))
                print("interchange at Hauz Khas")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
                predictor(x,"Hauz Khas")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}") 
                print(next_metro_time( k,"Hauz Khas"))
            elif caselist.index(count)==1:
                print("interchange at Yamuna Bank")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
                predictor(x,"Yamuna Bank")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")   
                print(next_metro_time( k,"Yamuna Bank"))  
                print("interchange at Janakpuri West")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Janakpuri West")) - minute
                predictor(x,"Janakpuri West")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Janakpuri West={k[0]}:{k[1]}") 
                print(next_metro_time( k,"Janakpuri West"))   
            elif caselist.index(count)==2:
                print("interchange at Yamuna Bank")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Yamuna Bank")) - minute
                predictor(x,"Yamuna Bank")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Yamuna Bank={k[0]}:{k[1]}")    
                print(next_metro_time( k,"Yamuna Bank"))  
                print("interchange at Botanical Garden")
                x = duration(count,Current_time)
                minute = (x[0] *60) + x[1]
                delay = hours_to_minutes(predictor(x,"Botanical Garden")) - minute
                predictor(x,"Botanical Garden")
                count+= delay
                k = (duration(count,x))
                print(f"METRO ARRIVING AT Botanical Garden={k[0]}:{k[1]}")
                print(next_metro_time( k,"Botanical Garden"))
        #################special  case#######################
    elif (x in station_blue and y in station_magenta) or (x in station_magenta and y in station_blue):
        print("two interchange needed at Rajiv Chowk and Hauz Khas")
        if x in station_blue:
            idx1 = station_blue.index(Source)
            idx2 = station_blue.index("Rajiv Chowk")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_blue[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx3 = station_yellow.index("Rajiv Chowk")
            idx4 = station_yellow.index("Hauz Khas")
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
            predictor(x,"Hauz Khas")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}")
            print(next_metro_time( k,"Hauz Khas"))
            idx5 = station_magenta.index("Hauz Khas")
            idx6 = station_magenta.index(desti)
            for k in range(min(idx5, idx6), max(idx5, idx6)):
                count += int(ds_magenta[k][3]) + 1
        else:
            idx1 = station_magenta.index(Source)
            idx2 = station_magenta.index("Hauz Khas")
            for i in range(min(idx1, idx2), max(idx1, idx2)):
                count += int(ds_magenta[i][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Hauz Khas")) - minute
            predictor(x,"Hauz Khas")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Hauz Khas={k[0]}:{k[1]}")
            print(next_metro_time( k,"Hauz Khas"))
            idx3 = station_yellow.index("Hauz Khas")
            idx4 = station_yellow.index("Rajiv Chowk")
            for j in range(min(idx3, idx4), max(idx3, idx4)):
                count += int(ds_yellow[j][3]) + 1
            x = duration(count,Current_time)
            minute = (x[0] *60) + x[1]
            delay = hours_to_minutes(predictor(x,"Rajiv Chowk")) - minute   
            predictor(x,"Rajiv Chowk")
            count+= delay
            k = (duration(count,x))
            print(f"METRO ARRIVING AT Rajiv Chowk={k[0]}:{k[1]}")
            print(next_metro_time( k,"Rajiv Chowk"))
            idx5 = station_blue.index("Rajiv Chowk")        
            idx6 = station_blue.index(desti)
            for k in range(min(idx5, idx6), max(idx5, idx6)):
                count += int(ds_blue[k][3]) + 1 

    return count
 

if pop == False:
    exit()
else:
    count = jrny_pred(Source,desti)
    print(f"DURATION:{ count } minutes")
    time= duration(count,Current_time)
    print(f"Arrival Time (HH:MM):{time[0]:.0f}:{ time[1]:.0f}")


def faircal(count ):
    fare=0
    if count <= 2:
        fare=10+1
    elif count >2 and count <=6:
        fare=20+11
    elif count >6 and count <=12:
        fare=30+11
    elif count >12 and count <=21:
        fare=40+11
    elif count >21 and count <=32:
        fare=50+11
    elif count >32 and count <=45:
        fare=60+11
    elif count >45 and count <=59:
        fare=70+11
    else:
        fare=80+11
    return fare
print(f"FARE: Rs.{faircal(count)}")