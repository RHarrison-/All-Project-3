from ProgramSetup import *
from tkinter import *
from Functions import *
import os
        
#========================= Initialisation ============================

#User can select one of 3 maps at the command line.
for root, dirnames, filenames in os.walk("E:\GitHub\Project3\All-Project-3\Maps"):
    Maps = (filenames)
    
x=0
for Map in Maps:
    print (x, ': ', Map)
    x+=1
    
print()     
size = input("Enter the map number than press enter")
print()

size = int(size)

mapname = Maps[size]

#initalises the program. This creates all of the objects used and the World.
(World,canvas,HUD) = Initialise(mapname)

#============================== Main =================================

'''
This is the main body of the program. Any items needed during the Main loop
are retured and stored when "Initialise" is called. The actual running of the
program is pretty basic, and the main loop looks very simular is design too
project one. However the actual complexity of the program and the overall design
is greatly improved.
'''

Running = True

while Running == True:
    for x in range (0,len(World.TrafficLightList)): #The simple random function to change the lights between the two possible colours. 
        rand = random.randint(0,1000)
        if rand >1 and rand <4:
            World.TrafficLightList[x].Switch('DodgerBlue2')
        if rand >3 and rand <6:
            World.TrafficLightList[x].Switch('Orange3')
            
    for x in range (0,len(World.RobotList)): #So all actions within here are implimented for both Robots
        
        if World.RobotList[x].HasObjective == False:  #If the Robot doesnt have a Objective, then the robot is assigned a new objective. 
            World.RobotList[x].FindNewObjective()
            World.RobotList[x].HasObjective = True
    
        World.RobotList[x].FollowPath() #The code to make the robot follow its path to the objective.
        
    HUD.Update(World.RobotList) #Update the HUD including the Score, position and Objective lines of the robots. 
    canvas.update() #Update the Main canvas. 
    time.sleep(0.01)
window.mainloop()
