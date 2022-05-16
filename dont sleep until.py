def get_command():
    import sys
    return sys.argv[1:]

def dont_sleep_for_x_time(unit, time):
    from os import system

    if unit == '-s':
        system(f'caffeinate -d -t {str(time)}')
        system('pmset displaysleepnow')

    elif unit == '-m':
        system(f'caffeinate -d -t {str(int(time) * 60)}')
        system('pmset displaysleepnow')

    elif unit == '-h':
        system(f'caffeinate -d -t {str(int(time) * 3600)}')
        system('pmset displaysleepnow')
    
    elif unit == '-d':
        system(f'caffeinate -d -t {str(int(time) * 86400)}')
        system('pmset displaysleepnow')

    else:
        print('Invalid unit. Please use -s, -m,-d, or -h.')
        
def dont_sleep_for_x_batt(percent):
    import subprocess
    from os import system
    from time import sleep
    while True:
        battery_percent = str(subprocess.check_output(['pmset', '-g', 'batt']))  
        current_percent = int(battery_percent[battery_percent.index(')\\t') + 3:battery_percent.index('%')])
        if current_percent == int(percent):
            break
        else:
            system('caffeinate -d -t 1')
            sleep(1)
            
    system('pmset displaysleepnow')
    
    
def dont_sleep_until_command_finishes(command):
    from os import system
    system(f'caffeinate -s {command}')
    system('pmset displaysleepnow')
    
def sleep_now():
    from os import system
    system('pmset displaysleepnow')

def interpret(command_list):
    if len(command_list) == 0:
	print('Invalid arguments. Please use -t, -b,-c , -n, or -h.')
    elif command_list[0] == '-t' and command_list[1] == '-s':
        dont_sleep_for_x_time('-s', int(command_list[2]))
    elif command_list[0] == '-t' and command_list[1] == '-m':
        dont_sleep_for_x_time('-m', command_list[2])
    elif command_list[0] == '-t' and command_list[1] == '-h':
        dont_sleep_for_x_time('-h', command_list[2])
    elif command_list[0] == '-t' and command_list[1] == '-d':
        dont_sleep_for_x_time('-d', command_list[2])
    elif command_list[0] == '-b':
        dont_sleep_for_x_batt(command_list[1])
    elif command_list[0] == '-c':
        dont_sleep_until_command_finishes(command_list[1])
    elif command_list[0] == '-n':
        sleep_now()
    elif command_list[0] == '-h' or command_list[0] == '--help':
	    print('\nhelp page\n\n-t = set timer to sleep in a certain amount of time (-s = seconds, -m = minutes, -h = hours, -d = days).\n-b = sleep when system approaches battery percentage\n-c = sleep after another command finishes executing\n-n = sleep now\n') 
    else:
        print('Invalid arguments. Please use -t, -b,-c , -n, or -h.')
        
interpret(get_command())
