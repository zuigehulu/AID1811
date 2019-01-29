import socket

#创建tcp套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('172.40.76.185',8888))
#设置监听
sockfd.listen(5)　#阻塞函数

#等待处理客户端连接
print('hello')


sockfd.close()

class conn:
    def __init__(self):
        self.connfd,self.addr = sockfd.accept()
    def fuwuduan(self):
        connfd,addr = sockfd.accept() #阻塞函数
        print('Connect from',addr) #打印客户端地址
        #消息收发
        while True:
            data = connfd.recv(1024)
            if not data:
                break
            print('Receuve Msg:',data.decode())
            n = connfd.send('欢迎光临，再见'.encode())
            print('Send %d bytes'%n)

        #关闭套接字
        connfd.close()
