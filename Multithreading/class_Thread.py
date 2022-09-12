from threading import *

class Demo:
    def display(self):
        for i in range(6):
            print("Child Thread\n")

d= Demo
t= Thread(target=d.display)
t.start()

for i in range(6):
    print("Main Thread\n")