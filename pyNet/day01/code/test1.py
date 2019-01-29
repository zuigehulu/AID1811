import socket

#建立套接字
sockfd = socket.socket()

sockfd.connect(('192.168.10.206',6666))

s ='hello,我知道你不是百度'.encode()
sockfd.send(s)

c = sockfd.recv(1024)
print(c.decode())

sockfd.close()