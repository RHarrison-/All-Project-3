from Worlds import *
from character import *
import os
 #on windows

class DebugWindow():
    def __init__(self,World):
        self.World = World
        window1 = Tk()
        window1.geometry('+1100+300')
        self.canvas = Canvas(window1, width=300, height=500, bg='white')
        
        self.canvas.pack()
        

    def update(self):
        self.canvas.delete(ALL)
        
        #characterInfo
        self.canvas.create_text(30,20,anchor = 'nw',text = 'Character info',fill = 'red' )
        self.canvas.create_text(30,35,anchor = 'nw',text = 'Player Direction :')
        self.canvas.create_text(150,35,anchor = 'nw',text = self.World.Player.direction )
        self.canvas.create_text(30,50,anchor = 'nw',text = 'Player Location :')
        self.canvas.create_text(150,50,anchor = 'nw',text = self.World.Player.PlayerLocation )
        self.canvas.create_text(30,65,anchor = 'nw',text = 'Grid location   :')
        self.canvas.create_text(150,65,anchor = 'nw',text = self.World.Player.GridLocation )
        self.canvas.create_text(30,80,anchor = 'nw',text = 'vx              :')
        self.canvas.create_text(150,80,anchor = 'nw',text = self.World.Player.vx )
        self.canvas.create_text(30,95,anchor = 'nw',text ='vy              :')
        self.canvas.create_text(150,95,anchor = 'nw',text = self.World.Player.vy )
        self.canvas.create_text(30,110,anchor = 'nw',text ='Has Objective :')
        self.canvas.create_text(150,110,anchor = 'nw',text = self.World.Player.HasObjective )
        
        
        self.canvas.create_text(30,150,anchor = 'nw',text ='Next Tile :')
        self.canvas.create_text(150,150,anchor = 'nw',text = self.World.Player.NextTile )

        p = self.World.screenlocation[0] 
        r = self.World.screenlocation[1] 

        #for s in range (0,40):
        #    for q in range (0,25):
        #        if ( p+s,r+q) in self.World.MapData: self.canvas.create_text((s*10,q*10),text = self.World.MapData[( p+s,r+q)])
        
        

        #World info
        self.canvas.create_text(30,170,anchor = 'nw',text = 'World information', fill = 'red' )
        self.canvas.create_text(30,185,anchor = 'nw',text = 'Screen Location :' )
        self.canvas.create_text(150,185,anchor = 'nw',text =  self.World.screenlocation)

        
