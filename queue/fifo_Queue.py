import queue

q= queue.Queue()

q.put(5)
q.put(10)
q.put(3)

while not q.empty():
    print(q.get())