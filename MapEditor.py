from tkinter import *
import random


import tkinter.filedialog as tkfd

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.canvas_Tiles = ''
        self.TType = 'Grass Tile'
        self.TNum = '1'
        self.x = 0
        self.y = 0
        self.grassimage1 = PhotoImage(file = 'Graphics\Grass1.png')
        self.grassimage2 = PhotoImage(file = 'Graphics\Grass2.png')
        self.waterimage1 = PhotoImage(file = 'Graphics\Water1.png')
        self.waterimage2 = PhotoImage(file = 'Graphics\Water2.png')
        self.stoneimage = PhotoImage(file = 'Graphics\Stone.png')
        self.flowerimage = PhotoImage(file = 'Graphics\Flower.png')
        self.stumpimage = [[PhotoImage(file = 'Graphics\TLStump.png'),
                           PhotoImage(file = 'Graphics\BLStump.png')],
                           [PhotoImage(file = 'Graphics\TRStump.png'),
                           PhotoImage(file = 'Graphics\BRStump.png')]]

        self.a = PhotoImage(file = 'Graphics\GrassCliffN.png')
        self.b = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.c = PhotoImage(file = 'Graphics\WaterCliffN.png')
        self.d = PhotoImage(file = 'Graphics\WaterN.png')
        
        self.e = PhotoImage(file = 'Graphics\GrassCliffNE.png')
        self.f = PhotoImage(file = 'Graphics\TopCliffNE.png')
        self.g = PhotoImage(file = 'Graphics\MiddleCliffNE.png')
        self.h = PhotoImage(file = 'Graphics\WaterCliffNE.png')
        self.i = PhotoImage(file = 'Graphics\WaterCLiffNtoNE.png')
        self.j = PhotoImage(file = 'Graphics\WaterNE.png')
        self.k = PhotoImage(file = 'Graphics\WaterOuterNE.png')
        self.l = PhotoImage(file = 'Graphics\WaterOuterNE2.png')

        self.m = PhotoImage(file = 'Graphics\TopCliffE.png')
        self.n = PhotoImage(file = 'Graphics\BottomCliffE.png')
        self.o = PhotoImage(file = 'Graphics\WaterCliffE.png')

        #self.LSE1 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        #self.LSE2 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        #self.LSE3 = PhotoImage(file = 'Graphics\WaterCliffE.png')

        #self.LS1 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        #self.LS2 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        #self.LS3 = PhotoImage(file = 'Graphics\WaterCliffE.png')

        #self.LWSW1 = PhotoImage(file = 'Graphics\TopCliffSW.png')
        #self.LWSW2 = PhotoImage(file = 'Graphics\BottomCliffSW.png')
        #self.LWSW3 = PhotoImage(file = 'Graphics\WaterCliffSW.png')
        
        #self.LWW1 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        #self.LWW2 = PhotoImage(file = 'Graphics\WaterCliffE.png')
        #self.LWW2 = PhotoImage(file = 'Graphics\WaterCliffE.png')
         
        #self.LWTCNW = PhotoImage(file = 'Graphics\TopCliffNW.png')
        #self.LWBCNW = PhotoImage(file = 'Graphics\BottomCliffNW.png')
        #self.LWWCNW = PhotoImage(file = 'Graphics\WaterCliffNW.png')
        

        
        self.binds = {'1':'1','2':'2','3':'3',
                      '4':'a','5':'b','6':'c','7':'d','8':'e','9':'f',
                      '10':'g','11':'h','12':'i','13':'j','14':'k','15':'l',
                      '16':'m','17':'n','18':'o',
                      '19':'','20':'21','22':'23','24':'25','26':'27','28':'28'}
                      
        self.TileWindow = {}
        self.MapData = {}
        self.MapExport = []
        self.MapName = ''
        self.rotation = 0

    def openfile(self):
        
        filename = tkfd.askopenfilename()
        
        file = open(filename,'r')
        
        p=0
        
        for line in file:
            p = p+1
            t = len(line)

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
                        self.draw(self.canvas_Tiles,self.TType,x*16,y*16)

    def reset(self):
        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,'Grass Tile',x,y)

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
               print(item)
        
    def draw(self,canvas,TType,x,y):
                
        if TType == '1':
            rand = random.randint(1, 100)
            if rand <95:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
            elif rand >=95:
                canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
 
 
        if TType == '2':
            rand = random.randint(1, 100)
            if rand <80:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand  >=80:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage2)

        if TType == '3': canvas.create_image(x,y,anchor="nw",image=self.stoneimage)
        if TType == '28': canvas.create_image(x,y,anchor="nw",image=self.flowerimage)

    

        if TType == 'a': canvas.create_image(x,y,anchor="nw",image=self.a)
        if TType == 'b': canvas.create_image(x,y,anchor="nw",image=self.b)
        if TType == 'c': canvas.create_image(x,y,anchor="nw",image=self.c)
        if TType == 'd': canvas.create_image(x,y,anchor="nw",image=self.d)
        
        if TType == 'e': canvas.create_image(x,y,anchor="nw",image=self.e)
        if TType == 'f': canvas.create_image(x,y,anchor="nw",image=self.f)
        if TType == 'g': canvas.create_image(x,y,anchor="nw",image=self.g)
        if TType == 'h': canvas.create_image(x,y,anchor="nw",image=self.h)
        if TType == 'i': canvas.create_image(x,y,anchor="nw",image=self.i)
        if TType == 'j': canvas.create_image(x,y,anchor="nw",image=self.j)
        if TType == 'k': canvas.create_image(x,y,anchor="nw",image=self.k)
        if TType == 'l': canvas.create_image(x,y,anchor="nw",image=self.l)

        if TType == 'm': canvas.create_image(x,y,anchor="nw",image=self.m)
        if TType == 'n': canvas.create_image(x,y,anchor="nw",image=self.n)
        if TType == 'o': canvas.create_image(x,y,anchor="nw",image=self.o)
        
        self.MapData[(y//16,x//16)] = self.TType
          

    def Click(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)
        self.draw(self.canvas,self.TType,x,y)

    def TClick(self,event):

        x=(round_down(event.x,16))//16
        y=(round_down(event.y,16))//16
        
        Tile = self.TileWindow[(x,y)]

        if not Tile:
            return

        print(Tile)
       
        self.TType = Tile
        
    def Key(self,event):
        
        if event.char.isdigit() == True:            
            self.TType = self.binds[event.char]
            self.TNum = event.char
        else:
                
            if event.char == 'p':
                print(self.MapData)
                
            if event.char == 's':
                self.savemap()
                
            if event.char == 'n':
                self.reset()

            if event.char == 'r':
                self.rotation +=1
                if self.rotation ==8: self.rotation = 0
                    

    def create(self,x,y):

        self.x = x
        self.y = y
    
        height = y*16
        width = x*16

        
        self.canvas = Canvas(self.window,width=width-2, height=height-2, bg='white')
        self.canvas_Tiles = Canvas(self.window,width=500, height=height, bg='white')

        self.canvas.grid(row = 0,column = 0)
        self.canvas_Tiles.grid(row = 0,column =1,rowspan=2)

        self.canvas.bind('<Button-1>',self.Click)
        self.canvas.bind('<B1-Motion>',self.Click)
        self.canvas_Tiles.bind('<Button-1>',self.TClick)
        self.window.bind_all('<Key>',self.Key)
        q=0
        with open('TilesforUse.txt','r') as f:
            for line in f:
                q+=1
                x=0
                for char in line:
                    if char =='\n': continue
                    x+=1
                    self.TType = char
                    self.draw(self.canvas_Tiles,self.TType,x*16,q*16)
                    self.TileWindow[(x,q)] = char
        print(self.TileWindow)
                    
                    
        self.TType = '1'

        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,self.TType,x*16,y*16)

        #self.canvas_Tiles.create_rectangle(2,2,25,height-1)
               
def round_down(num, divisor):
    return num - (num%divisor)


def something():
    surface1 = surface()
    surface1.create(25,20)
    #surface1.openfile()    
    surface1.window.mainloop()
    
something()

