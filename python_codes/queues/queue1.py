#queues in python
#first in first out FIFO
import queue

q = queue.Queue()

for x in range(10):
    q.put(x)
    
for x in range(10):
    q.get(x)
    