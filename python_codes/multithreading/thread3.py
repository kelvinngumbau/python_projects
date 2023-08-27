#waiting for thread
import threading

def function():
    for x in range(100):
        print("hello world!")

t1 = threading.Thread(target=function)
#starting the thread
t1.start()

#we use join function to output what will printed in the last line
t1.join(10)#number of the seconds it should wait is 10 seconds
print("This is the head")