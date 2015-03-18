from Worlds import *
from character import *
import os
 #on windows

class DebugWindow():
    def __init__(self,World):
        self.World = World
        window1 = Tk()
        window1.geometry('+1100+300')
        self.canvas = Canvas(window1, width=700, height=1000, bg='white')
        self.tick = 0
        
        self.canvas.pack()
        

    def update(self):
        self.tick +=1

        if self.tick == 20:
            self.tick = 0
        
            self.canvas.delete(ALL)
            
            for x in range (0,len(self.World.Characters)):
                xloc = 150 + (50*x)
                self.canvas.create_text(30,20,anchor = 'nw',text = 'Character info',fill = 'red' )
                self.canvas.create_text(xloc,20,anchor = 'nw', text = x, fill = 'red')
                self.canvas.create_text(30,35,anchor = 'nw',text = 'Player Direction :')
                self.canvas.create_text(xloc,35,anchor = 'nw',text = self.World.Characters[x].direction )
                self.canvas.create_text(30,50,anchor = 'nw',text = 'Player Location :')
                self.canvas.create_text(xloc,50,anchor = 'nw',text = self.World.Characters[x].PlayerLocation )
                self.canvas.create_text(30,65,anchor = 'nw',text = 'Grid location   :')
                self.canvas.create_text(xloc,65,anchor = 'nw',text = self.World.Characters[x].GridLocation )
                self.canvas.create_text(30,80,anchor = 'nw',text = 'vx              :')
                self.canvas.create_text(xloc,80,anchor = 'nw',text = self.World.Characters[x].vx )
                self.canvas.create_text(30,95,anchor = 'nw',text ='vy              :')
                self.canvas.create_text(xloc,95,anchor = 'nw',text = self.World.Characters[x].vy )
                self.canvas.create_text(30,110,anchor = 'nw',text ='Has Objective :')
                self.canvas.create_text(xloc,110,anchor = 'nw',text = self.World.Characters[x].HasObjective )
                self.canvas.create_text(30,125,anchor = 'nw',text ='Objective Location :')
                self.canvas.create_text(xloc,125,anchor = 'nw',text = self.World.Characters[x].ObjectiveLocation)        
                self.canvas.create_text(30,150,anchor = 'nw',text ='Next Tile :')
                self.canvas.create_text(xloc,150,anchor = 'nw',text = self.World.Characters[x].NextTile )

            p = self.World.screenlocation[0] 
            r = self.World.screenlocation[1] 

            for s in range (0,40):
                for q in range (0,25):
                    colour = 'black'
                    if (p+s,r+q) in self.World.MapData:
                        for rupee in self.World.rupees:
                            if (p+s,r+q) == rupee.location:
                                if rupee.collected == True:
                                    continue
                                self.canvas.create_text((s*10+30,q*10+230),text = '#',fill = 'yellow')
                               
                                
                        if self.World.MapData[( p+s,r+q)] == ']': colour = 'red'
                        if self.World.MapData[( p+s,r+q)] == ';': colour = 'green'
                        self.canvas.create_text((s*10+30,q*10+230),text = self.World.MapData[( p+s,r+q)],fill = colour)
            
            

            #World info
            self.canvas.create_text(30,170,anchor = 'nw',text = 'World information', fill = 'red' )
            self.canvas.create_text(30,185,anchor = 'nw',text = 'Screen Location :' )
            self.canvas.create_text(150,185,anchor = 'nw',text =  self.World.screenlocation)
            self.canvas.create_text(30,200,anchor = 'nw',text = 'Selected Character:' )
            self.canvas.create_text(150,200,anchor = 'nw',text =  self.World.Selected_Character)

            
        
