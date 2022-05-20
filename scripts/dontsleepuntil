#!/usr/bin/env python3

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
    
def never_sleep(voided=True):
    from os import system
    system('caffeinate -i')
    if not voided:
        system('pmset displaysleepnow')

def interpret(command_list):
    try:
        if len(command_list) == 0:
            print('Invalid arguments. Please use -t, -b, -c , -n, or -h for help.')
            quit()
        elif command_list[0] == '-t' and command_list[1] == '-s':
            dont_sleep_for_x_time('-s', command_list[2])
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
            try:
                if command_list[1] == '-v':
                    never_sleep()
            except IndexError:
                never_sleep(False)
        elif command_list[0] == '-i':
            sleep_now()
        elif command_list[0] in ['-h', '--help']:
            print("""
help page

-t = set timer to sleep in a certain amount of time (-s = seconds, -m = minutes, -h = hours, -d = days): usage - dontsleepuntil -t -m 50 (<-- sleeps after 50 mins)

-b = sleep when system approaches battery percentage: usage - dontsleepuntil -b 20 (<-- sleeps when system reaches 20 percent battery)

-c = sleep after another command finishes executing: usage - dontsleepuntil -c grep example (<-- sleeps after grep finshes executing)

-i = sleep immediately

-n = dont sleep until script is cancelled (sleep can be voided by -n -v)

-h = help page (this page)

                  """)
        else:
            print('Invalid arguments. Please use -t, -b, -c, -i, -n, or -h for further help.')
    except IndexError:
        print('missing or invalid arguments.(Index error detected)')


interpret(get_command())
