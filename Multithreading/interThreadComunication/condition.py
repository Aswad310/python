from threading import *
import time
import random

items=[]
def produce(c):
   while True:
       c.acquire() #Step 1.1
       item=random.randint(1,10) #Step 1.2
       print("Producer Producing Item:", item)
       items.append(item) #Step 1.3
       print("Producer giving Notification")
       c.notify() #Step 1.4
       c.release() #Step 1.5
       time.sleep(5)

def consume(c):
   while True:
       c.acquire() #Step 2.1
       print("Consumer waiting for update")
       c.wait() #Step 2.2
       print("Consumer consumed the item", items.pop()) #Step 2.3
       c.release() #Step 2.4
       time.sleep(5)

c=Condition()
c= Lock()
t1=Thread(target=consume, args=(c,))
t2=Thread(target=produce, args=(c,))
t1.start()
t2.start()