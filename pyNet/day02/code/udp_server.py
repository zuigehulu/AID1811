from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(('172.40.76.185',8888))
print('服务器已启动')
#消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print('Receive from %s:%s'%(addr,data.decode()))
    sockfd.sendto(b'Thanks for your msg',addr)

sockfd.close()