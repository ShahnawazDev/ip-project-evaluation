my code is simple , there were many paths leading to the destination so i took the path with least time possible.
the first i started with making lists of all th station in one line eg.station_blue... and onother set of list which 
had all had all the data of all the station on one metro list in one list eg ds_blue....then 

@functions line next_metro_time() which could tell when the next metro on the statipn will arive .
@ function  time_checker()which could check if the metro service are avilable on that time instant.
@ function duration()can add minutes and it returns the new time .
@function predictor() tell if the metro is avilavle on the station or at what time it will take to reach the station.
this function also changes the prediction based on peak hours.I have taken a assumption that the first metro in a line will
start at 6:00 from both ends of the line. After the first metro reaches the ends of the line all the station will get metro 
serviced in every 8 min / 4min  metro will continue at a frequency based on peak hours. every metro will stop at
11:00pm.
@function jrny_pred(x,y) can tell the path with shortest duration between two station it returns the duration on the
shortest path.i have considred all the cases which can happen during traveling in which three cases are special
in those special cases. in there spacial cases there were many path leading leadint to the same destination but i chose
the path with the least time. i have also considred the sedement of blue line from "yamuna bank" to "vaishali"
as a different line as ie Blue1. i have sepeated the cases based on no of intersection the:-
   cases:-
   @ NO INTERSECTION NEEDED
   @ ONE INTERSECTION NEEDED
   @ TWO INTERSECTION NEEDED
   @ THREE INTERSECTION NEEDED
   @ THREE SPECIAL CASES
I HAVE also included error handling station_checker() which can return if  input station name is
valid or not and the if the user  
the code has individual cases of each route with accurate calculation to give the shortest route.
i have also considred that the metro will wait for 1 min on every stoping station for te riders to get on/off the 
metro.


input
THE code takes three input source station(source),destination (desti) and current time

output
the code retunes out 
@ checks for metro STATUS
@ metro arrival time on the line on which the user is present@
@calculates the no of interchange with name of each interchange \
@metro arival time om interchange station
@next metro arrival time on the interchange station
@total duration on traveling
@arrival time
@fare of travel