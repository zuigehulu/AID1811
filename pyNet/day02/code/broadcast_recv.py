import socket

#创建数据包套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#设置套接字可以接受广播
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

sockfd.bind(('0.0.0.0',6688))

while True:
    try:
        msg,add = sockfd.recvfrom(1024)
        print("接收广播：",msg.decode())
    except KeyboardInterrupt:
        print('停止接收')
        break
    except Exception as e:
        print(e)

sockfd.close()
        
