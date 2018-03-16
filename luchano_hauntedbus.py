baseballteam = ['Tim','Bob','Mike','Robin']

class HauntedBus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers #!!!! this is error/ Do you know Why?

    def drop(self,name):
        self.passengers.remove(name)

hbus1 = HauntedBus(baseballteam)
print(hbus1.passengers)
hbus1.drop('Tim')
print(hbus1.passengers)
print(baseballteam)