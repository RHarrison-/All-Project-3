from tkinter import *
from Queues import *

class Player:
    def __init__(self,canvas):
        self.direction = 'down'
        self.PlayerImage = PhotoImage(file = 'Graphics/CharacterStillDown.png')
        self.DirectionImages = {'down':['Graphics/CharacterStillDown.png','Graphics/CharacterMoveDown1.png','Graphics/CharacterMoveDown2.png'],
                                'right':['Graphics/CharacterStillRight.png','Graphics/CharacterMoveRight1.png','Graphics/CharacterMoveRight2.png'],
                                'up':['Graphics/CharacterStillUp.png','Graphics/CharacterMoveUp1.png','Graphics/CharacterMoveUp2.png'],
                                'left':['Graphics/CharacterStillLeft.png','Graphics/CharacterMoveLeft1.png','Graphics/CharacterMoveLeft2.png']
                                }
        self.MovementCycle = 1
        self.Cycle = 0
                                
                                
                                
        self.PlayerSquare = ''
        self.PlayerLocation = ()
        self.GridLocation = ()
        self.canvas = canvas
        self.speed = 1
        self.vx = 0
        self.vy = 0
        self.NextTile = (0,0)
        self.Path = ''
        self.HasObjective = False
        self.size = 16
        self.backupvx = 0
        self.backupvy = 0
        
    def LeftKey(self,event):
        pass        

    def RightKey(self,event):
        pass

    def UpKey(self,event):
        pass

    def DownKey(self,event):
        pass

    #=================================

    def FollowPath(self):

        if self.NextTile == (0,0): self.NextTile = self.Path.get()

        self.vx,self.vy = self.backupvx,self.backupvy
        
        x,y = self.canvas.coords(self.PlayerSquare)
        self.CanvasLocation = x,y
        self.GridLocation = (x//16,y//16)

        x =x/16
        y =y/16

        if (x,y) == self.NextTile: #once the robot reaches the tile one the path it is heading towards.
            if self.Path.empty(): #If the path is empty, then the robot has arrived at its objects. 
                self.vx = 0
                self.vy = 0
                self.HasObjective = False
            else:
                self.NextTile =self.Path.get()

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
