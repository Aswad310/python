from threading import *
import time

def disp():
    print(current_thread().getName(), "...starting")
    time.sleep(3)
    print(current_thread().getName(), "...ending")

t1= Thread(target=disp, name="childthread1")
t2= Thread(target=disp, name="childthread2")
t3= Thread(target=disp, name="childthread3")

t1.start()
t2.start()
t3.start()

l= enumerate()
for i in l:
    print("Theead Name:",i.name)

time.sleep(5)

l= enumerate()
for i in l:
    print("Theead Name:",i.name)