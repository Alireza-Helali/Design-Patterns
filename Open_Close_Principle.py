# open close Principle

"""
open close principle:
        open close principle suggest that when you add new functionality
        you add it via extension not modification. in short build base classes
        and inherit from those classes this way your program become more
        dynamic.
"""

from enum import Enum
from abc import ABC, abstractmethod


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.size = size
        self.name = name
        self.color = color


class ProductFilter:
    """
        in this class we keep modifying class
        and adding new functionality and it's
        wrong based on open for extension and
        close for modification.
    """

    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    p1 = Product('apple', Color.RED, Size.SMALL)
    p2 = Product('tree', Color.GREEN, Size.LARGE)
    p3 = Product('house', Color.BLUE, Size.MEDIUM)

    products = [p1, p2, p3]
    better_filter = BetterFilter()
    print('color filter : ')
    color = ColorSpecification(Color.GREEN)
    for p in better_filter.filter(products, color):
        print(f'new approach : {p.name}')

    print('size filter : ')
    size = SizeSpecification(Size.MEDIUM)
    for p in better_filter.filter(products, size):
        print(f'new approach : {p.name}')

    print('medium and blue : ')
    # large_blue = AndSpecification(size, ColorSpecification(Color.BLUE))
    large_blue = size & ColorSpecification(Color.BLUE)
    for p in better_filter.filter(products, large_blue):
        print(f'{p.name} is medium and blue.')
