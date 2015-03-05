from ProgramSetup import *
from tkinter import *
from Functions import *
from Debug import *
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

'''
This is the main body of the program. Any items needed during the Main loop
are retured and stored when "Initialise" is called. The actual running of the
program is pretty basic, and the main loop looks very simular is design too
project one. However the actual complexity of the program and the overall design
is greatly improved.
'''

Debug1 = DebugWindow(World)

Running = True

while Running == True:
    for x in range (len(World.Characters)):
        if World.Characters[x].HasObjective == True:World.Characters[x].FollowPath()
                
    World.CheckScreenEdge()
    World.Animate()
    Debug1.update()
    
    World.canvas.update()
    time.sleep(0.01)
window.mainloop()
