#coding = utf-8

from socket import *
import sys,os
import time

#FTP类
class Ftp():
    
    def __init__(self,sockfd):
        self.sockfd = sockfd
        self.L = []
    
    def do_lst(self):
        self.sockfd.send(b'L')
        data = self.sockfd.recv(128)
        if data.decode() == 'OK':
            # print("查询成功，马上为您呈现")
            time.sleep(0.1)
        else:
            print(data.decode())
            return    
        lst = self.sockfd.recv(4096).decode()
        self.L = lst.split('\n')
        for x in self.L:
            print(x)

    def do_get(self):
        self.sockfd.send(b'G')
        try:
            num = int(input("请选择要下载的文件编号:"))
        except Exception:
            print("请重新输入编号")
            return
        self.sockfd.send(str(num).encode())
        num -= 1
        l = self.L[num]
        fil = l.split(':')
        fw = open(fil[1],'wb')
        data = self.sockfd.recv(1024)
        msg =data.decode()
        if not msg or msg[0] =='E'  :
            print(msg[1:])
        else:
            while True:
                fw.write(data)
                if data == b'##':
                    break
                data = self.sockfd.recv(1024)
        print("下载完成")
        fw.close()

    def do_put(self):
        self.sockfd.send(b'P')
        file = input('请输入文件名字:')
        try:
            fr =  open(file,'rb')
        except Exception:
            print("本地没有此文件") 
        self.sockfd.send(file.encode())
        da = self.sockfd.recv(1024)
        if da != b'OK':
            print('连接失败，重新连接')
            return
        time.sleep(0.1)
        print("已执行")
        while True:
            data = fr.read(1024)
            if not data:
                time.sleep(0.1)
                self.sockfd.send(b'##')
                break
            self.sockfd.send(data)
        print("上传完成")
        fr.close()

            
#界面
def jiemian():
    while True:
        print("\r\n**********命令选项*********")
        print("****** 1   查看文件    *******")
        print("****** 2   下载文件    *******")
        print("****** 3   上传文件    *******")
        print("****** 4    退出      *******") 
        print("*********************** *****")
        try:
            s = int(input("请输入:"))
            if 1 <= s <= 4:
                return s
        except Exception:
            print("输入错误，请重新输入")
            time.sleep(2)

#主函数
def main():
    sockfd = socket()
    sockfd.connect(("127.0.0.1",8888))
    ftp = Ftp(sockfd)
    while True:
        s = jiemian()
        if s == 2:
            ftp.do_get()
        elif s == 1:
            ftp.do_lst()
        elif s == 3:
            ftp.do_put()
        elif s == 4:
            sockfd.send(b'Q')
            sockfd.close()
            sys.exit("欢迎使用")
            # break

if __name__ == '__main__':
    main()