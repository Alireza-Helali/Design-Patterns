from copy import deepcopy

"""
ProtoType:
        prototype is creational design pattern that lets you
        copy existing objects without making your code dependant
        on your classes
"""


class Address:
    def __init__(self, street, building, city):
        self.street = street
        self.building = building
        self.city = city

    def __str__(self):
        return f'{self.street}, {self.building}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('sheykh bahayee', 'mapsa', 'tehran'))
    aux_office_employee = Employee('', Address('sohrevardi', 'mofid', 'tehran'))

    @staticmethod
    def __new_employee(proto, name, city):
        result = deepcopy(proto)
        result.name = name
        result.address.city = city
        return result

    @staticmethod
    def new_main_office_employee(name, city):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, city)

    @staticmethod
    def new_aux_office_employee(name, city):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, city
        )


p1 = EmployeeFactory.new_main_office_employee('alireza', 'isfahan')
p2 = EmployeeFactory.new_main_office_employee('faezeh', 'tabriz')

print(p1)
print(p2)
