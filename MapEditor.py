from tkinter import *
import random

import tkinter.filedialog as tkfd

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.canvas_Tiles = ''
        self.TType = 'Grass Tile'
        self.TNum = 1
        self.x = 0
        self.y = 0
        self.wallimage = PhotoImage(file = 'Graphics\Stone.gif')
        self.woodimage = PhotoImage(file = 'Graphics\Wood.gif')
        self.grassimage1 = PhotoImage(file = 'Graphics\Grass1.gif')
        self.grassimage2 = PhotoImage(file = 'Graphics\Grass2.gif')
        self.grassimage3 = PhotoImage(file = 'Graphics\Grass3.gif')
        self.lavaimage1 = PhotoImage(file = 'Graphics\Lava1.gif')
        self.lavaimage2 = PhotoImage(file = 'Graphics\Lava2.gif')
        self.lavaimage3 = PhotoImage(file = 'Graphics\Lava3.gif')
        self.sandimage1 = PhotoImage(file = 'Graphics\Sand1.gif')
        self.sandimage2 = PhotoImage(file = 'Graphics\Sand2.gif')
        self.sandimage3 = PhotoImage(file = 'Graphics\Sand3.gif')
        self.waterimage1 = PhotoImage(file = 'Graphics\Water1.gif')
        self.waterimage2 = PhotoImage(file = 'Graphics\Water2.gif')
        self.waterimage3 = PhotoImage(file = 'Graphics\Water3.gif')
        self.rockimage1 = PhotoImage(file = 'Graphics\Rocks1.gif')
        self.rockimage2 = PhotoImage(file = 'Graphics\Rocks2.gif')
        self.rockimage3 = PhotoImage(file = 'Graphics\Rocks3.gif')
        
        self.binds = {'1':'Grass Tile', '2':'Water Tile',
                      '3':'Wood Tile','4':'Wall Tile',
                      '5':'Rock Tile', '6':'Sand Tile',
                      '7':'Lava Tile'}
        self.MapData = {}
        self.MapExport = []
        self.MapName = ''

    def openfile(self):
        
        filename = tkfd.askopenfilename()
        
        file = open(filename,'r')
        
        p=0
        
        for line in file:
            p = p+1
            t = len(line)

        print(t,p)
        self.create(t,p)
        
        file.close()
         
        y=0
        
        with open(filename,'r') as f:
            for line in f:
                y+=1
                x=0
                for char in line:
                    x+=1
                    if char.isdigit() == True:
                        self.TType = self.binds[char]
                        self.draw(self.canvas,self.TType,x*10,y*10)

    def reset(self):
        self.TType = 'Grass Tile'
        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,self.TType,x*16,y*16)

    def savemap(self):
        self.MapExport.clear()
        for x in range (0,self.y):
            for y in range (0,self.x):
                self.MapExport.append(self.MapData[(x,y)])

        self.MapName = tkfd.asksaveasfile(mode = 'w', defaultextension=".txt")
        if self.MapName is None:
            return #stops trying to save the map if user presses cancel
        
        p = 0
        for item in self.MapExport:
            p+=1
            if p == self.x:
                self.MapName.write(str(item) + '\n')
                p = 0
            else:
               self.MapName.write(str(item))
        
    def draw(self,canvas,TType,x,y):
        
        if TType == 'Wood Tile': canvas.create_image(x,y,anchor="nw",image=self.woodimage)
        if TType == 'Wall Tile': canvas.create_image(x,y,anchor="nw",image=self.wallimage)
        
        if TType == 'Grass Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
            elif rand == 2:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
            elif rand == 3:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage3)
        if TType == 'Sand Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                canvas.create_image(x,y,anchor="nw",image=self.sandimage1)
            elif rand == 2:
                canvas.create_image(x,y,anchor="nw",image=self.sandimage2)
            elif rand == 3:
                canvas.create_image(x,y,anchor="nw",image=self.sandimage3)
        if TType == 'Water Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand == 2:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage2)
            elif rand == 3:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage3)
        if TType == 'Lava Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                canvas.create_image(x,y,anchor="nw",image=self.lavaimage1)
            elif rand == 2:
                canvas.create_image(x,y,anchor="nw",image=self.lavaimage2)
            elif rand == 3:
                canvas.create_image(x,y,anchor="nw",image=self.lavaimage3)
        if TType == 'Rock Tile':
            rand = random.randint(1, 3)
            if rand == 1:
                canvas.create_image(x,y,anchor="nw",image=self.rockimage1)
            elif rand == 2:
                canvas.create_image(x,y,anchor="nw",image=self.rockimage2)
            elif rand == 3:
                canvas.create_image(x,y,anchor="nw",image=self.rockimage3)
                

        mx,my = self.x *16,self.y*16
        
        if x>=0 and x <= mx and y>=0 and y <= my:
            self.MapData[(y//16,x//16)] = self.TNum

    def Click(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)
        self.draw(self.canvas,self.TType,x,y)
   
        
    def Key(self,event):
        
        if event.char.isdigit() == True:            
            self.TType = self.binds[event.char]
            self.TNum = event.char
        else:
                
            if event.char == 'p':
                print(self.MapData)
                
            if event.char == 's':
                self.savemap()
                
            if event.char == 'r':
                self.reset()

    def create(self,x,y):

        self.x = x
        self.y = y
    
        height = y*16
        width = x*16

        
        self.canvas = Canvas(self.window,width=width-2, height=height-2, bg='white')
        self.canvas_Tiles = Canvas(self.window,width=24, height=height, bg='white')

        self.canvas_Tiles.create_rectangle(2,2,23,height-1)

        self.canvas.grid(row = 0,column = 0)
        self.canvas_Tiles.grid(row = 0,column =1,rowspan=2)

        self.canvas.bind('<Button-1>',self.Click)
        self.canvas.bind('<B1-Motion>',self.Click)
        self.window.bind_all('<Key>',self.Key)

        for x in range (1,len(self.binds)+1):
            y = str(x)
            self.draw(self.canvas_Tiles,self.binds[y],5,1 + (20*x))

        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,self.TType,x*16,y*16)

        
def round_down(num, divisor):
    return num - (num%divisor)


def something():
    surface1 = surface()
    surface1.create(60,40)
    #surface1.openfile()    
    surface1.window.mainloop()
    
something()

