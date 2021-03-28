"""
Decorator:
        Decorator is a structural design pattern that allows
        adding new behaviors to objects dynamically by placing
        them inside special wrapper objects.

        Using decorators you can wrap objects countless number
        of times since both target objects and decorators follow
        the same interface. The resulting object will get a
        stacking behavior of all wrappers.
"""

from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'this is circle with radius of {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'this is a square with area of {self.side * 4}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransParentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100.0}% transparency'


if __name__ == '__main__':
    circle = Circle(2)
    red_circle = ColoredShape(circle, 'red')
    transparent_red_circle = TransParentShape(ColoredShape(Circle(3), 'green'), 0.5)
    print(transparent_red_circle)
