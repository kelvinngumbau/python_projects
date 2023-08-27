#threading

import threading
import time

lock = threading.Lock()
def function1():
    lock.acquire()
    for x in range(10):
        print("ONE")
        time.sleep(2)
    lock.release()
def function2():
    lock.acquire()
    for x in range(10):
        print("TWO")
        time.sleep(1)
    lock.release()

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t1.start()
t2.start()