# Delhi Metro Route and Schedule Simulator

A Python-based simulator for the Delhi Metro system that helps users find next train timings and plan journeys between stations on the Blue Line and Magenta Line.

## 📋 Table of Contents

- [Data Sources](#data-sources)
- [Assumptions Made](#assumptions-made)
- [Instructions to Run](#instructions-to-run)
- [Features](#features)

---

## 📊 Data Sources

The metro station data used in this project was collected from the following sources:

1. **Official DMRC Website**: [https://www.delhimetrorail.com/](https://www.delhimetrorail.com/)
   - Station names and order for Blue Line and Magenta Line
   - Interchange station information
   - Approximate travel times between consecutive stations

2. **Data Collection Details**:
   - **Blue Line**: Complete route from Dwarka Sector 21 to Noida Electronic City / Vaishali
   - **Magenta Line**: Complete route from Janakpuri West to Botanical Garden
   - Travel times between stations are approximate values based on typical metro operations
   - Interchange points identified where passengers can transfer between Blue and Magenta lines
    - **Green Line**: Route spanning Inderlok/Kirti Nagar to Brigadier Hoshiyar Singh, covering both branches
   - **Airport Express Line**: High-speed corridor from New Delhi to Dwarka Sector 21

3. **Data Format**:
   - Data is stored in `metro_data.txt` as a comma-separated text file
   - Format: `Line, Station, NextStation, TravelTime(min), InterchangePoint`
   - Header row is included and automatically skipped during data loading

---

## 🔍 Assumptions Made

The following assumptions have been made in the implementation:

### 1. **Service Hours**
   - Metro service operates from **06:00 AM to 11:00 PM (23:00)**
   - No service is available outside these hours
   - The program displays "No service available" for times outside service hours

### 2. **Train Frequency**
   - **Peak Hours**: Trains run every **4 minutes**
     - Morning peak: 08:00 AM - 10:00 AM
     - Evening peak: 05:00 PM - 07:00 PM
   - **Off-Peak Hours**: Trains run every **8 minutes**
     - All other times within service hours

### 3. **Train Schedule**
   - First train of the day departs from terminal stations at **06:00 AM**
   - Trains follow a regular schedule based on frequency intervals
   - Next train time is calculated based on the current time and frequency

### 4. **Interchange Handling**
   - **Interchange delay**: **3 minutes** is added when transferring between lines
   - This accounts for walking time between platforms and waiting for the connecting train
   - Interchange stations are marked in the data file with "Yes" in the InterchangePoint column

### 5. **Route Finding**
   - The program uses Breadth-First Search (BFS) algorithm to find the shortest path
   - For journeys requiring interchange, the program finds the best interchange point
   - Only one interchange is considered (direct route or one interchange)
   - Travel time is calculated as the sum of segment times plus interchange delay

### 6. **Station and Line Names**
   - Station and line names are case-insensitive (e.g., "blue", "Blue", "BLUE" all work)
   - The program normalizes input to match data file entries

### 7. **Time Format**
   - All times must be in **HH:MM format** (24-hour format)
   - Examples: "09:18", "17:30", "06:00"
   - Invalid time formats are rejected with an error message

### 8. **Data File**
   - The data file `metro_data.txt` must be in the same directory as the program
   - The file must have a header row that will be skipped
   - Each data row must have exactly 5 comma-separated values

---

## 🚀 Instructions to Run

### Prerequisites

- **Python 3.x** installed on your system
- `metro_data.txt` file in the same directory as `metro_simulator.py`

### Step-by-Step Instructions

1. **Navigate to the Project Directory**
   ```bash
   cd "/Users/mananpatel/Desktop/ip assignment"
   ```

2. **Verify Files are Present**
   - Ensure `metro_simulator.py` exists
   - Ensure `metro_data.txt` exists in the same directory

3. **Run the Program**
   ```bash
   python metro_simulator.py
   ```
   
   Or alternatively:
   ```bash
   python3 metro_simulator.py
   ```

4. **Using the Program**

   Once the program starts, you will see the main menu:
   ```
   ==**==**==**==**==**==**==**==**=**==**==**==
   Delhi Metro Route & Schedule Simulator
   ==**==**==**==**==**==**==**==**=**==**==**==

   1. Metro Timings
   2. Journey Planner
   3. Exit
   Choose 1-3:
   ```

   **Option 1: Metro Timings**
   - Enter the line name (e.g., "Blue" or "Magenta")
   - Enter the station name (e.g., "Rajiv Chowk")
   - Enter the current time in HH:MM format (e.g., "09:18")
   - The program will display the next train and subsequent train times

   **Option 2: Journey Planner**
   - Enter the starting station name
   - Enter the destination station name
   - Enter the time of travel in HH:MM format
   - The program will display:
     - Next available metro at source
     - Route details (direct or with interchange)
     - Arrival time at each station
     - Total travel time

   **Option 3: Exit**
   - Exits the program

### Example Usage

**Example 1: Check Next Train**
```
=== Metro Timings ===
Line (e.g. Blue): Blue
Station: Rajiv Chowk
Current time (HH:MM): 09:18

Output:
Next metro at 09:20
Following metros: 09:24, 09:28, 09:32, 09:36
```

**Example 2: Plan a Journey**
```
=*= Journey Planner =*=
Starting station: Dwarka
Final station: Botanical Garden
Time (HH:MM): 08:22

Output:
Journey Plan
Start at Dwarka (Blue Line)
Next metro at 08:24
Arrive Janakpuri West at 08:39
Next train departs at 08:42
Reach Botanical Garden at 09:15
Total travel time: 51 minutes
```

### Troubleshooting

- **File Not Found Error**: Ensure `metro_data.txt` is in the same directory as the Python script
- **Invalid Time Format**: Use HH:MM format (e.g., "09:18", not "9:18" or "9:18 AM")
- **Station Not Found**: Check spelling and ensure the station exists on the specified line
- **No Service Available**: Ensure the time is between 06:00 and 23:00

---

## ✨ Features

- ✅ **Metro Timings Module**: Find next train arrival times at any station
- ✅ **Journey Planner**: Plan complete journeys with route optimization
- ✅ **Interchange Support**: Automatic handling of line transfers
- ✅ **Peak Hour Detection**: Different train frequencies for peak and off-peak hours
- ✅ **Service Hours Validation**: Checks if metro service is available
- ✅ **Case-Insensitive Input**: Flexible station and line name entry
- ✅ **Error Handling**: User-friendly error messages for invalid inputs

---