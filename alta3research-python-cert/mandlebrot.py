#!/usr/bin/env python3
##Sourced from https://levelup.gitconnected.com/mandelbrot-set-with-python-983e9fc47f56
#I added the interaction and image collection
import matplotlib.pyplot as plt
import numpy as np

def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

def plotter(n, thresh, max_steps=25):
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    img=np.full((n,n), 255)
    for x in range(n):
        for y in range(n):
            it = get_iter(complex(*mapper(x,y)), thresh=thresh, max_steps=max_steps)
            img[y][x] = 255 - it
    return img

print("What Value of N. The higher the number the more zomes into the Mandlebrot you go. Try 1000 first then go less")
print("You will see the higher the number the better the definition, the lower the number and it pixilates")
# pause and collect input (wait for ENTER)
n = int(input() ) #Also note we only accept integers
#n=1000 #Basic starting point
img = plotter(n, thresh=4, max_steps=50)
plt.imshow(img, cmap="plasma")
plt.axis("off")

plt.show() #Displays the Graph
plt.savefig("/home/student/mycode/alta3research-python-cert/Mandle.png")  #This just saves the graph file
print("The graph is located /home/student/mycode/alta3research-python-cert/Mandle.png")
    #This just prints out the location for the user to get the graph

plt.savefig("/home/student/static/Mandle.png") #This saves an additional copy so we can view it on lab server in static
print("Also saved a copy here /home/student/static/Mandle.png")
    #This print just informs the user where the file is 
