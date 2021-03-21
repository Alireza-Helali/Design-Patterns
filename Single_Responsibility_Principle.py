# Single Responsibility principle


"""
Single responsibility principle :
        if you have a class that class should have it's primary responsibility
        and it's should not take on other responsibilities. the problem with
         below code is we added another responsibility to our class and that is
         for persistence this may cause modification and problem in future if
         we wanted to edit for example saving file path or loading it. so we move
         that persistence responsibility to other class.

         short:
            don't overload your objects with to many responsibilities
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def del_entries(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, file_name):
    #     file = open(file_name, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, file_name):
    #     pass
    #
    # def load_from_web(self, url):
    #     pass


class Persistence:
    @staticmethod
    def save(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    @staticmethod
    def load(journal, filename):
        pass

    @staticmethod
    def load_from_web(journal, url):
        pass


j = Journal()
j.add_entry('i ate a bug today')
j.add_entry('i cried today')

file_name = r'test.txt'
Persistence.save(j, file_name)

with open('test.txt', 'r') as file:
    print(file.read())
