from random import randint

"""
Singleton:
        Singleton is a creational design pattern that lets you
        ensure that a class has only one instance. while
        providing a global access point to this instance.
"""


class SingleTone(type):
    # _instance = None

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class DataBase(metaclass=SingleTone):
    def __init__(self):
        print('loading database')


data1 = DataBase()
data2 = DataBase()
print(data2 == data1)
print(data2 is data1)

print('--------------------')


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class SingleTone:
    def __init__(self):
        print(f'id = {randint(1, 100)}')


s1 = SingleTone()
s2 = SingleTone()
print(s1 == s2)
