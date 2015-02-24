from tkinter import *
import random


import tkinter.filedialog as tkfd

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.canvas_Tiles = ''
        self.TType = '1'
        self.TNum = '1'
        self.x = 0
        self.y = 0
        self.TileWindow = {}
        self.MapData = {}
        self.MapExport = []
        self.MapName = ''
        self.rotation = 0
        
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

        self.I1 = PhotoImage(file = 'Graphics\GrassCliffN.png')
        self.i1 = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.I2 = PhotoImage(file = 'Graphics\TopCliffN.png')
        self.I3 = PhotoImage(file = 'Graphics\WaterCliffN.png')
        self.I4 = PhotoImage(file = 'Graphics\WaterN.png')
        
        self.I5 = PhotoImage(file = 'Graphics\GrassCliffNE.png')
        self.I6 = PhotoImage(file = 'Graphics\TopCliffNE.png')
        self.I7 = PhotoImage(file = 'Graphics\MiddleCliffNE.png')
        self.I8= PhotoImage(file = 'Graphics\WaterCliffNE.png')
        self.I9 = PhotoImage(file = 'Graphics\WaterCLiffNtoNE.png')
        self.I10 = PhotoImage(file = 'Graphics\WaterNE.png')
        self.I11 = PhotoImage(file = 'Graphics\WaterOuterNE.png')
        self.I12 = PhotoImage(file = 'Graphics\WaterOuterNE2.png')

        self.I13 = PhotoImage(file = 'Graphics\TopCliffE.png')
        self.I14 = PhotoImage(file = 'Graphics\BottomCliffE.png')
        self.I15 = PhotoImage(file = 'Graphics\WaterCliffE.png')

        #self.I16 = PhotoImage(file = 'Graphics\.png') p
        #self.I17 = PhotoImage(file = 'Graphics\.png') q
        #self.I18 = PhotoImage(file = 'Graphics\.png') r

        #self.I19 = PhotoImage(file = 'Graphics\.png') s
        #self.I20 = PhotoImage(file = 'Graphics\.png') t
        #self.I21 = PhotoImage(file = 'Graphics\.png') u

        #self.I22 = PhotoImage(file = 'Graphics\.png') v
        #self.I23 = PhotoImage(file = 'Graphics\.png') w
        #self.I24 = PhotoImage(file = 'Graphics\.png') x

        #self.I25 = PhotoImage(file = 'Graphics\.png') y 
        #self.I26 = PhotoImage(file = 'Graphics\.png') z
        #self.I27 = PhotoImage(file = 'Graphics\.png') A
         
        #self.I28 = PhotoImage(file = 'Graphics\.png') B
        #self.I29 = PhotoImage(file = 'Graphics\.png') C 
        #self.I30 = PhotoImage(file = 'Graphics\.png') D
                      
        

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
                    self.TType = char
                    self.draw(self.canvas,self.TType,x*16,y*16)

    def reset(self):
        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,'1',x*16,y*16)

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
        if TType == '4': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][self.rotation])
        if TType == '5': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][self.rotation])
        if TType == '6': canvas.create_image(x,y,anchor="nw",image=self.flowerimage)


        if TType == 'a': canvas.create_image(x,y,anchor="nw",image=self.I1)
        if TType == 'b': canvas.create_image(x,y,anchor="nw",image=self.I2)
        if TType == 'c': canvas.create_image(x,y,anchor="nw",image=self.I3)
        if TType == 'd': canvas.create_image(x,y,anchor="nw",image=self.I4)
        
        if TType == 'e': canvas.create_image(x,y,anchor="nw",image=self.I5)
        if TType == 'f': canvas.create_image(x,y,anchor="nw",image=self.I6)
        if TType == 'g': canvas.create_image(x,y,anchor="nw",image=self.I7)
        if TType == 'h': canvas.create_image(x,y,anchor="nw",image=self.I8)
        if TType == 'i': canvas.create_image(x,y,anchor="nw",image=self.I9)
        if TType == 'j': canvas.create_image(x,y,anchor="nw",image=self.I10)
        if TType == 'k': canvas.create_image(x,y,anchor="nw",image=self.I11)
        if TType == 'l': canvas.create_image(x,y,anchor="nw",image=self.I12)

        if TType == 'm': canvas.create_image(x,y,anchor="nw",image=self.I13)
        if TType == 'n': canvas.create_image(x,y,anchor="nw",image=self.I14)
        if TType == 'o': canvas.create_image(x,y,anchor="nw",image=self.I15)
        
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
            self.TType = event.char
        else:
                
            if event.char == 'p':
                print(self.MapData)
                
            if event.char == 's':
                self.savemap()
                
            if event.char == 'n':
                self.reset()

            if event.char == 'r':
                self.rotation +=1
                if self.rotation ==2: self.rotation = 0
                    

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
    surface1.create(25,25)
    #surface1.openfile()    
    surface1.window.mainloop()
    
something()

