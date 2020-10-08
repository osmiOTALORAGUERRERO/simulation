from needle import Needle
from line import Line
from point import Point

class Board(object):
    """The board with parallel lines a needles droped."""

    def __init__(self, height=100, width=100, n_lines=20):
        super(Board, self).__init__()
        self.height = height
        self.width = width
        self.lines = []
        self.needles = []
        self.needles_intersection = []
        self.distance_between_lines = float(self.height/n_lines)
        self.generate_lines(n_lines)

    def throw_needle(self, needle):
        needle.place(self.width, self.height)
        self.needles.append(needle)
        intersection, line_index = self.__validate_intersection(self.lines, needle, 0, len(self.lines))
        if intersection:
            self.needles_intersection.append({'needle':needle, 'line':self.lines[line_index]})

    def generate_lines(self, n_lines=20):
        self.lines = []
        self.distance_between_lines = float(self.height/n_lines)
        for y_line in range(0, self.height+1, int(self.distance_between_lines)):
            self.lines.append(Line(y_line, self.width))

    @property
    def n_needles_intersection(self):
        return len(self.needles_intersection)

    @property
    def n_needles(self):
        return len(self.needles)

    @property
    def n_lines(self):
        return len(self.lines)

    def __validate_intersection(self, lines, needle, lB, uB):
        middlePoint = int((lB+uB)/2)

        if lB == uB:
            if (needle.head.y<=lines[middlePoint].start.y and needle.point.y>=lines[middlePoint].start.y) or (needle.head.y>=lines[middlePoint].start.y and needle.point.y<=lines[middlePoint].start.y):
                return True, middlePoint
            else:
                return False, -1
        else:
            if (needle.head.y<=lines[middlePoint].start.y and needle.point.y>=lines[middlePoint].start.y) or (needle.head.y>=lines[middlePoint].start.y and needle.point.y<=lines[middlePoint].start.y):
                return True, middlePoint
            else:
                if (needle.head.y < lines[middlePoint].start.y and needle.point.y < lines[middlePoint].start.y):
                    return self.__validate_intersection(lines, needle , lB, middlePoint)
                else:
                    return self.__validate_intersection(lines, needle, middlePoint+1, uB)
