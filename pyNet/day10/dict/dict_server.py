from multiprocessing import Process
from socket import *
import os,sys
import pymysql
import time

#验证账号密码
def yanzheng_zhanghao(conn,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql = "select * from user where uname = '%s' \
           and pword = '%s'"%(name,passwd)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        conn.send(b'OK')
        return
    else:
        conn.send(b'Error')
#注册账号密码
def zhuce_zhanghao(conn,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql = "select * from user where uname = '%s'"%name
    cursor.execute(sql)
    if cursor.fetchone():
        conn.send(b'chucuo')
        return
    sql = "insert into user values ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        conn.send(b'OK')
        return
    except Exception:
        db.rollback()
        c.send(b'FAIL')
        return
#查找单词
def chazhao_danci(conn,db,data):
    L = data.split(' ')
    word = " ".join(L[2:]).strip()
    print(word)
    cursor = db.cursor()
    sql = "select * from dict where word = '%s'"%word
    cursor.execute(sql)
    cword = cursor.fetchone()
    if not cword :
        conn.send("没有该单词".encode())
        return
    lst = list(cword)
    cdata = ' '.join(lst[1:])
    if cdata != None:
        conn.send(cdata.encode())
        sql = "insert into record values(null,'%s','%s','%s')"%(L[1],word,time.ctime())
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            return
        except Exception:
            db.rollback()
    else:
        conn.send("没有该单词".encode())
#查看历史记录
def lishi_history(conn,db,data):
    l = data.split(' ')
    name = l[1]
    cursor = db.cursor()
    sql = "select * from record where uname = '%s'"%name
    cursor.execute(sql)
    i = 1
    while True:
        lishi = cursor.fetchone()
        if not lishi or i >10:
            time.sleep(0.1)
            conn.send(b'##')
            return
        L = list(lishi)
        data = ' '.join(L[1:]) +"\r\n"
        conn.send(data.encode())
        i += 1
        

#连接
def lianjie(conn,db):
    while True:
        data = conn.recv(1024).decode()
        if (not data) or data[0] == 'E':
            print(conn.getpeername(),'退出')
            conn.close()
            sys.exit()
        elif data[0] == 'S':
            yanzheng_zhanghao(conn,db,data)
        elif data[0] =='R':
            zhuce_zhanghao(conn,db,data)
        elif data[0] == 'W':
            chazhao_danci(conn,db,data)
        elif data[0] == "C":
            lishi_history(conn,db,data)


#主函数
def main():
    sockfd = socket()
    sockfd.bind(('0.0.0.0',8000))
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.listen(5)
    db = pymysql.connect('localhost','root','123456','dict')
    while True:
        try:
            conn,addr = sockfd.accept()
            print("Connent from",addr)
            p = Process(target = lianjie,args=(conn,db))
            p.start() 
        except KeyboardInterrupt:
            sockfd.close()
            print("服务器退出")
        except Exception as e:
            p.join()
            # print(e)
            sys.exit()


if __name__ =='__main__':
    main()