from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message=input('input lowercase sentence.')
clientSocket.sendto(message.encode(),(serverName, serverPort))
# 接收 UDP 数据，与 recv() 类似，但返回值是（data,address）。其中 data 是包含接收数据的字符串，address 是发送数据的套接字地址。
modifiedMessage, severAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()