# Turtle.py

import math
import svgwrite

class Turtle:

    def __init__(self):
        self.posX = 250
        self.posY = 250
        self.angle = 90
        self.color = (0, 0 ,0)
        self.penStat = 2
        self.file = svgwrite.Drawing(filename = "teste.svg", size = ("100%", "100%"))

    def Forward(self, length):
        # O inicio da nova linha é na posição em que a tartaruga estava
        x1 = self.posX
        y1 = self.posY

        x2 = x1 + math.cos(math.radians(self.angle)) * length
        y2 = y1 + math.sin(math.radians(self.angle)) * length
    
        # Guardar a posição final da tartaruga
        self.posX = x2
        self.posY = y2

        self.file.add(self.file.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(self.color[0], self.color[1], self.color[2], '%'),
                                                        stroke_width = self.penStat))

    def Backward(self, length):
        x1 = self.posX
        y1 = self.posY

        x2 = x1 - math.cos(math.radians(self.angle)) * length
        y2 = y1 - math.sin(math.radians(self.angle)) * length

        self.posX = x2
        self.posY = y2

        self.file.add(self.file.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(self.color[0], self.color[1], self.color[2], '%'),
                                                        stroke_width = self.penStat))

    def Left(self, newAngle):
        self.angle -= newAngle

    def Right(self, newAngle):
        self.angle += newAngle
    
    def SetPos(self, x, y):
        self.posX = x
        self.posY = y
        self.file.add(self.file.line((x, y), (x, y)))

    def SetX(self, x):
        self.posX = x
        self.file.add(self.file.line((x, self.posY), (x, self.posY)))

    def SetY(self, y):
        self.posY = y
        self.file.add(self.file.line((self.posX, y), (self.posX, y)))

    def Home(self):
        self.posX = 250
        self.posY = 250
        self.angle = 90
        self.color = (0, 0 ,0)
        self.penStat = 2

    def PenDown(self):
        self.penStat = 2
    
    def PenUp(self):
        self.penStat = 0

    def PenColor(self, newColor):
        self.color = newColor
