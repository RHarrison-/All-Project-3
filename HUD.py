from tkinter import *

class RHUD():
    def  __init__(self,canvas,MainCanvas):
        #creating the labels on the screen which are munipluated later on by the 'UpdateHUD' function.
        self.InfoCanvas = canvas
        self.MainCanvas = MainCanvas
        
        self.RobotCordLabels = [] 
        self.RobotCordLabels.append(self.InfoCanvas.create_text(160,45,anchor=W,text = ''))
        self.RobotCordLabels.append(self.InfoCanvas.create_text(270,45,anchor=W,text = ''))
        
        self.RobotScoreLables = []
        self.RobotScoreLables.append(self.InfoCanvas.create_text(160,65,anchor=W,text =''))
        self.RobotScoreLables.append(self.InfoCanvas.create_text(270,65,anchor=W,text =''))
        
        self.RobotObjectiveLines = []
        self.RobotObjectiveLines.append(self.MainCanvas.create_line(0,0,10,20,fill = 'Orange3'))
        self.RobotObjectiveLines.append(self.MainCanvas.create_line(0,0,150,20,fill = 'DodgerBlue3'))
        

        
        self.InfoCanvas.create_text(100,25,anchor=E,text = 'Name:')
        self.InfoCanvas.create_text(270,25,anchor=W,text = 'Blue Bot',fill = 'DodgerBlue3')
        self.InfoCanvas.create_text(160,25,anchor=W,text = 'Orange Bot',fill = 'Orange3')
        self.InfoCanvas.create_text(100,45,anchor=E,text = 'Location:')
        self.InfoCanvas.create_text(100,65,anchor=E,text = 'Score:')

    def Update(self,RobotList):
        for x in range (0,len(RobotList)):
            
            rlx,rly,ignore1,ignore2 = RobotList[x].CanvasLocation
            rlx,rly = rlx+8,rly+8
            tlx,tly = RobotList[x].ObjectiveLocation
            tlx,tly = (tlx*16)+5,(tly*16)+5
             
            self.InfoCanvas.itemconfig(self.RobotCordLabels[x],text = RobotList[x].GridLocation)
            self.InfoCanvas.itemconfig(self.RobotScoreLables[x],text = RobotList[x].Score)

            self.MainCanvas.coords(self.RobotObjectiveLines[x],rlx,rly,tlx,tly)
