#发送广播
from socket import *
socket = socket(AF_INET,SOCK_DGRAM)

socket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = ('192.168.10.206',6688)

while True:
    d = '饿了'.encode()
    socket.sendto(d,data)

socket.close()
