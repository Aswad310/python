import queue # Basically Stacks 

q= queue.LifoQueue()

q.put(4)
q.put(10)
q.put(2)

while not q.empty():
    print(q.get())