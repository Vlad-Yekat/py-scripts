class Window:
    pass


class UnixWindow(Window):
    pass


class MacWindow(Window):
    pass


class WindowFactoryMethod:
    def __new__(cls, os):
        if os == 'UNIX':
            return UnixWindow()
        else:
            return MacWindow()


win = WindowFactoryMethod(os='UNIX')




