#!/usr/bin/env python3
## create file object in "r"ead mode
myfile = input("What config file:")
print(f'You entered {myfile}')
##with open(f'{myfile}', "r") as configfile: ##Also works
with open(myfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    count = len(open("vlanconfig.cfg", "r").readlines()) 
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("Number of Lines:", count)

