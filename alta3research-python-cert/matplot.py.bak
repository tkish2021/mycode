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
    y_pos = np.arange(len(fruits))
    numfruits = [ BANANAS , APPLES , ORANGES , PINNAPLES ]

    plt.bar(y_pos, numfruits, align='center', alpha=0.5)
    plt.xticks(y_pos, fruits)
    plt.ylabel('Number of Fruit')
    plt.title('How many Fruit in the basket')

    plt.show()
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/alta3research-python-cert/Fruit.png")
    print("The graph is located /home/student/alta3research-python-cert/Fruit.png")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/Fruit.png")
    print("Also saved a copy here /home/student/static/Fruit.png")

    
if __name__ == "__main__":
    main()

