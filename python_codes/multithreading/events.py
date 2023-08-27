#thread events

import threading
#creating an event using event function
event = threading.Event()

def function():
    print(" waiting for event...")
    event.wait()
    print("Continuing!")
    
thread = threading.Thread(target = function)
thread.start()

x = input("Trigger event?")

if x == "yes":
    #we set the event
    event.set()