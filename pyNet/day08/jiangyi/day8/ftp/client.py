from socket import * 
import sys 
import time 

#具体请求功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd 
    
    #查看文件列表
    def do_list(self):
        self.sockfd.send(b'L') #发送请求
        #等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
        else:
            print(data) #打印无法操作原因

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")
    
    def do_get(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

#网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器失败:",e)
        return 
    
    ftp = FtpClient(sockfd) #创建对象

    while True:
        print("\n======命令选项==========")
        print("=====    list     =====")
        print("=====   get file  =====")
        print("=====   put file  =====")
        print("=====    quit     =====")
        print("=======================\n")

        cmd = input("输入命令>>")
        if cmd.strip() == 'list': 
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        else:
            print("请输入正确命令")

main()