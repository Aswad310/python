from threading import *
import time

def disp():
    for i in range(5):
        print("First Thread")
        time.sleep(3)

t1= Thread(target=disp , name="ChildThread")

t1.start()
t1.join(5)

for i in range(5):
    print("Second Thread")
