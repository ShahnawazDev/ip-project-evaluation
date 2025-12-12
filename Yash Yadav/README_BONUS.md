Delhi Metro Route and Schedule Simulator Bonus Readme

For the bonus part of this assignment,  an additional feature was added to calculate the total fare of the metro journey based on the total journey time. This feature aligns the already existing time optimized route given by the program.

Extra Functionality -->

1.  Fare Calculation is based on the total time of journey.

2. The fare calculation is calculated in a dynamic manner; depending on whether the travel is same line or interchange travel.

3. In the output of the program, the total fare is printed catering to a realizing metro experience.

How it differs from the Main assignment —>

1. The main assignment deals with the optimized route and the total time. We added cost calculation.

2. We also provided monetary details on top of comparing interchange vs same line travel.

3. Enhanced user experience by providing fares instead of just providing basic arrival details.

Fare Calculation Rules —>

The fare calculation is governed by the total time elapsed since the user started his journey in the following manner:

Time elapsed				Amount(in Inr)
<=20 minutes				25
21- 40 minutes 				40
41 - 60 minutes 			50
>=60 minutes 				70

The fare calculation is a simplified version of DMRC fare calculation, with realistic fares to enhance user experience.

Assumptions, Design choices —>

1. The fare calculation was entirely done on the basis of total journey time only. No other factor governs fare calculation.

2. The interchange time of 3 minutes that the program assumes is a part of fare calculation.

3. The fare calculation does not account for peak hour surges and only considers the journey time.

4. The fare is designed to be simplistic and the logic implementation is the same for both direct and interchange. The main aim is to increase user relatability and improve the interaction with the program designed with real world like scenarios at the interface.

Name - Yash Yadav
Roll No. - 2025573








 


