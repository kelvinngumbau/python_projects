#priority queue in python

import queue

q = queue.PriorityQueue()

q.put((8,"Some string"))
q.put((1, 2023))
q.put((90, True))
q.put((2,10.23))

while not q.empty():
    print(q.get()[1])   #[1]is used for indexing and output all the values in index 1