
Metro Route and Schedule Simulator:
This project is a simple Python program designed to simulate the operational schedule and route planning for the Blue Line and Magenta Line of the Delhi Metro system.
It implements two core functionalities as required by the assignment:

Metro Timings Module: Calculates and displays the arrival times for the next few trains at any given station based on the current time and frequency rules.

Ride Journey Planner: Determines the most efficient route between any two stations, calculates the total travel time, and provides detailed steps, including necessary interchange procedures.

Instructions to Run the Program:
The program is designed to be run from the command line using the Python interpreter.

File Setup: Ensure I have both essential files saved in the exact same folder:

1.metro_simulator.py (The Python code)

2.metro_data.txt (The station data file)

Launch: Open my terminal, command prompt, or the built-in VS Code Terminal.
Execute: Run the program using the Python interpreter command:python metro_simulator.py
View Output: The program will automatically run the predefined test cases (for timing and journey planning) and display the results in the terminal.

Data Sources and File Structure:
The project relies on station and time data stored in a separate text file for modularity.

Data Source: The station order, names, interchange points, and inter-station travel times for the Blue Line and Magenta Line were structured based on publicly available information from the Official DMRC (Delhi Metro Rail Corporation) website and related metro maps.

Logic and Assumptions Made:
Service Hours:-The metro operates from 06:00 AM to 11:00 PM.	
Hardcoded time boundaries (360 to 1380 minutes) are used to check for "No service available".
Train Frequency:-Peak Hours (8-10 AM and 5-7 PM) have a 4-minute frequency. Off-Peak Hours have an 8-minute frequency.The code identifies peak hours by checking if the hour H is within (8 <= H < 10) or (17 <= H < 19).
Interchange Delay:-A fixed 3-minute delay is added for any transfer between the Blue and Magenta Lines.The INTERCHANGE_DELAY variable is set to 3 minutes.
Interchange Logic:-For route planning, the interchange point is simplified: If starting on Blue Line, the transfer is assumed to be at Janakpuri West. If starting on the Magenta Line, the transfer is assumed to be at Botanical Garden.	This simplified logic addresses the common interchange points between the two lines to facilitate basic route calculation.
README.md
External
Displaying README.md.