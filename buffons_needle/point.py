class Point(object):
    """docstring for Point."""

    def __init__(self, x:float, y:float):
        super(Point, self).__init__()
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x:float):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y:float):
        return self.__y
