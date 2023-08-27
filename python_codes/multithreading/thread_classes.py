#thread classes in python
import threading

#creating thread class
class Mythread(threading.Thread):
    def __init__ (self, meassage):
        threading.Thread. __init__(self)
        self.message = meassage
        
    def run(self):
        for x in range(100):
            print(self.message)
mt1 = Mythread("this is my thread")
mt1.start()