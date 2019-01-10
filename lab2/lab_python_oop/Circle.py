from lab_python_oop.GeometricFigure import GeometricFigures
from lab_python_oop.ShapeColor import Colors
from math import pi

class Circles(GeometricFigures, Colors):

    def __init__(self, color, radius, kind = "Circle"):
        self.color = color
        self.radius = radius #радиус
        self.kind = kind

    def CircSpace(space, radius):
        return pi * radius * radius

    def Kind(self):
        return Circles.kind

    def repr(self):
        return '{} : color {}, radius {}, space {}'.format(self.kind, self.color, self.radius, self.CircSpace(self.radius))