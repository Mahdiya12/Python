from turtle import *

# A function is defined for each part, with following steps
# 1. pen up
# 2. move to correct position
# 3. pen down
# 4. draw
# 5. return home

class Face:
    def __init__(self, xpos, ypos):
        self.size = 50
        self.coord = (xpos, ypos)
        self.nosesize = 'small'

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(-135)
        self.drawMouth()
        self.drawNose()

    # After drawing each part, turtle position
    # returns to centre. Parts can be drawn in any order
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)

    def drawOutline(self):
        penup()
        # move turtle pen in forward direction
        forward(self.size)
        pendown()
        # draw circle of given radius
        pencolor('black')
        circle(self.size)
        # return back to centre
        self.goHome()

    def drawEye(self, turn):
        penup()
        # move turtle pen to given angle
        left(turn)
        # move turtle pen in forward direction
        forward(self.size / 2)
        pendown()
        # draw circle of given radius
        dot(self.size/10)
        # return back to centre
        self.goHome()

    def drawMouth(self):
        penup()
        # move turtle pen to given angle
        right(135)
        # move turtle pen in forward direction
        forward(self.size/1.7)
        left(90)
        pendown()
        # draw arc of circle of given radius
        # but till given extent only