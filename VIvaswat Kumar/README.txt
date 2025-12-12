Course: CSE101 
Student Name: Vivaswat Kumar  
Roll No : 2025556 
Date: 25 November 2025

Project Overview

The Delhi Metro Simulator is a Python-based command-line application designed to simulate the operations of  Blue Line, Vaishali Branch, and Magenta Line.  The program reads network data from a structured text file and processes user queries in real-time.

Features
1) Find Next Train:

Takes user input for the current station, specific metro line, current time and next station  so to know the direction user is going towards.


Calculates the arrival time of the next available train and displays subsequent 3 train timings, adjusting for peak and off-peak frequencies.

2) Plan Route:

Finds the most efficient path between a Start Station and a Destination Station.

Identifies Direct Routes if both stations lie on the same line.

Identifies Interchange Routes if a transfer is required, checking major hubs (Janakpuri West, Botanical Garden, Yamuna Bank).

Generates a detailed itinerary including departure times, arrival times, and transfer duration.

3) Check Fare:

Calculates the estimated fare for a journey based on the total count of stations passed.

Supports fare calculation for both single-line trips and multi-line journeys involving interchanges.


Data Sources

The program utilizes a local text file named metro_data.txt as its database. This file contains the network topology including:

Line Name (Blue, Blue-Vaishali, Magenta)

Station Name and Next Station (Connectivity)

Travel Time between consecutive stations

Peak and Off-Peak headway (frequency)

Interchange availability status

The Data was taken from official dmrc website and consulting  LLM model for some details.

Format:
#Line Station NextStation TravelTime(min) PeakMins OffPeakMins Interchange_Point

Assumptions made

Operating Hours: The metro service is assumed to run strictly between 06:00 AM and 11:30 PM.

Peak Hours: Peak traffic hours are defined as 08:00–10:00 and 17:00–19:00.

Train Frequency:

During Peak Hours: Trains arrive every 4 minutes.

During Off-Peak Hours: Trains arrive every 8 minutes.

Interchange Time: A fixed buffer of 10 minutes is added to the travel time whenever a passenger switches lines to account for walking distance between platforms.

Fare Structure: Fares are calculated based on the number of stations traveled:

0-2 Stations: ₹10
3-5 Stations: ₹20
6-12 Stations: ₹30
13-21 Stations: ₹40
22-32 Stations: ₹50
32+ Stations: ₹60

Station Naming: The program handles input case-insensitively and treats underscores _ in the data file as spaces to ensure better user experience.


This project was conceptualized and ideated in a group setting with two other peers Soham Tikoo (2025497) Soham Bansal(2025495). While the initial brainstorming and logic flow were discussed collaboratively, the implementation, coding, and final execution of this project were performed independently. Any similarities in structure or approach are a result of this shared ideation process.