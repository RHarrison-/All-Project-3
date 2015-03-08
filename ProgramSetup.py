from tkinter import *
import collections, random, time, sys
from math import sqrt
from Worlds import *
from Functions import *
from character import *
from Treasures import *
from Landmarks import *

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

    World.drawgrid() # draws the world.

    ################################################################################

   
    RobotList = []
    LandmarkList = []
    TreasureList = []
    Treasures = [['Master Sword', 'The Master Sword is a fucking cool Sword'],
                 ['Jade drogon', ' A dragon which is Jade'],
                 ['Really cool thing', 'This thing is really cool'],
                 ['Another really cool thing','This thing is also really cool'],
                 ['Reeces seal of approval','You lucky person'],
                 ['FREE BEER','Its Beer. And its Free!']]
                 #['1','1'],
                 #['2','2'],
                 #['3','3'],
                 #['4','4'],
                 #['5','5']]
    
    
    for x in range (0,6): #Creating all the Landmarks
        x1,y1 = randomvalidcoord(World)
        LandmarkList.append(Landmark(x,x1,y1,canvasMain))

    TrA = len(Treasures)

    for x in range (0,TrA): #Uses information from the Treasure list to create Treasure Objects.
        Tr = Treasures.pop(0)
        TreasureList.append(Treasure(Tr[0],Tr[1],TreasureList,canvasTreasures))
        
    TL = 0

    while TL != TrA:
        TL = 0
        randLand= random.randint(0,len(LandmarkList)-1) # randomly assigning treasures to landmarks
         
        if LandmarkList[randLand].Treasure == '':
            for x in range (0,len(TreasureList)):
                if TreasureList[x].used == False: 
                    LandmarkList[randLand].Treasure = x
                    TreasureList[x].used = True
                    break
            
        for x in range (0,len(TreasureList)):
           if TreasureList[x].used == True:
               TL +=1

    World.LandmarkList = LandmarkList
    World.TreasureList = TreasureList

                
    ####################################################################################
    
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

    

    World.SpawnCharacter((37,14),Link)
    World.SpawnCharacter((10,2),Zelda)
    
        
    return World,World.canvas
