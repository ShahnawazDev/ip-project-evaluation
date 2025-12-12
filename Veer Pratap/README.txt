# Delhi Metro Route Planner

This is a python program planned to calculate total time, intersection, timing of next metro, lines connection and daily schedule.

1) Features

Handles journeys across Magenta Line, Blue1, and Blue2
Real-time Schedule Calculation
Automatically selects the best interchange points
Different metro frequencies during rush hours (4 min) vs normal hours (8 min)
Includes Interchange Timing, helps in finding the timing for next train
Ensures metro service is available or not at a given time (6:00 AM - 11:00 PM)

2) Metro Lines and Stations

Magenta Line
Blue Line 1  
Blue Line 2

3) Metro Frequency Schedule

Peak Hours: 8:00-10:00 AM & 5:00-7:00 PM → 4 minutes frequency
Normal Hours: All other operational times → 8 minutes frequency
Service Hours: 6:00 AM to 11:00 PM


4) Main interchange Stations

Janakpuri West: Connects Magenta Line and Blue Line 1 (10 min interchange)
Botanical Garden: Connects Magenta Line and Blue Line 1 (5 min interchange)  
Yamuna Bank: Connects Blue Line 1 and Blue Line 2 (5 min interchange)

##Assumption we take that there is a 5 minute inter change at Yamuna bank every time when we go to blue line 2 from any line or vice versa.


5) File Requirements

"metro_data.txt": Contains station data in format:

#Source of data
 a. https://delhimetrorail.com/map
 b. https://web.iitd.ac.in/~tobiastoll/Metro.pdf

6) How to Use

a. Run the program and provide the required inputs:
   Enter Current Station: [Your starting station]
   Enter Final Station: [Your destination station]
   Current time(24 hour format): [HH:MM]

b. Output will be:
   Starting station and line
   Next 3 metro departure times from starting station
   Route details including interchanges
   Arrival times at each interchange
   Walking time for interchanges
   Final arrival time and total travel duration

7) Core Functions used:
Frequency(minutes):helps us to give the frequency
Next metro time: determines the next metro time
Hourconverter(minutes): helps us to convert the minutes into the hour form


8) Data Structure

"lines": Dictionary storing stations for each line
"time": Dictionary storing travel times between stations
Data taken from `metro_data.txt` file

9) Error Handling

Invalid time format validation
Station existence verification  
Metro service availability check
Time boundary validation (0-59 minutes, 6:00-23:00 service)

10) Limitations

Fixed interchange walking times
Assumes consistent travel times
No real-time delay considerations
Limited to the three specified metro lines

“The system helps you figure out the best way to travel on the Delhi Metro and tells you how long your journey will take.”
