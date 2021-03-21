# Interface Segregation Principle


"""
The idea of interface segregation principle is that
you dont really want to stick too many elements or too
many methods in to an interface.
"""

from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def printer(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionPrinter(Machine):
    def printer(self, document):
        print(f'print {document}')

    def fax(self, document):
        print(f'faxing {document}')

    def scan(self, document):
        print(f'scanning {document}')


class OldFashionPrinter(Machine):
    """THe problem with this class is old fashion
    printer doesn't support fax and scanning and
    client instantiate this class see's fax and scan
    and assume that this machine support this features"""

    def printer(self, document):
        print('print document')

    def fax(self, document):
        pass  # old fashion printer don't have this feature

    def scan(self, document):
        pass  # old fashion printer don't have this feature


"""
So instead of having one class and all the methods
in it we are going to break that class to smaller
classes. in this way machines will have the exact 
feature that they should had.
"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    def scan(self, document):
        pass


class MyCopier(Printer):

    def print(self, document):
        print(f'print {document}')


class PhotoCopier(Printer, Scanner):
    def print(self, photo):
        print(f'print {photo}')

    def scan(self, photo):
        print(f'print {photo}')


class MultiFunctionMachine(Scanner, Fax, ABC):
    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionDevice(MultiFunctionMachine):
    def fax(self, document):
        print(f'faxing {document}')

    def scan(self, document):
        print(f'scanning {document}')
