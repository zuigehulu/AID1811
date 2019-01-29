from socket import *
from select import *

#创建流式套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)
#初始化poll
pf = poll()
#创建字典
dmap = {sockfd.fileno():sockfd}

pf.register(sockfd,POLLIN|POLLERR)

while True:
    events = pf.poll()
    for fl,event in events:
        if sockfd.fileno() == fl:
            conn,addr = dmap[sockfd.fileno()].accept()
            print('Connect from',addr)
            pf.register(conn,POLLIN|POLLERR)
            dmap[conn.fileno()] = conn
        elif fl == conn.fileno():
            data = dmap[fl].recv(1024)
            if not data:
                sockfd.close()
                pf.unregister(sockfd)
                del dmap[sockfd.fileno()]
            else:
                print(data.decode())
                # conn.send("shoudao".encode())

