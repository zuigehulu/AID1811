from socket import *
import os 

#如果文件已经存在则删除
if os.path.exists("./sock"):
    os.remove('./sock')

#创建本地套接子
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定套接子文件
sockfd.bind("./sock")
#监听
sockfd.listen(3)

while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()



