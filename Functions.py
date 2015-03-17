import random
from tkinter import *
from character import *
import pygame

  
#======================== Functions ================================

'''
This is a recursive function that i use to find a random coordinate on the map.
This coordinate is valid if it is a grass tile, and that tile is not already
occupied by a traffic light.
'''
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
def polling(World):
    for x in range (len(World.Characters)):
        if World.Characters[x].HasObjective == True:World.Characters[x].FollowPath()

        for y in range (0,len(World.SwitchWalls)):
            if World.MapDataCoords(World.Characters[x].GridLocation) == World.SwitchWalls[y].location and World.SwitchWalls[y].flippos == 0:
                World.SwitchWalls[y].active()
                sSwitch = pygame.mixer.Sound('assets\PP_Switch.wav').play()
                sSwitch.set_volume(0.08)
                continue
                
            if World.SwitchWalls[y].flippos == 1:
                ontop = False
                for q in range (0,len(World.Characters)):
                    if World.MapDataCoords(World.Characters[q].GridLocation) == World.SwitchWalls[y].location:
                        ontop = True

                if ontop == False:
                    World.SwitchWalls[y].inactive()
                    sSwitch = pygame.mixer.Sound('assets\PP_Switch.wav').play()
                    sSwitch.set_volume(0.09)

        x,y =  World.MapDataCoords(World.Characters[x].GridLocation)
        for rupee in World.rupees:
            if rupee.location == (x,y) and rupee.collected == False:
                rupee.collected = True
                World.canvas.delete(rupee.rupeesquare)
                World.Characters[0].rupees += rupee.points
                CRupee = pygame.mixer.Sound('assets\GetRupeeGreen.wav').play()
                CRupee.set_volume(0.15)
                World.canvas2.delete(World.rupeenumber)
                World.rupeenumber = World.canvas2.create_text(70,9,anchor = 'nw',text = World.Characters[0].rupees)

        for Key in World.Keys:
            if Key.location == (x,y) and Key.collected == False:
                Key.collected = True
                World.canvas.delete(Key.keysquare)
                World.Characters[0].Keys += 1
                World.canvas2.delete(World.keynumber)
                World.keynumber = World.canvas2.create_text(120,9,anchor = 'nw',text = World.Characters[0].Keys)
                

    x,y = World.MapDataCoords(World.Characters[0].GridLocation)
    

    neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

    for neighbor in neighbors:
        if neighbor not in World.MapData: continue
        if World.MapData[neighbor] == '>':
            if World.Characters[0].Keys > 0:
                World.Characters[0].Keys -=1
                World.canvas2.delete(World.keynumber)
                World.keynumber = World.canvas2.create_text(120,9,anchor = 'nw',text = World.Characters[0].Keys)
                p,q = World.ScreenCoords(neighbor)
                p=p*16
                q=q*16
                World.canvas.create_image(p,q,anchor = 'nw',image = World.grassimage1)
                World.SpawnCharacter((p//16,q//16),Zelda)
                World.MapData[neighbor] = '1'
                
def randomvalidcoord(World): #Finds a random coordinate which can be used(not a wall)

    x1 = random.randint(1,World.width)
    y1 = random.randint(1,World.height)

    x1 = random.randint(1,35)
    y1 = random.randint(1,23)

        
    if World.MapData[(x1,y1)] == '1':
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
