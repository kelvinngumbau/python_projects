#queue resources in python
#first import thread

import threading

import queue
import math
import time

q = queue.Queue()
threads = []

def work():
    while True:
        item = q.get()
        if item is None:
            break
        print(math.factorial(item))
    q.tast_done()
    
    for x in range(5):
        t1 = threading.Thread(target = work)
        t1.start()
        threads.append(t)
        
    zahlen = [134000,14,5,300,98,88,11,23]
    
    for items in zahlen:
        q.put(item)
        
        q.join()
        
    for i in range(5):
        q.put(None)
                