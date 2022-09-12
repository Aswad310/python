# Duck Typing Philosophy of Python

# class of Duck 
class Duck:
    #method
    def quak(self):
        print("I am Quaking!")

    def fly(self):
        print("I am Flying!")

# class of Person
class Person:
    #method
    def walk(self):
        print("I am Walking!")

# class of Ghost
class Ghost:
    pass

# this function is checking what is the type will be. . .
def duck_and_person(thing):
    if isinstance(thing, Duck):
        thing.quak()
        thing.fly()
    elif isinstance(thing, Person):
        thing.walk()
    else:
        print("Should be person or duck!")

# Object 
d= Duck()
duck_and_person(d)

print()

# Object
p= Person()
duck_and_person(p)

print()

# Object 
c= Ghost()
duck_and_person(c)