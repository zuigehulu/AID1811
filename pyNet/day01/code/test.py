import socket

#创建服务器端

#创建socket的对象　套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('192.168.10.206',6666))

#监听
sockfd.listen(5)

#等待客户连接
print('等待访问中。。。。')
connfd,addr = sockfd.accept()
print('连接来自:',addr)

#接收／发送

date = connfd.recv(1024)
print(date.encode())
n = connfd.send('hello'.encode())

#关闭
connfd.close()
sockfd.close()
