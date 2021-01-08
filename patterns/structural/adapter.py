"""
Convert the interface of a class into another interface clients expect.
An adapter lets classes work together that could not otherwise because of incompatible interfaces.
The enterprise integration pattern equivalent is the translator.
"""


def client_func(message, destination):
    """
    the client is awaiting for <send> method of destination
    """
    destination.send(message)


class NonAdapted:
    """
    but we have <write> method in our (new)class
    """
    def write(self, message):
        print(message)


class Adapted:
    """
    so , our class perform <send> for client by using <write>
    """
    def __init__(self):
        self.non_adapted = NonAdapted()

    def send(self, message):
        self.non_adapted.write(message)


client_class = Adapted()
client_func('message', client_class)
