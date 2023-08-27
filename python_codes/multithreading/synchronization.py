#synchronization in python
import threading
import time
x = 8192
def halve():
    global x
    while(x>1):
        x /=2
        print(x)
        time.sleep(1)
        print("End!")
    
def double():
    
    global x
    while(x<16384):
        x *=2
        print(x)
        time.sleep(1)
        print("End!")

t1 = threading.Thread(target = halve)
t2 = threading.Thread(target = double)
t1.start()
t2.start()