class Car(object):
    def start(self):
        print("Car started")

car = Car()   # Class name must be capitalized
car.start()

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

car = Car()
car.start()