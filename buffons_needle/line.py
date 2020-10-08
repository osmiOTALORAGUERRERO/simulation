from point import Point

class Line(object):
    """represents a parallel line for the board."""

    def __init__(self, y_start, x_end):
        super(Line, self).__init__()
        self.__start = None
        self.__end = None
        self.__set_start(y_start)
        self.__set_end(x_end, y_start)

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __set_start(self, y):
        self.__start = Point(0, y)

    def __set_end(self, x, y):
        self.__end = Point(x, y)
