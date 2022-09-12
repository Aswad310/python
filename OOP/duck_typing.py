class Duck:
    def quak(self):
        print("I am Quaking!")

    def fly(self):
        print("I am Flying!")

class Person:
    def walk(self):
        print("I am Walking!")

class Check:
    pass

def duck_and_person(thing):
    if isinstance(thing, Duck):
        thing.quak()
        thing.fly()
    elif isinstance(thing, Person):
        thing.walk()
    else:
        print("Should be person or duck!")

d= Duck()
duck_and_person(d)

print()

p= Person()
duck_and_person(p)

print()

c= Check()
duck_and_person(c)
