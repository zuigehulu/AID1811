from socket import *
fw = open('timw.jpg','wb')
sockfd = socket()
sockfd.connect(('127.0.0.1',8888))
while True:
    data = sockfd.recv(1024)
    if not data:
        break
    fw.write(data)
fw.close()
sockfd.close()