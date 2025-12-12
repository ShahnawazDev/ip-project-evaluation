def data(filename):
    data_line = {}
    station_index = {}
    cline = None

    f = open(filename, "r")
    for i in f:
        line = i.strip()
        if line == "":
            continue
        truline = line.lower()
        if ("blue" in truline) and ("line1" in truline):
            cline = "Blue3"
            data_line[cline] = {}
            continue
        elif ("blue" in truline) and ("line2" in truline):
            cline = "Blue4"
            data_line[cline] = {}
            continue
        elif truline.startswith("magenta line"):
            cline = "Magenta"
            data_line[cline] = {}
            continue
        if cline is None:
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        
        name = " ".join(parts[:-2])
        inter = parts[-2].strip()
        nexttime = int(parts[-1])
        
        data_line[cline][name] = [inter, nexttime]
        key = name.strip().lower()
        index = list(data_line[cline].keys()).index(name)

        if key not in station_index:
            station_index[key] = [(cline, index)]
        else:
            station_index[key].append((cline, index))
    f.close()
    return data_line, station_index

def time_decoder(str):
    h,m=str.split(":")
    return ((int(h)*60)+int(m))
def time_encoder(a):
    h = a//60
    m = a%60
    if len(str(h)) == 1 and len(str(m)) == 1:
        new_time = f"0{h}:0{m}"
    elif len(str(h)) == 1 and len(str(m)) == 2:
        new_time = f"0{h}:{m}"
    elif len(str(h)) == 2 and len(str(m)) == 1:
        new_time = f"{h}:0{m}"
    elif len(str(h)) == 2 and len(str(m)) == 2:
        new_time = f"{h}:{m}"
    return new_time

def firstarival(line, stationame):
    off = 0
    for name, data in line.items():
        if name == stationame:
            return off
        off += data[1]
    return None
def totaltime(line_stations):
    total = 0
    for station,time in line_stations.items():
        total += time[1]
    return total
def nextrain(now, traintime1, stations, direction,n=5):
    lst = []
    startime = 6 * 60
    stoptime = 23 * 60
    noon = 24 * 60
    o2 = totaltime(stations) - traintime1
    # This is for the normal case from 6:00am to 12:00pm, with 12:00pm exclusive and 6:00am inclusive
    dep = startime
    while dep < stoptime:
        hour = dep // 60
        if (8 <= hour < 10 or 17 <= hour < 19):
            freq = 4
        else: 
            freq = 8
        ttime = dep + traintime1
        if ttime > now:
            lst.append(ttime)
        if direction:
            a2 = dep + o2
            if a2 > now:
                lst.append(a2)
        dep += freq
    # 2) for train finally departing at 23:00pm last time from each ends of the metro line.
    # for forward
    lasttime = stoptime
    final_arrivals = []
    finaltime1 = lasttime + traintime1
    if finaltime1 > now and finaltime1 < noon:
        final_arrivals.append(finaltime1)
    # for backword
    if direction:
        finaltime2 = lasttime + o2
        if finaltime2 > now and finaltime2 < noon:
            final_arrivals.append(finaltime2)
    # if time is more than or equal to 23:00pm
    if now >= stoptime:
        if not final_arrivals:
            return []
        return [min(final_arrivals)]
    if final_arrivals:
        earliest_final = min(final_arrivals)
        if earliest_final not in lst:
            lst.append(earliest_final)
    lst = sorted(set(lst))
    return lst[:5]

def routebuilder(stations_dict, i1, i2):    
    names = list(stations_dict.keys())
    route = []
    if i2 >= i1:
        step = 1 
    else:
        step = -1
    i = i1
    while True:
        name = names[i]
        nexttime = stations_dict[name][1]
        route.append((name, nexttime))
        if i == i2:
            break
        i += step
    return route

def total_time(route):
    return sum(t for x, t in route[:-1])

def interchange1(data_lines, station_index, sourcename, destinationname):
    #Error handeling
    if sourcename.lower() not in station_index or destinationname.lower() not in station_index:
        return None

    sourceline = set(l for (l, m) in station_index[sourcename.lower()])
    destinationline = set(l for (l, m) in station_index[destinationname.lower()])
    
    shortest = None
    best = None

    for sl in sourceline:
        for dl in destinationline:
            if sl == dl:
                continue

            s = data_lines[sl]
            d = data_lines[dl]

            s_names = set(name.lower() for name in s)
            d_names = set(name.lower() for name in d)
            common = s_names & d_names

            for inter_lower in common:
                inter_name = [name for name in s if name.lower() == inter_lower][0]

                index_source = [idx for (l, idx) in station_index[sourcename.lower()] if l == sl][0]
                index_destination = [idx for (l, idx) in station_index[destinationname.lower()] if l == dl][0]

                csource = list(s.keys()).index(inter_name)
                cdest = list(d.keys()).index(inter_name)

                r1 = routebuilder(s, index_source, csource)
                r2 = routebuilder(d, cdest, index_destination)
                t = total_time(r1) + total_time(r2)

                if best is None or t < best:
                    best = t
                    shortest = (sl, dl, inter_name, index_source, csource, cdest, index_destination)
    return shortest


def interchange2(lines_data, station_index, sourcename, destinationname):
    if sourcename.lower() not in station_index or destinationname.lower() not in station_index:
        return None

    sourceline = set(l for (l, m) in station_index[sourcename.lower()])
    destinationline = set(l for (l, m) in station_index[destinationname.lower()])
    all_lines = list(lines_data.keys())

    shortest = None
    best = None

    for sl in sourceline:
        for dl in destinationline:
            if sl == dl:
                continue
            for ml in all_lines:
                if ml in (sl, dl):
                    continue
                s= lines_data[sl]
                m= lines_data[ml]
                d = lines_data[dl]

                s_names = set(name.lower() for name in s)
                m_names = set(name.lower() for name in m)
                d_names = set(name.lower() for name in d)

                cm1 = s_names & m_names
                cm2 = m_names & d_names

                if not cm1 or not cm2:
                    continue

                index_source = [idx for (l, idx) in station_index[sourcename.lower()] if l == sl][0]
                index_destination = [idx for (l, idx) in station_index[destinationname.lower()] if l == dl][0]

                for inter1_lower in cm1:
                    inter1_name = [n for n in s if n.lower() == inter1_lower][0]
                    intersource = list(s.keys()).index(inter1_name)
                    interm1= list(m.keys()).index(inter1_name)

                    for inter2_lower in cm2:
                        inter2_name = [n for n in d if n.lower() == inter2_lower][0]
                        interm2 = list(m.keys()).index(inter2_name)
                        interdest = list(d.keys()).index(inter2_name)

                        r1 = routebuilder(s, index_source, intersource)
                        r2 = routebuilder(m, interm1, interm2)
                        r3 = routebuilder(d, interdest, index_destination)
                        t = total_time(r1) + total_time(r2) + total_time(r3)

                        if best is None or t < best:
                            best = t
                            shortest = (sl, ml, dl, index_source, intersource, interm1, interm2, interdest, index_destination,
                                    inter1_name, inter2_name)
    return shortest
def time_module(data):
    line = input("Enter line (Blue3/Blue4/Magenta): ").strip()
    if line not in data:
        print("Invalid line.")
        return None
    
    stationame = input("Enter station name: ").strip()
    stations = data[line]
    found = False
    for i in stations:
        if i.lower() == stationame.strip().lower():
            stationame = i
            found = True
            break
    if not found:
        print("Station not found on this line.")
        return None    
    ctime = input("Enter time (HH:MM): ").strip()
    h,m = list(map(int,ctime.split(":")))
    try:
        now = time_decoder(ctime)
    except:
        print("Invalid time.")
        return None    
    if h < 6:
        print("No service before 06:00.")
        return None
    
    traintime1 = firstarival(stations, stationame)
    list_train = nextrain(now,traintime1,stations,True,n=5)
    if not list_train:
        print("Metro is unavailble at this time.")
        return None
    print("\nNext metro at", time_encoder(list_train[0]))
    if len(list_train) > 1:
        print("Next Metro's are arriving at", ", ".join(time_encoder(x) for x in list_train[1:]))
    print()
def planner(lines_data, station_index):
    changedelay = 3
    source = input("Enter source station: ").strip()
    dest = input("Enter destination station: ").strip()
    time = input("Enter time (HH:MM): ").strip()
    h,m = list(map(int,time.split(":")))
    try:
        now = time_decoder(time)
    except:
        print("Invalid time.")
        return
    if h < 6:
        print("No service before 06:00.")
        return

    sk = source.lower()
    dk = dest.lower()
    if sk not in station_index:
        print("Source station not found.")
        return
    if dk not in station_index:
        print("Destination station not found.")
        return

    print("\nJourney Plan:")
    src_opts = station_index[sk]
    dest_opts = station_index[dk]
    src_lines = [l for (l, m) in src_opts]
    dest_lines = [l for (l, m) in dest_opts]

    same = None
    for l in src_lines:
        if l in dest_lines:
            same = l
            break
    if same:
        s_idx = [idx for (l, idx) in src_opts if l == same][0]
        d_idx = [idx for (l, idx) in dest_opts if l == same][0]
        stations = lines_data[same]
        route = routebuilder(stations, s_idx, d_idx)

        off = firstarival(stations, list(stations.keys())[s_idx])
        arr = nextrain(now, off, stations, False ,n = 1)
        if not arr:
            print("No service at this time.")
            return
        board = arr[0]

        names = list(stations.keys())
        print("Start at", names[s_idx], "(" + same + " Line)")
        print("Next metro at", time_encoder(board))

        cur = board
        for i in range(1, len(route)):
            cur += route[i - 1][1]
            print("Arrive at", route[i][0], "at", time_encoder(cur))

        print("Total travel time:", cur - board, "minutes\n")
        return
    one = interchange1(lines_data, station_index, source, dest)
    if one:
        sl, dl, inter, s_idx, i_s, i_d, d_idx = one
        s_sts = lines_data[sl]
        d_sts = lines_data[dl]

        r1 = routebuilder(s_sts, s_idx, i_s)
        r2 = routebuilder(d_sts, i_d, d_idx)

        names_s = list(s_sts.keys())
        off = firstarival(s_sts, names_s[s_idx])
        arr = nextrain(now, off, s_sts, False, n=1)
        if not arr:
            print("No service at this time.")
            return

        board_src = arr[0]

        print("Start at", names_s[s_idx], "(" + sl + " Line)")
        print("Next metro at", time_encoder(board_src))
        cur = board_src

        for i in range(1, len(r1)):
            cur += r1[i - 1][1]
            print("Arrive at", r1[i][0], "at", time_encoder(cur))

        print("Transfer to", dl, "Line at", inter)
        cur += changedelay

        off2 = firstarival(d_sts, inter)
        arr2 = nextrain(cur, off2, d_sts, False,n=1)
        if not arr2:
            print("No connecting metro after interchange.")
            return

        board_dest = arr2[0]
        if board_dest > cur:
            print("Wait for", board_dest - cur, "minutes")

        print("Next", dl, "metro at", time_encoder(board_dest))
        cur = board_dest

        for i in range(1, len(r2)):
            cur += r2[i - 1][1]
            print("Arrive at", r2[i][0], "at", time_encoder(cur))

        print("Total travel time:", cur - board_src, "minutes\n")
        return
    two = interchange2(lines_data, station_index, source, dest)
    if not two:
        print("No possible route between these stations with current data.")
        return

    sl, ml, dl, s_idx, i_s, i_m1, i_m2, i_d, d_idx, inter1_name, inter2_name = two
    s_sts = lines_data[sl]
    m_sts = lines_data[ml]
    d_sts = lines_data[dl]

    r1 = routebuilder(s_sts, s_idx, i_s)
    r2 = routebuilder(m_sts, i_m1, i_m2)
    r3 = routebuilder(d_sts, i_d, d_idx)

    names_s = list(s_sts.keys())
    off = firstarival(s_sts, names_s[s_idx])
    arr = nextrain(now, off, s_sts,False, n=1)
    if not arr:
        print("No service at this time.")
        return

    board_src = arr[0]
    print("Start at", names_s[s_idx], "(" + sl + " Line)")
    print("Next metro at", time_encoder(board_src))
    cur = board_src

    for i in range(1, len(r1)):
        cur += r1[i - 1][1]
        print("Arrive at", r1[i][0], "at", time_encoder(cur))

    print("Transfer to", ml, "Line at", inter1_name)
    cur += changedelay

    off_m1 =firstarival(m_sts, inter1_name)
    arr_m1 = nextrain(cur, off_m1, m_sts, False,n=1)
    if not arr_m1:
        print("No connecting metro after first interchange.")
        return

    board_mid = arr_m1[0]
    if board_mid > cur:
        print("Wait for", board_mid - cur, "minutes")
    print("Next", ml, "metro at", time_encoder(board_mid))
    cur = board_mid

    for i in range(1, len(r2)):
        cur += r2[i - 1][1]
        print("Arrive at", r2[i][0], "at", time_encoder(cur))

    print("Transfer to", dl, "Line at", inter2_name)
    cur += changedelay

    off_d2 = firstarival(d_sts, inter2_name)
    arr_d2 = nextrain(cur, off_d2, d_sts, False,n=1)
    if not arr_d2:
        print("No connecting metro after second interchange.")
        return

    board_dest = arr_d2[0]
    if board_dest > cur:
        print("Wait for", board_dest - cur, "minutes")
    print("Next", dl, "metro at", time_encoder(board_dest))
    cur = board_dest

    for i in range(1, len(r3)):
        cur += r3[i - 1][1]
        print("Arrive at", r3[i][0], "at", time_encoder(cur))

    print("Total travel time:", cur - board_src, "minutes\n")
    fair = 0
    
    if (cur-board_src)<5:
        fair = 10
    elif 5<=(cur-board_src)<15:
        fair = 23
    elif 15<=(cur-board_src)<25:
        fair = 43
    elif 25<=(cur-board_src)<50:
        fair = 60
    else:
        fair = 90
        
    print("Total Fair for the journey is",fair)
data_line, station_index = data("metro_data.txt")
def inp():
    print('''Welcome to DMRC,We have following functionalities:
            1. Metro Timings Module: To calculate when the next train will arrive at any station based on the current time.
            2. Ride journey planner: Finds the best route between
                                    two stations, showing total travel time, interchange points, and when the rider can catch
                                    the next train.''')
    inp = input("Enter your option[1 or 2]:")
    return inp.strip()
ch = inp()
if ch == "1":
    time_module(data_line)
elif ch == "2":
    planner(data_line, station_index)
else:
    print("Invalid choice.\n")
