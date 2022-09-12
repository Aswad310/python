from threading import *
import time

def disp():
    print(current_thread().getName(),"staring...")
    time.sleep(3)
    print(current_thread().getName(),"ending...")

t1= Thread(target=disp, name="ChildThread1")
t2= Thread(target=disp, name="ChildThread2")
t3= Thread(target=disp, name="ChildThread3")

t1.start()
t2.start()
t3.start()

print(t1.name, "isAlive", t1.is_alive()) 
print(t2.name, "isAlive", t2.is_alive()) 
print(t3.name, "isAlive", t3.is_alive()) 

time.sleep(3)

print(t1.name, "isAlive", t1.is_alive()) 
print(t2.name, "isAlive", t2.is_alive()) 
print(t3.name, "isAlive", t3.is_alive()) 
