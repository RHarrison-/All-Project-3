import random
from tkinter import *
  
#======================== Functions ================================
'''
This is a recursive function that i use to find a random coordinate on the map.
This coordinate is valid if it is a grass tile, and that tile is not already
occupied by a traffic light.
'''
def randomvalidcoord(World): #Finds a random coordinate which can be used(not a wall)
    x1 = random.randint(1,200)
    y1 = random.randint(1,200)
        
    if (x1,y1) in World.grass:
        return (x1,y1)
    else:
        return randomvalidcoord(World)
        

Map = ['Maps\MAP1 - Large.txt','Maps\MAP1 - Medium.txt','Maps\MAP1 - Small.txt']
ProjectBanner = ['Graphics\LargeBanner.gif','Graphics\LargeBanner.gif','Graphics\SmallBanner.gif']
Width =[1210,910,510]
Height =[610,510,410]
GWidth = [120,90,50]
GHeight =[60,50,40]

'''
A small function i use to retrieve the correct details when initialaising the program.
'''
def getinfo(num):
    Mapc = Map[num]
    Widthc = Width[num]
    Heightc = Height[num]
    GWidthc = GWidth[num]
    GHeightc = GHeight[num]
    ProjectBannerc = ProjectBanner[num]

    return Mapc,Widthc,Heightc,GWidthc,GHeightc,ProjectBannerc

'''
This contains all of the code for changing items of the screen. 
'''

