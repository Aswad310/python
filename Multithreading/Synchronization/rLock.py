from threading import *

l= RLock()

def factorial(n):
    l.acquire()
    if n==0:
        ans= 1
    else:
        ans= n * factorial(n-1)
    l.release()        
    return ans

def display(n):
    print("Factorial of",n,"is:",factorial(n))

t1= Thread(target=display, args=(2,))
t2= Thread(target=display, args=(3,))

t1.start()
t2.start()