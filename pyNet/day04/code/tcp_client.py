from socket import *
#创建套接字
sockfd = socket()

#发起连接请求
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#消息收发
while True:
    date = sockfd.recv(1024)
    print(date.decode())
    data = input('>>')
    if not data:
        break
    sockfd.send(data.encode())
#关闭套接字
sockfd.close()