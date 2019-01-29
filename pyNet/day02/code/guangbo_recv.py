#接收广播
from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
sockfd.bind(('0.0.0.0',6688))
# sockfd.bind(('0.0.0.0',8888))

while True:
    data,addr = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()