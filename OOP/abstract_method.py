from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Its a Laptop")

class Mobile(Computer):
    def process(self):
        print("Its a Mobile")

class Developer:
    def work(self, comp):
        print("Developer you got this")

        comp.process()
        
l= Laptop()
m= Mobile()

d= Developer()
d.work(l)