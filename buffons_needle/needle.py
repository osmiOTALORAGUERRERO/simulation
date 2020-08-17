from point import Point
import random
import math

class Needle(object):
    """docstring for Needle."""

    def __init__(self, size:float):
        super(Needle, self).__init__()
        self.__size = size
        self.__head = None
        self.__point = None

    def place(self, widthBoard:int, heightBoard:int):
        self.__set_head(widthBoard, heightBoard)
        self.__set_point(widthBoard, heightBoard)

    @property
    def size(self):
        return self.__size

    @property
    def head(self):
        return self.__head

    @property
    def point(self):
        return self.__point

    def __set_head(self, x_max, y_max):
        x = round(random.uniform(0, x_max), 5)
        y = round(random.uniform(0, y_max), 5)
        self.__head = Point(x,y)

    def __set_point(self, x_max, y_max):
        alpha_angle = random.randrange(0, 91)
        x = 0
        y = 0
        while True:
            a = self.__size*round(math.cos(math.radians(alpha_angle)),10)
            b = self.__size*round(math.sin(math.radians(alpha_angle)),10)
            direction_x = 1 if (random.random()<0.5) else -1
            direction_y = 1 if (random.random()<0.5) else -1
            x = round(self.head.x + (a*direction_x),5)
            y = round(self.head.y + (b*direction_y),5)
            if (x<=x_max and x>=0) and (y<=y_max and y>=0):
                break;
        self.__point = Point(x,y)
