# 创建udp服务端
import socket
socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socket.bind(('192.168.10.206',6688))

data,addr = socket.recvfrom(1024)

n = socket.sendto('你好'.encode(),addr)

socket.close()