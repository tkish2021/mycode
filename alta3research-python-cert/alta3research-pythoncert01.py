#! /usr/bin/env python3
import os

while True: #Sets up an infinite loop
    print("1. Make an API request" )
    print("2. Use matplotlib" )
    print("3. Guessing game" )
    print("4. Pandas to create a dataframe" )
    print("5. Anything else you find interesting!" )
    print("6. Quit." )
    print("\n Make a Number Selection:")

    selection=int(input() )  #force input as integer for comparitor. Get user input
    if selection == 1: 
        print( "Make an API request" )
        os.system("./nasaexoplanet_api.py|more")
        break
    elif selection == 2: 
        print( "Use matplotlib")
        os.system("./matplot.py")
        break
    elif selection == 3:
        print( "Guessing game three tries" )
        print("First Flip")
        os.system("./guessing.py")
        print("Second Flip")
        os.system("./guessing.py")
        print("Third Flip")
        os.system("./guessing.py")
        break
    elif selection == 4:
        print( "Pandas to create a dataframe" )
        os.system("./pandasdataframe.py|more")
        break
    elif selection == 5:
        print( "Anything else you find interesting!" )
        print( "Mandlebrots!" )
        os.system("./mandlebrot.py")
        break
    elif selection == 6: 
        print( "Quitting")
        break
    else: 
        print( "Unknown Option Selected!")

