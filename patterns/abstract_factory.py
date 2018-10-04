# from Coursera with fun
# Abstract Factory StarWars

from abc import ABC, abstractmethod


class StarWarsFactory(ABC):
    @abstractmethod
    def create_hero(self, name):
        pass

    @abstractmethod
    def create_spell(self):
        pass

    @abstractmethod
    def create_weapon(self):
        pass


class SithFactory(StarWarsFactory):
    def create_hero(self, name):
        return Sith(name)

    def create_spell(self):
        return Power()

    def create_weapon(self):
        return Energy()


class JediFactory(StarWarsFactory):
    def create_hero(self, name):
        return Yoda(name)

    def create_spell(self):
        return Power()

    def create_weapon(self):
        return Lightsaber()


class Sith:
    def __init__(self, name):
        self._name = name
        self.spell = None
        self.weapon = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print("Woo")

    def cast(self):
        print("Welcome to the dark side")


class Yoda:
    def __init__(self, name):
        self._name = name
        self.spell = None
        self.weapon = None
        self.armor = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print("Wa by Yoda")
        self.weapon.hit()

    def cast(self):
        print("new cast by Yoda")


class Power:
    def cast(self):
        return "Use mind"


class Energy:
    def hit(self):
        return "Lightning"


class Lightsaber:
    def hit(self):
        return "Lightsaber"


def create_hero(factory):
    hero = factory.create_hero("hero name")
    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)
    return hero


player = create_hero(JediFactory())
player.hit()
player.cast()

player2 = create_hero(SithFactory())
player2.hit()
player2.cast()
