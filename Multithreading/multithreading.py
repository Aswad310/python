from threading import *
import time

def divison(numbers):
    for n in numbers:
        time.sleep(1)
        print("Divison:", n/5)

def multiplication(numbers):
    for n in numbers:
        time.sleep(1)
        print("Multiplication: ", n*5) 

numbers= [2, 3, 5, 1]

begintime= time.time()

t1= Thread(target= divison, args= (numbers,))
t2= Thread(target= multiplication, args= (numbers,))

t1.start()
t2.start()
t1.join()
t2.join()


print("Total Time Taken: ", time.time()-begintime)  