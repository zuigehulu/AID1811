from select import *
from socket import *

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#创建poll对象
p = poll()

#建立查找字典
fdmap = {s.fileno():s}

#注册关注IO
p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()  #监控IO
    print("有io没处理")
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from',addr)
            #添加新的关注事件
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c
        #通过按位与判断是否是某个时间就行
        # elif event & POLLIN: 
        elif fd == c.fileno():
            data = fdmap[fd].recv(1024)
            if not data:
                #客户端退出则取消关注，从字典删除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print('receive:',data.decode())
                fdmap[fd].send(b'shou dao')

