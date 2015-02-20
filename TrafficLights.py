from tkinter import *

class TrafficLight():
    def __init__(self, canvas, Location,World):
        self.Location = Location
        self.canvas = canvas
        self.onoff = 'off'
        self.TrafficOpenImage = PhotoImage(file = 'Graphics\TrafficOpen.Gif')
        self.TrafficClosedImage = PhotoImage(file = 'Graphics\TrafficClosed.Gif')
        self.TLImage = self.canvas.create_image(self.Location,anchor = "nw", image = self.TrafficOpenImage)
        self.World = World
        self.LSquare = []
        self.state = ''
        
    #Switches the traffic lights when called. 
    def Switch(self,TYPE):
        self.canvas.delete(self.TLImage)
        self.state = TYPE
        
        if self.onoff =='on':
            self.state = 'off'
            self.TLImage=self.canvas.create_image(self.Location,anchor = 'nw', image = self.TrafficOpenImage)
            self.onoff='off'
            for z in range (0,len(self.LSquare)):
                self.canvas.delete(self.LSquare[z])
            
                    
        else:
            self.TLImage=self.canvas.create_image(self.Location,anchor = "nw", image = self.TrafficClosedImage)
            self.onoff='on'

            x,y=self.Location
    
            x1=x/16
            y1=y/16

            xx = -2
            i=0

            for x in range (0,3):
                xx+=1
                yy =-2
            
                for x in range (0,3):
                    yy+=1
                    p1,p2 = x1,y1
                    if (xx,yy) == (0,0):
                        continue
                    
                    p1 = p1+xx
                    
                    p1=p1*16
                    
                    p2=p2+yy
                    
                    p2=p2*16

                    if (p1/16,p2/16) in self.World.grass:
                        i=i+1
                        self.LSquare.append(self.canvas.create_rectangle(p1,p2,p1+16,p2+16,fill = TYPE,outline = 'light green'))
                    
                    
                    
                    
            

            

            

    
            
            
            
            

        
