
#  line, station, nextstation, traveltime(min), interchange point, fare
f=open("metro_data.txt","w")

blue_line_data = [
    "Blue, Dwarka Sector 21, Dwarka Sector 8, 3, No, 11\n",
    "Blue, Dwarka Sector 8, Dwarka Sector 9, 2, No, 11\n",
    "Blue, Dwarka Sector 9, Dwarka Sector 10, 2, No, 11\n",
    "Blue, Dwarka Sector 10, Dwarka Sector 11, 2, No, 11\n",
    "Blue, Dwarka Sector 11, Dwarka Sector 12, 2, No, 11\n",
    "Blue, Dwarka Sector 12, Dwarka Sector 13, 2, No, 11\n",
    "Blue, Dwarka Sector 13, Dwarka Sector 14, 2, No, 11\n",
    "Blue, Dwarka Sector 14, Dwarka, 2, No, 11\n",
    "Blue, Dwarka, Dwarka Mor, 2, No, 11\n",
    "Blue, Dwarka Mor, Nawada, 2, No, 11\n",
    "Blue, Nawada, Uttam Nagar West, 2, No, 11\n",
    "Blue, Uttam Nagar West, Uttam Nagar East, 2, No, 11\n",
    "Blue, Uttam Nagar East, Janakpuri West, 2, No, 11\n",
    "Blue, Janakpuri West, Janakpuri East, 2, Yes, 11\n",
    "Blue, Janakpuri East, Tilak Nagar, 2, No, 11\n",
    "Blue, Tilak Nagar, Subhash Nagar, 2, No, 11\n",
    "Blue, Subhash Nagar, Tagore Garden, 2, No, 11\n",
    "Blue, Tagore Garden, Rajouri Garden, 2, No, 11\n",
    "Blue, Rajouri Garden, Ramesh Nagar, 2, No, 11\n",
    "Blue, Ramesh Nagar, Moti Nagar, 2, No, 11\n",
    "Blue, Moti Nagar, Kirti Nagar, 2, No, 11\n",
    "Blue, Kirti Nagar, Shadipur, 2, No, 11\n",
    "Blue, Shadipur, Patel Nagar, 2, No, 11\n",
    "Blue, Patel Nagar, Rajendra Place, 2, No, 11\n",
    "Blue, Rajendra Place, Karol Bagh, 2, No, 11\n",
    "Blue, Karol Bagh, Jhandewalan, 2, No, 11\n",
    "Blue, Jhandewalan, Ramakrishna Ashram Marg, 2, No, 11\n",
    "Blue, Ramakrishna Ashram Marg, Rajiv Chowk, 2, No, 11\n",
    "Blue, Rajiv Chowk, Barakhamba Road, 2, No, 11\n",
    "Blue, Barakhamba Road, Mandi House, 2, No, 11\n",
    "Blue, Mandi House, Supreme Court, 2, No, 11\n",
    "Blue, Supreme Court, Indraprastha, 2, No, 11\n",
    "Blue, Indraprastha, Yamuna Bank, 3, No, 11\n",
    "Blue, Yamuna Bank, Akshardham, 3, No, 11\n",
    "Blue, Akshardham, Mayur Vihar - I, 3, No, 11\n",
    "Blue, Mayur Vihar - I, Mayur Vihar Extension, 2, No, 11\n",
    "Blue, Mayur Vihar Extension, New Ashok Nagar, 2, No, 11\n",
    "Blue, New Ashok Nagar, Noida Sector-15, 2, No, 11\n",
    "Blue, Noida Sector-15, Noida Sector-16, 2, No, 11\n",
    "Blue, Noida Sector-16, Noida Sector-18, 2, No, 11\n",
    "Blue, Noida Sector-18, Botanical Garden, 2, No, 11\n",
    "Blue, Botanical Garden, Golf Course, 3, Yes, 11\n",
    "Blue, Golf Course, Noida City Centre, 2, No, 11\n",
    "Blue, Noida City Centre, Sector - 34 Noida, 2, No, 11\n",
    "Blue, Sector - 34 Noida, Sector - 52 Noida, 2, No, 11\n",
    "Blue, Sector - 52 Noida, Sector - 61 Noida, 2, No, 11\n",
    "Blue, Sector - 61 Noida, Sector - 59 Noida, 2, No, 11\n",
    "Blue, Sector - 59 Noida, Sector - 62 Noida, 2, No, 11\n",
    "Blue, Sector - 62 Noida, Noida Electronic City, 2, No, 11\n",
    "Blue, Yamuna Bank, Laxmi Nagar, 3, No, 11\n",
    "Blue, Laxmi Nagar, Nirman Vihar, 3, No, 11\n",
    "Blue, Nirman Vihar, Preet Vihar, 2, No, 11\n",
    "Blue, Preet Vihar, Karkarduma, 2, No, 11\n",
    "Blue, Karkarduma, Anand Vihar ISBT, 2, No, 11\n",
    "Blue, Anand Vihar ISBT, Kaushambi, 2, No, 11\n",
    "Blue, Kaushambi, Vaishali, 2, No, 11\n"
]

magenta = [
    "Magenta, Krishna Park Extension, Janakpuri West, 12, Yes, 21\n",
    "Magenta, Janakpuri West, Dabri Mor – Janakpuri South, 5, No, 11\n",
    "Magenta, Dabri Mor – Janakpuri South, Dashrathpuri, 5, No, 11\n",
    "Magenta, Dashrathpuri, Palam, 2, No, 11\n",
    "Magenta, Palam, Sadar Bazar Cantonment, 4, No, 11\n",
    "Magenta, Sadar Bazar Cantonment, Terminal 1-IGI Airport, 3, No, 11\n",
    "Magenta, Terminal 1-IGI Airport, Shankar Vihar, 3, No, 11\n",
    "Magenta, Shankar Vihar, Vasant Vihar, 3, No, 11\n",
    "Magenta, Vasant Vihar, Munirka, 3, No, 11\n",
    "Magenta, Munirka, R.K.Puram, 2, No, 11\n",
    "Magenta, R.K.Puram, IIT, 2, No, 11\n",
    "Magenta, IIT, Hauz Khas, 2, No, 11\n",
    "Magenta, Hauz Khas, Panchsheel Park, 3, No, 11\n",
    "Magenta, Panchsheel Park, Chirag Delhi, 2, No, 11\n",
    "Magenta, Chirag Delhi, Greater Kailash, 2, No, 11\n",
    "Magenta, Greater Kailash, Nehru Enclave, 2, No, 11\n",
    "Magenta, Nehru Enclave, Kalkaji Mandir, 2, No, 11\n",
    "Magenta, Kalkaji Mandir, Okhla NSIC, 2, No, 11\n",
    "Magenta, Okhla NSIC, Sukhdev Vihar, 2, No, 11\n",
    "Magenta, Sukhdev Vihar, Jamia Millia Islamia, 2, No, 11\n",
    "Magenta, Jamia Millia Islamia, Okhla Vihar, 2, No, 11\n",
    "Magenta, Okhla Vihar, Jasola Vihar Shaheen Bagh, 5, No, 11\n",
    "Magenta, Jasola Vihar Shaheen Bagh, Kalindi Kunj, 5, No, 11\n",
    "Magenta, Kalindi Kunj, Okhla Bird Sanctuary, 2, No, 11\n",
    "Magenta, Okhla Bird Sanctuary, Botanical Garden, 3, No, 11\n"
]

f.writelines(blue_line_data)
f.writelines(magenta)
f.close()

import datetime

f=open("metro_data.txt",'r')
interchange_delay=3


start_time=datetime.time(6,0)
end_time=datetime.time(23,0)


line1 = ""
line2 = ""


source=input("Source: ")
destination=input("Destination: ")
time=input("Enter time (HH:MM): ")
hours,minutes=time.split(":")
hours=int(hours)
minutes=int(minutes)
h1=hours
m1=minutes
try:
    assert(hours>6)
    assert(hours<23)
except:
    print("No Service Available")
    exit()

f=open("metro_data.txt", "r")
working_data=[]
for i in f:
    c1=i.strip().split(", ")
    c1[3]=int(c1[3])
    c1[5]=int(c1[5])
    working_data.append(c1)
f.close()

reverse_data=[]
for i in working_data:
    line,start,end,t,int,f=i
    reverse_data.append([line,end,start,t,int,f])
working_data=working_data+reverse_data

def fare_calculator(source,destination):
    fare= 0
    found= False
    for i in working_data:
        if(i[1]==source and i[0]==line1):
            found = True
        if(found==True and i[0]==line1):
            fare += i[5]
        if(i[2]==destination and found and i[0]==line1):
            break
    return fare








#for calculating metro time at starting
def metro_timing(hours,minutes):
    time_min=hours*60+minutes
    start=6*60
    end=23*60
    if(time_min<start):
        print("No Service Available")
        return
    if(time_min>=end):
        print("No Service Available")
        return 
    if(8<=hours<10):
        frequecy=4
    elif(17<=hours<19):
        frequecy=4
    else:
        frequecy=8
    i=start
    while(i<=time_min):
        i+=frequecy
    next_metro_hour=i//60
    next_metro_minute=i%60
    print("Next metro at", next_metro_hour, ":", next_metro_minute)

metro_timing(hours,minutes)

#for calculating metro at interchange
def metro_timing_interchange():
    global hours , minutes, line2
    time_min=hours*60+minutes
    start=6*60
    end=23*60
    if(time_min<start):
        print("No Service Available")
        return
    if(time_min>=end):
        print("No Service Available")
        return 
    if(8<=hours<10):
        frequency=4
    elif(17<=hours<19):
        frequency=4
    else:
        frequency=8
    i=start
    while(i<=time_min):
        i+=frequency
    next_metro_hour=i//60
    next_metro_minute=i%60
    print("Next", line2, "metro departs at", next_metro_hour, ":", next_metro_minute)


def time_calculator1(source,destination,time):
    global hours, minutes, line1, line2
    is_interchange=False
    line1=""
    line2=""
    start_hours=hours
    start_minutes=minutes

    for i in working_data:
        if(i[1]==source):
            line1=i[0]
        if(i[1]==destination):
            line2=i[0]

    if(line1==line2):
        total_time=0
        found=False
        for i in working_data:
            if(i[0]!=line1):
                continue
            if(i[1]==source):
                found=True
            if found:
                total_time+=i[3]
            if(i[2]==destination and found):
                break
        #for reverse if we have the station is not found in forward direction
        if(found==False or i[2]!=destination):
            total_time=0
            found=False
            for i in range(len(working_data)-1,-1,-1):
                rev=working_data[i]
                if(rev[0]!=line1):
                    continue
                if(rev[1]==source):
                    found=True
                if(found):
                    total_time+=rev[3]
                if(rev[2]==destination and found):
                    break
        # arrival time
        final_minutes = start_minutes + total_time
        final_hours = start_hours + (final_minutes//60)
        final_minutes = final_minutes%60

        print("Journey Plan:")
        print("Start at", source, "(", line1, "Line )")
        print("Arrive at", destination, "at", final_hours, ":", final_minutes)
        print("Total travel time:", total_time, "minutes")
        f= fare_calculator(source, destination)
        print("Total Fare:", f)
        return
    else:
        is_interchange=True
        shortest_time=[]
        interchange_station=["Janakpuri West","Botanical Garden"]
        for z in interchange_station:
            found1=False
            time1=0
            for j in working_data:
                if(j[0]!=line1):
                    continue
                if(j[1]==source):
                    found1=True
                if(found1):
                    time1+=j[3]
                if(j[2]==z and found1):
                    break
            #for reverse
            if(found1==False or j[2]!=z):
                found1=False
                time1=0
                for i in range(len(working_data)-1,-1,-1):
                    rev1=working_data[i]
                    if(rev1[0]!=line1):
                        continue
                    if(rev1[1]==source):
                        found1=True
                    if(found1):
                        time1+=rev1[3]
                    if(rev1[2]==z and found1):
                        break
            found2=False
            time2=0
            for j in working_data:
                if(j[0]!=line2):
                    continue
                if(j[1]==z):
                    found2=True
                if(found2):
                    time2+=j[3]
                if(j[2]==destination and found2):
                    break
            if(found2==False or j[2]!=destination):
                time2=0
                found2=False
                for i in range(len(working_data)-1,-1,-1):
                    rev3=working_data[i]
                    if(rev3[0]!=line2):
                        continue
                    if(rev3[1]==z):
                        found2=True
                    if(found2):
                        time2+=rev3[3]
                    if(rev3[2]==destination and found2):
                        break

            total=time1+time2+interchange_delay
            shortest_time.append([total,time1,time2,z])

        if(shortest_time[0][0]<shortest_time[1][0]):
            total_time = shortest_time[0][0]
            best = shortest_time[0][1]
            best_interchanging_station = shortest_time[0][3]
        else:
            total_time = shortest_time[1][0]
            best = shortest_time[1][1]
            best_interchanging_station = shortest_time[1][3]

        arrival_minute = start_minutes + best
        arrival_hours = start_hours + (arrival_minute//60)
        arrival_minute = arrival_minute%60

        final_minute = start_minutes + total_time
        final_hours = start_hours + (final_minute//60)
        final_minute = final_minute%60

        print("")
        print("Journey Plan:")
        print("Start at", source, "(", line1, "Line )")
        print("Arrive at", best_interchanging_station, "at", arrival_hours, ":", arrival_minute)
        print("Transfer to", line2, "Line")

        hours = arrival_hours
        minutes = arrival_minute
        metro_timing_interchange()

        print("Arrive at", destination, "at", final_hours, ":", final_minute)
        print("Total travel time:", total_time, "minutes")
        f1 = fare_calculator(source, z)
        f2= fare_calculator(z, destination)
        print("Total Fare:", f1 + f2)


time_calculator1(source,destination,time)
