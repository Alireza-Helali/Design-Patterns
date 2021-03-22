"""
Abstract Factory:
        abstract factory is a creational design pattern
        that let you produce families of related objects
        without specifying their concrete classes
"""

from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('this tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('this coffee is delicious')


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    initialized = False
    factories = []

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in self.AvailableDrink:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def order_drink(self):
        for d in self.factories:
            print(d[0])
        order = int(input(f'please pick a drink (0-{len(self.factories) - 1}) :'))
        amount = int(input('specify amount: '))
        return self.factories[order][1].prepare(amount)


# def order_drink(type):
#     if type == 'tea':
#         return TeaFactory().prepare(200)
#     elif type == 'coffee':
#         return CoffeeFactory().prepare(50)
#     else:
#         return None


if __name__ == '__main__':
    # entry = input('what kind of drink would you like ? ')
    # drink = order_drink(entry)
    # try:
    #     drink.consume()
    # except:
    #     print("we don't have your order")
    drink = HotDrinkMachine()
    d = drink.order_drink()
    d.consume()
