from lab_python_oop.Rectangle import Rectangles
from lab_python_oop.Circle import Circles
from lab_python_oop.Square import Squares

if __name__ == "__main__":
    Rect = Rectangles('blue', 2, 3)
    print(Rect.repr())
    Circ = Circles('green', 5)
    print(Circ.repr())
    Squa = Squares('red', 5)
    print(Squa.repr())