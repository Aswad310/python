from threading import *
import time
import random
import queue

items=[]
def produce(c):
   while True:
       item=random.randint(1,10) #Step 1.2
       print("Producer Producing Item:", item)
       q.put(item)
       print("Producer giving Notification")
       time.sleep(5)

def consume(c):
   while True:
       print("Consumer waiting for update")
       print("Consumer consumed the item", q.get())
       time.sleep(5)

q=queue.Queue()
t1=Thread(target=consume, args=(q,))
t2=Thread(target=produce, args=(q,))
t1.start()
t2.start()