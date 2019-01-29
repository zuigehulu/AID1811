#只允许连接４个客户端，如果重复就提示其错误，不再接收
from socket import *
from select import *
import struct

def myrecv():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8888))
    sockfd.listen(5)
    rlist = [sockfd]
    wlist = []
    xlist = []
    while True:
        rs,ws,xs = select(rlist,wlist,xlist)
        for r in rs:
            rb = 1 if len(rlist) <= 4 else  0
            if rb == 1:
                if r == sockfd:
                    conn,addr = r.accept()
                    print("welcome com",addr)
                    rlist.append(conn)
                    conn.send('已连接'.encode())
            elif rb == 0:
                if r == sockfd:
                    conn,addr = r.accept()
                    conn.send('连接已满，请换房'.encode())
                    conn.close()
            else:
                data = r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                    continue
                print(data.decode())
myrecv()