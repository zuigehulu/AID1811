from socket import *
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)
conn,addr = sockfd.accept()
fr = open('timg.jpg','rb')
while True:
    data = fr.read(1024)
    if not data:
        break
    conn.sendall(data)
fr.close()
conn.close()
sockfd.close()

