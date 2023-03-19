class Window:
    pass


class UnixWindow(Window):
    pass


class MacWindow(Window):
    pass


class Button:
    pass


class UnixButton(Button):
    pass


class MacButton(Button):
    pass


class WindowFactory:
    def __init__(self, os):
        if os == 'UNIX':
            self.window = UnixWindow()
            self.button = UnixButton()
        else:
            self.window = MacWindow()
            self.button = MacButton()


win = WindowFactory(os='UNIX')



