#创建udp客户端
from socket import *

socket = socket(AF_INET,SOCK_DGRAM)
addr = ('192.168.10.206',6688)
socket.sendto('你好'.encode(),addr)
data,addr = socket.recvfrom(1024)
print(data.decode())

socket.close()