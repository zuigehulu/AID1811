import socket
import time

#创建数据包套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#设置套接字可以接受广播
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

# sockfd.bind(('0.0.0.0',9999))
dest=('172.40.76.255',6688)
while True:
        time.sleep(1)
        s = '晚上吃啥'
        sockfd.sendto(s.encode(),dest)
        print(s)
sockfd.close()
        
