# Liskov Substitution Principle

"""
Liskov Substitution Principle:
        The idea is if you have some interface that takes
        some sort of base class you should be able to stick
        in any of it's inheritors and everything should work.
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'width is {self.width}, height is {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._height = self._width = value

    @Rectangle.width.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = w * rc.height
    print(f'expected {expected} but got {rc.area}')


rc = Rectangle(2, 5)
use_it(rc)

sq = Square(5)
use_it(sq)