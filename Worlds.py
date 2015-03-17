from tkinter import *
from character import *
from Functions import *
import random
#=================== The World Generation =====================    
class squaregrid:
    def __init__ (self,canvas,canvas2):
        self.canvas = canvas
        self.canvas2 = canvas2
        self.screenwidth = 40
        self.screenheight = 25
        self.screenlocation = (0,0)
        
        self.Characters = []
        self.SwitchWalls = []
        self.Selected_Character = 0
        self.SelectedPlayerImage = ''
        self.rupeecountimage = ''
        self.rupeenumber = ''
        self.keycountimage = ''
        self.keynumber = ''
        
        self.CursorSquare = ''
        self.MapData = {}
        self.rupees = []
        self.Keys = []
        self.MousePosition = ()

        self.LandmarkList = []
        self.TreasureList = []
        self.cursorimage = PhotoImage(file = 'assets\cursor.png')
        self.cursorimageRED = PhotoImage(file = 'assets\cursorred.png')
        
        self.stoneimage = PhotoImage(file = 'assets\Stone.png')
        self.grassimage1 = PhotoImage(file = 'assets\Grass1.png')
        self.grassimage2 = PhotoImage(file = 'assets\Grass2.png')
        self.waterimage1 = PhotoImage(file = 'assets\Water1.png')
        self.waterimage2 = PhotoImage(file = 'assets\Water2.png')
        self.flowerimage = PhotoImage(file = 'assets\Flower.png')
        self.stumpimage = [[PhotoImage(file = 'assets\TLStump.png'),
                           PhotoImage(file = 'assets\BLStump.png')],
                           [PhotoImage(file = 'assets\TRStump.png'),
                           PhotoImage(file = 'assets\BRStump.png')]]
        self.I1 = PhotoImage(file = 'assets\GrassCliffN.png') #a
        self.i1 = PhotoImage(file = 'assets\TopCliffN.png')#b
        self.I2 = PhotoImage(file = 'assets\TopCliffN.png')#c
        self.I3 = PhotoImage(file = 'assets\WaterCliffN.png')#d
        self.I4 = PhotoImage(file = 'assets\WaterN.png')#e
        self.I5 = PhotoImage(file = 'assets\GrassCliffNE.png')#f
        self.I6 = PhotoImage(file = 'assets\TopCliffNE.png')#g
        self.I7 = PhotoImage(file = 'assets\MiddleCliffNE.png')#h
        self.I8 = PhotoImage(file = 'assets\WaterCliffNE.png')#i
        self.I9 = PhotoImage(file = 'assets\WaterCLiffNtoNE.png')#j
        self.I10 = PhotoImage(file = 'assets\WaterNE.png')#k
        self.I11 = PhotoImage(file = 'assets\WaterOuterNE.png')#l
        self.I12 = PhotoImage(file = 'assets\WaterOuterNE2.png')#m
        self.I13 = PhotoImage(file = 'assets\TopCliffE.png')#n
        self.I14 = PhotoImage(file = 'assets\BottomCliffE.png')#o
        self.I15 = PhotoImage(file = 'assets\WaterCliffE.png')#p
        self.I16 = PhotoImage(file = 'assets\TopCliffNW.png')#q
        self.I17 = PhotoImage(file = 'assets\CliffMiddleNW.png')#r
        self.I18 = PhotoImage(file = 'assets\CliffBottomNW.png')#s
        self.I19 = PhotoImage(file = 'assets\CliffGrassNW.png')#t
        self.I20 = PhotoImage(file = 'assets\WaterCliffNW.png') #u       
        self.I21 = PhotoImage(file = 'assets\CliffTopW.png')#v
        self.I22 = PhotoImage(file = 'assets\MiddleCliffW.png')#w
        self.I23 = PhotoImage(file = 'assets\WaterW.png')#x
        self.I24 = PhotoImage(file = 'assets\GrassCliffSW.png')#y
        self.I25 = PhotoImage(file = 'assets\TopCliffSW.png')  #z
        self.I26 = PhotoImage(file = 'assets\GrassSW.png')      #A
        self.I27 = PhotoImage(file = 'assets\BottomCliffSW.png') #B
        self.I28 = PhotoImage(file = 'assets\WaterSW.png') #C
        self.I29 = PhotoImage(file = 'assets\WaterCornerSW.png') #D
        self.I30 = PhotoImage(file = 'assets\GrassCliffS.png')#E
        self.I31 = PhotoImage(file = 'assets\TopCliffS.png') #F
        self.I32 = PhotoImage(file = 'assets\MiddleCliffS.png')#G
        self.I33 = PhotoImage(file = 'assets\BottomCliffS.png')#H
        self.I34 = PhotoImage(file = 'assets\WaterS.png')#I
        self.I35 = PhotoImage(file = 'assets\GrassSE.png')#J
        self.I36 = PhotoImage(file = 'assets\GrassCliffSE.png')#K
        self.I37 = PhotoImage(file = 'assets\TopCliffSE.png')#L
        self.I38 = PhotoImage(file = 'assets\BottomCliffSE.png')#M
        self.I39 = PhotoImage(file = 'assets\WaterCliffSE.png')#N
        self.I40 = PhotoImage(file = 'assets\CornerWaterSE.png')#O
        self.I41 = PhotoImage(file = 'assets\Tree1.png')#O
        self.I42 = PhotoImage(file = 'assets\Tree2.png')#P
        self.I43 = PhotoImage(file = 'assets\Tree3.png')#Q
        self.I44 = PhotoImage(file = 'assets\Tree4.png')#R
        self.I45 = PhotoImage(file = 'assets\Tree5.png')#S
        self.I46 = PhotoImage(file = 'assets\Tree6.png')#T
        self.I47 = PhotoImage(file = 'assets\Tree7.png')#U
        self.I48 = PhotoImage(file = 'assets\Tree8.png')#V
        self.I49 = PhotoImage(file = 'assets\Tree9.png')#W
        self.I50 = PhotoImage(file = 'assets\Tree10.png')#X
        self.I51 = PhotoImage(file = 'assets\Tree11.png')#Y
        self.I52 = PhotoImage(file = 'assets\Tree12.png')#Z
        self.I53 = PhotoImage(file = 'assets\Tree13.png')#!
        self.I54 = PhotoImage(file = 'assets\Tree14.png')#"
        self.I55 = PhotoImage(file = 'assets\Tree15.png')#£
        self.I56 = PhotoImage(file = 'assets\Tree16.png')#$
        self.I57 = PhotoImage(file = 'assets\Tree17.png')#%
        self.I58 = PhotoImage(file = 'assets\Tree18.png')#^
        self.I59 = PhotoImage(file = 'assets\Tree19.png')#&
        self.I60 = PhotoImage(file = 'assets\Tree20.png')#*
        self.I61 = PhotoImage(file = 'assets\HorozontalFence.png')#(
        self.I62 = PhotoImage(file = 'assets\VerticleFenceLeft.png')#)
        self.I63 = PhotoImage(file = 'assets\VerticleFenceRight.png')#-
        self.I64 = PhotoImage(file = 'assets\BottomGrassCliff.png')#_
        self.I65 = PhotoImage(file = 'assets\GrassGrassCliffSW.png')#=
        self.I66 = PhotoImage(file = 'assets\GrassGrassCliffSE.png')#+
        self.I67 = PhotoImage(file = 'assets\StepsLeft.png')#[
        self.I68 = PhotoImage(file = 'assets\StepsRight.png')#{
        self.I69 = PhotoImage(file = 'assets\PressurePlate.png')#}
        self.I70 = PhotoImage(file = 'assets\WallUP.png')#]
        self.I71 = PhotoImage(file = 'assets\WallDOWN.png')#;
        self.I72 = PhotoImage(file = 'assets/rupeeRED.png')#:
        self.I73 = PhotoImage(file = 'assets/rupeeBLUE.png')#@
        self.I74 = PhotoImage(file = 'assets/rupeeGREEN.png')##
        self.I75 = PhotoImage(file = 'assets/Path.png')#~
        self.I76 = PhotoImage(file = 'assets/PinkFlower.png')#,
        self.I77 = PhotoImage(file = 'assets/HorizontalPath1.png')#<
        self.I78 = PhotoImage(file = 'assets/HorizontalPath2.png')#.
        self.I79 = PhotoImage(file = 'assets/ZeldaCage.png')#>
        self.I80 = PhotoImage(file = 'assets/Key.png')#/

    def MapDataCoords(self,gridid): #pass grid coords, not canvas coords.
        x,y = gridid
        p,q = self.screenlocation
        gridid = (x+p,y+q)

        return gridid

    def ScreenCoords(self,gridid):
        x,y = gridid
        p,q = self.screenlocation
        gridid = (x-p,y-q)

        return gridid

    def ShowCursor(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)
        x=x//16
        y=y//16
        gridid = self.MapDataCoords((x,y))
        
        self.canvas.delete(self.CursorSquare)
        
        if self.MapData[gridid] == '1' or self.MapData[gridid] == '[' or self.MapData[gridid] ==  '{' or self.MapData[gridid] ==  '}' or self.MapData[gridid] ==  ';' or self.MapData[gridid] ==  ':' or self.MapData[gridid] == '@' or self.MapData[gridid] == '#' or self.MapData[gridid] == '~' or self.MapData[gridid] == '<' or self.MapData[gridid] == '.' :
            Image = self.cursorimage
        else:
            Image = self.cursorimageRED

        x=x*16
        y=y*16
            
        self.CursorSquare = self.canvas.create_image(x,y,anchor = 'nw',image = Image)
        
    def SpawnCharacter(self,location,character):
        x,y = location
        self.Characters.append(character(self.canvas))
        self.Characters[len(self.Characters)-1].GridLocation = (x,y)
        x=x*16
        y=y*16
        self.Characters[len(self.Characters)-1].PlayerLocation = (x,y)
        self.Characters[len(self.Characters)-1].PlayerSquare = self.canvas.create_image(x,y,anchor = 'nw',image = self.Characters[len(self.Characters)-1].PlayerImage)

    def Animate(self):
        pass

    def MoveScreen(self,c):
        self.canvas.delete(ALL)
        moveam = 0
        if self.Characters[c].direction == 'right': movam = (40,0)
        if self.Characters[c].direction == 'left': movam = (-40,0)
        if self.Characters[c].direction == 'up': movam = (0,-25)
        if self.Characters[c].direction == 'down': movam = (0,25)

        self.screenlocation = (addcords(self.screenlocation,movam))
        
        p = self.screenlocation[0] 
        r = self.screenlocation[1]
        
        for s in range (0,40):
            for q in range (0,25):
                if ( p+s,r+q) in self.MapData: (self.drawtile((s,q),self.MapData[( p+s,r+q)]))

        for rupee in self.rupees:
            if rupee.collected == False:
                l,k = rupee.location
                x,y = self.screenlocation               
                
                if l > x and l < x+40:
                    if k > y and k < y+25:
                        rupee.draw()

        for key in self.Keys:
            if key.collected == False:
                l,k = key.location
                x,y = self.screenlocation               
                
                if l > x and l < x+40:
                    if k > y and k < y+25:
                        key.draw()

        x,y = self.Characters[c].GridLocation
        
        if self.Characters[c].direction == 'right':
            self.Characters[c].GridLocation = (0,y)
            direction = 'right'
        if self.Characters[c].direction == 'left':
            self.Characters[c].GridLocation = (self.screenwidth-1,y)
            direction = 'left'
        if self.Characters[c].direction == 'up':
            self.Characters[c].GridLocation = (x,self.screenheight-1)
            direction = 'up'
        if self.Characters[c].direction == 'down':
            self.Characters[c].GridLocation = (x,1)
            direction = 'down'

        for q in range (0,len(self.Characters)):

            x,y = self.Characters[c].GridLocation

            self.Characters[q].GridLocation = (x,y)
        
            x=x*16
            y=y*16

            self.Characters[q].PlayerLocation = (x,y)
            self.Characters[q].NextTile = (0,0)
            self.Characters[q].HasObjective = False
            self.Characters[q].direction = direction
        
            self.Characters[q].PlayerSquare = self.canvas.create_image(x,y,anchor = 'nw',image = self.Characters[q].PlayerImage)
              

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

    def neighbors(self,gridid):
        (x,y) = gridid
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        
        results = filter(self.in_bounds,results)
        results = filter(self.passable,results)

        
        return results

    def passable(self, gridid):
        x,y = gridid
        gridid = self.MapDataCoords(gridid)
        return self.MapData[gridid] == '1' or self.MapData[gridid] == '[' or self.MapData[gridid] ==  '{' or self.MapData[gridid] ==  '}' or self.MapData[gridid] ==  ';' or self.MapData[gridid] ==  ':' or self.MapData[gridid] == '@' or self.MapData[gridid] == '#' or self.MapData[gridid] == '~' or self.MapData[gridid] == '<' or self.MapData[gridid] == '.'
    

    def in_bounds(self, gridid):
        x,y = gridid
        return 0 <= x < self.screenwidth and 0 <= y < self.screenheight

    def FindPlayerPath(self,gridid):
        MovementGrid = self.FindPath(self.Characters[self.Selected_Character].GridLocation,gridid)
        
        CPath = self.ReconstructPath(MovementGrid,self.Characters[self.Selected_Character].GridLocation,gridid)
        CPath.reverse()
        self.Characters[self.Selected_Character].HasObjective = True
        self.Characters[self.Selected_Character].Path = CPath

    def ClosestPath(self,startpoint):
        MovementGrid = self.FindPath(self.Characters[self.Selected_Character].GridLocation,startpoint)
        self.Characters[self.Selected_Character].ObjectiveLocation = (startpoint)
        frontier = Queue()
        frontier.put(startpoint)
        came_from = []
        x=0
        
        while not frontier.empty():
            current = frontier.get()
            if current in MovementGrid:
                break
            x,y = current
            neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for next in neighbors:
                if next not in came_from:
                    frontier.put(next)
                    came_from.append(current)

                    
        self.FindPlayerPath(current)     

    def CheckScreenEdge(self):
        for c in range(len(self.Characters)):
            x,y = self.Characters[c].GridLocation
            
            if x == 0 and self.Characters[c].direction == 'left':
                self.MoveScreen(c) 
            if x == self.screenwidth-1 and self.Characters[c].direction == 'right':
                self.MoveScreen(c)
            if y == 0 and self.Characters[c].direction == 'up':
                self.MoveScreen(c)
            if y == self.screenheight-1 and self.Characters[c].direction == 'down':
                self.MoveScreen(c)
            
    def Click(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)

        x=x//16
        y=y//16

        if (x,y) not in self.MapData: return 
        
        gridid = self.MapDataCoords((x,y))
        
        self.ClosestPath(self.ScreenCoords(gridid))

    def Rclick(self,event):
        if self.Characters[self.Selected_Character].name == 'Link':
            pass           

        if self.Characters[self.Selected_Character].name == 'Zelda':
            pass            
        
    def Key(self,event):
         pass

    def MouseWheel(self,event): #Changing between characters.
        if event.delta == 120:
             self.Selected_Character -=1
    
        if event.delta == -120:
             self.Selected_Character +=1
        

        if self.Selected_Character == len(self.Characters):
             self.Selected_Character = 0
        if self.Selected_Character == -1:
            self.Selected_Character = len(self.Characters)-1

        self.SelectedPlayerImage = PhotoImage(file= self.Characters[self.Selected_Character].DirectionImages['down'][0])
        self.canvas2.create_image(8,8,anchor = 'nw', image = self.SelectedPlayerImage)
        self.canvas2.create_rectangle(4,4,28,28,outline = 'Green', width = 2)
                
    def RightClick(self):
        pass

    def LeftKey(self,event):
        pass        

    def RightKey(self,event):
        pass

    def UpKey(self,event):
        pass

    def DownKey(self,event):
        pass            
        
    def drawgrid(self):
        
        p = self.screenlocation[0] 
        r = self.screenlocation[1] 

        for s in range (0,40):
            for q in range (0,25):
                if ( p+s,r+q) in self.MapData: (self.drawtile((s,q),self.MapData[( p+s,r+q)]))

    def drawtile(self,gridid,TType):
        
        x,y = gridid        
        x = (x*16)
        y = (y*16)

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
        if TType == '4': self.canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][0])
        if TType == '5': self.canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][0])
        if TType == '6': self.canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][1])
        if TType == '7': self.canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][1])
        if TType == '8': self.canvas.create_image(x,y,anchor="nw",image=self.flowerimage)
        
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
        if TType == 'z': self.canvas.create_image(x,y,anchor="nw",image=self.I26)
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
        if TType == 'O': self.canvas.create_image(x,y,anchor="nw",image=self.I41)
        if TType == 'P': self.canvas.create_image(x,y,anchor="nw",image=self.I42)
        if TType == 'Q': self.canvas.create_image(x,y,anchor="nw",image=self.I43)
        if TType == 'R': self.canvas.create_image(x,y,anchor="nw",image=self.I44)
        if TType == 'S': self.canvas.create_image(x,y,anchor="nw",image=self.I45)
        if TType == 'T': self.canvas.create_image(x,y,anchor="nw",image=self.I46)
        if TType == 'U': self.canvas.create_image(x,y,anchor="nw",image=self.I47)
        if TType == 'V': self.canvas.create_image(x,y,anchor="nw",image=self.I48)
        if TType == 'W': self.canvas.create_image(x,y,anchor="nw",image=self.I49)
        if TType == 'X': self.canvas.create_image(x,y,anchor="nw",image=self.I50)
        if TType == 'Y': self.canvas.create_image(x,y,anchor="nw",image=self.I51)
        if TType == 'Z': self.canvas.create_image(x,y,anchor="nw",image=self.I52)
        if TType == '!': self.canvas.create_image(x,y,anchor="nw",image=self.I53)
        if TType == '"': self.canvas.create_image(x,y,anchor="nw",image=self.I54)
        if TType == '£': self.canvas.create_image(x,y,anchor="nw",image=self.I55)
        if TType == '$': self.canvas.create_image(x,y,anchor="nw",image=self.I56)
        if TType == '%': self.canvas.create_image(x,y,anchor="nw",image=self.I57)
        if TType == '^': self.canvas.create_image(x,y,anchor="nw",image=self.I58)
        if TType == '&': self.canvas.create_image(x,y,anchor="nw",image=self.I59)
        if TType == '*': self.canvas.create_image(x,y,anchor="nw",image=self.I60)
        if TType == '(': self.canvas.create_image(x,y,anchor="nw",image=self.I61)
        if TType == ')': self.canvas.create_image(x,y,anchor="nw",image=self.I62)
        if TType == '-': self.canvas.create_image(x,y,anchor="nw",image=self.I63)
        if TType == '_': self.canvas.create_image(x,y,anchor="nw",image=self.I64)
        if TType == '=': self.canvas.create_image(x,y,anchor="nw",image=self.I65)
        if TType == '+': self.canvas.create_image(x,y,anchor="nw",image=self.I66)
        if TType == '[': self.canvas.create_image(x,y,anchor="nw",image=self.I67)
        if TType == '{': self.canvas.create_image(x,y,anchor="nw",image=self.I68)
        if TType == '}': self.canvas.create_image(x,y,anchor="nw",image=self.I69)
        if TType == ']': self.canvas.create_image(x,y,anchor="nw",image=self.I70)
        if TType == ';': self.canvas.create_image(x,y,anchor="nw",image=self.I71)
        if TType == ':': self.canvas.create_image(x,y,anchor="nw",image=self.I72)
        if TType == '@': self.canvas.create_image(x,y,anchor="nw",image=self.I73)
        if TType == '#': self.canvas.create_image(x,y,anchor="nw",image=self.I74)
        if TType == '~': self.canvas.create_image(x,y,anchor="nw",image=self.I75)
        if TType == ',': self.canvas.create_image(x,y,anchor="nw",image=self.I76)
        if TType == '<': self.canvas.create_image(x,y,anchor="nw",image=self.I77)
        if TType == '.': self.canvas.create_image(x,y,anchor="nw",image=self.I78)
        if TType == '>': self.canvas.create_image(x,y,anchor="nw",image=self.I79)
        if TType == '/': self.canvas.create_image(x,y,anchor="nw",image=self.I80)
        
def round_down(num, divisor):
    return num - (num%divisor)

def addcords(cord1,cord2):
    x1,y1 = cord1
    x2,y2 = cord2

    x3,y3 = (x1+x2,y1+y2)

    return (x3,y3)
