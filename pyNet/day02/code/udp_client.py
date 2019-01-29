from socket import *
import sys

#从命令行传入服务器ip port
HOST = sys.argv[1]
PORT = sys.argv[2]
ADDR = (HOST,int(PORT))

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('Msg>>')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print('From server:%s  %s'%(addr,msg))

sockfd.close()