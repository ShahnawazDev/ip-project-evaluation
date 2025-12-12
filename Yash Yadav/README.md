Delhi Metro Route and Schedule Simulator Assignment

This program is a simplified Delhi metro route planner, which aims to provide the most time optimized journey to the user for 2 lines of Delhi metro.
It decides if the user should prefer same line journey or take an interchange in between.
It outputs the optimal route, total journey time and calculates the fare for the journey.

Assumptions made by the program -->

1. The metro operates in the given time window of 6:00 to 23:00 only. No trains are available outside this time window.

2. The frequency of trains is 4 minutes in the window of 8 - 10 am and 5 - 7 pm; and 8 minutes otherwise.

3. We have considered the interchange time at the station to be of 3 minutes on average.

4. If both interchange and direct journey are possible, the most time efficient journey is recommended.

5. Similarly if multiple interchanges are possible; shortest time journey is suggested to the user.

6. The program assumes that the trains move in single direction based on the route. We don't consider simultaneous trains arriving from both ends.

7. The program does accept input in the case insensitive manner but wrong format leads to error output.

8. The fare is calculated on the basis of time of travel according to the following rules - 

   If the user travels for less than or equal to 20 minutes; the fare is 25 Rupees.
   If the travel time varies between 20 to 40 minutes; the fare is 40 Rupees.
   If the travel time varies between 40 to 60 minutes; the fare is 50 Rupees.
   If the travel time exceeds an hour; the fare is 70 Rupees.

9. Only 2 lines; Blue and magenta are implemented in the program.

10.The program does not account for real time delays in the metro trains.

11.The program assumes that the metro_data.txt file is apt and well formatted and no error arises due to extra whitespace or some other formatting issue.

Data Sources -->

1. The DMRC website(https://delhimetrorail.com/) was used to refer the metro mappings, interchanges stations and timings to prepare the metro_data.txt file. Also inspiration for the fare calculation was taken from the website.

2. Google maps was used to get the average timings between 2 consecutive stations.

Instructions -->

1. The user must initiate the program through the terminal (using the command - python3 metro_simulator.py).

2. The user is prompted to enter the following--> Enter the current station:
						  Enter the final station:
						  Time at the moment:

3. While inputting your stations and time, keep in mind that case sensitivity is irrelevant but on entering the wrong stations (by making a spelling mistake, or using wrong format) the program
   produces an error.

4. While entering the time, make sure you input the time in HH:MM format.

5. The time must be entered in 24 hours format so as to output the correct result.

6. Ensure that the metro_data.txt and the metro_simulator.py are in the same directory to ensure the program is able to read from the file.

7. Ensure that python is installed on your system.

Sample Input - 

Enter the current station: dwarka sec 21
Enter the final station: janakpuri west
Time at the moment: 14:00

Sample Output - 

|Same Line Journey|
Route:  Dwarka Sec 21-->Dwarka Sec 8-->Dwarka Sec 9-->Dwarka Sec 10-->Dwarka Sec 11-->Dwarka Sec 12-->Dwarka Sec 13-->Dwarka Sec 14-->Dwarka-->Dwarka Mor-->Nawada-->Uttam Nagar West-->Uttam Nagar East-->Janakpuri West
Total Time:  27.0 minutes
Final Arrival Time: 14:27
Fare for the trip in inr is:  40

Name - Yash Yadav
Roll no. - 2025573


						 

	