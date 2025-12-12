Project: Delhi Metro Fare Calculator (Module)
CSE101 Assignment
Student Name: Vivaswat Kumar
Roll No: 2025556
Date: 25 November 2025
1. Module Overview
This document details the Fare Calculation module of the Delhi Metro Simulator. This specific component is responsible for determining the travel cost for commuters based on the number of stations traveled. It integrates with the route planning logic to sum the total stations across single lines or interchange journeys and applies the Delhi Metro's tiered pricing structure to output the final ticket price.

2. Features

The Fare Calculation module offers the following functionalities:

Station Counting:

Accurately calculates the number of stations between a starting point and a destination on a single line.

Handles both "Up" and "Down" direction movements (forward and backward traversal) to ensure positive integer counts.

Interchange Handling:

For complex routes, it aggregates the station count of the first leg (Start → Hub) and the second leg (Hub → Destination) to derive the Total Stations.

Tiered Fare Structure:

Implements a slab-based pricing model.

Ensures a minimum fare of ₹10 and a maximum capped fare of ₹60.

3. Data Sources

The calculation relies on the indices provided by the metro_data.txt file processing.

Line Data Lists: The module uses the parsed lists (blue, blue_vaishali, magenta) to determine the index position of specific stations.

Logic: The fare is derived mathematically from the difference in list indices, rather than reading hardcoded fare values from a file.

4. Assumptions Made

For the purpose of this assignment, the following assumptions govern the fare logic:

Distance Metric: Fare is calculated strictly based on the number of stations passed, not the distance in kilometers.

Slab Consistency: The fare slabs are fixed as per the assignment guidelines and do not fluctuate based on time of day (no peak-hour surcharges).

Interchange Stations: When changing lines, the interchange station itself is accounted for in the total station count logic to ensure continuity.

5. Working of the Code

The logic is encapsulated in two primary functions within the main script.

A. Station Counting Logic (get_station_count)

This function determines the "distance" in terms of stations between two points on the same line.

Index Retrieval: It searches the specific metro line list to find the index of the start_st and end_st.

Path Calculation:

It calculates the absolute difference: |Index_Start - Index_End|.

This ensures the result is always a positive integer regardless of the train's direction.

Validation: If either station is not found on the specified line, the function returns None.

B. Fare Slab Implementation (calculate_fare)

Once the total_stations are determined (either directly or by summing two legs of an interchange journey), this function maps the count to a monetary value using the following conditional structure:

Number of Stations

Fare (₹)

0 - 2

₹10

3 - 5

₹20

6 - 12

₹30

13 - 21

₹40

22 - 32

₹50

> 32

₹60

C. Interchange Integration

In the "Check Fare" menu option:

The code first attempts to find a direct station count.

If a direct connection doesn't exist, it checks known interchange hubs (Janakpuri West, Botanical Garden, Yamuna Bank).

It calculates Leg 1 Stations + Leg 2 Stations to get the total_stations before passing it to calculate_fare.
