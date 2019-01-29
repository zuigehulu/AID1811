from socket import *
sockfd = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',8888)
sockfd.sendto('我连接了'.encode(),ADDR)
data = sockfd.recvfrom(1024)
print(data)