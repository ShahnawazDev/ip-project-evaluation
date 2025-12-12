def loadmetro(file):
    stations_by_line = {}
    station_lines = {}
    interchanges = set()

    try:
        fh = open(file, "r", )
    except:
        # keep return shape consistent (used elsewhere)
        return None, None, None, {}, {}

    lines = fh.readlines()
    fh.close()

    # skip header if present
    if len(lines) > 0:
        start = 1
    else:
        start = 0

    i = start
    while i < len(lines):
        raw = lines[i].strip()
        i += 1
        if raw == "":
            continue
        parts = raw.split(",")
        # remove extra spaces
        j = 0
        for j in range(len(parts)):
            parts[j] = parts[j].strip()
        if len(parts) < 5:
            continue
        line = parts[0]
        station = parts[1]
        nxt = parts[2]
        time_str = parts[3]
        interchange_flag = parts[4]

        # travel time as integer
        try:
            t = int(time_str)
        except:
            continue

        # build stations_by_line[line][station][nxt] = t
        if line not in stations_by_line:
            stations_by_line[line] = {}
        if station not in stations_by_line[line]:
            stations_by_line[line][station] = {}
        stations_by_line[line][station][nxt] = t

        # register station lines
        if station not in station_lines:
            station_lines[station] = []
        if line not in station_lines[station]:
            station_lines[station].append(line)

        if nxt not in station_lines:
            station_lines[nxt] = []
        if line not in station_lines[nxt]:
            station_lines[nxt].append(line)

        if interchange_flag.lower() == "yes":
            interchanges.add(station)

    # build case-insensitive maps
    line_map = {ln.lower(): ln for ln in stations_by_line.keys()}
    station_map = {st.lower(): st for st in station_lines.keys()}

    return stations_by_line, station_lines, interchanges, line_map, station_map


def timetomin(s):
    parts = s.split(":")
    h = int(parts[0])
    m = int(parts[1])
    return h * 60 + m

def mintotime(total):
    h = total // 60
    m = total % 60
    hh = str(h)
    if len(hh) < 2:
        hh = "0" + hh
    mm = str(m)
    if len(mm) < 2:
        mm = "0" + mm
    return hh + ":" + mm

def validtime(s):
    parts = s.split(":")
    if len(parts) != 2:
        return False
    hh = parts[0]
    mm = parts[1]
    if not (hh.isdigit() and mm.isdigit()):
        return False
    if len(hh) != 2 or len(mm) != 2:
        return False
    h = int(hh)
    m = int(mm)
    if h < 0 or h > 23:
        return False
    if m < 0 or m > 59:
        return False
    return True

def servicehours(s):
    m = timetomin(s)
    # 06:00 to 23:00 -> 360 to 1380
    return 360 <= m <= 1380

def peakhour(s):
    m = timetomin(s)
    # morning 08:00-10:00 and evening 17:00-19:00
    return (480 <= m < 600) or (1020 <= m < 1140)

def trainfreq(s):
    if peakhour(s):
        return 4
    return 8

def nexttraintime(current, line, station):
    # returns next train time string or None
    if not servicehours(current):
        return None
    freq = trainfreq(current)
    cur = timetomin(current)
    start = 360
    # trains run from start every freq minutes
    # find how many trains have left since start
    since = (cur - start) // freq
    if since < 0:
        since = 0
    nextt = start + (since + 1) * freq
    if nextt < cur:
        nextt = cur + freq
    if nextt > 1380:
        return None
    return mintotime(nextt)

def nexttrains(line, station, current, data):
    stations_by_line = data
    if not servicehours(current):
        return []
    first = nexttraintime(current, line, station)
    if first is None:
        return []
    trains = []
    trains.append(first)
    freq = trainfreq(first)
    base = timetomin(first)
    i = 1
    while i <= 4:
        t = base + i * freq
        if t <= 1380:
            trains.append(mintotime(t))
        i += 1
    return trains

def buildgraph(line, stations_by_line):
    graph = {}
    if line not in stations_by_line:
        return graph
    # make bidirectional edges
    for st in stations_by_line[line]:
        if st not in graph:
            graph[st] = {}
        neighbors = stations_by_line[line][st]
        for n in neighbors:
            cost = neighbors[n]
            graph[st][n] = cost
            if n not in graph:
                graph[n] = {}
            graph[n][st] = cost
    return graph

def bfsline(line, src, dst, stations_by_line):
    graph = buildgraph(line, stations_by_line)
    if src not in graph or dst not in graph:
        return None
    queue = []
    queue.append((src, [src], 0))
    visited = {}
    visited[src] = True
    while len(queue) > 0:
        item = queue.pop(0)
        cur = item[0]
        path = item[1]
        total = item[2]
        if cur == dst:
            return {"path": path, "time": total, "line": line}
        neigh = graph[cur]
        for nb in neigh:
            if nb not in visited:
                visited[nb] = True
                newpath = []
                for p in path:
                    newpath.append(p)
                newpath.append(nb)
                newtotal = total + neigh[nb]
                queue.append((nb, newpath, newtotal))
    return None

def findroute(src, dst, stations_by_line, station_lines, interchanges):
    src_lines = []
    if src in station_lines:
        for l in station_lines[src]:
            src_lines.append(l)
    dst_lines = []
    if dst in station_lines:
        for l in station_lines[dst]:
            dst_lines.append(l)
    if len(src_lines) == 0 or len(dst_lines) == 0:
        return None

    # direct same line
    i = 0
    while i < len(src_lines):
        l = src_lines[i]
        j = 0
        found = False
        while j < len(dst_lines):
            if l == dst_lines[j]:
                direct = bfsline(l, src, dst, stations_by_line)
                if direct is not None:
                    return direct
            j += 1
        i += 1

    # try one interchange (two-leg)
    best = None
    for inter in interchanges:
        a = 0
        while a < len(src_lines):
            la = src_lines[a]
            leg1 = bfsline(la, src, inter, stations_by_line)
            if leg1 is None:
                a += 1
                continue
            b = 0
            while b < len(dst_lines):
                lb = dst_lines[b]
                leg2 = bfsline(lb, inter, dst, stations_by_line)
                if leg2 is None:
                    b += 1
                    continue
                total = leg1["time"] + leg2["time"] + 3
                combo = {
                    "path": leg1["path"] + leg2["path"][1:],
                    "time": total,
                    "source_route_time": leg1["time"],
                    "dest_route_time": leg2["time"],
                    "source_line": la,
                    "dest_line": lb,
                    "interchange": inter,
                    "interchange_delay": 3
                }
                if best is None or total < best["time"]:
                    best = combo
                b += 1
            a += 1
    return best

def planjourney(src, dst, time_s, data):
    stations_by_line, station_lines, interchanges = data[0], data[1], data[2]

    if not validtime(time_s):
        return {"error": "Invalid time format"}
    if not servicehours(time_s):
        return {"error": "No service", "message": "Service runs 06:00 to 23:00"}

    route = findroute(src, dst, stations_by_line, station_lines, interchanges)
    if route is None:
        return {"error": "Route not found"}

    # choose source line
    if "source_line" in route:
        src_line = route["source_line"]
    else:
        # pick first line for source
        lines = station_lines.get(src, [])
        if len(lines) == 0:
            return {"error": "No line for source"}
        src_line = lines[0]

    depart = nexttraintime(time_s, src_line, src)
    if depart is None:
        return {"error": "No trains right now"}

    result = {}
    result["source"] = src
    result["destination"] = dst
    result["source_line"] = src_line
    result["departure_time"] = depart

    depart_min = timetomin(depart)
    if "interchange" in route:
        arrive_inter = depart_min + route["source_route_time"]
        ready = arrive_inter + route["interchange_delay"]
        next_conn = nexttraintime(mintotime(ready), route["dest_line"], route["interchange"])
        if next_conn is None:
            return {"error": "No connecting train"}
        arrive_dest = timetomin(next_conn) + route["dest_route_time"]
        result["interchange"] = route["interchange"]
        result["arrival_at_interchange"] = mintotime(arrive_inter)
        result["interchange_departure"] = next_conn
        result["arrival_at_destination"] = mintotime(arrive_dest)
        result["total_time"] = arrive_dest - depart_min
    else:
        arrival = depart_min + route["time"]
        result["arrival_at_destination"] = mintotime(arrival)
        result["total_time"] = route["time"]

    return result

def printjourney(res):
    if res is None:
        print("No result")
        return
    if "error" in res:
        print("Error: " + res["error"])
        if "message" in res:
            print(res["message"])
        return
    print("")
    print("Journey Plan")
    print("Start at " + res["source"] + " (" + res["source_line"] + " Line)")
    print("Next metro at " + res["departure_time"])
    if "interchange" in res:
        print("Arrive " + res["interchange"] + " at " + res["arrival_at_interchange"])
        print("Next train departs at " + res["interchange_departure"])
    print("Reach " + res["destination"] + " at " + res["arrival_at_destination"])
    print("Total travel time: " + str(res["total_time"]) + " minutes")
    print("")

def metrotimings(data):
    stations_by_line = data[0]
    line_map = data[3]
    station_map = data[4]

    print("")
    print("=== Metro Timings ===")
    line = input("Line (e.g. Blue): ").strip()
    station = input("Station: ").strip()
    current = input("Current time (HH:MM): ").strip()

    # case-insensitive lookup
    if line.lower() in line_map:
        line_canonical = line_map[line.lower()]
    else:
        print("Error: Invalid line.")
        return

    if station.lower() in station_map:
        station_canonical = station_map[station.lower()]
    else:
        print("Error: Invalid station.")
        return

    if line_canonical not in stations_by_line:
        print("Error: Invalid line.")
        return
    if station_canonical not in stations_by_line[line_canonical]:
        print("Error: Invalid station for this line.")
        return
    if not validtime(current):
        print("Error: Use HH:MM format.")
        return
    trains = nexttrains(line_canonical, station_canonical, current, stations_by_line)
    if len(trains) == 0:
        print("No trains available right now.")
        return
    print("Next metro at " + trains[0])
    if len(trains) > 1:
        i = 1
        s = ""
        while i < len(trains):
            if i > 1:
                s = s + ", "
            s = s + trains[i]
            i += 1
        print("Following metros: " + s)

def journeyplanner(data):
    line_map = data[3]
    station_map = data[4]

    print("")
    print("=*= Journey Planner =*=")
    src = input("Starting station: ").strip()
    dst = input("Final station: ").strip()
    time_s = input("Time (HH:MM): ").strip()
    if not validtime(time_s):
        print("Error: Use HH:MM format.")
        return

    # normalize station names case-insensitively
    if src.lower() in station_map:
        src_canonical = station_map[src.lower()]
    else:
        print("Error: Unknown source station.")
        return
    if dst.lower() in station_map:
        dst_canonical = station_map[dst.lower()]
    else:
        print("Error: Unknown destination station.")
        return

    res = planjourney(src_canonical, dst_canonical, time_s, data)
    printjourney(res)

def main():
    print("==**==**==**==**==**==**==**==**=**==**==**==")
    print("Delhi Metro Route & Schedule Simulator")
    print("==**==**==**==**==**==**==**==**=**==**==**==")
    data = loadmetro("metro_data.txt")
    if data[0] is None:
        print("metro_data.txt not found.")
        return
    while True:
        print("")
        print("1. Metro Timings")
        print("2. Journey Planner")
        print("3. Exit")
        choice = input("Choose 1-3: ").strip()
        if choice == "1":
            metrotimings(data)
        elif choice == "2":
            journeyplanner(data)
        elif choice == "3":
            print("Thanks for Visiting!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()