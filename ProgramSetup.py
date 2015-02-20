from tkinter import *
import collections, random, time, sys
from math import sqrt
from Queues import *
from Worlds import *
from Treasures import *
from Landmarks import *
from Robots import *
from Functions import *
from ProgramSetup import *
from TrafficLights import *
from HUD import * 

'''
This is the Initialise function. This is called by the main program and is used to set up the entire
program. This creates all tkinter objects on the screen, loads the imagaes and creates the class objects
to be manipulated. 
'''

def Initialise(mapname):
    
    #changing between the different sized maps

    Width,Height = getDimentions(mapname) #Loading variables for screen size and the maps to be used. 
                 
    window = Tk() # creating the window

    window.title("Virtual Robot: Treasure Hunt   "  + mapname) #renaming the window.
    
    canvasMain = Canvas(window, width=Width, height=Height, bg='white') #creating the three canvas's whhich are drawn too. 
    canvasTreasures = Canvas(window, width=200, height=Height+100, bg='White')
    canvasRobotInfo = Canvas(window, width=Width-10, height=100, bg='White')

    World = squaregrid(canvasMain,(Width//16)+1,(Height//16)+1) #This is the World that the robots navigate. 
                                                    #we pass the world the canvas to draw on and its dimensions. 
    canvasMain.grid(row = 0,column = 0)
    canvasTreasures.grid(row = 0,column =1,rowspan=2)
    canvasRobotInfo.grid(row = 1,column = 0)

    canvasTreasures.create_rectangle(2,8,200,Height+100)
    canvasRobotInfo.create_rectangle(5,2,Width-15,98)

    HUD = RHUD(canvasRobotInfo,canvasMain)
    
    x = 0
    y = 0

    with open('Maps/' + mapname,'r') as f: # This is the code which reads the text files allowing me to create multiple maps
        for line in f:       # which can be loaded into the program. The loop reads the individual characters
            y += 1           # and and appends the coordinates to the appropiate attribute in the world.
            for character in line:
                x += 1
                if x == len(line):
                    x = 0
                #print ((x,y), character)
                if character == '1': World.grass.append((x,y))
                if character == '2': World.water.append((x,y))
                if character == '3': World.wood.append((x,y))
                if character == '4': World.walls.append((x,y))
                if character == '5': World.rocks.append((x,y))
                if character == '6': World.sand.append((x,y))
                if character == '7': World.lava.append((x,y))

    World.drawgrid() # draws the world.

    

    TrafficLightList = []
    RobotList = []
    LandmarkList = []
    TreasureList = []
    Treasures = [['Master Sword', 'The Master Sword is a fucking cool Sword'],
                 ['Jade drogon', ' A dragon which is Jade'],
                 ['Really cool thing', 'This thing is really cool'],
                 ['Another really cool thing','This thing is also really cool'],
                 ['Reeces seal of approval','You lucky person'],
                 ['FREE BEER','Its Beer. And its Free!'],
                 ['1','1'],
                 ['2','2'],
                 ['3','3'],
                 ['4','4'],
                 ['5','5']]
    
    #for x in range (0,10):#Creating all the Traffic Lights
    #    x1,y1 = randomvalidcoord(World)
    #    x1=x1*16
    #    y1=y1*16
    #    TrafficLightList.append(TrafficLight(canvasMain,(x1,y1),World))

    for x in range (0,5): #Creating all the Landmarks
        x1,y1 = randomvalidcoord(World)
        LandmarkList.append(Landmark(x,x1,y1,canvasMain))

    TrA = 3 #len(Treasures)

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

    for x in range (0,2): #creating the Robots into the world.
        x1,y1 = randomvalidcoord(World)
        Colour = 'DodgerBlue2'
        if x % 2 == 0: Colour = 'Orange3'
        print(x1,y1)
        RobotList.append(Robot(canvasMain,x,x1,y1,LandmarkList,TreasureList,TrafficLightList,World,speed = 1,size= 16,colour = Colour))

    World.RobotList = RobotList
    World.TrafficLightList = TrafficLightList
        
    return World,canvasMain,HUD
