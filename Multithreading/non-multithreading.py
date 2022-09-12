from threading import *
import time

def divison(numbers):
    for n in numbers:
        time.sleep(1)
        print("Divison: ", n/5)

def multiplication(numbers):
    for n in numbers:
        time.sleep(1)
        print("Multiplication: ", n*5) 

numbers= [2, 3, 5, 1]

begintime= time.time()

divison(numbers)
multiplication(numbers)

print("Total Time Taken: ", time.time()-begintime)  