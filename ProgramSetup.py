from tkinter import *
import collections, random, time, sys
from math import sqrt
from Worlds import *
from Functions import *
from character import *

'''
This is the Initialise function. This is called by the main program and is used to set up the entire
program. This creates all tkinter objects on the screen, loads the imagaes and creates the class objects
to be manipulated. 
'''

def Initialise(mapname):
                 
    window = Tk() # creating the window
    window.geometry('+200+300')
    window.title("Virtual Robot"  + mapname) #renaming the window.
    width = 640
    height = 400
    canvasMain = Canvas(window, width=width, height=height, bg='black') 
    canvasTreasures = Canvas(window, width=200, height=height+100, bg='White')
    canvasRobotInfo = Canvas(window, width=width-10, height=100, bg='White')

    canvasMain.grid(row = 0,column = 0)
    canvasTreasures.grid(row = 0,column =1,rowspan=2)
    canvasRobotInfo.grid(row = 1,column = 0)

    canvasTreasures.create_rectangle(2,8,200,height+100)
    canvasRobotInfo.create_rectangle(2,2,width-13,98)

    World = squaregrid(canvasMain)

    y = -1
    with open('Maps/' + mapname,'r') as f:
        for line in f:
            y += 1
            x=-1
            for character in line:
                x += 1
                World.MapData[(x,y)] = character
                World.width = len(line)
                World.height = y

    window.bind('<Button-1>',World.Click)
    window.bind('<Motion>',World.ShowCursor)
    window.bind('<Key>',World.Key)
    window.bind('<MouseWheel>', World.MouseWheel)

    window.bind_all('<Left>',World.LeftKey)
    window.bind_all('<Right>',World.RightKey)
    window.bind_all('<Up>',World.UpKey)
    window.bind_all('<Down>',World.DownKey)
    window.bind("<MouseWheel>", World.MouseWheel)

    World.canvas.config(cursor="none")

    World.drawgrid() # draws the world.

    World.SpawnCharacter((37,14),Link)
    World.SpawnCharacter((10,2),Zelda)
    
        
    return World,World.canvas
