from multiprocessing import Process
from socket import *
import sys
import signal #信号处理模块

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.1',8888))
s.listen(5)


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
    sys.exit(0)  #客户端子进程也退出

#忽略子进程退出释放资源请求，交由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
    try:
        conn,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器退出')
    except Exception as e:
        print('服务器异常')
        continue
    p = Process(target = headler,args=(c,))
    p.daemon = True
    p.start()

