Delhi Metro Route and Schedule 

Course: CSE101 Assignment

1. Project Overview

This Python program simulates the Delhi Metro network, with a specific focus on the Blue Line (including the Vaishali branch) and the Magenta Line. It allows users to:

Check upcoming metro timings for any station in both directions.

Plan a journey between two stations, automatically handling interchanges.

2. Files Included

metro_simulator.py: The main Python source code containing all logic for data loading, time calculation, and route planning.

metro_data.txt: The database file containing station names, travel times, and interchange points.

README.txt: This documentation file.

3. Data Sources & Structure

The data in metro_data.txt is structured based on the official DMRC network map.

Format: CSV-style (Line, Station, NextStation, TravelTime, Interchange).

Blue Line: Includes the main line (Dwarka Sec 21 to Noida Electronic City) and the branch (Yamuna Bank to Vaishali).

Magenta Line: Full route from Janakpuri West to Botanical Garden.

Travel Times: Approximated as 2-3 minutes between stations based on standard metro speeds. Most are 2 minutes but some are 3 minutes too.

4. Assumptions Made

Operating Hours: Metro services run from 06:00 AM to 11:00 PM.

Frequency:

Peak Hours (08:00-10:00, 17:00-19:00): Trains run every 4 minutes.

Off-Peak Hours: Trains run every 8 minutes.

Start Times: It is assumed that the first train departs from both ends of every line (Terminal Stations) exactly at 06:00 AM.

Interchange Delay: A fixed buffer of 5 minutes is added to any journey requiring a line change to account for walking time and boarding the metro.

Branching: The Blue Line splits at Yamuna Bank. The program treats the "Vaishali Branch" as a connected extension that requires a virtual transfer/check at Yamuna Bank. Thus, to find the route and timing of the Vaishali branch, the user needs to type the line 'blue' as "blue-branch"; otherwise, the code won't work and will show an error.

5. How to Run the Program

Ensure Python 3 is installed on your system.

Place metro_simulator.py and metro_data.txt in the same folder.

Open a terminal or command prompt in that folder.

Run the command:
python metro_simulator.py

Follow the on-screen menu prompts to check timings or plan a journey.

6. Usage Examples

Check Timings: Select Option 1, enter "Blue", "Rajiv Chowk", and current time "08:30". The system will show the next train towards Noida and towards Dwarka.

Plan Journey: Select Option 2, enter "Dwarka Sector 21" (Source) and "Botanical Garden" (Destination). The system will display the route, including the interchange at Janakpuri West or Botanical Garden.