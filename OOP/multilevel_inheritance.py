class SuperParent:
    def a(self):
        print("This is SuperParent.")

class Parent(SuperParent):
    def b(self):
        print("This is Parent.")

class Child(Parent):
    def c(self):
        print("This is Child.")

ch= Child()
ch.a()
ch.b()
ch.c()
