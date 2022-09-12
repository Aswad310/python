import queue

q= queue.PriorityQueue()

q.put((89, "Aswad"))
q.put((18, "Abad"))
q.put((1, "Ahmer"))
q.put((44, "Butt"))
q.put((322, "Basharat"))

while not q.empty():
    print(q.get())
    # print(q.get()[0])