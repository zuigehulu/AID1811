#coding = utf-8

from socket import *
import os,sys

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(1024)
        print(data.decode)

#创建套接字
def main():
    #从命令行输入ip
    if len(sys.argv) < 3:
        print("argv is error!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建udp套接字
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        msg = "L " + name #发送标示位，告诉服务器是要验证姓名
        s.sendto(msg.encode(),ADDR)
        #等待回应
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    elif pid == 0:
        pass
    else:
        recv_msg(s)
main()