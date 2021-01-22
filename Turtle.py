# Turtle.py

import math
import svgwrite

class Turtle:

    def __init__(self):
        self.posX = 100
        self.posY = 100
        self.angle = 90
        self.color = (0, 0 ,0)
        self.penStat = 2
        self.file = svgwrite.Drawing(filename = "teste.svg", size = ("100%", "100%"))

    def Forward(self, length):
        # O inicio da nova linha é na posição em que a tartaruga estava
        x1 = self.posX
        y1 = self.posY

        """
        Com soma o sentido da tartaruga é de cima para baixo.
        """
        x2 = x1 + math.cos(math.radians(self.angle)) * length
        y2 = y1 + math.sin(math.radians(self.angle)) * length
    
        # Guardar a posição final da tartaruga
        self.posX = x2
        self.posY = y2

        """ Fdx de onde crlh vem o polyline???? """
        #self.file.add(self.file.poly)
        # self.file.add(self.file.svgwrite.shapes.Polyline(points=(x1,y1), stroke = ...))

        """ Tentar assim """
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
        """
        Alterei para soma, desta maneira a linha vira para a esquerda, vista do utilizador.
        Acho que fica mais intuitivo.
        """
        self.angle += newAngle

    def Right(self, newAngle):
        self.angle -= newAngle
    
    def SetPos(self, x, y):
        self.posX = x
        self.posY = y
        self.file.add(self.file.line((x, y), (x, y)))

    def SetXY(self, x, y):
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
        self.posX = 100
        self.posY = 100
        self.angle = 90
        # Fazemos reset a tudo? # FIXME
        self.color = (0, 0 ,0)
        self.penStat = 2

    def PenDown(self):
        self.penStat = 2
    
    def PenUp(self):
        self.penStat = 0

    def PenColor(self, newColor):
        self.color = newColor


""" Testar """
svg = Turtle()

color = (255, 0, 0)
svg.PenColor(color)
svg.Forward(100)
svg.Right(90)
svg.Forward(100)
svg.Left(45)
svg.Forward(100)
svg.Right(45)
svg.Forward(100)

color = (0, 255, 0)
svg.PenColor(color)
svg.SetPos(300, 200)
svg.Forward(50)
svg.Right(90)
svg.Forward(50)
svg.Right(90)
svg.Forward(50)
svg.Right(90)
svg.Forward(50)
svg.Right(90)

svg.Home()
color = (0, 50, 255)
svg.PenColor(color)
svg.SetX(120)
svg.Backward(30)
svg.Left(90)
svg.Backward(30)
svg.Left(90)
svg.Backward(30)
svg.Left(90)
svg.Backward(30)
svg.Left(90)

""" svg.Forward(50)
svg.SetX(500)
svg.Forward(50)
svg.SetY(300)
svg.Right(90)
svg.SetPos(100, 100)
svg.Forward(50)
svg.Right(90)
svg.SetXY(300, 300)
svg.Forward(50) """

#svg.SetPos(5, 10)

""" svg.Home()

svg.Forward(50)
svg.Right(90)
svg.Forward(50)
svg.Right(90)
svg.Forward(50)
svg.Right(90)
svg.Forward(50) """

""" color = (0, 255, 0)
svg.PenColor(color)
svg.Forward(100)
svg.Right(90)
color = (255, 0, 0)
svg.PenColor(color)
svg.Forward(100)
svg.Right(90)
color = (0, 0, 255)
svg.PenColor(color)
svg.Forward(100)
svg.Right(90)
color = (255, 0, 0)
svg.PenColor(color)
svg.Forward(100)
svg.Right(90)
svg.Right(45)
color = (0, 123, 0)
svg.PenColor(color)
svg.Forward(141.421356237) """

svg.file.save()