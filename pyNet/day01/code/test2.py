import socket

sockfd = socket.socket()

sockfd.bind(('192.168.10.206',8888))

sockfd.listen(5)
print('等待连接:')

connfd,addr= sockfd.accept()
# data = connfd.recv(1024)        
try:
    fr = open('timg.jpg','rb')
    #客户端退出，服务的recv立即返回空字符串
    for x in fr:
        print(addr,'连接了')
        connfd.send(x.)
        print(x)
finally:
    fr.close()
    connfd.close()
    sockfd.close()

