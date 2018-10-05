from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):

    def feed(self):
        print("eat")

    def move(self):
        print("Walk")

    def make_noise(self):
        print("Wo")


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):
    def move(self):
        print("swim")

    def make_noise(self):
        print('Zzz')


class Predator(AbstractDecorator):
    def feed(self):
        print("other")


class FastPredator(AbstractDecorator):
    def move(self):
        self.base.move()
        print("fast")

animal = Animal()
animal.move()


swimming_animal = Swimming(Animal)
swimming_animal.move()

predator = Predator(swimming_animal)
predator.feed()
predator.make_noise()

fast = FastPredator(predator)
fast.move()

fastfast = FastPredator(fast)
fastfast.move()

fastfast.base = fastfast.base.base
fastfast.move()

