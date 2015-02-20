from tkinter import *
import random
#=================== The World Generation =====================    
class squaregrid:
    def __init__ (self,canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.walls = []
        self.wallimage = PhotoImage(file = 'Graphics\stone.gif')
        self.wood = []
        self.woodimage = PhotoImage(file = 'Graphics\Wood.gif')
        self.grass = []
        self.grassimage1 = PhotoImage(file = 'Graphics\Grass1.gif')
        self.grassimage2 = PhotoImage(file = 'Graphics\Grass2.gif')
        self.grassimage3 = PhotoImage(file = 'Graphics\Grass3.gif')
        self.lava= []
        self.lavaimage1 = PhotoImage(file = 'Graphics\Lava1.gif')
        self.lavaimage2 = PhotoImage(file = 'Graphics\Lava2.gif')
        self.lavaimage3 = PhotoImage(file = 'Graphics\Lava3.gif')
        self.sand = []
        self.sandimage1 = PhotoImage(file = 'Graphics\Sand1.gif')
        self.sandimage2 = PhotoImage(file = 'Graphics\Sand2.gif')
        self.sandimage3 = PhotoImage(file = 'Graphics\Sand3.gif')
        self.water = []
        self.waterimage1 = PhotoImage(file = 'Graphics\Water1.gif')
        self.waterimage2 = PhotoImage(file = 'Graphics\Water2.gif')
        self.waterimage3 = PhotoImage(file = 'Graphics\Water3.gif')
        self.rocks = []
        self.rockimage1 = PhotoImage(file = 'Graphics\Rocks1.gif')
        self.rockimage2 = PhotoImage(file = 'Graphics\Rocks2.gif')
        self.rockimage3 = PhotoImage(file = 'Graphics\Rocks3.gif')
        
        self.TrafficLightList = []
        self.RobotList = []

    def drawgrid(self):
        for y in range(self.height+1):
            for x in range(self.width+1):
                TType = self.draw_tile((x,y))
                self.drawtile((x,y),TType)

    def drawtile(self,gridid,TType):
        x,y = gridid
        
        x = x*16
        y = y*16
        
        if TType == 'Wood Tile': self.canvas.create_image(x,y,anchor="nw",image=self.woodimage)
        if TType == 'Wall Tile': self.canvas.create_image(x,y,anchor="nw",image=self.wallimage)
        
        if TType == 'Grass Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                self.canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
            elif rand == 2:
                self.canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
            elif rand == 3:
                self.canvas.create_image(x,y,anchor="nw",image=self.grassimage3)
        if TType == 'Sand Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                self.canvas.create_image(x,y,anchor="nw",image=self.sandimage1)
            elif rand == 2:
                self.canvas.create_image(x,y,anchor="nw",image=self.sandimage2)
            elif rand == 3:
                self.canvas.create_image(x,y,anchor="nw",image=self.sandimage3)
        if TType == 'Water Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand == 2:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage2)
            elif rand == 3:
                self.canvas.create_image(x,y,anchor="nw",image=self.waterimage3)
        if TType == 'Lava Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                self.canvas.create_image(x,y,anchor="nw",image=self.lavaimage1)
            elif rand == 2:
                self.canvas.create_image(x,y,anchor="nw",image=self.lavaimage2)
            elif rand == 3:
                self.canvas.create_image(x,y,anchor="nw",image=self.lavaimage3)
        if TType == 'Rock Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                self.canvas.create_image(x,y,anchor="nw",image=self.rockimage1)
            elif rand == 2:
                self.canvas.create_image(x,y,anchor="nw",image=self.rockimage2)
            elif rand == 3:
                self.canvas.create_image(x,y,anchor="nw",image=self.rockimage3)

        #print ((x,y), TType)

    def draw_tile(self,gridid):

        r = ''
    
        if gridid in self.walls: r = 'Wall Tile'
        if gridid in self.wood: r = 'Wood Tile'
        if gridid in self.grass: r = 'Grass Tile'
        if gridid in self.water: r = 'Water Tile'
        if gridid in self.lava: r = 'Lava Tile'
        if gridid in self.sand: r = 'Sand Tile'
        if gridid in self.rocks: r = 'Rock Tile'
    
        return r

    def neighbors(self,gridid):
        (x,y) = gridid
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.passable,results)
        results = filter(self.in_bounds,results)
        return results

    def passable(self, gridid):
       return gridid not in self.walls and gridid not in self.wood and gridid not in self.water and gridid not in self.lava and gridid not in self.rocks

    def in_bounds(self, gridid):
        (x, y) = gridid
        return 0 <= x < self.width and 0 <= y < self.height

