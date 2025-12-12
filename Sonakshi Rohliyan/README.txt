DATA SOURCE - All the data, including station names and timings between two consecutive stations, is sourced from the official DMRC website.

Lines included- Blue, Blue extension, Magenta, Airport express, Green, Gray.

Line naming convention-
1) Blue line (main branch/ to noida) = blue 
2) Blue line (extension/ to Vaishali) = blue2 
3) Magenta line = magenta 
4) Airport Express line = airport 
5) Gray line = gray 
6) Green line = green 

ASSUMPTIONS- The interchange at Janakpuri West, Yamuna Bank, Kirti Nagar, Dwarka Sector 21 and botanical garden takes 2 minutes. And assumed that the metro stops at each station for 0.5 minute.

REQUIREMENTS- Python 3.13.5 should be installed. metro_simulator.py and metro_data.txt should be in the same folder and file directly.

INSTRUCTION TO RUN THE PROGRAM-

-To run the file type "python3 metro_simulator.py" in the terminal after making sure metro_simulator.py and metro_data.txt are in the same file directory.

If the program is run successfully, you should see
"Welcome to Delhi Metro Route and Schedule Simulator
Would you like to user Metro Timings Module or Ride journey planner"

Input whether you want to Metro Timings Module or Ride journey planner.

IF you want to use Metro Timings Module- 
1) input the line you want to travel in, the station in the line whose metro timing you want to know and the current time. MAKE sure there are no typos and the names of the station start with a capital letter.(eg-Noida Electronic City, Uttam Nagar East) The format of the station name should be as given on the DMRC website (eg-Terminal 1 - IGI Airport, Sector - 34 Noida, Airport (T-3), Brig. Hoshiar Singh). 
2) input the time in correct format (HH:MM) in 24 hour clock. for eg- 6:23am is incorrect, but 06:00 is correct. 03:35 pm is incorrect but 15:35 is correct.

IF you want to use Ride journey planner.
1) Input the source (Starting station) in correct spelling and format.
2) Input the destination (final station) in correct spelling and format.
3) The time you start travelling, in correct format.


HOW THE PROGRAM WORKS-


1) Reading Metro Data- The code reads metro_data.txt and stores station names and travel times in different lists for each metro line. 

It also builds a combined nested list stations which contains a list for each station that contains its name, the line, and the time it takes to get to the next station


2) metro_sim(line, station, current_time)- This function returns next metro arrival time at the given station and the subsequent 5 arrival times

It calculates based on fixed starting time, 6:00 AM from line endpoints.

An empty list is made that stores value of every arrival time of the metro. The frequency is changed based on timing.

6–8 AM - every 8 minutes
8–10 AM - every 4 minutes
10–5 PM - every 8 minutes
5–7 PM - every 4 minutes
7–11 PM - every 8 minutes

3) plan() — Journey Planner- This function takes start station, destination, and start time and checks if both stations exist, and returns an error message if it doesn't.

It first finds out if the travel is on the same line, and finds the time taken as the sum of time taken to go through consecutive stations while pausing at each station for half a minute. 

If the travel is not on the same line, it checks whether it requires one transfer or Two transfers (via Blue Line). It is done using finding out if one station name occurs in our full list 'stations' more than once. Then that station would be an interchange point. 
In the program, To get from any line to blue line, you need only one transfer, and to get from any line to any other line you need two transfer.
hence two functions are defined transfer() and two_transfer()

Based on that, it calculates and prints- 

Starting station and line
When the next metro arrives.
When you reach the first transfer station (if any)
Transfer to which line (if any)
When the next metro arrives.
When you reach the second transfer station (if any)
Transfer to which line (if any)
Final station, and arrival time
Total travel time

4) user_input()- This function gives you an option to input What you want the code to do.


