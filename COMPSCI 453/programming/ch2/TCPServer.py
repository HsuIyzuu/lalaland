from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive.')

while True:
    # server waits on accept() for incoming requests, new socket created on return
    connectionSocket, addr = serverSocket.accept()

    # read bytes from socket (but not address as in UDP)
    sentence=connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()