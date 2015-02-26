from tkinter import *
from character import *
import random
#=================== The World Generation =====================    
class squaregrid:
    def __init__ (self,canvas):
        self.canvas = canvas
        self.width = 0
        self.height = 0
        self.screenlocation = (0,0)
        self.Player = ''
        self.CursorSquare = ''
        
        self.MapData = {}
        
        self.stoneimage = PhotoImage(file = 'Graphics\Stone.png')
        self.grassimage1 = PhotoImage(file = 'Graphics\Grass1.png')
        self.grassimage2 = PhotoImage(file = 'Graphics\Grass2.png')
        self.waterimage1 = PhotoImage(file = 'Graphics\Water1.png')
        self.waterimage2 = PhotoImage(file = 'Graphics\Water2.png')
        self.flowerimage = PhotoImage(file = 'Graphics\Flower.png')
        self.stumpimage = [[PhotoImage(file = 'Graphics\TLStump.png'),
                           PhotoImage(file = 'Graphics\BLStump.png')],
                           [PhotoImage(file = 'Graphics\TRStump.png'),
                           PhotoImage(file = 'Graphics\BRStump.png')]]
        self.I1 = PhotoImage(file = 'Graphics\GrassCliffN.png') #a
        self.i1 = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.I2 = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.I3 = PhotoImage(file = 'Graphics\WaterCliffN.png')
        self.I4 = PhotoImage(file = 'Graphics\WaterN.png')
        self.I5 = PhotoImage(file = 'Graphics\GrassCliffNE.png')
        self.I6 = PhotoImage(file = 'Graphics\TopCliffNE.png')
        self.I7 = PhotoImage(file = 'Graphics\MiddleCliffNE.png')
        self.I8 = PhotoImage(file = 'Graphics\WaterCliffNE.png')
        self.I9 = PhotoImage(file = 'Graphics\WaterCLiffNtoNE.png')
        self.I10 = PhotoImage(file = 'Graphics\WaterNE.png')
        self.I11 = PhotoImage(file = 'Graphics\WaterOuterNE.png')
        self.I12 = PhotoImage(file = 'Graphics\WaterOuterNE2.png')
        self.I13 = PhotoImage(file = 'Graphics\TopCliffE.png')
        self.I14 = PhotoImage(file = 'Graphics\BottomCliffE.png')
        self.I15 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        self.I16 = PhotoImage(file = 'Graphics\TopCliffNW.png')
        self.I17 = PhotoImage(file = 'Graphics\CliffMiddleNW.png')
        self.I18 = PhotoImage(file = 'Graphics\CliffBottomNW.png')
        self.I19 = PhotoImage(file = 'Graphics\CliffGrassNW.png')
        self.I20 = PhotoImage(file = 'Graphics\WaterCliffNW.png')        
        self.I21 = PhotoImage(file = 'Graphics\CliffTopW.png')
        self.I22 = PhotoImage(file = 'Graphics\MiddleCliffW.png')
        self.I23 = PhotoImage(file = 'Graphics\WaterW.png')
        self.I24 = PhotoImage(file = 'Graphics\GrassCliffSW.png')
        self.I25 = PhotoImage(file = 'Graphics\TopCliffSW.png')  
        self.I26 = PhotoImage(file = 'Graphics\GrassSW.png')         
        self.I27 = PhotoImage(file = 'Graphics\BottomCliffSW.png') 
        self.I28 = PhotoImage(file = 'Graphics\WaterSW.png') 
        self.I29 = PhotoImage(file = 'Graphics\WaterCornerSW.png') 
        self.I30 = PhotoImage(file = 'Graphics\GrassCliffS.png')
        self.I31 = PhotoImage(file = 'Graphics\TopCliffS.png') 
        self.I32 = PhotoImage(file = 'Graphics\MiddleCliffS.png')
        self.I33 = PhotoImage(file = 'Graphics\BottomCliffS.png')
        self.I34 = PhotoImage(file = 'Graphics\WaterS.png')
        self.I35 = PhotoImage(file = 'Graphics\GrassSE.png')
        self.I36 = PhotoImage(file = 'Graphics\GrassCliffSE.png')
        self.I37 = PhotoImage(file = 'Graphics\TopCliffSE.png')
        self.I38 = PhotoImage(file = 'Graphics\BottomCliffSE.png')
        self.I39 = PhotoImage(file = 'Graphics\WaterCliffSE.png')
        self.I40 = PhotoImage(file = 'Graphics\CornerWaterSE.png')
        #self.I41 = PhotoImage(file = 'Graphics\.png')# O
        #self.I42 = PhotoImage(file = 'Graphics\.png')# P
        #self.I43 = PhotoImage(file = 'Graphics\.png')# Q
        #self.I44 = PhotoImage(file = 'Graphics\.png')# R
        #self.I45 = PhotoImage(file = 'Graphics\.png')# S
        #self.I46 = PhotoImage(file = 'Graphics\.png')# T
        #self.I47 = PhotoImage(file = 'Graphics\.png')# U
        #self.I48 = PhotoImage(file = 'Graphics\.png')# V
        #self.I49 = PhotoImage(file = 'Graphics\.png')# W
        #self.I50 = PhotoImage(file = 'Graphics\.png')# X
        #self.I51 = PhotoImage(file = 'Graphics\.png')# Y
        #self.I52 = PhotoImage(file = 'Graphics\.png')# Z

    def ShowCursor(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)
        
        self.canvas.delete(self.CursorSquare)
        if self.MapData[(x//16,y//16)] == '1':
            colour = 'White'
        else:
            colour = 'Red'
            
        self.CursorSquare = self.canvas.create_rectangle(x+2,y+2,x+18,y+18,fill = '',
                                                         outline = colour, width = 2)

    def SpawnCharacter(self,location):
        x,y = location
        self.Player.GridLocation = (x,y)
        x=x*16
        y=y*16
        print(x,y)
        self.Player.PlayerLocation = (x,y)
        self.Player.PlayerSquare = self.canvas.create_image(x,y,anchor = 'nw',image = self.Player.PlayerImage)

    def MoveScreen(self):
        self.canvas.delete(ALL)
        moveam = 0
        if self.Player.direction == 'right': movam = (40,0)
        if self.Player.direction == 'left': movam = (-40,0)
        if self.Player.direction == 'up': movam = (0,-25)
        if self.Player.direction == 'down': movam = (0,25)

        self.screenlocation = (addcords(self.screenlocation,movam))
        p = self.screenlocation[0] 
        r = self.screenlocation[1]
        for s in range (0,40):
            for q in range (0,25):
                if ( p+s,r+q) in self.MapData: (self.drawtile((s,q),self.MapData[( p+s,r+q)]))

        #================= Search Algorithm
    '''
    This is the search alogorith which is implimented to find the path which the robot follows to the landmarks.
    This is basically a breadth first search with a early exit.
    The World is made up of nodes which this algorith the orgonises into a dictionary showing which node are
    accesable from where. 
    '''
    def FindPath(self,startpoint,goal):
        frontier = Queue()
        frontier.put(startpoint)
        came_from = {}
        came_from[startpoint] = None

        while not frontier.empty():
            current = frontier.get()
            #x,y = current
            #square = self.canvas.create_rectangle((x*16),(y*16),(x*16)+16,(y*16)+16,outline = 'red')

            if current == goal: # early exit. 
                break
            
            for next in self.neighbors(current):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current      
        return came_from

    '''
    The reconstuct path method uses the dictionary produced by the FindRobotPath method returns the nodes which
    create a path between the start and the goal. 
    '''

    def ReconstructPath(self,came_from, start, goal):
        current = goal
        path = Queue()
        path.put(current)
        while current != start:
            current = came_from[current]
            path.put(current)
        return path

    def FindPlayerPath(self,x,y):
        MovementGrid = self.FindPath(self.Player.GridLocation,(x,y))
        
        CPath = self.ReconstructPath(MovementGrid,self.Player.GridLocation,(x,y))
        self.Player.HasObjective = True
        CPath.reverse()
        self.Player.Path = CPath
        

    def Click(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)

        x=x//16
        y=y//16
        print(x,y)
        if self.MapData[(x,y)] == '1':
            self.FindPlayerPath(x,y)

    def Key(self,event):
        pass            
        
    def drawgrid(self):
        
        p = self.screenlocation[0] 
        r = self.screenlocation[1] 

        for s in range (0,40):
            for q in range (0,25):
                if ( r+q,p+s) in self.MapData: self.drawtile((s,q),self.MapData[(p+s, r+q)])

    def drawtile(self,gridid,TType):
        
        x,y = gridid        
        x = (x*16)+2
        y = (y*16)+2

        if TType == '1':
             rand = random.randint(1, 100)
             if rand <95:
                 self.canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
             elif rand >=95:
                 self.canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
 
        if TType == '2':
            rand = random.randint(1, 100)
            if rand <80:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand  >=80:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage2)      

        if TType == '3': self.canvas.create_image(x,y,anchor="nw",image=self.stoneimage)
        if TType == '4': self.canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][self.rotation])
        if TType == '5': self.canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][self.rotation])
        if TType == '6': self.canvas.create_image(x,y,anchor="nw",image=self.flowerimage)
        
        if TType == 'a': self.canvas.create_image(x,y,anchor="nw",image=self.I1)
        if TType == 'b': self.canvas.create_image(x,y,anchor="nw",image=self.I2)
        if TType == 'c': self.canvas.create_image(x,y,anchor="nw",image=self.I3)
        if TType == 'd': self.canvas.create_image(x,y,anchor="nw",image=self.I4)
        if TType == 'e': self.canvas.create_image(x,y,anchor="nw",image=self.I5)
        if TType == 'f': self.canvas.create_image(x,y,anchor="nw",image=self.I6)
        if TType == 'g': self.canvas.create_image(x,y,anchor="nw",image=self.I7)
        if TType == 'h': self.canvas.create_image(x,y,anchor="nw",image=self.I8)
        if TType == 'i': self.canvas.create_image(x,y,anchor="nw",image=self.I9)
        if TType == 'j': self.canvas.create_image(x,y,anchor="nw",image=self.I10)
        if TType == 'k': self.canvas.create_image(x,y,anchor="nw",image=self.I11)
        if TType == 'l': self.canvas.create_image(x,y,anchor="nw",image=self.I12)
        if TType == 'm': self.canvas.create_image(x,y,anchor="nw",image=self.I13)
        if TType == 'n': self.canvas.create_image(x,y,anchor="nw",image=self.I14)
        if TType == 'o': self.canvas.create_image(x,y,anchor="nw",image=self.I15)
        if TType == 'p': self.canvas.create_image(x,y,anchor="nw",image=self.I16)
        if TType == 'q': self.canvas.create_image(x,y,anchor="nw",image=self.I17)
        if TType == 'r': self.canvas.create_image(x,y,anchor="nw",image=self.I18)
        if TType == 's': self.canvas.create_image(x,y,anchor="nw",image=self.I19)
        if TType == 't': self.canvas.create_image(x,y,anchor="nw",image=self.I20)
        if TType == 'u': self.canvas.create_image(x,y,anchor="nw",image=self.I21)
        if TType == 'v': self.canvas.create_image(x,y,anchor="nw",image=self.I22)
        if TType == 'w': self.canvas.create_image(x,y,anchor="nw",image=self.I23)
        if TType == 'x': self.canvas.create_image(x,y,anchor="nw",image=self.I24)
        if TType == 'y': self.canvas.create_image(x,y,anchor="nw",image=self.I25)
        if TType == 'z': cself.anvas.create_image(x,y,anchor="nw",image=self.I26)
        if TType == 'A': self.canvas.create_image(x,y,anchor="nw",image=self.I27)
        if TType == 'B': self.canvas.create_image(x,y,anchor="nw",image=self.I28)
        if TType == 'C': self.canvas.create_image(x,y,anchor="nw",image=self.I29)
        if TType == 'D': self.canvas.create_image(x,y,anchor="nw",image=self.I30)
        if TType == 'E': self.canvas.create_image(x,y,anchor="nw",image=self.I31)
        if TType == 'F': self.canvas.create_image(x,y,anchor="nw",image=self.I32)
        if TType == 'G': self.canvas.create_image(x,y,anchor="nw",image=self.I33)
        if TType == 'H': self.canvas.create_image(x,y,anchor="nw",image=self.I34)
        if TType == 'I': self.canvas.create_image(x,y,anchor="nw",image=self.I35)
        if TType == 'J': self.canvas.create_image(x,y,anchor="nw",image=self.I36)
        if TType == 'K': self.canvas.create_image(x,y,anchor="nw",image=self.I37)
        if TType == 'L': self.canvas.create_image(x,y,anchor="nw",image=self.I38)
        if TType == 'M': self.canvas.create_image(x,y,anchor="nw",image=self.I39)
        if TType == 'N': self.canvas.create_image(x,y,anchor="nw",image=self.I40)
        #if TType == 'O': self.canvas.create_image(x,y,anchor="nw",image=self.I41)
        #if TType == 'P': self.canvas.create_image(x,y,anchor="nw",image=self.I42)
        #if TType == 'Q': self.canvas.create_image(x,y,anchor="nw",image=self.I43)
        #if TType == 'R': self.canvas.create_image(x,y,anchor="nw",image=self.I44)
        #if TType == 'S': canvas.create_image(x,y,anchor="nw",image=self.I45)
        #if TType == 'T': canvas.create_image(x,y,anchor="nw",image=self.I46)
        #if TType == 'U': canvas.create_image(x,y,anchor="nw",image=self.I47)
        #if TType == 'V': canvas.create_image(x,y,anchor="nw",image=self.I48)
        #if TType == 'W': canvas.create_image(x,y,anchor="nw",image=self.I49)
        #if TType == 'X': canvas.create_image(x,y,anchor="nw",image=self.I50)
        #if TType == 'Y': canvas.create_image(x,y,anchor="nw",image=self.I51)
        #if TType == 'Z': canvas.create_image(x,y,anchor="nw",image=self.I52)      

    def neighbors(self,gridid):
        (x,y) = gridid
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        
        #results = filter(self.in_bounds,results)
        results = filter(self.passable,results)
        
        return results

    def passable(self, gridid):
        return self.MapData[gridid] == '1' 

    def in_bounds(self, gridid):
        (x, y) = gridid
        return 0 <= x < self.width and 0 <= y < self.height

def round_down(num, divisor):
    return num - (num%divisor)
def addcords(cord1,cord2):
    x1,y1 = cord1
    x2,y2 = cord2

    x3,y3 = (x1+x2,y1+y2)

    return (x3,y3)

