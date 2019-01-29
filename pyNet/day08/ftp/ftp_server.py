#coding = utf-8

from socket import *
import sys,os
import time 
#发送列表
def lst(conn,L):
    conn.send(b'OK')
    time.sleep(0.1)
    files = ''
    i = 1
    for x in L:
        if x[0] != '.' and os.path.isfile(FILES+x):
            a = str(i) +':'+ x 
            files = files + a +'\n'
            wenjian.append(a)
            i += 1
    conn.send(files.encode())

#下载文件
def get(conn,L,addr):
    data = conn.recv(1024).decode()
    if int(data) >= len(L):
        conn.send('E 输入错误,没有此编号'.encode())
        return
    l = wenjian[int(data)-1]
    file = l.split(':')[1]
    with open(FILES+file,'rb') as fr:
        while True:
            x = fr.read(1024)
            if not x :
                time.sleep(0.1)
                conn.send(b"##")
                break
            conn.send(x)
    fw = open('record.txt','a')
    record = '%s　download %s  %s'%(addr,file,time.ctime())
    fw.write(record)
    fw.write('\r\n')
    fw.close()
#上传文件
def put(conn,L,addr):
    file = conn.recv(1024)
    if not file: 
        conn.send(b'shibai')
        return
    conn.send(b'OK')
    file = file.decode()
    files = FILES+file
    with open(files,'wb') as fw:
        while True:
            data = conn.recv(1024)
            if data == b'##':
                break
            fw.write(data)
    fw = open('record.txt','a')
    record = '%s　update %s  %s'%(addr,file,time.ctime())
    fw.write(record)
    fw.write('\r\n')
    fw.close()
#接收消息
def lianjie(conn,addr):
    while True:
        L = os.listdir(FILES)
        data = conn.recv(1024).decode()      
        if data == 'Q' or not data :
            conn.close()
            # print(addr,":已退出")
            return
        elif data == 'L':
            lst(conn,L)
        elif data == 'G':
            get(conn,L,addr)
        elif data == 'P':
            put(conn,L,addr)
        else:
            conn.send('查询失败，请重试'.encode())
                
HOST = '0.0.0.0'
POOR = 8888
ADDR =(HOST,POOR)
FILES = '../../day07/code/'
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(5)
print("已准备，可以连接:",ADDR)
wenjian=[]
while True:
    conn,addr = sockfd.accept()
    print(addr,"已连接")
    pid = os.fork()
    if pid == 0:
        p = os.fork()
        if p == 0:
            sockfd.close()
            #接收连接函数
            lianjie(conn,addr)
            print(addr,end='')
            sys.exit("断开连接")
        else:
            os._exit(0)
    else:
        conn.close()
        os.wait()