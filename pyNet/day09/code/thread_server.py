from socket import *
from threading import Thread
import sys,os

#客户端处理函数
def handler(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Thank You')
    c.close()

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.1',8888))
s.listen(3)

#循环接收客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器退出')
    except Exception as e:
        print('服务器异常:',e)
        continue
    #创建线程处理客户端请求
    t = Thread(target=handler,args=(c,))
    t.setDaemon(True)
    t.start()
        