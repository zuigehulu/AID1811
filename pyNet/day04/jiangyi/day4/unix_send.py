from socket import * 

sockfd = socket(AF_UNIX,SOCK_STREAM)

#两端需要使用相同的套接子文件
sockfd.connect('./sock') 

while True:
    msg = input(">>")
    if not msg:
        break 
    sockfd.send(msg.encode())

sockfd.close()