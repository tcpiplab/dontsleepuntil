#!/bin/bash

read -p "Enter y to accept that this program appends text to a configuration file, enter anything else to cancel and in the program: " consent 
if [ $consent == "y" ] || [ "$consent" = "Y" ]
then
    echo "You have accepted the terms of the agreement"
    echo ""
    read -p "Enter the path of the configuration file: " path
    echo ""
    read -p "Enter the alias name, to default, press enter with nothing entered (defaults to 'dontsleepuntil'): " alias
    if [ -z $alias ]
    then
        alias="dontsleepuntil"
    fi
    echo ""
    read -p "Enter the path of the dontsleepuntil.py program file: " program
    program=${program// /\\ }
    echo ""
    echo "Appending text to the configuration file"
    echo "alias $alias='python3.9 $program'" >> $path
    echo "refreshing the configuration file"
    source $path
    echo "alias added,the command '$alias' should now execute dontsleepuntil's program, if not,open a new terminal window or run the command 'source $path' to refresh the configuration file manually"
    echo 'exiting'
    exit
else
    echo "You have declined the terms of the agreement, to run this program again please run the script again"
    echo "Exiting the program"
fi
