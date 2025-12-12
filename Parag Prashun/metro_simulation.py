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
def q2():
    
   Timei=0
   metro_lines={}
   cur_line=None
   with open("metro_data.txt","r") as file:
      # skip first 99 lines (option-2 data starts after line 99)
      for i in range(0):
         try:
            next(file)
         except StopIteration:
            break
      for line in file:
         line=line.strip()
         if line=="":
            continue
         if line.startswith("/"):
               cur_line=line[1:]
               metro_lines[cur_line]=[]
               continue
         if cur_line:
               try:
                  station,timemin=line.split(",")
                  metro_lines[cur_line].append([station.strip(),int(timemin.strip())])
               except Exception:
                  pass

   magenta = metro_lines.get("magenta",[])
   blue1   = metro_lines.get("blue1",[])
   blue2   = metro_lines.get("blue2",[])
   blue3   = metro_lines.get("blue3",[])
   blue4   = metro_lines.get("blue4",[])
   blue5   = metro_lines.get("blue5",[])

   def timecal(timemin):
      hour=timemin//60
      minute=timemin%60
      return f"{hour:02d}:{minute:02d}"

   def timecal_rev(timehour,timemin):
      return int(timehour)*60+int(timemin)

   def finaltime():
      return "There is no metro available"

   def case5_(timesum, timee):
      if timee > 1380:
         return "Metro is closed now"
      if timee >= timesum:
         return timecal(timee)
      return case5_(timesum, timee + 8)

   def case4peak_(timesum, timee):
      if timee >= timesum:
         return timecal(timee)
      if timee > 1140:
         return case5_(timesum, timee)
      return case4peak_(timesum, timee + 4)

   def case3_(timesum, timee):
      if timee >= timesum:
         return timecal(timee)
      if timee > 1020:
         return case4peak_(timesum, timee)
      return case3_(timesum, timee + 8)

   def case2peak_(timesum, timee):
      if timee >= timesum:
         return timecal(timee)
      if timee > 600:
         return case3_(timesum, timee)
      return case2peak_(timesum, timee + 4)

   def case1_(timesum, timee):
      if timee >= timesum:
         return timecal(timee)
      if timee > 480:
         return case2peak_(timesum, timee)
      return case1_(timesum, timee + 8)

   def sum_forward(line, src):
      found=False
      s=0
      for name,t in line:
         if name==src:
            found=True
         if found:
            s+=t
      return s

   def sum_backward(line, src):
      found=False
      s=0
      k=len(line)
      for i in range(k):
         name,t = line[k-1-i]
         if name==src:
            found=True
         if found:
            s+=t
      return s

   def sum_magenta_between(line, src, dst):
      found=False
      s=0
      k=len(line)
      for i in range(k):
         name,t = line[k-1-i]
         if name==src:
            found=True
         if name==dst:
            found=False
         if found:
            s+=t
      return s

   def ride_plan():
      magenta_m=67
      blue=64
      blue1_total=28
      blue2_total=35
      blue3_total=16
      blue4_total=18
      blue5_total=15
      print("Rider Journey Planner\nUser Input:")
      source=input("Source: ").strip()
      dest=input("Destination: ").strip()
      t=input("Time of travel: ").strip()
      try:
         h,m=t.split(":")
      except Exception:
         return "Invalid time format"
      time_m=timecal_rev(h,m)

      if dest in [s[0] for s in magenta]:
          dest_d="magenta"
      elif dest in [s[0] for s in blue1]:
          dest_d="blue1"
      elif dest in [s[0] for s in blue2]:
          dest_d="blue2"
      elif dest in [s[0] for s in blue3]:
          dest_d="blue3"
      elif dest in [s[0] for s in blue4]:
          dest_d="blue4"
      elif dest in [s[0] for s in blue5]:
          dest_d="blue5"
      else:
          return "invalid dest"

      if source in [s[0] for s in magenta]:
          source_d="magenta"
      elif source in [s[0] for s in blue1]:
          source_d="blue1"
      elif source in [s[0] for s in blue2]:
          source_d="blue2"
      elif source in [s[0] for s in blue3]:
          source_d="blue3"
      elif source in [s[0] for s in blue4]:
          source_d="blue4"
      elif source in [s[0] for s in blue5]:
          source_d="blue5"
      else:
          return "invalid source"

      if time_m>1380 or time_m<360:
         return finaltime()

      # special interchange cases: instantaneous transfers (time = 0)
      if source == "JanakpuriWest" and (dest_d=="magenta" or dest_d=="blue1" or dest_d=="blue2"):
         return 0
      if dest == "JanakpuriWest" and (source_d=="magenta" or source_d=="blue1" or source_d=="blue2"):
         return 0

      if source == "BotanicalGarden" and (dest_d=="magenta" or dest_d=="blue4" or dest_d=="blue5"):
         return 0
      if dest == "BotanicalGarden" and (source_d=="magenta" or source_d=="blue4" or source_d=="blue5"):
         return 0

      if source == "YamunaBank" and (dest_d=="blue2" or dest_d=="blue3" or dest_d=="blue4"):
         return 0
      if dest == "YamunaBank" and (source_d=="blue2" or source_d=="blue3" or source_d=="blue4"):
         return 0

      # fallback: same-line magenta
      if source_d=='magenta' and dest_d=='magenta':
         return sum_magenta_between(magenta, source, dest)

      # many case-based route patterns (keeps your original structure)
      if source_d != "magenta" and dest_d != "magenta":

            janak=2
            botanical=2
            yamuna=3

            if source_d == "blue1" and dest_d == "blue3":
               sum_val = blue2_total
               sum_val += sum_forward(blue1, source)
               sum_val += sum_forward(blue3, dest)  # forward from start of blue3 to dest
               return sum_val + janak + yamuna

            elif source_d == "blue3" and dest_d == "blue1":
               sum_val = blue2_total
               sum_val += sum_backward(blue3, source)
               sum_val += sum_backward(blue1, dest)
               return sum_val + janak + yamuna

            elif source_d == "blue1" and dest_d == "blue2":
               sum_val = sum_forward(blue1, source)
               sum_val += sum_forward(blue2, dest)
               return sum_val

            elif source_d == "blue2" and dest_d == "blue1":
               sum_val = sum_backward(blue2, source)
               sum_val += sum_backward(blue1, dest)
               return sum_val

            elif source_d == "blue2" and dest_d == "blue3":
               sum_val = sum_forward(blue2, source)
               sum_val += sum_forward(blue3, dest)
               return sum_val

            elif source_d == "blue3" and dest_d == "blue2":
               sum_val = sum_backward(blue3, source)
               sum_val += sum_backward(blue2, dest)
               return sum_val

            elif source_d == "blue3" and dest_d == "blue4":
               sum_val = sum_backward(blue3, source)
               sum_val += sum_forward(blue4, dest)
               return sum_val + yamuna

            elif source_d == "blue4" and dest_d == "blue3":
               sum_val = sum_backward(blue4, source)
               sum_val += sum_forward(blue3, dest)
               return sum_val + yamuna

            elif source_d == "blue4" and dest_d == "blue5":
               sum_val = sum_forward(blue4, source)
               sum_val += sum_forward(blue5, dest)
               return sum_val + botanical

            elif source_d == "blue5" and dest_d == "blue4":
               sum_val = sum_backward(blue5, source)
               sum_val += sum_backward(blue4, dest)
               return sum_val + botanical

            elif source_d == "blue1" and dest_d == "blue4":
               sum_val = blue2_total + blue3_total
               sum_val += sum_forward(blue1, source)
               sum_val += sum_forward(blue4, dest)
               return sum_val + janak + yamuna

            elif source_d == "blue4" and dest_d == "blue1":
               sum_val = blue2_total + blue3_total
               sum_val += sum_backward(blue4, source)
               sum_val += sum_backward(blue1, dest)
               return sum_val + janak + yamuna

            elif source_d == "blue1" and dest_d == "blue5":
               sum_val = blue2_total + blue4_total
               sum_val += sum_backward(blue1, source)
               sum_val += sum_forward(blue5, dest)
               return sum_val + janak + yamuna + botanical

            elif source_d == "blue5" and dest_d == "blue1":
               sum_val = blue4_total + blue2_total
               sum_val += sum_backward(blue5, source)
               sum_val += sum_backward(blue1, dest)
               return sum_val + janak + yamuna + botanical

            elif source_d == "blue2" and dest_d == "blue4":
               sum_val = sum_forward(blue2, source)
               sum_val += sum_forward(blue4, dest)
               return sum_val + yamuna

            elif source_d == "blue4" and dest_d == "blue2":
               sum_val = sum_backward(blue4, source)
               sum_val += sum_backward(blue2, dest)
               return sum_val + yamuna

            elif source_d == "blue2" and dest_d == "blue5":
               sum_val = blue4_total
               sum_val += sum_forward(blue2, source)
               sum_val += sum_forward(blue5, dest)
               return sum_val + yamuna + botanical

            elif source_d == "blue5" and dest_d == "blue2":
               sum_val = blue4_total
               sum_val += sum_backward(blue5, source)
               sum_val += sum_backward(blue2, dest)
               return sum_val + yamuna + botanical

            elif source_d == "blue3" and dest_d == "blue5":
               sum_val = blue4_total
               sum_val += sum_backward(blue3, source)
               sum_val += sum_forward(blue5, dest)
               return sum_val + yamuna + botanical

            elif source_d == "blue5" and dest_d == "blue3":
               sum_val = blue4_total
               sum_val += sum_backward(blue5, source)
               sum_val += sum_forward(blue3, dest)
               return sum_val + yamuna + botanical

      # magenta <> other-line cases
      if source_d == "magenta" and dest_d != "magenta":
            # magenta -> blue2 (via Janakpuri & Botanical)
            if dest_d == "blue2":
               # try both directions and pick smaller
               temp1 = sum_forward(magenta, source) + janak + botanical  # magenta forward -> janak -> botanical -> blue2
               temp2 = sum_backward(blue2, dest) + janak + botanical
               return temp1 if temp1<=temp2 else temp2

            if dest_d == "blue1":
               return sum_backward(magenta, source) + 0

            if dest_d == "blue3":
               sum_val = blue4_total
               sum_val += sum_forward(magenta, source)
               sum_val += sum_forward(blue3, dest)
               return sum_val + botanical + yamuna

            if dest_d == "blue4":
               sum_val = sum_forward(magenta, source)
               sum_val += sum_backward(blue4, dest)
               return sum_val + botanical

            if dest_d == "blue5":
               sum_val = sum_forward(magenta, source)
               sum_val += sum_forward(blue5, dest)
               return sum_val + botanical

      if dest_d == "magenta" and source_d != "magenta":
            # blue2 -> magenta
            if source_d == "blue2":
               temp1 = sum_forward(blue2, source) + janak + botanical
               temp2 = sum_backward(magenta, dest) + janak + botanical
               return temp1 if temp1<=temp2 else temp2

            if source_d == "blue1":
               return sum_forward(blue1, source) + 0

            if source_d == "blue3":
               sum_val = blue4_total
               sum_val += sum_backward(blue3, source)
               sum_val += sum_backward(magenta, dest)
               return sum_val + botanical + yamuna

            if source_d == "blue4":
               sum_val = sum_backward(blue4, source)
               sum_val += sum_forward(magenta, dest)
               return sum_val + botanical

            if source_d == "blue5":
               sum_val = sum_backward(blue5, source)
               sum_val += sum_backward(magenta, dest)
               return sum_val + botanical

      return "Route not found"

   return ride_plan()
def q1():
    print('UserInput')
    Line = input('Line = ')
    Station = input('Station = ')
    C_time = h_m(input('Current time = '))
    condq1(Line,Station,C_time)

def menu1():

    print("Welcome to Delhi Metro\nMetro Timings - Press 1\nRider Journey Planner - Press 2\nExit - Press 3")
    try:
       op=int(input("Enter your choice: ").strip())
    except Exception:
       print("Wrong Choice\nTry Again")
       menu1()
       return
    if op==1:
        q1()
    elif op==2:
        q2()
        print()
    elif op==3:
        print("Thank You for Using Delhi Metro")
    else:
        print("Wrong Choice")
        print('Try Again"')
        menu1()

menu1()
