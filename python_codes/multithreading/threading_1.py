#thread in python
#we have to import threading

import threading

def hello():
    print("hello world!")

t1 = threading.Thread(target=hello)#referring to our function we dont put parenthesis after function
t1.start()