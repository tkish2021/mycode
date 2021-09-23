#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# python3 -m pip install crayons
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring with RED
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

def rebootpush(devicereboot): # devicereboot==dict

    for ip in devicereboot.keys(): # looping through the dict
        print(f'{crayons.red("Rebooting")}. .. ... Connecting to.. {ip}') # fstring with RED
        # we'll learn to write code that connects to devices here
        for myips in devicereboot[ip]:
            print(f'REBOOTING NOW! --> {myips}')
            # we'll learn to write code that sends cmds to device here
    return None
# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

   # dict containing IPs mapped to a list of physical interfaces and their state
    devicereboot = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher") # welcome message with blue text

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    rebootpush(devicereboot) # call function to push reboot to devices

# call our main function
main()

