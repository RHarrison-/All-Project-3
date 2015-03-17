from tkinter import PhotoImage
class Key():
    def __init__(self,canvas,location):
        self.canvas = canvas
        self.collected = False
        self.location = location
        x,y = location
        
        if x > 40:
            x = x - 40
        if x > 80:
            x = x - 80

        if y > 25:
            y = y - 25

        self.screenlocation = (x,y)
        self.keyimage = PhotoImage(file = 'assets/Key.png')
        self.keysquare = ''

    def draw(self):
        x,y = self.screenlocation
        x=x*16
        y=y*16
        self.keysquare = self.canvas.create_image(x,y,anchor = 'nw', image = self.keyimage)
        

    
    
