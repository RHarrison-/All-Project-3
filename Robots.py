from Queues import *
from Functions import *

'''
This is the class for the robots in project.This hold all data relevant to the robots and most of the
functionality of the project.
'''

#================== Robots ================================
class Robot:
    def __init__(self,canvas,RobotID, x, y,LandmarkList,TreasureList,TrafficLightList,World,size =16, speed =1.0, colour='blue'):
        self.canvas = canvas
        self.RobotID = RobotID
        self.colour = colour
        self.Square = self.canvas.create_rectangle(x*16,y*16,x*16 + 16,y*16+16,fill = self.colour,outline = 'White')
        self.GridLocation = (x,y)
        self.CanvasLocation  = self.canvas.coords(self.Square)
        self.path = Queue()
        self.NextTile = (0,0)
        self.HasObjective = False
        self.ObjectiveLocation = (0,0)
        self.speed = speed 
        self.size = size 
        self.vx = 0
        self.vy = 0
        self.Score = 0
        self.LandmarkList = LandmarkList
        self.World = World
        self.TreasureList = TreasureList
        self.TrafficLightList = TrafficLightList
        self.backupvx=0
        self.backupvy=0
        self.UnderLight = 999

    #================= Search Algorithm
    '''
    This is the search alogorith which is implimented to find the path which the robot follows to the landmarks.
    This is basically a breadth first search with a early exit.
    The World is made up of nodes which this algorith the orgonises into a dictionary showing which node are
    accesable from where. 
    '''
    def FindRobotPath(self,startpoint,goal):
        frontier = Queue()
        frontier.put(startpoint)
        came_from = {}
        came_from[startpoint] = None

        while not frontier.empty():
            current = frontier.get()
            #x,y = current
            #square = canvasMain.create_rectangle((x*10),(y*10),(x*10)+16,(y*10)+16,outline = 'red')

            if current == goal: # early exit. 
                break
            
            for next in self.World.neighbors(current):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current      
        return came_from

    '''
    The reconstuct path method uses the dictionary produced by the FindRobotPath method returns the nodes which
    create a path between the start and the goal. 
    '''

    def reconstruct_path(self,came_from, start, goal):
        current = goal
        path = Queue()
        path.put(current)
        while current != start:
            current = came_from[current]
            path.put(current)
        return path

    #=================================

    def FollowPath(self): #Robot follows the path to the treasure.

        self.UnderLight = 999

        for x in range (0,len(self.TrafficLightList)):
            x1,y1 = self.TrafficLightList[x].Location
            x1=x1-16
            y1=y1-16
            centrex,centrey,q,w = self.CanvasLocation
            centrex = centrex + 8
            centrey = centrey + 8

            if centrex > x1 and centrex < x1 + 48:
                if centrey > y1 and centrey < y1 + 48:
                    self.UnderLight = x #returns the number of the Traffic light, if a robot is under that light. 

        self.vx,self.vy = self.backupvx,self.backupvy
        
        if self.NextTile == (0,0): self.NextTile = self.path.get()
        
        x,y,x2,y2 = self.canvas.coords(self.Square)
        self.CanvasLocation = x,y,x2,y2

        x =x/16
        y =y/16

        if (x,y) in self.World.grass: #update the stored information for the grid location
            self.GridLocation = (x,y)
            

        if (x,y) == self.NextTile: #once the robot reaches the tile one the path it is heading towards.
            if self.path.empty(): #If the path is empty, then the robot has arrived at its objects. 
                self.vx = 0
                self.vy = 0
                self.HasObjective = False #Robot no longer has an objective.
                
            else:
                self.NextTile =self.path.get() #Returns the next tile in the path to move towards, and remove it from the list.
                ntx,nty = self.NextTile
                self.vx = ntx - x #calculates the velocity in which the robot should move to arrive at the next tile on the path.
                self.vy = nty - y
                
                self.backupvx,self.backupvy = self.vx,self.vy

        
        #If the robot is under a light, and that light is the same colour as the robot, the robots velocity is
        for st in range (0,len(self.TrafficLightList)): # set to 0. 
            if self.colour == self.TrafficLightList[st].state and self.UnderLight == st:
                self.vx,self.vy = 0,0
                
        #caluclation of the corrent coordinate which the robot should move too.
        x = ((x *16) + (self.vx)*self.speed)  
        y = ((y *16) + (self.vy)*self.speed)

        #Updates the position on the canvas in which the robot should be.
        self.canvas.coords(self.Square , x, y, x + self.size, y + self.size) 
    
    def FindNewObjective(self):
        x1,y1 = self.GridLocation
        shortestdistance = 999
        closest = 0
       
        '''
        All of this code is used to determine the optimal landmark in which the robot should move towards.
        once the target is aquired, the bottom three lines of code call the methods to find and constuct a new
        path for the robot.        
        '''
   
        for c in range (0,len(self.LandmarkList)):
            if (x1,y1) == self.LandmarkList[c].location:
                self.canvas.itemconfig(self.LandmarkList[c].square,outline = 'white')
                if  self.LandmarkList[c].found == False:
                    self.LandmarkList[c].found = True
                    self.Score += 100
                    if self.LandmarkList[c].Treasure == '':
                        continue
                    else:
                        self.canvas.itemconfig(self.LandmarkList[c].square,fill = self.colour)
                        self.TreasureList[self.LandmarkList[c].Treasure].Reveal(self.colour)
                        self.TreasureList[self.LandmarkList[c].Treasure].Found = True
                        self.Score += 50
    
            if self.LandmarkList[c].found == True: continue
            
            distance = (self.LandmarkList[c].GetDistance(x1,y1))
            
            if distance < shortestdistance:
                shortestdistance = distance
                closest = c

        if shortestdistance == 999:
            x,y = randomvalidcoord(self.World)
            self.ObjectiveLocation = (x,y)
        else:
            x,y = self.LandmarkList[closest].location
            self.ObjectiveLocation = (x,y)

        parents = self.FindRobotPath((x1,y1),(x,y))
        self.path = self.reconstruct_path(parents,(x1,y1),(x,y))
        self.path.reverse()
