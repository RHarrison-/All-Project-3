from tkinter import *

class SwitchWall:
    def __init__(self,PLocation,SWTiles,World):
        self.World = World
        self.location = PLocation
        self.flippos = 0
        self.SWTiles = SWTiles

        self.World.MapData[self.location] = '}'
        
        for x in range(0,len(self.SWTiles)):
            self.World.MapData[self.SWTiles[x]] = ']'   
        
    def active(self):
        for x in range(0,len(self.SWTiles)):
            self.World.MapData[self.SWTiles[x]] = ';'
            x,y = self.World.ScreenCoords(self.SWTiles[x])
            x=x*16
            y=y*16
            self.World.canvas.create_image(x,y,anchor="nw",image=self.World.I71)
       
        self.flippos = 1

    def inactive(self):
        for x in range(0,len(self.SWTiles)):
            
            self.World.MapData[self.SWTiles[x]] = ']'
            x,y = self.World.ScreenCoords(self.SWTiles[x])
            x=x*16
            y=y*16
            self.World.canvas.create_image(x,y,anchor="nw",image=self.World.I70)
      
            
        self.flippos = 0 

        
        

        
        
