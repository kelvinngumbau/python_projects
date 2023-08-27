#port scanning in python

import socket

target = "10.0.0.5"

def portscan(port):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        conn = s.connect((target, port))
        
        return True
    except:
        
        return False
for x in range(1, 501):
    
    if(portscan(x)):
        
        print("port {} is open".format(x))
    
    else:
    
        print("port {} is closed!".format(x))