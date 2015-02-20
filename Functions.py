import random
from tkinter import *
  
#======================== Functions ================================

'''
This is a recursive function that i use to find a random coordinate on the map.
This coordinate is valid if it is a grass tile, and that tile is not already
occupied by a traffic light.
'''

def randomvalidcoord(World): #Finds a random coordinate which can be used(not a wall)
    x1 = random.randint(1,World.width)
    y1 = random.randint(1,World.height)
        
    if (x1,y1) in World.grass:
        return (x1,y1)
    else:
        return randomvalidcoord(World)
        
'''
A small function i use to retrieve the correct details when initialaising the program.
'''

def getDimentions(mapname):
    x=0
    y=0
    with open('Maps/' + mapname,'r') as f:
                             # This is the code which reads the text files allowing me to create multiple maps
        for line in f:       # which can be loaded into the program. The loop reads the individual characters
            y += 1           # and and appends the coordinates to the appropiate attribute in the world.
            for character in line:
                x += 1
                if x == len(line):
                    x = 0
    width = len(line)
    width=width+1
    y=y+1
    width = width *16
    y=y*16
              
    return width,y
