from threading import *
import time

l= Semaphore(2) # alows only 2 Threads at a time

def dis(name, age):
    for i in range(3):
        l.acquire()
        print("Your name:",name)
        time.sleep(2)
        print("Your age:",age)
        l.release()

t1= Thread(target=dis, args=("Aswad", 17))
t2= Thread(target=dis, args=("Abad", 15))
t3= Thread(target=dis, args=("Ahmer", 22))
t4= Thread(target=dis, args=("Fassih", 19))
t5= Thread(target=dis, args=("Moon", 24))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()