class Single(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Single, cls).__new__(cls)
        return cls.instance

print(Single() is Single())
Single().x = 1
c = Single()
d = Single()
print(c.x)
print(d.x)
c.x=2
print(d.x)


