from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('0.0.0.0',8888))
data,addr = sockfd.recvfrom(1024)
print(data.decode())
sockfd.sendto('你好'.encode(),addr)
