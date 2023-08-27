#locking a thread
import threading

import time

x = 8192
lock = threading.Lock()

def halve():
    
    global x, lock
    lock.acquire()
    while x > 1:
        
        x /=2
        print(x)
        
        time.sleep(2)
    print("End!")
    lock.release()
    
def double():
    
    global x, lock
    lock.acquire()
    
    while x < 16384:
        
        x *=2
        print(x)
        
        time.sleep(2)
    print("End!")
    lock.release()
    
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target = double)
t1.start()
t2.start()