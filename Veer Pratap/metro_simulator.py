current_station = input("Enter Current Station:").strip()
final_station = input("Enter Final Station:").strip()
current_time = input("Current time(24 hour format):").split(":")

current_hour = int(current_time[0])
current_minute = int(current_time[1])
current_total_minutes = current_hour * 60 + current_minute

if current_minute < 0 or current_minute > 59:
    print("time error!!!")

else:
    if current_total_minutes < 6*60 or current_total_minutes > 23*60:
        print("Metro service is not available at this time!!!")

    else:    
        def frequency(minutes):
            if (8*60 <= minutes < 10*60) or (17*60 <= minutes < 19*60):
                return 4  #4 minutes during peak hours
            else:
                return 8  #8 minutes during normal hours
            
        """3) Metro Frequency Schedule

	Peak Hours: 8:00-10:00 AM & 5:00-7:00 PM → 4 minutes frequency
	Normal Hours: All other operational times → 8 minutes frequency
	Service Hours: 6:00 AM to 11:00 PM
"""
        def next_metro_timing(current_min, freq):
            remainder = current_min % freq
            if remainder == 0:
                return current_min
            else:
                return current_min + (freq - remainder) 
                
        def hourconverter(minutes):
            hours = minutes // 60
            mins = minutes % 60
            return f"{hours}:{mins:02d}"   

        freq = frequency(current_total_minutes)
        next_metro_time = next_metro_timing(current_total_minutes, freq)

        f=open("C:/Users/Veer Pratap/OneDrive/Documents/metro_data.txt", mode='r')
        file_lines = f.readlines()

        lines={"magenta":[],"blue1":[],"blue2":[]}    #arranging stations line wise
        time={"t_magenta":[],"t_blue1":[],"t_blue2":[]}  #arranging time line wise
        for line in file_lines:
            line = line.strip()
            parts = line.split(',')

            if len(parts) > 1 and parts[0]== "magenta":  
                lines["magenta"].append(parts[1])
                time["t_magenta"].append(int(parts[3]))
            if len(parts) > 1 and parts[0]== "blue1":  
                lines["blue1"].append(parts[1])
                time["t_blue1"].append(int(parts[3]))
            if len(parts) > 1 and parts[0]== "blue2":  
                lines["blue2"].append(parts[1])
                time["t_blue2"].append(int(parts[3])) 

        stations = lines["magenta"] + lines["blue1"] + lines["blue2"]

        if current_station not in stations:
            print(F"{current_station} station does not exist in this line!!!")
        if final_station not in stations:
            print(F"{final_station} station does not exist in this line!!!")    

        traveltime=0

        #if we start from magenta line
        if current_station in lines["magenta"]:
            line_i="magenta"
            print(f"Start at {current_station} ({line_i} line)")
            print(f"Next metro at {hourconverter(next_metro_time)}") 
            for i in range(1,3):
                metro_time = next_metro_time + (i * freq)
                print(f"Next to next metro {i}: {hourconverter(metro_time)}")

            if final_station in lines["magenta"]:#from magenta to magenta
                line_f="magenta"
                start_index = lines["magenta"].index(current_station)
                end_index = lines["magenta"].index(final_station)

                start = min(start_index, end_index)
                end = max(start_index, end_index)

                time_intervals = time["t_magenta"][start : end]
                traveltime = sum(time_intervals)

                interchange = "no"      
            elif final_station in lines["blue1"]:#from magenta to blue1
                line_f="blue1"
                interchange1= "janakpuri west"
                interchange2= "botanical garden"
                start_index = lines["magenta"].index(current_station)
                inter_index = lines["magenta"].index("janakpuri west")
                inter_index2 = lines["magenta"].index("botanical garden")
                start_1= min(start_index, inter_index)
                end_1 = max(start_index, inter_index)
                start_2= min(start_index, inter_index2)
                end_2 = max(start_index, inter_index2)
                magenta_time1 = sum(time["t_magenta"][start_1: end_1])
                magenta_time2 = sum(time["t_magenta"][start_2: end_2])
                inter_1_index = lines["blue1"].index("janakpuri west")
                final_1_index = lines["blue1"].index(final_station)
                inter_2_index = lines["blue1"].index("botanical garden")
                final_2_index = lines["blue1"].index(final_station)
                blue1_time1 = sum(time["t_blue1"][min(inter_1_index, final_1_index): max(inter_1_index, final_1_index)])
                blue1_time2 = sum(time["t_blue1"][min(inter_2_index, final_2_index): max(inter_2_index, final_2_index)])
                total_time1 = magenta_time1 + blue1_time1+ 10  # extra 10 min for interchange
                total_time2 = magenta_time2 + blue1_time2 + 5  # extra 5 min for interchange
                if total_time1 <= total_time2:
                    traveltime = total_time1
                    interchange = "janakpuri west"
                    arrival_at_interchange = next_metro_time + magenta_time1
                    print(f"Arrive at {interchange} at {hourconverter(arrival_at_interchange)}")
                    print(f"Interchange walking time: 10 minutes")
                    print(f"Transfer to {line_f} line")
                    inter_freq = frequency(arrival_at_interchange + 10)
                    next_inter_metro = next_metro_timing(arrival_at_interchange + 10, inter_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_inter_metro)}")
                else:
                    traveltime = total_time2
                    interchange = "botanical garden"
                    arrival_at_interchange = next_metro_time + magenta_time2
                    print(f"Arrive at {interchange} at {hourconverter(arrival_at_interchange)}")
                    print(f"Interchange walking time: 5 minutes")
                    print(f"Transfer to {line_f} line")
                    inter_freq = frequency(arrival_at_interchange + 5)
                    next_inter_metro = next_metro_timing(arrival_at_interchange + 5, inter_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_inter_metro)}")
                

            elif final_station in lines["blue2"]:#from magenta to blue2
                line_f="blue2"
                interchange_1 = "yamuna bank"
                interchange_2 = "janakpuri west"
                interchange_3 = "botanical garden"
                start_index = lines["magenta"].index(current_station)
                inter_index1 = lines["magenta"].index("janakpuri west") 
                inter_index2 = lines["magenta"].index("botanical garden")
                start_1= min(start_index, inter_index1)
                end_1 = max(start_index, inter_index1)
                magenta_time1 = sum(time["t_magenta"][start_1: end_1])
                start_2= min(start_index, inter_index2)
                end_2 = max(start_index, inter_index2)
                magenta_time2 = sum(time["t_magenta"][start_2: end_2])
                inter_1_index = lines["blue1"].index("janakpuri west")
                inter_2_index = lines["blue1"].index("botanical garden")
                inter_3_index = lines["blue1"].index("yamuna bank")
                start_3=min(inter_1_index, inter_3_index)
                end_3=max(inter_1_index, inter_3_index)
                blue1_time1 = sum(time["t_blue1"][start_3: end_3])
                start_4=min(inter_2_index, inter_3_index)
                end_4=max(inter_2_index, inter_3_index)
                blue1_time2 = sum(time["t_blue1"][start_4: end_4])
                inter_2_index = lines["blue2"].index("yamuna bank")
                final_2_index = lines["blue2"].index(final_station)
                blue2_time = sum(time["t_blue2"][min(inter_2_index, final_2_index): max(inter_2_index, final_2_index)])
                total_time1 = magenta_time1 + blue1_time1 + blue2_time + 10 +5# extra 15min for interchanges
                total_time2 = magenta_time2 + blue1_time2 + blue2_time  +5 +5   # extra 10 min for interchange
                if total_time1 <= total_time2:
                    traveltime = total_time1
                    interchange = interchange_2
                    first_interchange_time = next_metro_time + magenta_time1
                    print(f"Arrive at {interchange_2} at {hourconverter(first_interchange_time)}")
                    print(f"Interchange walking time: 10 minutes")
                    print("Transfer to blue1 line")
                    blue1_freq = frequency(first_interchange_time + 10)
                    next_blue1 = next_metro_timing(first_interchange_time + 10, blue1_freq)
                    print(f"Next blue1 metro departs at {hourconverter(next_blue1)}")
                    second_interchange_time = next_blue1 + blue1_time1
                    print(f"Arrive at {interchange_1} at {hourconverter(second_interchange_time)}")
                    print(f"Interchange walking time: 5 minutes")
                    print(f"Transfer to {line_f} line")
                    blue2_freq = frequency(second_interchange_time + 5)
                    next_blue2 = next_metro_timing(second_interchange_time + 5, blue2_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_blue2)}")
                else:
                    traveltime = total_time2
                    interchange = interchange_3
                    first_interchange_time = next_metro_time + magenta_time2
                    print(f"Arrive at {interchange_3} at {hourconverter(first_interchange_time)}")
                    print(f"Interchange walking time: 5 minutes")
                    print("Transfer to blue1 line")
                    blue1_freq = frequency(first_interchange_time + 5)
                    next_blue1 = next_metro_timing(first_interchange_time + 5, blue1_freq)
                    print(f"Next blue1 metro departs at {hourconverter(next_blue1)}")
                    second_interchange_time = next_blue1 + blue1_time2
                    print(f"Arrive at {interchange_1} at {hourconverter(second_interchange_time)}")
                    print(f"Interchange walking time: 5 minutes")
                    print(f"Transfer to {line_f} line")
                    blue2_freq = frequency(second_interchange_time + 5)
                    next_blue2 = next_metro_timing(second_interchange_time + 5, blue2_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_blue2)}")
                    
        elif current_station in lines["blue1"]:#from blue1 line
            line_i="blue1"
            print(f"Start at {current_station} ({line_i} line)")
            print(f"Next metro at {hourconverter(next_metro_time)}") 
            for i in range(1,3):
                metro_time = next_metro_time + (i * freq)
                print(f"Next to next metro {i}: {hourconverter(metro_time)}")

            if final_station in lines["blue1"]:#from blue1 to blue1
                line_f="blue1"
                start_index = lines["blue1"].index(current_station)
                end_index = lines["blue1"].index(final_station)

                start = min(start_index, end_index)
                end = max(start_index, end_index)

                time_intervals = time["t_blue1"][start : end]
                traveltime = sum(time_intervals)
                interchange = "no"
            elif final_station in lines["magenta"]:#from blue1 to magenta
                line_f="magenta"
                start_index = lines["blue1"].index(current_station)
                inter_index = lines["blue1"].index("janakpuri west")
                inter_index2 = lines["blue1"].index("botanical garden")
                start_1= min(start_index, inter_index)
                end_1 = max(start_index, inter_index)
                start_2= min(start_index, inter_index2)
                end_2 = max(start_index, inter_index2)
                blue1_time1 = sum(time["t_blue1"][start_1: end_1])
                blue1_time2 = sum(time["t_blue1"][start_2: end_2])
                inter_1_index = lines["magenta"].index("janakpuri west")
                final_1_index = lines["magenta"].index(final_station)
                inter_2_index = lines["magenta"].index("botanical garden")
                final_2_index = lines["magenta"].index(final_station)
                magenta_time1 = sum(time["t_magenta"][min(inter_1_index, final_1_index): max(inter_1_index, final_1_index)])
                magenta_time2 = sum(time["t_magenta"][min(inter_2_index, final_2_index): max(inter_2_index, final_2_index)])
                total_time1 = blue1_time1 + magenta_time1 + 10  # extra 10 min for interchange
                total_time2 = blue1_time2 + magenta_time2 + 5  # extra 5 min for interchange
                if total_time1 <= total_time2:
                    traveltime = total_time1
                    interchange = "janakpuri west"
                    arrival_at_interchange = next_metro_time + blue1_time1
                    print(f"Arrive at janakpuri west at {hourconverter(arrival_at_interchange)}")
                    print(f"Interchange walking time: 10 minutes")
                    magenta_freq = frequency(arrival_at_interchange + 10)
                    next_magenta = next_metro_timing(arrival_at_interchange + 10, magenta_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_magenta)}")
                    print(f"Transfer to {line_f} line")
                else:
                    traveltime = total_time2
                    interchange = "botanical garden"
                    arrival_at_interchange = next_metro_time + blue1_time2
                    print(f"Arrive at botanical garden at {hourconverter(arrival_at_interchange)}")
                    print(f"Interchange walking time: 5 minutes")
                    magenta_freq = frequency(arrival_at_interchange + 5)
                    next_magenta = next_metro_timing(arrival_at_interchange + 5, magenta_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_magenta)}")
                    print(f"Transfer to {line_f} line")    
            elif final_station in lines["blue2"]:#from blue1 to blue2
                line_f="blue2"
                interchange = "yamuna bank"
                start_index = lines["blue1"].index(current_station)
                inter_index = lines["blue1"].index("yamuna bank")
                start_1= min(start_index, inter_index)
                end_1 = max(start_index, inter_index)
                blue1_time = sum(time["t_blue1"][start_1: end_1])
                inter_2_index = lines["blue2"].index("yamuna bank")
                final_2_index = lines["blue2"].index(final_station)
                blue2_time = sum(time["t_blue2"][min(inter_2_index, final_2_index): max(inter_2_index, final_2_index)])
                traveltime = blue1_time + blue2_time +5
                arrival_at_interchange = next_metro_time + blue1_time
                print(f"Arrive at {interchange} at {hourconverter(arrival_at_interchange)}")
                print(f"Interchange walking time: 5 minutes")
                blue2_freq = frequency(arrival_at_interchange + 5)
                next_blue2 = next_metro_timing(arrival_at_interchange + 5, blue2_freq)
                print(f"Next {line_f} metro departs at {hourconverter(next_blue2)}")
                print(f"Transfer to {line_f} line")
                
        elif current_station in lines["blue2"]:#from blue2 line
            line_i="blue2"
            print(f"Start at {current_station} ({line_i} line)")
            print(f"Next metro at {hourconverter(next_metro_time)}") 
            for i in range(1,3):
                metro_time = next_metro_time + (i * freq)
                print(f"Next to next metro {i}: {hourconverter(metro_time)}")            

            if final_station in lines["blue2"]:#from blue2 to blue2
                line_f="blue2"
                start_index = lines["blue2"].index(current_station)
                end_index = lines["blue2"].index(final_station)

                start = min(start_index, end_index)
                end = max(start_index, end_index)

                time_intervals = time["t_blue2"][start : end]
                traveltime = sum(time_intervals)
                interchange = "no"
            elif final_station in lines["blue1"]:#from blue2 to blue1
                line_f="blue1"
                interchange = "yamuna bank"
                start_index = lines["blue2"].index(current_station)
                inter_index = lines["blue2"].index("yamuna bank")
                start_1= min(start_index, inter_index)
                end_1 = max(start_index, inter_index)
                blue2_time = sum(time["t_blue2"][start_1: end_1])
                inter_2_index = lines["blue1"].index("yamuna bank")
                final_2_index = lines["blue1"].index(final_station)
                blue1_time = sum(time["t_blue1"][min(inter_2_index, final_2_index): max(inter_2_index, final_2_index)])
                traveltime = blue2_time + blue1_time +5
                arrival_at_interchange = next_metro_time + blue2_time
                print(f"Arrive at {interchange} at {hourconverter(arrival_at_interchange)}")
                print(f"Interchange walking time: 5 minutes")
                blue1_freq = frequency(arrival_at_interchange + 5)
                next_blue1 = next_metro_timing(arrival_at_interchange + 5, blue1_freq)
                print(f"Next {line_f} metro departs at {hourconverter(next_blue1)}")
                print(f"Transfer to {line_f} line")
            elif final_station in lines["magenta"]:#from blue2 to magenta
                line_f="magenta"
                interchange_1 = "yamuna bank"
                interchange_2 = "janakpuri west"
                interchange_3 = "botanical garden"
                start_index = lines["blue2"].index(current_station)
                inter_index = lines["blue2"].index("yamuna bank")
                inter_index1 = lines["blue1"].index("yamuna bank")
                inter_index2 = lines["blue1"].index("janakpuri west")
                inter_index3 = lines["blue1"].index("botanical garden")
                start_1= min(start_index, inter_index)
                end_1 = max(start_index, inter_index)
                blue2_time = sum(time["t_blue2"][start_1: end_1])
                start_2=min(inter_index1, inter_index2)
                end_2=max(inter_index1, inter_index2)
                blue1_time1 = sum(time["t_blue1"][start_2: end_2])  
                start_3=min(inter_index1, inter_index3)
                end_3=max(inter_index1, inter_index3)
                blue1_time2 = sum(time["t_blue1"][start_3: end_3])
                inter_1_index = lines["magenta"].index("janakpuri west")
                final_1_index = lines["magenta"].index(final_station)
                inter_2_index = lines["magenta"].index("botanical garden")
                final_2_index = lines["magenta"].index(final_station)
                magenta_time1 = sum(time["t_magenta"][min(inter_1_index, final_1_index): max(inter_1_index, final_1_index)])
                magenta_time2 = sum(time["t_magenta"][min(inter_2_index, final_2_index): max(inter_2_index, final_2_index)])    
                total_time1 = blue2_time + blue1_time1 + magenta_time1 + 10+5
                total_time2 = blue2_time + blue1_time2 + magenta_time2 + 5+5
                if total_time1 <= total_time2:
                    traveltime = total_time1
                    interchange = interchange_2
                    first_interchange_time = next_metro_time + blue2_time
                    print(f"Arrive at {interchange_1} at {hourconverter(first_interchange_time)}")
                    print(f"Interchange walking time: 5 minutes")
                    print("Transfer to blue1 line")
                    blue1_freq = frequency(first_interchange_time + 5)
                    next_blue1 = next_metro_timing(first_interchange_time + 5, blue1_freq)
                    print(f"Next blue1 metro departs at {hourconverter(next_blue1)}")
                    second_interchange_time = next_blue1 + blue1_time1     
                    print(f"Arrive at {interchange_2} at {hourconverter(second_interchange_time)}")
                    print(f"Interchange walking time: 10 minutes")
                    print(f"Transfer to {line_f} line")
                    magenta_freq = frequency(second_interchange_time + 10)
                    next_magenta = next_metro_timing(second_interchange_time + 10, magenta_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_magenta)}")
                    
                else:
                    traveltime = total_time2
                    interchange = interchange_3
                    first_interchange_time = next_metro_time + blue2_time
                    print(f"Arrive at {interchange_1} at {hourconverter(first_interchange_time)}")
                    print(f"Interchange walking time: 5 minutes")
                    print("Transfer to blue1 line")
                    blue1_freq = frequency(first_interchange_time + 5)
                    next_blue1 = next_metro_timing(first_interchange_time + 5, blue1_freq)
                    print(f"Next blue1 metro departs at {hourconverter(next_blue1)}")
                    second_interchange_time = next_blue1 + blue1_time2
                    print(f"Arrive at {interchange_3} at {hourconverter(second_interchange_time)}")
                    print(f"Interchange walking time: 5 minutes")
                    print(f"Transfer to {line_f} line")
                    magenta_freq = frequency(second_interchange_time + 5)
                    next_magenta = next_metro_timing(second_interchange_time + 5, magenta_freq)
                    print(f"Next {line_f} metro departs at {hourconverter(next_magenta)}")  
                    """Route Calculation Logic

Same Line Travel : we calculate the direct route
Single Interchange: by adding the walking time to the overall time 
Double Interchange: For multiple changing routes across all three lines
Time-based Scheduling: Real-time metro schedule consideration
"""
                    
        final_arrival_time = next_metro_time + traveltime
        print(f"Arrive at {final_station} at {hourconverter(final_arrival_time)}")          
        print(f"Total travel time: {traveltime} minutes")