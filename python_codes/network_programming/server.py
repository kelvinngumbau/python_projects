#network programming
#choose between internet socket, socket.AF_INET
#transmission protocol, TCP, SOCK.STREAM
#ip address, 127.0.0.1
#port number , 9999

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the connection assigning ip address and port number

s.bind(("127.0.0.1",9999))
s.listen()

print("listening...")

while True:
    client, address = s.accept()
    
    print("connected to {}".format(address))
    message = "hello client"
    message2 = "how can I help you"
    client.send(message2.encode('ascii'))
    client.close()