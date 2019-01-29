from socket import *
#创建套接字
sockfd = socket()

#发起连接请求
server_addr = ('172.40.76.185',9999)
sockfd.connect(server_addr)

#消息收发
while True:
    data = input('>>')
    if not data:
        break
    sockfd.send(data.encode())
    # date = sockfd.recv(1024)
    # print(date.decode())
#关闭套接字
sockfd.close()