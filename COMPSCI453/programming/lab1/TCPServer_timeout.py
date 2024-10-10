from socket import *

serverHost="localhost"
serverPort=4567
serverSocker=socket(AF_INET, SOCK_STREAM)
serverSocker.bind((serverHost, serverPort))
serverSocker.listen(1)

counter = 0
while counter<3:
    connSocket,connAddr = serverSocker.accept()
    connSocket.settimeout(10)

    try:
        connMessage = serverSocker.recv(1024).decode()
        connSocket.send(connMessage)
    except timeout:
        counter += 1

    connSocket.close()

# - A shepherd boy tends his master’s sheep.
# - If he sees a wolf, he can send a message to villagers for help using a TCP socket. 
# - The boy found it fun to connect to the server without sending any messages. But the villagers don’t think so.  
# - And they decided that if the boy connects to the server and doesn’t send the wolf location within 10 seconds for three times, they will stop listening to him forever and ever.

