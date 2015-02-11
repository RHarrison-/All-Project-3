from tkinter import *

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.TType = 'Wall Tile'
        self.wallimage = PhotoImage(file = 'Graphics\Wall.gif')
        self.treeimage = PhotoImage(file = 'Graphics\Tree.gif')
        self.grassimage = PhotoImage(file = 'Graphics\Grass.gif')
        self.binds = {'1':'Grass Tile', '2':'Water Tile',
                      '3':'Tree Tile','4':'Wall Tile'}
        
    def draw(self,TType,x,y):
        x=x*10
        y=y*10
        if TType == 'Tree Tile': self.canvas.create_image(x,y,anchor="nw",image=self.treeimage)
        if TType == 'Wall Tile': self.canvas.create_image(x,y,anchor="nw",image=self.wallimage)
        if TType == 'Grass Tile': self.canvas.create_rectangle(x,y,x+10,y+10,outline = 'medium sea green',fill= 'forest green')
        if TType == 'Water Tile': self.canvas.create_rectangle(x,y,x+10,y+10,outline = 'sky blue',fill= 'light sea green')

    def Click(self,event):
        x=round_down(event.x,10)
        y=round_down(event.y,10)
        x=x//10
        y=y//10
        self.draw(self.TType,x,y)  
        print (x,y, self.TType)

    def Drag(self,event):
        x=round_down(event.x,10)
        y=round_down(event.y,10)
        x=x//10
        y=y//10
        self.draw(self.TType,x,y)

    def Key(self,event):
        self.TType = self.binds[event.char]

    def create(self,x,y):
    
        height = y*10
        width = x*10
        
        self.canvas = Canvas(self.window,width=width-2, height=height, bg='white')
        
        self.canvas.bind('<Button-1>',self.Click)
        self.canvas.bind('<ButtonRelease-1>',self.Click)
        self.window.bind('<Key>',self.Key)
        self.window.bind('<B1-Motion>',self.Drag)
        
        self.canvas.pack()

    
def round_down(num, divisor):
        return num - (num%divisor)


def something(x,y):
    surface1 = surface()
    surface1.create(x,y)

    surface1.canvas.mainloop()

something(50,50)
