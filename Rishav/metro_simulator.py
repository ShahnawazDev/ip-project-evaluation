# FIRST PART = TIME FOR NEXT TRAIN
# SEC PART IS BELOW THE FIRST PART PLS CHECK THAT ALSO
def time_min(t):
    h,m= map(int,t.split(":"))
    h=h*60
    t=h+m
    return t


def min_time(x):
    h=x//60
    m=x%60
    if h < 10:
        h="0" + str(h)
    else:
        h=str(h)
    if m < 10:
        m="0" + str(m)
    else:
        m=str(m)
    return h+":"+m


line_colour = input()
current_station=input()
current_time=input()
current_time=time_min(current_time)


if(360 < current_time <1380):    
    def reach_time(current_station):
        total_time=0  # time to reach current station from souce
        f=open('metro_data.txt','r') 
        line=f.readlines()
        for k in line:
            k=k.strip().split(",")
            sn=k[1].strip() #sn=station name
            trs=int(k[3])  # trs=time to reach next station
            if(current_station.lower()==sn.lower()):
               return total_time
            else:
               total_time+=trs
        
    
    reachtime=int(reach_time(current_station))

    start_time=360
    count=0
    while start_time <= 1380 :
        arrive_time=reachtime + start_time

        if arrive_time >= current_time :
            if count==0:
                print(f"Next metro at {min_time(arrive_time)}")
            elif count==1:
                print(f"Subsequent metro at {min_time(arrive_time)}", end=(""))
            else:
                print(f",{min_time(arrive_time)}", end="")
            count += 1 
            if count==3:
                break
        if (480 <= start_time <= 600) or (1020 <= start_time <= 1140):
            start_time  += 4
        else:
            start_time  += 8  

else:
    print("Service Unavilable")



# SECOND PART = RIDE PLANNER PART
   
# AND THIS PART IS INCOMPLETE BUT ABOVE PART A IS COMPLETED AND GIVING CORRECT OUTPUT
# I have done second part seperatly mean I define every and each function and variable new 
# So pls run both codes seperatly 


# def time_min(t):
#     h,m= map(int,t.split(":"))
#     h=h*60
#     t=h+m
#     return t


# def min_time(x):
#     h=x//60
#     m=x%60
#     if h < 10:
#         h="0" + str(h)
#     else:
#         h=str(h)
#     if m < 10:
#         m="0" + str(m)
#     else:
#         m=str(m)
#     return h+":"+m

# current_station=input("source :")
# destiny_station=input("Destination :")
# current_time=input()
# current_time=time_min(current_time)

# def reach_time2(current_station , colour):
#     f=open('metro_data.txt','r') 
#     line=f.readlines()
#     total_time=0  # time to reach current station from souce
#     for k in line:
#         k=k.strip().split(",")
#         ln = k[0].strip() # ln=line name
#         sn =k[1].strip()  # sn=station name
#         trs=int(k[3])     # trs=time to reach next station
#         if (ln==colour.strip()):
#             if (sn==current_station):
#                 return int(total_time)
#         total_time += trs
#     return None

# def nexttrain_time(total_time,current_time):
#     start_time=360
#     while start_time <= 1380 :
#         arrive_time=total_time + start_time
#         if arrive_time >= current_time :
#             return arrive_time
#         if (480 <= start_time <= 600) or (1020 <= start_time <= 1140):
#             start_time  += 4
#         else:
#             start_time  += 8

# ccoblue=reach_time2(current_station,"Blue") # check currentstation on blue
# cdoblue=reach_time2(destiny_station,"Blue") # check destinystation on blue
 
# if((ccoblue!= None) and (cdoblue!= None)):
#     arrival_time=nexttrain_time(ccoblue,current_time)
#     bw_time=abs(cdoblue-ccoblue)
#     reachtime2=arrival_time + bw_time
#     print("\n" +" Direct (Blue Line)")
#     print("Next Metro at :"+ min_time(arrival_time))
#     print("Reach Destination at :" + min_time(reachtime2))

# ccomag=reach_time2(current_station,"Magenta") # check destinystation on blue
# cdomag=reach_time2(destiny_station,"Magenta") # check destinystation on blue

# if((ccomag!= None) and (cdomag!= None)):
#     arrival_time=nexttrain_time(ccomag,current_time)
#     bw_time=abs(cdomag-ccomag)
#     reachtime2=arrival_time + bw_time
#     print("\n" +" Direct (Magenta Line)")
#     print("Next Metro at :"+ min_time(arrival_time))
#     print("Reach Destination at :" + min_time(reachtime2))  





    
    



    


