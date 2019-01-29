from socket import *
import sys,getpass
import time

#登录界面
def jiemian():
    print("**********************************")
    print("************　电子词典　************")
    print("************　1.登　录　************")
    print("************　2.注　册　************")
    print("************　3.退　出　************")
    print("**********************************")

#输入账号密码验证
def shuruzhanghao(sockfd):
    while True:
        user = input('请输入账号:')
        password = getpass.getpass("请输入密码")
        if not user or not password:
            print('账号或密码为空，请重新输入')
            continue
        if ' ' in user or ' ' in password:
            print("账号密码不允许有空格，请重新输入")
            continue
        msg = "S %s %s"%(user,password)
        print(msg)
        sockfd.send(msg.encode())
        data = sockfd.recv(1024)
        if data ==b'OK':
            print("恭喜您，登陆成功")
            erjijiemian(sockfd,user)
            return
        else:
            print("账号输入有误，请重新输入")
            continue
#查询单词界面
def erjijiemian(sockfd,name):
    while True:
        print("********************")
        print("  1.要查询的单词")
        print("  2.查看历史记录")
        print("  3.注销")
        print("********************")
        data = input("请选择:")
        if data == '3':
            return
        elif data == '1':
            word = input("请输入您要查询的单词:")
            msg = 'W %s %s'%(name,word)
            sockfd.send(msg.encode())
            words = sockfd.recv(1024).decode()
            print(words)
            time.sleep(2)
        elif data == '2':
            chakan_history(sockfd,name)
            
def chakan_history(sockfd,name):
    msg = 'C %s'%(name)
    sockfd.send(msg.encode())
    while True:
        history = sockfd.recv(1024).decode()
        if history == '##':
            return
        print(history)
#注册账号界面
def zhucezhanghao(sockfd):
    while True:
        user = input('请输入您要注册的账号：')
        password = getpass.getpass("请输入您的密码:")
        password1 = getpass.getpass("请再次输入密码:")
        if password != password1:
            print("密码输入不一致")
            continue
        if ' ' in user or ' ' in password:
            print("账号密码输入错误")
            continue
        if not user or not password:
            print('账号或密码为空，请重新输入')
            continue
        msg = 'R %s %s'%(user,password)
        sockfd.sendall(msg.encode())
        data = sockfd.recv(1024).decode()
        if data == 'OK':
            print("恭喜您，注册成功")
            erjijiemian(sockfd,user)
            return
        else:
            print("账号密码验证失败")
            return


def main():
    if len(sys.argv)< 3:
        print("输入错误")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    sockfd = socket()
    sockfd.connect(ADDR)
    
    while True:
        try:
            jiemian()
            num = input("请选择:")
            if num == '1':
                shuruzhanghao(sockfd)
            elif num == '2':
                zhucezhanghao(sockfd)
            elif num == '3':
                sockfd.send(b'E ')
                break
            else:
                print("输入错误，请重新输入")
        except KeyboardInterrupt:
            sys.exit("谢谢使用")
        except Exception:
            sockfd.close()
            sys.exit("谢谢您使用")
    

if __name__ == "__main__":
    main()