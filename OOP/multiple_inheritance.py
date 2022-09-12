class Parent1:
    def a(self):
        print("This is Parent1 Class!")

class Parent2:
    def a(self):
        print("This is Parent2 Class!")

class Child(Parent1, Parent2):
    def c(self):
        print("This is CHILD.")

c= Child()
c.a()
c.c()