#!/usr/bin/env python3
##python3 -m pip install matplotlib==3.0.3 ##Install matplotlib
##python3 -m pip install numpy ## Install numpy
#import matplotlib.pyplot as plt
#import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Run time code"""
# print question
    print("How Many Bananas in the basket")
# pause and collect input (wait for ENTER)
    BANANAS = int(input() )

    print("How Many Apples in the basket")
# pause and collect input (wait for ENTER)
    APPLES = int(input() )

    print("How Many Oranges in the basket")
# pause and collect input (wait for ENTER)
    ORANGES = int(input() )

    print("How Many Pinnaples in the basket")
# pause and collect input (wait for ENTER)
    PINNAPLES = int(input() )

    fruits = ('Bananas', 'Apples', 'Oranges', 'Pinnaples')
    numfruits = [ BANANAS , APPLES , ORANGES , PINNAPLES ]
    
    y_pos = np.arange(len(fruits)) #Sets auto number scaling based on user number inputs for axes Y
    #x_pos = np.arange(len(fruits))

    plt.bar(y_pos, numfruits, align='center', alpha=0.5) #Sets Y position for Each Fruit
    #plt.bar(x_pos, fruits, color=['yellow', 'red', 'orange', 'brown'])
    plt.xticks(y_pos, fruits) #Ticks are based off from Auto Scaling
    plt.ylabel('Number of Fruit') #Basic Label for Y Axes
    plt.title('How many Fruit in the basket') #Title for the Graph

    plt.show() #Displays the Graph
    plt.savefig("/home/student/alta3research-python-cert/Fruit.png")  #This just saves the graph file
    print("The graph is located /home/student/alta3research-python-cert/Fruit.png")
    #This just prints out the location for the user to get the graph

    plt.savefig("/home/student/static/Fruit.png") #This saves an additional copy so we can view it on lab server in static
    print("Also saved a copy here /home/student/static/Fruit.png")
    #This print just informs the user where the file is 

    
if __name__ == "__main__":
    main()

