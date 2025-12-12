DATA SOURCE:
* official DMRC website (for know stations on blue and magneta line and time and timings)
* google maps and gemini (for know the estimation time between two stations and metro)
* assinment guidlines (for ex - start and end time, peak hours,etc)


ASSUMPTIONS MADE
* same assumptiions from assignment like starting and ending time of metro
* peak hours of metro
* user only use blue and magenta line for travel


INSTRUCTION TO RUN CODE/USAGE GUIDE
* must write correct current station name
* must use 24-hour clock format i.e ( 11,12,13,14,15.......23)

CODE EXPLAINATION
* first two function convert time in total minutes and total minutes to time respectively, 
  this I done because it is easy to computation (add,multiply,compare,etc) in numbers 
* then I write code within a if statement with condition to check time given by user is within schedule time of metro( 06:00 AM to  06:00 AM)
  if condition true then it will run code otherwise print SERVICE UNAVLAIBLE.
* now in if statement I wrote my 3rd function to get time which metro take to reach current station from source.
  it find currrent station name and time from metro.data.text if name found it return total time otherwise add in total time which was initilaise as 0.
* now last section of code I put while loop from start to end time 
and caluate arrive time and if it match or inc the current time it give output according to if,elif,else condition



RIDE PLANNER
* this code is working till there is no interchange


