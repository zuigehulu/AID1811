from socket import *
import os,sys

#接收信息
def jieshou(sockfd):
    while True:
        data = sockfd.recv(1024)
        if data == 'break':
            sys.exit()
        print(data.decode())

#发送信息 
def fasong(sockfd,name):
    while True:
        data = input("消息:")    
        if data == '##':
            msg = 'Q %s: %s'%(name,data)
            sockfd.send(msg.encode())
            sys.exit()  
        msg = "%s: %s"%(name,data)
        sockfd.send(msg.encode())

#分进程
def fenjinchen(sockfd,name):
    pid = os.fork()
    if pid < 0:
        print("Error")
        sys.exit(0)
    elif pid == 0:
        jieshou(sockfd)
    else:
        fasong(sockfd,name)
        

def yanzheng_name(sockfd):
    while True:
        name = input("请输入名字:")
        sockfd.send(name.encode())
        msg = sockfd.recv(1024)
        if msg.decode() == 'OK':
            print('欢迎进入聊天室') 
            break    
        elif name == '##':
            break
        else:
            print(msg.decode())
    fenjinchen(sockfd,name)


def main():
    if len(sys.argv) < 3:
        print("参数输入错误")
        return
    sockfd = socket()
    HOST = sys.argv[1]
    DUAN = int(sys.argv[2])
    ADDR = (HOST,DUAN)
    sockfd.connect(ADDR)
    yanzheng_name(sockfd)

if __name__=='__main__':
    main()