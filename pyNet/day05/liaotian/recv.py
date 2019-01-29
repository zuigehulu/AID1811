from socket import *
from select import *
from os import *

def xiaoxi_fasong(conn,user,sockfd,rlist):
    data = conn.recv(1024).decode()
    # print(data)
    L = data.split(' ')
    # print(L)
    if L[0] == 'Q':
        conn.send(b'break')
        data = ' '.join(L[1:])+'：退出聊天室'
        conn.close()
        rlist.remove(conn)
        for r,u in user.items():
        # print(u) 
            a,c = u
            if c == conn:
                del user[r]
                break
    for u in user.values():
        # print(u) 
        a,c = u
        if c == conn:
            continue
        c.send(data.encode())

def yanzheng_name(conn,rlist,user,addr):
    name = conn.recv(1024).decode()
    if name in user:
        conn.send("名字已存在，请重新输入!".encode())
    else:
        conn.send(b"OK")
        for a,c in user.values():
            # if not c:
            #     break
            data = '欢迎%s进入聊天室'%name
            c.send(data.encode())
        rlist.append(conn)
        user[name] = (addr,conn)

# 进行连接
def jieshou(sockfd):
    user ={}
    rlist = [sockfd]
    wlist = []
    xlist = []
    while True:
        rs,ws,xs = select(rlist,wlist,xlist)
        for r in rs:
            if r is sockfd:
                conn,addr = r.accept()
                yanzheng_name(conn,rlist,user,addr)
            else:
                xiaoxi_fasong(r,user,sockfd,rlist)
                
#主函数
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8888))
    sockfd.listen(5)
    jieshou(sockfd)

if __name__ == "__main__":
    main()                


