from select import select 
from socket import *
import sys
from time import ctime

#准备要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

f = open('mylog','a') #日志文件

#添加关注列表
rlist = [s,sys.stdin]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        elif r is sys.stdin:
            #获取从终端的输入
            data = sys.stdin.readline()
            data = ctime()+'  '+data+'\n'
            f.write(data)
            f.flush()  #清理写缓存
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue 
            data = ctime()+'  '+data+'\n'
            f.write(data)
            f.flush()
            r.send(b'Add logging')
   