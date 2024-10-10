from socket import *
import threading
import time

def handle_client(clientSocket):
    try:
        message = clientSocket.recv(1024).decode()
        print(message)
        
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        clientSocket.sendall("HTTP/1.1 200 ok\r\n".encode())
        clientSocket.send("\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            clientSocket.send(outputdata[i].encode())
        clientSocket.send("\r\n".encode())
        time.sleep(2)
        clientSocket.close()
    except IOError:
        # Send response message for file not found
        print("file not find")
        clientSocket.sendall("HTTP/1.1 404 not found\r\n".encode())
        clientSocket.send("\r\n".encode())
    clientSocket.close()

def server_loop():
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("localhost",4567))
    serverSocket.listen(5)

    while True:
        print('ready to server...')
        # 接受TCP客户端连接,(阻塞式)等待连接的到来
        connectionSocket, connectionaddr = serverSocket.accept()
        print("accept from", connectionaddr)

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_handler.start()

if __name__=="__main__":
    server_loop()