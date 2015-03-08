from tkinter import *
from Queues import *


class Character:
    def __init__(self,canvas):
        
        self.direction = 'down'
        self.MovementCycle = 1
        self.Cycle = 0
        self.PlayerSquare = ''
        self.PlayerLocation = ()
        self.GridLocation = ()
        self.canvas = canvas
        self.speed = 1
        self.Score = 0
        self.vx = 0
        self.vy = 0
        self.NextTile = (0,0)
        self.Path = Queue
        self.HasObjective = False
        self.ObjectiveLocation = (0,0)
        self.size = 16
        self.backupvx = 0
        self.backupvy = 0

    #=================================

    def FollowPath(self):
        
        if self.NextTile == (0,0): self.NextTile = self.Path.get()
        
        
        self.vx,self.vy = self.backupvx,self.backupvy
        
        x,y = self.canvas.coords(self.PlayerSquare)

        self.GridLocation = (x//16,y//16)

        x =x/16
        y =y/16

        if (x,y) == self.NextTile: #once the robot reaches the tile on the path it is heading towards.
            if self.Path.empty(): #If the path is empty, then the robot has arrived at its objects. 
                self.vx = 0
                self.vy = 0
                self.HasObjective = False
                self.PTO()
                
            else:
                self.NextTile = self.Path.get()

                ntx,nty = self.NextTile
                self.vx = ntx - x 
                self.vy = nty - y
                self.backupvx,self.backupvy = self.vx,self.vy
     
        x = ((x *16) + (self.vx)*self.speed)  
        y = ((y *16) + (self.vy)*self.speed)

        self.Cycle +=1
        
        if self.Cycle == 10: self.Cycle =  0
        if self.Cycle == 5: self.MovementCycle +=1
        if self.MovementCycle == 3:self.MovementCycle = 1
        
        if self.vx == 1: self.direction = 'right'
        if self.vx == -1: self.direction = 'left'
        if self.vy == 1: self.direction = 'down'
        if self.vy == -1: self.direction = 'up'
        

        self.PlayerImage = PhotoImage(file = self.DirectionImages[self.direction][self.MovementCycle])
        self.canvas.itemconfig(self.PlayerSquare,image = self.PlayerImage)

        self.canvas.coords(self.PlayerSquare , x, y)

    def PTO(self):
        x,y = self.GridLocation
        p,q = self.ObjectiveLocation
        
        x=int(x-p)
        y=int(y-q)
            
        if x>0: self.direction = 'left'
        if x<0: self.direction = 'right'
        if y>0: self.direction = 'up'
        if y<0: self.direction = 'down'

    

class Link(Character):
    def __init__(self,canvas):
        Character.__init__(self,canvas)
        self.name = 'Link'
        self.colour = 'blue'
        self.PlayerImage = PhotoImage(file = 'assets/LinkStillDown.png')
        self.DirectionImages = {'down':['assets/LinkStillDown.png','assets/LinkMoveDown1.png','assets/LinkMoveDown2.png'],
                                'right':['assets/LinkStillRight.png','assets/LinkMoveRight1.png','assets/LinkMoveRight2.png'],
                                'up':['assets/LinkStillUp.png','assets/LinkMoveUp1.png','assets/LinkMoveUp2.png'],
                                'left':['assets/LinkStillLeft.png','assets/LinkMoveLeft1.png','assets/LinkMoveLeft2.png']}

    def cut(self,gridid):
         self.ClosestPath(gridid)

         
class Zelda(Character):
    def __init__(self,canvas):
        Character.__init__(self,canvas)
        self.name = 'Zelda'
        self.colour = 'pink'
        self.PlayerImage = PhotoImage(file = 'assets/ZeldaMoveDown1.png')
        self.DirectionImages = {'down':['assets/ZeldaMoveDown1.png','assets/ZeldaMoveDown1.png','assets/ZeldaMoveDown2.png'],
                                'right':['assets/ZeldaMoveRight1.png','assets/ZeldaMoveRight1.png','assets/ZeldaMoveRight2.png'],
                                'up':['assets/ZeldaMoveUp1.png','assets/ZeldaMoveUp1.png','assets/ZeldaMoveUp2.png'],
                                'left':['assets/ZeldaMoveLeft1.png','assets/ZeldaMoveLeft1.png','assets/ZeldaMoveLeft2.png']}


