#!/usr/bin/env python3
##python3 -m pip install matplotlib==3.0.3 ##Install matplotlib
##python3 -m pip install numpy ## Install numpy
import matplotlib.pyplot as plt
import numpy as np

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

    fig = plt.figure()

    #ax.set_yticks(np.arange(0, 10, 1))
    
    Fruits = ['Bananas', 'Apples', 'Oranges', 'Pinnaples']
    Numfruits = [ BANANAS , APPLES , ORANGES , PINNAPLES ]

    ax = fig.add_axes([0,0,1,1])    
    ax.set_title('Fruit in a Basket')
    ax.set_ylabel('Fruit Count')
    ax.bar(Fruits,Numfruits)

    print(Fruits)
    print(Numfruits)

    plt.show()

    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/alta3research-python-cert/Fruit.png")
    print("The graph is located /home/student/alta3research-python-cert/Fruit.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/Fruit.png")
    print("Also saved a copy here /home/student/static/Fruit.png")

    
if __name__ == "__main__":
    main()
