# Delhi Metro Simulator
Delhi Metro Journey Planner
The main this is csv files created with help of dmrc website source
Welcome to the Delhi Metro Journey Planner. This simple yet powerful Python tool helps commuters navigate the Delhi Metro network. It calculates the most efficient route between two stations, estimates travel time, and accounts for line changes—just like a real-world navigation app.
I have fetched the data from the official DMRC webstie
where this interactive map is there 
which shows all the timings between two station and wherever the interchnage is
i have created a text file and a python file for logic /n
basically i have created a list to add times 
to check if interchanging is happeing

This program takes the guesswork out of your commute. Instead of staring at a map, you simply input your location and time, and the planner handles the rest.

Key Features:

Route Calculation: Automatically detects if your journey is on a single line or requires an interchange.

"forward" or "reverse" on the line to reach your destination reverse list is made so that we can go backward too

Time Estimation: Calculates arrival times based on actual travel duration between stations.

Peak Hour Logic: Adjusts the "Next Metro" waiting time based on the time of day (shorter waits during rush hour, longer waits off-peak).

Interchange Management: Identifies the exact station where you need to switch lines and calculates the transfer time.

Behind the scenes, the script reads real metro data from a text file. 

It loads station connections, travel times, and line information.

It checks if a direct train exists. If not, it searches for a common interchange station between your starting line and your destination line.

It takes your current time, determines the gap between trains (4 minutes during peak hours, 8 minutes otherwise), and projects your arrival time at every key stop.
Initially, a dictionary was attempted, but:
Reversing direction became difficult
Traversing forward/backward station-by-station was confusing
List-of-lists gave a clean, readable, and simple structure
