from abc import ABC, abstractmethod

class Some(ABC):
    @abstractmethod
    def result(self):
        pass

class Square(Some):
    def result(self, a):
        print("Square: ",(a*a))

class Cube(Some):
    def result(self, a):
        print("Square: ",(a*a*a))
        
s= Square()
c= Cube()

s.result(2)
c.result(2)