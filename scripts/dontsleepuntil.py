#!/usr/bin/env python3

import sys
import re


def get_command():  # gets the command to pass the arguments to the rest of the script

    return sys.argv[1:]


from subprocess import check_output
from time import sleep


def dont_sleep_until_hhmm(time_hhmm):
    """
    Waits until a specified time and then puts the screen to sleep.

    This function takes a time in the format 'HH:MM' and continuously checks the current time.
    If the current time matches the specified time, the function breaks out of the loop and returns.
    Otherwise, it waits for a short duration (10 seconds) before checking again.

    Args:
        time_hhmm (str): The target time in the format 'HH:MM'.

    Note:
        The function assumes the existence of the following functions:
        - convert_time_to_hhmm: Converts the input time to the 'HH:MM' format.
        - check_output: Retrieves the current time from the system.
        - sleep_now: Performs the necessary actions to put the program to sleep.

    Raises:
        Any exceptions raised by the underlying functions may propagate up to the caller.
    """

    formatted_time = convert_time_to_hhmm(time_hhmm)

    while True:
        # Get the current time
        current_time = check_output(['date', '+%H:%M']).decode('utf-8').strip()

        # Break the loop if the current time matches the target time
        if current_time == formatted_time:
            sleep_now()  # Put the screen to sleep
            break

        # Sleep for a short duration before checking again
        sleep(10)


def convert_time_to_hhmm(time_hhmm):

    # Regular expression to capture hour and optionally minute, and am/pm indicator
    time_pattern = re.compile(r'(?P<hour>\d{1,2})(?::?(?P<minute>\d{2}))?(?P<indicator>am|pm)?', re.IGNORECASE)

    # Match the input time string against the regular expression
    match = time_pattern.match(time_hhmm)

    if not match:
        raise ValueError(f"Invalid time format: {time_hhmm}")

    # Extract matched components
    hour = int(match.group('hour'))
    minute = int(match.group('minute')) if match.group('minute') else 0
    indicator = (match.group('indicator') or '').lower()

    # Convert 12-hour format to 24-hour format
    if indicator == 'pm':
        hour = hour + 12 if hour != 12 else 12

    elif indicator == 'am':
        hour = hour if hour != 12 else 0

    formatted_time = f"{hour:02d}:{minute:02d}"

    return formatted_time


def dont_sleep_for_x_time(unit, time):
    from os import system
    # multiplies the input based in the selected unit of time
    # caffeinates system for that amount of time in seconds
    # sleeps after caffeinate finishes

    if unit == '-s':
        system(f'caffeinate -d -t {str(time)}')  # no change
        system('pmset displaysleepnow')

    elif unit == '-m':
        system(f'caffeinate -d -t {str(int(time) * 60)}')  # 60 seconds in a day
        system('pmset displaysleepnow')

    elif unit == '-h':
        system(f'caffeinate -d -t {str(int(time) * 3600)}')  # 3600 seconds in a day
        system('pmset displaysleepnow')

    elif unit == '-d':
        system(f'caffeinate -d -t {str(int(time) * 86400)}')  # 86400 seconds in a day
        system('pmset displaysleepnow')

    else:
        print('Invalid unit. Please use -s, -m,-d, or -h.')


def dont_sleep_for_x_batt(percent):  # waits until battery reaches a percent to sleep
    import subprocess
    from os import system
    from time import sleep
    while True:  # while loop to constantly check the battery percent
        battery_percent = str(
            subprocess.check_output(['pmset', '-g', 'batt']))  # isolates the battery percent in this string
        current_percent = int(battery_percent[battery_percent.index(')\\t') + 3:battery_percent.index('%')])
        if current_percent == int(percent):
            break  # breaks if current battery reaches target percentage
        system('caffeinate -d -t 1')  # makes sure the system does not sleep
        sleep(1)

    system('pmset displaysleepnow')


def dont_sleep_until_command_finishes(command):
    from os import system
    system(f'caffeinate -d -s {command}')  # formats command into caffeinate command
    system('pmset displaysleepnow')


def sleep_now():  # sleeps immediately
    from os import system
    system('pmset displaysleepnow')


def never_sleep(voided=True):
    from os import system
    system('caffeinate -d -i')  # never sleeps
    if not voided:
        system(
            'pmset displaysleepnow')  # when the user exits with ctrl c, the computer wont sleep if its voided with -v


def help_page():  # help page that waits .05 seconds between each output so there is a rolling effect
    from time import sleep
    print("\n\nhelp page")
    sleep(.05)
    print(
        '\n-u  = set time to wake up: usage - dontsleepuntil -u 5pm (<-- sleeps at 5:00pm)')
    sleep(.05)
    print(
        '\n-t = set timer to sleep in a certain amount of time (-s = seconds, -m = minutes, -h = hours, -d = days): usage - dontsleepuntil -t -m 50 (<-- sleeps after 50 mins)')
    sleep(.05)
    print(
        "\n-b = sleep when system approaches battery percentage: usage - dontsleepuntil -b 20 (<-- sleeps when system reaches 20 percent battery)")
    sleep(.05)
    print("\n-c = sleep when command finishes: usage - dontsleepuntil -c 'ls -l' (<-- sleeps when ls -l finishes)")
    sleep(.05)
    print("\n-n = never sleep: usage - dontsleepuntil -n (<-- never sleeps)")
    sleep(.05)
    print("\n-i = sleep now: usage - dontsleepuntil -i (<-- sleeps now)")
    sleep(.05)
    print("\n-h = help page: usage - dontsleepuntil -h (<-- prints this page)")
    print('\n')


def interpret(command_list):  # interprets the arguments in the comamnd line
    try:
        if len(command_list) == 0:
            print(
                'Invalid arguments. Please use -u, -t, -b, -c , -n, or -h for help.')  # if there are no arguments passed the program quits
            quit()
        elif command_list[0] == '-u':
            dont_sleep_until_hhmm(command_list[1])
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
            help_page()
        else:
            print('Invalid arguments. Please use -u, -t, -b, -c, -i, -n, or -h for further help.')
    except IndexError:  # if there is a wrong number of arguments passed
        print('missing or invalid arguments.(Index error detected)')


if __name__ == "__main__":
    interpret(get_command())  # main
