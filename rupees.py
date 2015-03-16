from tkinter import PhotoImage
class rupee():
    def __init__(self,colour,canvas,location):
        self.colour = colour
        self.canvas = canvas
        self.collected = False
        self.location = location
        pointsdic = {'red':5,'green':1,'blue':20}
        self.imagedic = {'red':PhotoImage(file = 'assets/rupeeRED.png'),
                    'green':PhotoImage(file = 'assets/rupeeGREEN.png'),
                    'blue':PhotoImage(file = 'assets/rupeeBLUE.png')}
        self.points = pointsdic[colour]
        self.rupeesquare = ''

    def draw(self):
        print(self.colour)
        x,y = self.location
        x=x*16
        y=y*16
        self.rupeesquare = self.canvas.create_image(x,y,anchor = 'nw', image = self.imagedic[self.colour])
        

    
    
