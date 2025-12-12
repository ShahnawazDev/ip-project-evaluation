class Time:
    def __init__(self, hours,mins):
        self.hour=hours
        self.min=mins

    def Add_Time(self,time):
        min_add=self.min+time.min
        if min_add>59:
            hour_add=min_add//60
            min_add=min_add%60

            hour_add+=self.hour+time.hour
            return Time(hour_add,min_add)
        
        else:
            hour_add=self.hour+time.hour
            return Time(hour_add,min_add)
        
    def Subtract_Time(self,time):
        min_subtract=self.min-time.min
        if min_subtract<0:
            hours=self.hour
            mins=self.min
            hours-=1
            mins+=60
            min_subtract=mins-time.min
            hour_subtract=hours-time.hour
            return Time(hour_subtract,min_subtract)
        else:
            hour_subtract=self.hour-time.hour
            return Time(hour_subtract,min_subtract)


    def Min_To_Time(mins):
        hour=mins//60
        min=mins%60
        return Time(hour,min)
    
    def __str__(self):
        return f"{self.hour:02}:{self.min:02}"
    
f=open(r"C:\Users\Vineet\Desktop\assignment\Data.txt","r")
a=f.readlines()
for i in range(len(a)):
    a[i]=a[i][:-1:]

for j in range(len(a)):
    if a[j]=='Noida Electronic City':
        a[j]=['Noida Electronic City']
    elif a[j]=='Botanical Garden':
        a[j]=['Botanical Garden']
    elif a[j]=='':
        pass
    else:
        a[j]=a[j].split(",")

blue1=a[:49:]
for i in range(len(blue1)):
    if i==0:
        pass
    else:
        blue1[i][1]=int(blue1[i][1])
blue2=a[50:57:]
for i in range(len(blue2)):
    blue2[i][1]==int(blue2[i][1])

magenta=a[58::]
for i in range(len(magenta)):
    if i==0:
        pass
    else:
        magenta[i][1]=int(magenta[i][1])

interchange=['Botanical Garden','Janak Puri West','Yamuna bank']

blueline1=[]
blueline2=[]
magentaline=[]
for i in blue1:
    blueline1.append(i[0])
for j in blue2:
    blueline2.append(j[0])
for k in magenta:
    magentaline.append(k[0])

peak1_start=Time(8,00)
peak1_end=Time(10,00)
peak2_start=Time(17,00)
peak2_end=Time(19,00)
end_time=Time(23,0)
all_metro_timing=[]
time_t=Time(6,0)
while time_t.hour <= end_time.hour:
    if time_t.hour==end_time.hour:
        if time_t.min!=0:
            break
    all_metro_timing.append(time_t)
    if time_t.hour >= peak1_start.hour  and time_t.hour < peak1_end.hour or time_t.hour >= peak2_start.hour and time_t.hour < peak2_end.hour :
        time_t=time_t.Add_Time(Time(0,4))
    else:
        time_t=time_t.Add_Time(Time(0,8))

def Find_next_Train(time,currtime):
    if currtime.hour>=6 and currtime.hour<=23:
        lst=[]
        for i in all_metro_timing:
            lst.append(i.hour*60+i.min)
        time_in_mins=(time.hour*60)+time.min
        if time_in_mins<=360:
            return Time.Min_To_Time(lst[0])
        elif time_in_mins>=1380:
            return Time.Min_To_Time(lst[-1])
        else:
            for j in range(len(lst)):
                if lst[j]<time_in_mins:
                    if lst[j+1]>=time_in_mins:
                        return Time.Min_To_Time(lst[j+1])
    else:
        print("No Service Avaliable.")

def calc_traveltime(station1,station2,line):
    line=line.lower()
    if line=="blue1":
        index=[]
        for i in range(len(blueline1)):
            if blueline1[i]==station1:
                index.append(i)
        for i in range(len(blueline1)):
            if blueline1[i]==station2:
                index.append(i)
        i1=index[0]
        i2=index[1]
        traveltime=0
        trace=blue1[(i1+1):(i2+1):]
        for i in trace:
            traveltime+=i[1]
        return traveltime

    elif line=="blue2":
        index=[]
        for i in range(len(blueline2)):
            if blueline2[i]==station1:
                index.append(i)
        for i in range(len(blueline2)):
            if blueline2[i]==station2:
                index.append(i)
        i1=index[0]
        i2=index[1]
        traveltime=0
        trace=blue2[(i1+1):(i2+1):]
        for i in trace:
            traveltime+=i[1]
        return traveltime
    elif line=="magenta":
        index=[]
        for i in range(len(magentaline)):
            if magentaline[i]==station1:
                index.append(i)
        for i in range(len(magentaline)):
            if magentaline[i]==station2:
                index.append(i)
        i1=index[0]
        i2=index[1]
        traveltime=0
        trace=magenta[(i1+1):(i2+1):]
        for i in trace:
            traveltime+=i[1]
        return traveltime

def find_next_train_on_station(station,source,time,line):
    traveltime=calc_traveltime(source,station,line)
    time_at_source=time.Subtract_Time(Time.Min_To_Time(traveltime))
    train_dept_source=Find_next_Train(time_at_source,time)
    next_train_on_station=train_dept_source.Add_Time(Time.Min_To_Time(traveltime))
    return next_train_on_station

#Ques1
def Metro_Timing():
    line=input("Line=")
    station=input("Station=")
    currtime=input("Current Time (24 hours)= ")
    currtime=currtime.split(":")
    currtime=Time(int(currtime[0]),int(currtime[1]))
    if line.lower()== "blue":
        station_in_blue1=False
        station_in_blue2=False
        for i in blue1:
            if i[0]==station:
                station_in_blue1=True
            else:
                pass
        for i in blue2:
            if i[0]==station:
                station_in_blue2=True
            else:
                pass

        if station_in_blue1:
            traveltime_towards_dwarka=0
            traveltime_towards_noidaelec=0
            flag=0
            for i in blue1:
                if i[0]==station and len(i)!=1:
                    flag=i[1]

            sliceflag=0
            breaklst=[station,flag]
            for j in range(len(blue1)):
                if blue1[j]==breaklst:
                    sliceflag=j
                    break

            splitted1=blue1[:sliceflag:]
            splitted2=blue1[sliceflag+1::]
            if len(splitted1)==0:
                pass
            else:
                if len(splitted1)==1:
                    traveltime_towards_noidaelec+=breaklst[1]
                else:

                    traveltime_towards_noidaelec+=breaklst[1]
                    for i in splitted1:
                        if i[0]!='Noida Electronic City':
                            traveltime_towards_noidaelec+=i[1]

            if len(splitted2)==0:
                pass
            else:
                for i in splitted2:
                    traveltime_towards_dwarka+=i[1]
            
            time_at_noidaelec=currtime.Subtract_Time(Time.Min_To_Time(traveltime_towards_noidaelec))
            time_at_dwarka=currtime.Subtract_Time(Time.Min_To_Time(traveltime_towards_dwarka))
            train_dept_time_noidaelec=Find_next_Train(time_at_noidaelec,currtime)
            train_dept_time_dwarka=Find_next_Train(time_at_dwarka,currtime)
            
            
            train_time_at_dwarka=train_dept_time_dwarka.Add_Time(Time.Min_To_Time(traveltime_towards_dwarka))
            train_time_at_noidaelec=train_dept_time_noidaelec.Add_Time(Time.Min_To_Time(traveltime_towards_noidaelec))
            train_dept_time_noidaelec2=find_next_train_on_station(station,"Noida Electronic City",train_time_at_noidaelec.Add_Time(Time.Min_To_Time(1)),"blue1")
            train_dept_time_noidaelec3=find_next_train_on_station(station,"Noida Electronic City",train_dept_time_noidaelec2.Add_Time(Time.Min_To_Time(1)),"blue1")
            train_dept_time_noidaelec4=find_next_train_on_station(station,"Noida Electronic City",train_dept_time_noidaelec3.Add_Time(Time.Min_To_Time(1)),"blue1")
            train_time_at_dwarka2=Find_next_Train(train_time_at_dwarka.Add_Time(Time.Min_To_Time(1)),train_time_at_dwarka)
            train_time_at_dwarka3=Find_next_Train(train_time_at_dwarka2.Add_Time(Time.Min_To_Time(1)),train_time_at_dwarka2)
            train_time_at_dwarka4=Find_next_Train(train_time_at_dwarka3.Add_Time(Time.Min_To_Time(1)),train_time_at_dwarka3)

            print("_____________________________________________________")
            print("Next Train towards Noida Electronic City at ",train_time_at_noidaelec)
            print("Subsequent Metros :",train_dept_time_noidaelec2,",",train_dept_time_noidaelec3,",",train_dept_time_noidaelec4)
            print("Next Train towards Dwarka Sector - 21 at ",train_time_at_dwarka)
            print("Subsequent Metros :",train_time_at_dwarka2,",",train_time_at_dwarka3,",",train_time_at_dwarka4)
            print("_____________________________________________________")
            
        elif station_in_blue2:
            traveltime_towards_vaishali=0
            traveltime_towards_yamunabank=0
            flag=0
            for i in blue2:
                if i[0]==station and len(i)!=1:
                    flag=i[1]

            sliceflag=0
            breaklst=[station,flag]
            for j in range(len(blue2)):
                if blue2[j]==breaklst:
                    sliceflag=j
                    break

            splitted1=blue2[:sliceflag:]
            splitted2=blue2[sliceflag+1::]
            if len(splitted1)==0:
                pass
            else:
                if len(splitted1)==1:
                    traveltime_towards_yamunabank+=breaklst[1]
                else:

                    traveltime_towards_yamunabank+=breaklst[1]
                    for i in splitted1:
                        if i[0]!='Laxmi Nagar':
                            traveltime_towards_yamunabank+=i[1]

            if len(splitted2)==0:
                pass
            else:
                for i in splitted2:
                    traveltime_towards_vaishali+=i[1]
            
            traveltime_towards_yamunabank+=blue2[0][1]
            time_at_laxmi=currtime.Subtract_Time(Time.Min_To_Time(traveltime_towards_yamunabank))
            time_at_vaishali=currtime.Subtract_Time(Time.Min_To_Time(traveltime_towards_vaishali))
            train_dept_time_laxmi=Find_next_Train(time_at_laxmi,currtime)
            train_dept_time_vaishali=Find_next_Train(time_at_vaishali,currtime)
            train_time_at_vaishali=train_dept_time_vaishali.Add_Time(Time.Min_To_Time(traveltime_towards_vaishali))
            train_time_at_laxmi=train_dept_time_laxmi.Add_Time(Time.Min_To_Time(traveltime_towards_yamunabank))
            train_time_at_laxmi2=find_next_train_on_station(station,"Laxmi Nagar",train_time_at_laxmi.Add_Time(Time.Min_To_Time(1)),"blue2")
            train_time_at_laxmi3=find_next_train_on_station(station,"Laxmi Nagar",train_time_at_laxmi2.Add_Time(Time.Min_To_Time(1)),"blue2")
            train_time_at_laxmi4=find_next_train_on_station(station,"Laxmi Nagar",train_time_at_laxmi3.Add_Time(Time.Min_To_Time(1)),"blue2")
            train_time_at_vaishali2=find_next_train_on_station(station,"Vaishali",train_time_at_vaishali.Add_Time(Time.Min_To_Time(1)),"blue2")
            train_time_at_vaishali3=find_next_train_on_station(station,"Vaishali",train_time_at_vaishali2.Add_Time(Time.Min_To_Time(1)),"blue2")
            train_time_at_vaishali4=find_next_train_on_station(station,"Vaishali",train_time_at_vaishali3.Add_Time(Time.Min_To_Time(1)),"blue2")
            print("_____________________________________________________")
            print("Next Train towards Laxmi Nagar at ",train_time_at_laxmi)
            print("Subsequent trains:",train_time_at_laxmi2,",",train_time_at_laxmi3,",",train_time_at_laxmi4)
            print("Next Train towards Vaishali at ",train_time_at_vaishali)
            print("Subsequent trains:",train_time_at_vaishali2,",",train_time_at_vaishali3,",",train_time_at_vaishali4)
            print("_____________________________________________________")

            

    elif line.lower()== "magenta":
        traveltime_towards_janakpuri=0
        traveltime_towards_botanical=0
        flag=0
        for i in magenta:
            if i[0]==station and len(i)!=1:
                flag=i[1]

        sliceflag=0
        breaklst=[station,flag]
        for j in range(len(magenta)):
            if magenta[j]==breaklst:
                sliceflag=j
                break

        splitted1=magenta[:sliceflag:]
        splitted2=magenta[sliceflag+1::]
        if len(splitted1)==0:
            pass
        else:
            if len(splitted1)==1:
                traveltime_towards_botanical+=breaklst[1]
            else:

                traveltime_towards_botanical+=breaklst[1]
                for i in splitted1:
                    if i[0]!='Botanical Garden':
                        traveltime_towards_botanical+=i[1]

        if len(splitted2)==0:
            pass
        else:
            for i in splitted2:
                traveltime_towards_janakpuri+=i[1]
        
        time_at_botanical=currtime.Subtract_Time(Time.Min_To_Time(traveltime_towards_botanical))
        time_at_janakpuri=currtime.Subtract_Time(Time.Min_To_Time(traveltime_towards_janakpuri))
        train_dept_time_botanical=Find_next_Train(time_at_botanical,currtime)
        train_dept_time_dwarka=Find_next_Train(time_at_janakpuri,currtime)
        train_time_at_janakpuri=train_dept_time_dwarka.Add_Time(Time.Min_To_Time(traveltime_towards_janakpuri))
        train_time_at_botanical=train_dept_time_botanical.Add_Time(Time.Min_To_Time(traveltime_towards_botanical))
        train_dept_time_botanical2=find_next_train_on_station(station,"Botanical Garden",train_time_at_botanical.Add_Time(Time.Min_To_Time(1)),"blue1")
        train_dept_time_botanical3=find_next_train_on_station(station,"Botanical Garden",train_dept_time_botanical2.Add_Time(Time.Min_To_Time(1)),"blue1")
        train_dept_time_botanical4=find_next_train_on_station(station,"Botanical Garden",train_dept_time_botanical3.Add_Time(Time.Min_To_Time(1)),"blue1")
        train_dept_time_janakpuri2=find_next_train_on_station(station,"",train_time_at_janakpuri.Add_Time(Time.Min_To_Time(1)),"blue1")
        train_dept_time_janakpuri3=find_next_train_on_station(station,"",train_dept_time_janakpuri2.Add_Time(Time.Min_To_Time(1)),"blue1")
        train_dept_time_janakpuri4=find_next_train_on_station(station,"",train_dept_time_janakpuri3.Add_Time(Time.Min_To_Time(1)),"blue1")

        print("_____________________________________________________")
        print("Next Train towards Botanical Garden at ",train_time_at_botanical)
        print("Subsequent Trains :",train_dept_time_botanical2,",",train_dept_time_botanical3,",",train_dept_time_botanical4)
        print("Next Train towards Janakpuri West at ",train_time_at_janakpuri)
        print("Subsequent Trains :",train_dept_time_janakpuri2,",",train_dept_time_janakpuri3,",",train_dept_time_janakpuri4)
        print("_____________________________________________________")


def calculate_fare(mins):
    if mins<=10: 
        return 11
    elif mins<=25: 
        return 21
    elif mins<=45: 
        return 32
    elif mins<=65: 
        return 43
    elif mins<=90: 
        return 54
    else: 
        return 64

#Ques2
def Journey_Planner():
    def Output(interchange,source,time_source,destination,time_destination,line,travel_time):
        if interchange[0]=="No":
            print("_____________________________________________________")
            print("Journey Plan:")
            print("Start at", source ,"(",line, "Line )")
            print("Next metro at",time_source)
            print("Arrive at", destination,"at",time_destination)
            print("Total travel time:",travel_time)
            print("Total fare : Rs.",calculate_fare(travel_time))
            print("_____________________________________________________")
        elif interchange[0]=="Yes":
            print("_____________________________________________________")
            print("Journey Plan:")
            print("Start at", source ,"(",line, "Line)")
            print("Next metro at",time_source)
            print("Arrive at", interchange[1],"at",interchange[2])
            print("Transfer to", interchange[3] ,"Line")
            print("Next",line, "metro departs at", interchange[4])
            print("Arrive at", destination,"at",time_destination)
            print("Total travel time:",travel_time)
            print("Total fare : Rs.",calculate_fare(travel_time))
            print("_____________________________________________________")

    src=input("Enter Source Station : ")
    dst=input("Enetr Destination Station : ")
    t=input("Enter time of travel : ")
    t=t.split(":")
    t=Time(int(t[0]),int(t[1]))

    if src in blueline1 and dst in blueline1:
        interchange=["No"]
        src_indx=blueline1.index(src)
        dst_indx=blueline1.index(dst)
        line="Blue"

        if src_indx<dst_indx:
            time_src=find_next_train_on_station(src,"Noida Electronic City",t,"blue1")
            travelt=calc_traveltime(src,dst,"blue1")
            time_dst=time_src.Add_Time(Time.Min_To_Time(travelt))
            Output(interchange,src,time_src,dst,time_dst,line,travelt)
        elif src_indx>dst_indx:
            time_src=find_next_train_on_station(src,"Dwarka Sector - 21",t,"blue1")
            travelt=calc_traveltime(dst,src,"blue1")
            time_dst=time_src.Add_Time(Time.Min_To_Time(travelt))
            Output(interchange,src,time_src,dst,time_dst,line,travelt)
        else:
            print("Enter 2 different stations.")

    elif src in blueline1 and dst in blueline2:
        interchange=["Yes"]
        src_indx=blueline1.index(src)
        dst_indx=blueline2.index(dst)
        line="Blue 1"
        if src_indx<16:
            time_src=find_next_train_on_station(src,"Noida Electronic City",t,"blue1")
            travelt1=calc_traveltime(src,"Yamuna bank","blue1")
            travelt2=calc_traveltime("Laxmi Nagar",dst,"blue2")
            travelt=travelt1+travelt2+3
            interchange_sat=time_src.Add_Time(Time.Min_To_Time(travelt1))
            interchange_station="Yamuna bank"
            interchange_line="Blue 2"
            interchange_dept=find_next_train_on_station("Yamuna bank","Noida Electronic City",interchange_sat,"blue1")
            time_dst=interchange_dept.Add_Time(Time.Min_To_Time(2+travelt2))
            interchange.append(interchange_sat)
            interchange.append(interchange_station)
            interchange.append(interchange_line)
            interchange.append(interchange_dept)
            Output(interchange,src,time_src,dst,time_dst,line,travelt)
        if src_indx>16:
            time_src=find_next_train_on_station(src,"Dwarka Sector - 21",t,"blue1")
            travelt1=calc_traveltime(src,"Yamuna bank","blue1")
            travelt2=calc_traveltime("Laxmi Nagar",dst,"blue2")
            travelt=travelt1+travelt2+3
            interchange_sat=time_src.Add_Time(Time.Min_To_Time(travelt1))
            interchange_station="Yamuna bank"
            interchange_line="Blue 2"
            interchange_dept=find_next_train_on_station("Yamuna bank","Dwarka Sector - 21",interchange_sat,"blue1")
            time_dst=interchange_dept.Add_Time(Time.Min_To_Time(2+travelt2))
            interchange.append(interchange_sat)
            interchange.append(interchange_station)
            interchange.append(interchange_line)
            interchange.append(interchange_dept)
            Output(interchange,src,time_src,dst,time_dst,line,travelt)

    elif src in blueline1 and dst in magentaline:
        interchange=["Yes"]
        options=["Botanical Garden", "Janak Puri West"]
        lst=[]

        for i in options:
            dis1=calc_traveltime(src, i, "blue1")
            dis2=calc_traveltime(i, dst, "magenta")
            lst.append([i,dis1+dis2])

        time_via_botanical=lst[0][1]
        time_via_jpwest=lst[1][1]

        if time_via_botanical < time_via_jpwest:
            interchange_station=lst[0][0]
            travelt1=calc_traveltime(src, interchange_station, "blue1")
            travelt2=calc_traveltime(interchange_station, dst, "magenta")
        else:
            interchange_station=lst[1][0]
            travelt1=calc_traveltime(src, interchange_station, "blue1")
            travelt2=calc_traveltime(interchange_station, dst, "magenta")

        src_idx=blueline1.index(src)
        interchange_idx=blueline1.index(interchange_station)
        
        if src_idx < interchange_idx:
            dir_blue="Dwarka Sector - 21"
        else:
            dir_blue="Noida Electronic City"

        time_src=find_next_train_on_station(src, dir_blue, t, "blue1")
        arrival_at_interchange=time_src.Add_Time(Time.Min_To_Time(travelt1))
        mag_start_idx=magentaline.index(interchange_station)
        mag_end_idx=magentaline.index(dst)
        
        if mag_start_idx < mag_end_idx:
            dir_mag="Janak Puri West"
        else:
            dir_mag="Botanical Garden"

        dept_from_interchange=find_next_train_on_station(interchange_station, dir_mag, arrival_at_interchange, "magenta")
        
        time_dst=dept_from_interchange.Add_Time(Time.Min_To_Time(travelt2))
        total_time=travelt1+travelt2
        
        interchange.append(interchange_station)
        interchange.append(arrival_at_interchange)
        interchange.append("Magenta")
        interchange.append(dept_from_interchange)
        Output(interchange, src, time_src, dst, time_dst, "Blue 1", total_time)
    
    elif src in blueline2 and dst in blueline1:
        interchange=["Yes"]
        interchange_station="Yamuna bank"
        travelt_to_laxmi=calc_traveltime(src, "Laxmi Nagar", "blue2")
        travelt1=travelt_to_laxmi+3 
        time_src=find_next_train_on_station(src, "Laxmi Nagar", t, "blue2")
        arrival_at_interchange=time_src.Add_Time(Time.Min_To_Time(travelt1))        
        travelt2=calc_traveltime(interchange_station, dst, "blue1")
        yb_idx=blueline1.index(interchange_station)
        dst_idx=blueline1.index(dst)

        if dst_idx < yb_idx:
            direction_blue1="Noida Electronic City"
        else:
            direction_blue1="Dwarka Sector - 21"

        dept_from_interchange=find_next_train_on_station(interchange_station, direction_blue1, arrival_at_interchange, "blue1")
        time_dst=dept_from_interchange.Add_Time(Time.Min_To_Time(travelt2))
        total_time=travelt1+travelt2

        interchange.append(interchange_station)
        interchange.append(arrival_at_interchange)
        interchange.append("Blue 1")
        interchange.append(dept_from_interchange)

        Output(interchange, src, time_src, dst, time_dst, "Blue 2", total_time)

    elif src in blueline2 and dst in blueline2:
        interchange=["No"]
        src_indx=blueline1.index(src)
        dst_indx=blueline1.index(dst)
        line="Blue"

        if src_indx<dst_indx:
            time_src=find_next_train_on_station(src,"Noida Electronic City",t,"blue2")
            travelt=calc_traveltime(src,dst,"blue1")
            time_dst=time_src.Add_Time(Time.Min_To_Time(travelt))
            Output(interchange,src,time_src,dst,time_dst,line,travelt)
        elif src_indx>dst_indx:
            time_src=find_next_train_on_station(src,"Dwarka Sector - 21",t,"blue2")
            travelt=calc_traveltime(dst,src,"blue1")
            time_dst=time_src.Add_Time(Time.Min_To_Time(travelt))
            Output(interchange,src,time_src,dst,time_dst,line,travelt)
        else:
            print("Enter 2 different stations.")

    elif src in blueline2 and dst in magentaline:
        interchange=["Yes"]
        
        t_yamuna=calc_traveltime(src, "Laxmi Nagar", "blue2")+3
        time_src=find_next_train_on_station(src, "Laxmi Nagar", t, "blue2")
        arrival_yamuna=time_src.Add_Time(Time.Min_To_Time(t_yamuna))
        
        options=["Botanical Garden", "Janak Puri West"]
        lst=[]
        for i in options:
            d1=calc_traveltime("Yamuna bank", i, "blue1")
            d2=calc_traveltime(i, dst, "magenta")
            lst.append([i, d1+d2])

        if lst[0][1] < lst[1][1]:
            interchange_station=lst[0][0]
            t_blue1=calc_traveltime("Yamuna bank", interchange_station, "blue1")
            t_magenta=calc_traveltime(interchange_station, dst, "magenta")
        else:
            interchange_station=lst[1][0]
            t_blue1=calc_traveltime("Yamuna bank", interchange_station, "blue1")
            t_magenta=calc_traveltime(interchange_station, dst, "magenta")

        yb_idx=blueline1.index("Yamuna bank")
        int_idx=blueline1.index(interchange_station)
        
        if yb_idx < int_idx:
            dir_blue1="Dwarka Sector - 21"
        else:
            dir_blue1="Noida Electronic City"

        dept_yamuna=find_next_train_on_station("Yamuna bank", dir_blue1, arrival_yamuna.Add_Time(Time.Min_To_Time(5)), "blue1")
        arrival_interchange=dept_yamuna.Add_Time(Time.Min_To_Time(t_blue1))

        mag_start=magentaline.index(interchange_station)
        mag_end=magentaline.index(dst)
        
        if mag_start < mag_end:
            dir_mag="Janak Puri West"
        else:
            dir_mag="Botanical Garden"

        dept_interchange=find_next_train_on_station(interchange_station, dir_mag, arrival_interchange.Add_Time(Time.Min_To_Time(10)), "magenta")
        
        time_dst=dept_interchange.Add_Time(Time.Min_To_Time(t_magenta))
        total_time=t_yamuna+5+t_blue1+10+t_magenta

        interchange.append(interchange_station)
        interchange.append(arrival_interchange)
        interchange.append("Magenta")
        interchange.append(dept_interchange)

        Output(interchange, src, time_src, dst, time_dst, "Blue 2", total_time)

    elif src in magentaline and dst in blueline1:
        interchange=["Yes"]
        options=["Botanical Garden", "Janak Puri West"]
        lst=[]

        for i in options:
            d1=calc_traveltime(src, i, "magenta")
            d2=calc_traveltime(i, dst, "blue1")
            lst.append([i, d1+d2])

        if lst[0][1] < lst[1][1]:
            interchange_station=lst[0][0]
            t_magenta=calc_traveltime(src, interchange_station, "magenta")
            t_blue1=calc_traveltime(interchange_station, dst, "blue1")
        else:
            interchange_station=lst[1][0]
            t_magenta=calc_traveltime(src, interchange_station, "magenta")
            t_blue1=calc_traveltime(interchange_station, dst, "blue1")

        mag_src_idx=magentaline.index(src)
        mag_int_idx=magentaline.index(interchange_station)

        if mag_src_idx < mag_int_idx:
            dir_mag="Janak Puri West"
        else:
            dir_mag="Botanical Garden"

        time_src=find_next_train_on_station(src, dir_mag, t, "magenta")
        arrival_interchange=time_src.Add_Time(Time.Min_To_Time(t_magenta))

        blue_int_idx=blueline1.index(interchange_station)
        blue_dst_idx=blueline1.index(dst)

        if blue_int_idx < blue_dst_idx:
            dir_blue="Dwarka Sector - 21"
        else:
            dir_blue="Noida Electronic City"

        dept_interchange=find_next_train_on_station(interchange_station, dir_blue, arrival_interchange.Add_Time(Time.Min_To_Time(10)), "blue1")

        time_dst=dept_interchange.Add_Time(Time.Min_To_Time(t_blue1))
        total_time=t_magenta+10+t_blue1

        interchange.append(interchange_station)
        interchange.append(arrival_interchange)
        interchange.append("Blue 1")
        interchange.append(dept_interchange)

        Output(interchange, src, time_src, dst, time_dst, "Magenta", total_time)

    elif src in magentaline and dst in blueline2:
        interchange=["Yes"]
        options=["Botanical Garden", "Janak Puri West"]
        lst=[]
        for i in options:
            d1=calc_traveltime(src, i, "magenta")
            d2=calc_traveltime(i, "Yamuna bank", "blue1")
            lst.append([i, d1+d2])
        if lst[0][1] < lst[1][1]:
            interchange_station=lst[0][0]
            t_magenta=calc_traveltime(src, interchange_station, "magenta")
            t_blue1=calc_traveltime(interchange_station, "Yamuna bank", "blue1")
        else:
            interchange_station=lst[1][0]
            t_magenta=calc_traveltime(src, interchange_station, "magenta")
            t_blue1=calc_traveltime(interchange_station, "Yamuna bank", "blue1")
        mag_src_idx=magentaline.index(src)
        mag_int_idx=magentaline.index(interchange_station)
        if mag_src_idx < mag_int_idx:
            dir_mag="Janak Puri West"
        else:
            dir_mag="Botanical Garden"
        time_src=find_next_train_on_station(src, dir_mag, t, "magenta")
        arrival_interchange=time_src.Add_Time(Time.Min_To_Time(t_magenta))
        blue_int_idx=blueline1.index(interchange_station)
        blue_yb_idx=blueline1.index("Yamuna bank")
        if blue_int_idx < blue_yb_idx:
            dir_blue1="Dwarka Sector - 21"
        else:
            dir_blue1="Noida Electronic City"
        dept_interchange=find_next_train_on_station(interchange_station, dir_blue1, arrival_interchange.Add_Time(Time.Min_To_Time(10)), "blue1")
        arrival_yamuna=dept_interchange.Add_Time(Time.Min_To_Time(t_blue1))
        dept_laxmi=find_next_train_on_station("Laxmi Nagar", "Vaishali", arrival_yamuna, "blue2")
        t_blue2=calc_traveltime("Laxmi Nagar", dst, "blue2")
        time_dst=dept_laxmi.Add_Time(Time.Min_To_Time(t_blue2))
        total_time=t_magenta+10+t_blue1+8+t_blue2
        interchange.append(interchange_station)
        interchange.append(arrival_interchange)
        interchange.append("Blue 1 -> Blue 2")
        interchange.append(dept_interchange)
        Output(interchange, src, time_src, dst, time_dst, "Magenta", total_time)

    elif src in magentaline and dst in magentaline:
        interchange=["No"]
        travelt=calc_traveltime(src, dst, "magenta")
        src_idx=magentaline.index(src)
        dst_idx=magentaline.index(dst)
        if src_idx < dst_idx:
            direction="Janak Puri West"
        else:
            direction="Botanical Garden"
        time_src=find_next_train_on_station(src, direction, t, "magenta")
        time_dst=time_src.Add_Time(Time.Min_To_Time(travelt))
        Output(interchange, src, time_src, dst, time_dst, "Magenta", travelt)

def Menu():
    print("_____________________________________________________")
    print("1. Know Metro_Timing")
    print("2. Get Your Journey Planned")
    print("_____________________________________________________")
    user_inp=int(input("Choose your option : "))
    if user_inp==1:
        Metro_Timing()
    if user_inp==2:
        Journey_Planner()

while True:
    Menu()
    a=input("Do you want to proceed (y/n):")
    if a in "nN":
        break
    else:
        pass