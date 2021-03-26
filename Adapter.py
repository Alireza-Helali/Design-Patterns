"""
Adapter:
        Adapter is a structural design pattern that tries to
        adapt the interface that you are given  to the interface
        that you actually need.
"""


class Target:
    def request(self):
        return 'Target : thr default target behavior'


class Adaptee:
    def specific_request(self):
        return '.eetpadA eht fo roivaheb laicepS'


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f'TRANSLATED : {self.adaptee.specific_request()[::-1]}'


def client_code(target):
    print(target.request())


if __name__ == '__main__':
    target = Target()
    print('Client: I can work just fine with the Target objects:')
    client_code(target)
    print('\n')

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f'Adaptee : {adaptee.specific_request()}')
    print('\n')

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
