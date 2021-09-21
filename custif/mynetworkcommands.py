#!/usr/bin/env python3
import subprocess
import os

message = 'Switch: '
print('1. write mem')
print('2. cp backup running')
print('3. interface mode')
# wrap connection in a float() to accept decimals as numbers
menu = float(input("Select an option?"))

# if input value was higher or equal to 25
if menu == 1:
    message = message + 'writing that memory now!!.'
    subprocess.call(["free", "-g"])
elif menu == 2:
    message = message + 'backing up the config'
    subprocess.call(["echo", "....copied"]) 
elif menu == 3:
    message = message + 'entering interface mode'
    os.system("ip addr show")
else:
    message = message + 'Try again only this time pick one of the valid options'
print(message)

