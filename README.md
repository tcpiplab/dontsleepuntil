# dontsleepuntil
python(3) script/command line tool that does not let the system sleep until some specfic conditions are met

Features:

    ⦿ prevent sleeping until battery percentage is met
  
    ⦿ prevent sleeping until time condition is met
  
    ⦿ prevent sleeping until proceding command has finished running
  
    ⦿ sleep immediately
    
    ⦿ never sleep
   
    

Recomendations:
  
    ⦿ this script should be run on a unix/bsd-based system (best with laptops)
  
    ⦿ intended to be run in a terminal 
  
    ⦿ this is script is given an alias in your terminals config. file 


Usage:

     ⦿ -t = set timer to sleep in a certain amount of time (-s = seconds, -m = minutes, -h = hours, -d = days): usage - dontsleepuntil -t -m 50 (<-- sleeps after 50 mins)

     ⦿ -b = sleep when system approaches battery percentage: usage - dontsleepuntil -b 20 (<-- sleeps when system reaches 20 percent battery)

     ⦿ -c = sleep after another command finishes executing: usage - dontsleepuntil -c grep example (<-- sleeps after grep finshes executing)

     ⦿ -i = sleep immediately

     ⦿ -n = dont sleep until script is cancelled (sleep can be voided by -n -v)

     ⦿ -h = help page
