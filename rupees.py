from tkinter import PhotoImage
class rupee():
    def __init__(self,colour,canvas,location):
        self.colour = colour
        self.canvas = canvas
        rupee.onscreen = ''
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
        pointsdic = {'red':5,'green':1,'blue':20}
        self.imagedic = {'red':PhotoImage(file = 'assets/rupeeRED.png'),
                    'green':PhotoImage(file = 'assets/rupeeGREEN.png'),
                    'blue':PhotoImage(file = 'assets/rupeeBLUE.png')}
        self.points = pointsdic[colour]
        self.rupeesquare = ''

    def draw(self):
        x,y = self.screenlocation
        x=x*16
        y=y*16
        self.rupeesquare = self.canvas.create_image(x,y,anchor = 'nw', image = self.imagedic[self.colour])
        

    
    
