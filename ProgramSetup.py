from tkinter import *
import collections, random, time, sys
from math import sqrt
from Worlds import *
from Functions import *
from character import *
from SwitchWall import *
from rupees import *

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
    canvasMain = Canvas(window, width=width, height=height,highlightthickness=0, relief='ridge', bg='black')
    canvasInfo = Canvas(window, width=width, height=32,highlightthickness=0, relief='ridge', bg='white')
    canvasMain.grid(row = 0,column = 0)
    canvasInfo.grid(row = 1,column = 0)


    World = squaregrid(canvasMain,canvasInfo)

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
                if character == ':':
                    World.rupees.append(rupee('blue',canvasMain,(x,y)))
                    World.MapData[(x,y)] = '1'
                    
                if character == '@':
                    World.rupees.append(rupee('red',canvasMain,(x,y)))
                    World.MapData[(x,y)] = '1'
                    
                if character == '#':
                    World.rupees.append(rupee('green',canvasMain,(x,y)))
                    World.MapData[(x,y)] = '1'

                
                    

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
    World.SwitchWalls.append(SwitchWall((9,6),[(1,3),(2,3),(3,3),(4,3),(5,3),(5,2),(5,1)],World))
    World.SwitchWalls.append(SwitchWall((52,12),[(65,8),(65,9),(65,10),(66,10),(67,10),(68,10),(68,9)],World))

    World.drawgrid() # draws the world.

    print((len(World.rupees)))
    
    for x in range (0,len(World.rupees)):
        World.rupees[x].draw()

    World.SpawnCharacter((11,2),Link)
    World.SpawnCharacter((10,2),Zelda)
    World.SpawnCharacter((38,20),Zelda)
    
        
    return World,World.canvas
