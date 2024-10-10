# learn how to send and receive datagram packets using UDP sockets
# learn how to set a proper socket time out
# gain familiarity with a Ping application and its usefulness in computing statistics such as packet loss rate.

import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind=(('',12000))

while True:
    rand = random(0,10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    # If rand is less is than 4, we consider the packet lost and do not respond 
    if rand < 4: 
        continue 
# Otherwise, the server responds     
    serverSocket.sendto(message, address)

