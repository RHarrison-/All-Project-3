
from ProgramSetup import *
from tkinter import *
from Functions import *
from Debug import *
import pygame
import winsound
import os

#========================= Initialisation ============================

#User can select one of 3 maps at the command line.
for root, dirnames, filenames in os.walk("Maps"):
    Maps = (filenames)
    
x=0
for Map in Maps:
    print (x, ': ', Map)
    x+=1
    
print()     
choice = input("Enter the map number than press enter")
print()

choice = int(choice)
 
mapname = Maps[choice]


#initalises the program. This creates all of the objects used and the World.
(World,canvas) = Initialise(mapname)

#============================== Main =================================

Debug1 = DebugWindow(World)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
Music = pygame.mixer.Sound('assets\KokiriForest.wav').play()
Music.set_volume(0.05)
Running = True

while Running == True:
    polling(World)
    World.CheckScreenEdge()
    Debug1.update()
    World.canvas.update()
    time.sleep(0.01)
window.mainloop()
