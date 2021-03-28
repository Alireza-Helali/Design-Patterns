"""
Observer:
        observer is a behavioral design pattern and is
        a object that wishes to be informed about events
        happening in the system. the entity generating
        the events is an observer.
"""


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fall_ill = Event()

    def catch_cold(self):
        self.fall_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs doctor at {address}')


if __name__ == '__main__':
    person = Person('alireza', 'imaginary address')
    person.fall_ill.append(call_doctor)
    person.catch_cold()
