# Dependency inversion principle


"""
Dependency Inversion Principle:
        One of the things that the dependency inversion
        principle states that high level modules in your
        code should not depend on low level classes or
        modules. instead they should depend on abstraction.
"""
from enum import Enum
from abc import abstractmethod


class Relation(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class RelationShips(RelationBrowser):
    """
    low level module because it's dealing with storage
    and if you wanted to change the storage to something
    like database the Research module would not break
    because it doesn't depend on a low level module and
    you will modify just find_all_children_of method.
    """
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relation.PARENT, child))

    def find_all_children_of(self, name):
        for p in self.relations:
            if p[0].name == 'asghar' and p[1] == Relation.PARENT:
                yield p[2].name


class Research:  # high level module
    # def __init__(self, relationships):
    #     relation = relationships.relations
    #     for r in relation:
    #         if r[0].name == 'asghar' and r[1] == Relation.PARENT:
    #             print(f'asghar has a child name {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('asghar'):
            print(f'asghar has child named {p}')


person1 = Person('asghar')
person2 = Person('scarlet')
person3 = Person('angelina')

r = RelationShips()
r.add_parent_and_child(person1, person2)
r.add_parent_and_child(person1, person3)

Research(r)
