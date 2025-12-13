metro_lines={}
n_line=None
with open("metro_data.txt", "r") as f: # to open the   file
    for li in f:
        li=li.strip()
        
        if li ==  "":
            continue
        if li.startswith ("/"):
            n_line = li[1:]
            metro_lines[n_line] =[]
            continue
        if n_line:
            try:
                parts =  [p.strip() for p in li.split(",")]
                station = parts[0]
                time_min  = parts[1] if len(parts) >= 2 else "0"
                interchagne = parts[2] if len(parts) >= 3 else ""
                metro_lines[n_line].append([station, int(time_min)])
            except Exception:
                print("Invalid line:", li)


def h_m(f):
    k,l = map(int, f.split(':'))
    return k*60 + l

def m_h(f):
    k,l = f//60, f%60
    return f'{k:02d}:{l:02d}'

def timedealer(time):
    if 480 <= time < 600 or 1020 <= time< 1140:
        return 4
    return 8

def case5(timesum,timee):
    if timee > 1380:
        return "Metro is closed now"
    if timee >= timesum:
        timee1=timedealer(timee)+timee
        timee2=timedealer(timee1)+timee1
        timee3=timedealer(timee2)+timee2
        timee4=timedealer(timee3)+timee3
        l=[timee1,timee2,timee3,timee4]

        l=[x for x in l if x<1380]
        if len(l)==4:
            return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(l[0])},{m_h(l[1])},{m_h(l[2])},{m_h(l[3])}...")
        elif len(l)==3:
            return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(l[0])},{m_h(l[1])},{m_h(l[2])},")
        elif len(l)==2:
            return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(l[0])},{m_h(l[1])}")
        elif len(l)==1:
            return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(l[0])},")
    return case5(timesum, timee+8)

def case4peak(timesum,timee):
    if timee >= timesum:
        timee1=timedealer(timee)+timee
        timee2=timedealer(timee1)+timee1
        timee3=timedealer(timee2)+timee2
        timee4=timedealer(timee3)+timee3
        return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(timee1)},{m_h(timee2)},{m_h(timee3)},{m_h(timee4)}...")
    if timee > 1140:
        return case5(timesum,timee)
    return case4peak(timesum, timee+4)

def case3(timesum,timee):
    if timee >= timesum:
        timee1=timedealer(timee)+timee
        timee2=timedealer(timee1)+timee1
        timee3=timedealer(timee2)+timee2
        timee4=timedealer(timee3)+timee3
        return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(timee1)},{m_h(timee2)},{m_h(timee3)},{m_h(timee4)}...")
    if timee > 1020:
        return case4peak(timesum,timee)
    return case3(timesum, timee+8)

def case2peak(timesum,timee):
    if timee >= timesum:
        timee1=timedealer(timee)+timee
        timee2=timedealer(timee1)+timee1
        timee3=timedealer(timee2)+timee2
        timee4=timedealer(timee3)+timee3
        return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(timee1)},{m_h(timee2)},{m_h(timee3)},{m_h(timee4)}...")
    if timee > 600:
        return case3(timesum,timee)
    return case2peak(timesum, timee+4)

def case1(timesum,timee):
    if timee >= timesum:
        timee1=timedealer(timee)+timee
        timee2=timedealer(timee1)+timee1
        timee3=timedealer(timee2)+timee2
        timee4=timedealer(timee3)+timee3
        return(f"Next metro at: {m_h(timee)}\nSubsequent metros at {m_h(timee1)},{m_h(timee2)},{m_h(timee3)},{m_h(timee4)}...")
    if timee > 480:
        return case2peak(timesum,timee)
    return case1(timesum, timee+8)

def nextmetro(lines,stations,c_times):
    total = 0
    for a in range(len(stations)):
        if a==c_times:
            break
        total += stations[a][1]
    return total

def condq1(Line,Station,C_time):

    for m,n in metro_lines.items():
        if m.lower() == Line.lower():
            for i in n:
                if i[0].strip().lower() == Station.strip().lower():
                    idx = n.index(i)
                    l = nextmetro(m,n,idx)
                    timesum = l + 360
                    
                    return print(case1(timesum, C_time))

    for m,n in metro_lines.items():
        for i in n:
            if Station.strip().lower() in i[0].strip().lower() or i[0].strip().lower().startswith(Station.strip().lower()):
                idx = n.index(i)
                l = nextmetro(m,n,idx)
                timesum = l + 360
                print(f"Line not found — using line '{m}'.")
                
                return print(case1(timesum, C_time))
    print("Not found")

# Test the journey planner with print statement fix
print("Testing journey planner with simple routes...")
print("\n=== Test 1: Same line journey (Blue line) ===")
print("Source: Dwarka, Destination: Rajiv Chowk")

# Simulating what q2 does - let me just test if the data structures work
magenta = metro_lines.get("magenta",[])
blue = metro_lines.get("blue",[])
blue1 = metro_lines.get("blue1",[])

print(f"Blue line stations: {len(blue)}")
print(f"Blue1 line stations: {len(blue1)}")
print(f"Magenta line stations: {len(magenta)}")
print(f"\nBlue line sample: {blue[:3]}")
print(f"Magenta line sample: {magenta[:3]}")
