from lab_python_oop.Rectangle import Rectangles

class Squares(Rectangles):

    def __init__(self, color, size, kind = "Square"):
        self.color = color
        self.height = size
        self.width = size
        self.kind = kind

    def repr(self):
        return '{} : color {}, height {}, width {}, space {}'.format(self.kind, self.color, self.height, self.width, self.RectSpace())