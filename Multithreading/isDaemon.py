from threading import *
import time

def disp():
    for i in range(5):
        print("ChildThread")
        time.sleep(2)

t= Thread(target=disp)
t.setDaemon(True)

t.start()

time.sleep(5)
print("Main Thread")