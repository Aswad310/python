from abc import ABC, abstractmethod
# class
class Bank(ABC):

    # contructor
    def __init__(self, b_name):
        print("Welcome to Bank->", b_name)

    # abstract method
    @abstractmethod
    def balance(self):
        pass

class MCB(Bank):
    def balance(self):
        print("MCB have 1 Billion.")

class HBL(Bank):
    def balance(self):
        print("HBL have 1 Million.")