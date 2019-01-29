from select import select
from socket import *

#准备要关注的IO
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('172.40.76.185',9999))
sockfd.listen(3)

#添加关注列表
rlist = [sockfd]
wlist = []
xlist = []

#监控IO的发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    print(rs)
    #遍历三个列表，确定哪个ＩＯ发生
    for r in rs:
        #如果遍历到sockfd，说明S就绪，有客户端发起连接
        if r is sockfd:
            conn,addr = r.accept()
            print("Connect from",addr)
            rlist.append(conn)
        #客户端连接套接字就绪，则接受消息
        else:
            data = r.recv(1024)
            if not data:
                #客户端退出从关注列表移出
                rlist.remove(r)
                r.close()
                continue
            print("Receive from %s:%s"%(r.getpeername(),data.decode()))
            # r.send(b'shoudao')
            # wlist.append(r)

    # for w in rs:
    #     w.send(b'shou dao')
    #     wlist.remove(w)
    #     pass
    # for x in xs:
    #     pass


