from threading import *
import time

# Event object is the simplest communication mechanism between the threads
event= Event()

def traficSignal():
    while True:
        time.sleep(5)
        print("Traffic Signal is GREEN⚫⚫🟢")
        event.set() # returns the True flag

        time.sleep(10)

        print("Traffic Signal is RED🔴⚫⚫")
        event.clear() # returns the False flag

def driver():
    num=0
    while True:
        print("Drivers waiting for GREEN Signal")
        event.wait() # wait untill true or false event is set

        # when event sets to TRUE
        print("Now signal is GREEN... Vehical can move")
        while event.is_set():
            num= num+1
            print("Vehical🚗 No.",num, "crossing the Road cross")

            time.sleep(2)

        # when event sets to FALSE
        print("Now signal is RED... Driver have to wait")

# Threading
t1= Thread(target=traficSignal)
t2=Thread(target=driver)

t1.start()
t2.start()