# from Coursera with fun
# Chain of responsibility pattern


class Zombie:
    def __init__(self):
        self.name = 'Trooper'
        self.experience = 0
        self.prepare_movie = set()
        self.performed_movie = set()

WORK_SCREAM, WORK_EAT, WORK_RUN = "WSCREAM", "WEAT", "WRUN"


class Event:
    def __init__(self, kind):
        self.kind = kind


class NUllHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, animal, event):
        if self.__successor is not None:
            self.__successor.handle(animal, event)


class WorkScream(NUllHandler):
    def handle(self, animal, event):
        if event.kind == WORK_SCREAM:
            work_name = 'Frigthen people'
            experience = 100
            if work_name not in (animal.prepare_movie | animal.performed_movie):
                print('Begin ', work_name)
                animal.prepare_movie.add(work_name)
            elif work_name in animal.performed_movie:
                print('End ', work_name)
                animal.performed_movie.add(work_name)
                animal.prepare_movie.remove(work_name)
                animal.experience += experience
        else:
            print('Transfer event next')
            super().handle(animal, event)


class WorkEat(NUllHandler):
    def handle(self, animal, event):
        if event.kind == WORK_EAT:
            work_name = 'Eat people'
            experience = 200
            if work_name not in (animal.prepare_movie | animal.performed_movie):
                print('Begin ', work_name)
                animal.prepare_movie.add(work_name)
            elif work_name in animal.performed_movie:
                print('End ', work_name)
                animal.performed_movie.add(work_name)
                animal.prepare_movie.remove(work_name)
                animal.experience += experience
        else:
            print('Transfer event next')
            super().handle(animal, event)


class WorkRun(NUllHandler):
    def handle(self, animal, event):
        if event.kind == WORK_RUN:
            work_name = 'Run for people'
            experience = 300
            if work_name not in (animal.prepare_movie | animal.performed_movie):
                print('Begin ', work_name)
                animal.prepare_movie.add(work_name)
            elif work_name in animal.performed_movie:
                print('End ', work_name)
                animal.performed_movie.add(work_name)
                animal.prepare_movie.remove(work_name)
                animal.experience += experience
        else:
            print('Transfer event next')
            super().handle(animal, event)


class ZombieBoss:
    def __init__(self):
        self.handlers = WorkScream(WorkEat(WorkRun(NUllHandler)))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_task(self, zombie):
        for event in self.events:
            self.handlers.handle(zombie, event)


# go go go
events = [Event(WORK_SCREAM), Event(WORK_EAT), Event(WORK_RUN)]

zombie_boss = ZombieBoss()

for event in events:
    zombie_boss.add_event(event)

zombie1 = Zombie()

zombie_boss.handle_task(zombie1)

zombie1.performed_movie = {'Frigthen people', 'Run for people'}

zombie_boss.handle_task(zombie1)

