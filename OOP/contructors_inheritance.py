class Parent:
    def __init__(self) -> None:
        print("This is Parent1 Constructor")

class Child(Parent):
    def a(self):
        print("This is Child Class!")

c= Child()