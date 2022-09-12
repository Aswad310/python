from threading import *
import time

l= Lock()

def dis(name, age):
    for i in range(3):
        l.acquire()
        print("Your name:",name)
        time.sleep(3)
        print("Your age:",age)
        l.release()

t1= Thread(target=dis, args=("Aswad", 17))
t2= Thread(target=dis, args=("Abad", 15))

t1.start()
t2.start()