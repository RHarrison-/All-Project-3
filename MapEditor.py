from tkinter import *

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.canvas_Tiles = ''
        self.TType = 'Grass Tile'
        self.TNum = 1
        self.x = 0
        self.y = 0
        self.wallimage = PhotoImage(file = 'Graphics\Wall.gif')
        self.treeimage = PhotoImage(file = 'Graphics\Tree.gif')
        self.grassimage = PhotoImage(file = 'Graphics\Grass.gif')
        self.binds = {'1':'Grass Tile', '2':'Water Tile',
                      '3':'Tree Tile','4':'Wall Tile'}
        self.MapData = {}
        self.MapExport = []

    def savemap(self):
        self.MapExport.clear()
        for x in range (0,self.y):
            for y in range (0,self.x):
                self.MapExport.append(self.MapData[(x,y)])
        print(self.MapExport)
        file = open('testmapstuff.txt','w')
        p = 0
        for item in self.MapExport:
            p+=1
            if p == self.x:
                file.write(str(item) + '\n')
                p = 0
            else:
                file.write(str(item))
        
    def draw(self,canvas,TType,x,y):
        
        if TType == 'Tree Tile': canvas.create_image(x,y,anchor="nw",image=self.treeimage)
        if TType == 'Wall Tile': canvas.create_image(x,y,anchor="nw",image=self.wallimage)
        if TType == 'Grass Tile': canvas.create_rectangle(x,y,x+10,y+10,outline = 'medium sea green',fill= 'forest green')
        if TType == 'Water Tile': canvas.create_rectangle(x,y,x+10,y+10,outline = 'sky blue',fill= 'light sea green')

        mx,my = self.x *10,self.y*10
        
        if x>=0 and x <= mx and y>=0 and y <= my:
            self.MapData[(y//10,x//10)] = self.TNum

    def Click(self,event):
        x=round_down(event.x,10)
        y=round_down(event.y,10)
        self.draw(self.canvas,self.TType,x,y)
   

    def Key(self,event):
        if event.char.isdigit() == True:
            self.TType = self.binds[event.char]
            self.TNum = event.char
        if event.char == 'p':
            print (self.MapData)
        if event.char == 's':
            self.savemap()

    def create(self,x,y):

        self.x = x
        self.y = y
    
        height = y*10
        width = x*10
        
        self.canvas = Canvas(self.window,width=width-2, height=height-2, bg='white')
        self.canvas_Tiles = Canvas(self.window,width=24, height=height, bg='white')

        self.canvas_Tiles.create_rectangle(2,2,23,height-1)

        for x in range (1,len(self.binds)+1):
            y = str(x)            
            self.draw(self.canvas_Tiles,self.binds[y],7,1 + (20*x))

        self.canvas.grid(row = 0,column = 0)
        self.canvas_Tiles.grid(row = 0,column =1,rowspan=2)

        for x in range (0,self.x):
            for y in range(0,self.y):
                self.draw(self.canvas,self.TType,x*10,y*10)

        self.canvas.bind('<Button-1>',self.Click)
        self.window.bind('<B1-Motion>',self.Click)
        self.window.bind('<Key>',self.Key)
        
        
def round_down(num, divisor):
    return num - (num%divisor)


def something(x,y):
    surface1 = surface()
    surface1.create(x,y)
    
    surface1.canvas.mainloop()
    
something(59,50)

