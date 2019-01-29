from socket import *
from select import select
from sys import stdin
from time import sleep

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',6688))
sockfd.listen(3)
rlist = [sockfd,stdin]
wlist = []
xlist = []
fw = open('test.txt','wt')

try:
    while True:
        rs,ws,xs = select(rlist,wlist,xlist)
        for r in rs:
            if r is sockfd:
                conn,addr = r.accept()
                rlist.append(conn)
            elif r is stdin:
                data = r.readline()            
                print(r,'say',data)
                fw.write(str(data))                
            else:
                data = r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                    continue
                print(addr,'say:',data.decode())
                fw.write(str(addr))
                fw.write(str(data.decode()))
                fw.write('\n')
                wlist.append(r)

        for w in ws:
            w.send('shou dao'.encode())
            wlist.remove(w)
            pass
        for x in xs:
            pass
except:
    print('出错')
finally:
    fw.close()