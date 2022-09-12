class Parent:
    def a(self):
        print("This is Parent Class!")

class Child(Parent):
    def b(self):
        print("This is Child Class!")

c= Child()
c.a()
c.b()