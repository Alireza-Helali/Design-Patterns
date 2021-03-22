"""
Factory method:
        factory method is a creational design pattern
        that provides an interface for creating an object
        in superclass but allows subclasses to alter the
        type of objects that will be created. it's a simply
        a method that creates an object.
"""

from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        raise NotImplementedError

    @staticmethod
    def new_polar_point(rho, theta):
        raise NotImplementedError


class PointFactory(Point):
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)


if __name__ == '__main__':
    p = PointFactory(2, 3)
    print(p.new_polar_point(2, 1))


# --------------- OR ----------------


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * sin(theta), rho * cos(theta))

        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)


if __name__ == '__main__':
    p1 = Point.PointFactory.new_polar_point(2, 1)
    print(p1)
