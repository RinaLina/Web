from lab_python_oop.GeometricFigure import GeometricFigures
from lab_python_oop.ShapeColor import Colors

class Rectangles(GeometricFigures, Colors):

    def __init__(self, color, height, width, kind = "Rectangle"):
        self.color = color
        self.height = height #высота
        self.width = width #ширина
        self.kind = kind

    def RectSpace(self):
        return self.height * self.width

    def Kind(self):
        return Rectangles.kind

    def repr(self):
        return '{} : color {}, height {}, width {}, space {}'.format(self.kind, self.color, self.height, self.width, self.RectSpace())