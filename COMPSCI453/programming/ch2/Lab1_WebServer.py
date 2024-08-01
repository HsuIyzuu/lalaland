from socket import *
import sys

serverSocket = socket(AF_INET,SOCK_STREAM)
serverHost = "localhost"
serverPort = 4567
serverSocket.bind((serverHost,serverPort))
serverSocket.listen(1)

while True:
    print('ready to server...')

    connectionSocket, addr = serverSocket.accept()
    print("accept from", addr)

    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        connectionSocket.sendall("HTTP/1.1 200 ok\r\n".encode())
        connectionSocket.send("\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        print("file not find")
        connectionSocket.sendall("HTTP/1.1 404 not found\r\n".encode())
        connectionSocket.send("\r\n".encode())
    connectionSocket.close()

serverSocket.close()
sys.exit()