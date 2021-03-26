from copy import deepcopy


class Address:
    def __init__(self, street, city, country):
        self.country = country
        self.city = city
        self.street = street

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} lives in {self.address}'


"""
Problem:
        with copying instance number one to instance number two
        we actually referring to memory address of instance one
        so with changing attribute of instance two both instances
        attributes will change
"""

p1 = Person('alireza', Address('vanak', 'tehran', 'iran'))
print(p1)
p2 = p1
p2.address.street = 'narmak'
p2.name = 'person2'
print('----------------')
print(p1)
print(p2)

"""
solution:
        simply to use deepcopy.what deepcopy does is recursively
        copying all element to new one so finally we have a nae
        object that is not referring to an other object
"""

print('------------------')
p3 = deepcopy(p1)
p3.name = 'person3'
p3.address.city = 'isfahan'
print(p1)
print(p3)
