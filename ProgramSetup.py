from tkinter import *
import collections, random, time, sys
from math import sqrt
from Worlds import *
from Functions import *
from character import *

from SwitchWall import *
from Key import *
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

    World.rupeecountimage = PhotoImage(file= 'assets/rupeeCOUNT.png')
    canvasInfo.create_image(40,8,anchor = 'nw', image = World.rupeecountimage)
    World.keycountimage = PhotoImage(file= 'assets/keyCOUNT.png')
    canvasInfo.create_image(90,8,anchor = 'nw', image = World.keycountimage)

    World.SelectedPlayerImage = PhotoImage(file= 'assets/CharacterStillDown.png')
    canvasInfo.create_image(8,8,anchor = 'nw', image = World.SelectedPlayerImage)
    canvasInfo.create_rectangle(4,4,28,28,outline = 'Green', width = 2)

    canvasInfo.create_text(60,9,anchor = 'nw',text = 'x')
    World.rupeenumber = canvasInfo.create_text(70,9,anchor = 'nw',text = '0')

    canvasInfo.create_text(110,9,anchor = 'nw',text = 'x')
    World.keynumber = canvasInfo.create_text(120,9,anchor = 'nw',text = '0')
    

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

                if character == '/':
                    World.Keys.append(Key(canvasMain,(x,y)))
                    World.MapData[(x,y)] = '1'

                

    
    window.bind('<Button-1>',World.Click)
    window.bind('<Button-3>',World.Rclick)

    window.bind('<Motion>',World.ShowCursor)
    window.bind('<Key>',World.Key)
    window.bind('<MouseWheel>', World.MouseWheel)

    window.bind_all('<Left>',World.LeftKey)
    window.bind_all('<Right>',World.RightKey)
    window.bind_all('<Up>',World.UpKey)
    window.bind_all('<Down>',World.DownKey)
    window.bind("<MouseWheel>", World.MouseWheel)

    World.canvas.config(cursor="none")
    
    World.SwitchWalls.append(SwitchWall((22,2),[(19,4),(19,5),(19,6),(19,7),(19,8),(19,9),
                                                (19,4),(20,4),(21,4),(22,4),(23,4),(24,4),(25,4),(26,4),(27,4),(28,4),(29,4),(30,4),
                                                (19,9),(20,9),(21,9),(22,9),(23,9),(24,9),(25,9),(26,9),(27,9),(28,9),(29,9),(30,9),
                                                (30,4),(30,5),(30,6),(30,7),(30,8),(30,9)],World))
    
    World.SwitchWalls.append(SwitchWall((7,2),[(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),
                                               (4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),
                                               (4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(10,6),
                                               (4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),
                                               (4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),
                                               (4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9)],World))

    World.SwitchWalls.append(SwitchWall((65,16),[(67,16),(68,16),(69,16),(70,16),(71,16),(72,16),
                                                 (73,16),(74,16),(75,16),(76,16),(77,16),(78,16)],World))

    World.SwitchWalls.append(SwitchWall((65,18),[(67,18),(68,18),(69,18),(70,18),(71,18),(72,18),
                                                 (73,18),(74,18),(75,18),(76,18),(77,18),(78,18)],World))

    World.SwitchWalls.append(SwitchWall((65,20),[(67,20),(68,20),(69,20),(70,20),(71,20),(72,20),
                                                 (73,20),(74,20),(75,20),(76,20),(77,20),(78,20)],World))

    World.SwitchWalls.append(SwitchWall((65,22),[(67,22),(68,22),(69,22),(70,22),(71,22),(72,22),
                                                (73,22),(74,22),(75,22),(76,22),(77,22),(78,22)],World))

    World.drawgrid() # draws the world.

    for thing in World.rupees:
        x,y = thing.location
        if x < 40:
            if y < 25:
                thing.onscreen = True
                thing.draw()

    for anotherthing in World.Keys:
        x,y = anotherthing.location
        if x < 40:
            if y < 25:
                anotherthing.draw()
                
    World.SpawnCharacter((11,2),Link)
    
        
    return World,World.canvas
