from turtle import *

class Face():
    def __init__(self, xpos, ypos):

        self.size = 90
        self.coord = (xpos, ypos)
        self.nosesize = "small"

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome()
        pensize(3)    
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)

    def goHome():
        

