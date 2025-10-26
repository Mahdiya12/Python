from turtle import *

# ------- Class for Drawing a Face -------
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

    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)

    def drawOutline(self):
        penup()
        forward(self.size)
        pendown()
        pencolor('black')
        circle(self.size)
        self.goHome()

    def drawEye(self, turn):
        penup()
        left(turn)
        forward(self.size / 2)
        pendown()
        dot(self.size / 10)
        self.goHome()

    def drawMouth(self):
        penup()
        right(135)
        forward(self.size / 1.7)
        left(90)
        pendown()
        circle(self.size / 2.5, 90)
        self.goHome()

    def drawNose(self):
        penup()
        right(90)
        forward(self.size / 3)
        pendown()
        dot(self.size / 15)
        self.goHome()


# ------- Class for Rectangle Calculation -------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def areaRectangle(self):
        return self.length * self.width


# ------- Main Program -------
# Create and draw a face using turtle
face1 = Face(0, 0)
face1.setSize(80)
face1.draw()

# Create a rectangle and show its area
newRectangle = Rectangle(10, 20)
print(f"Rectangle dimensions → width = {newRectangle.width}, length = {newRectangle.length}")
print(f"Area of rectangle is {newRectangle.areaRectangle()}")

done()
