#访问服务器
import socket
sockfd = socket.socket()
sockfd.connect(('192.168.10.206',8888))

try:
    fw = open('aid1811zhang/pyNet/day01/tim.jpg','wb')
    # while True:
    data = sockfd.recv(1024)
    
        # if not data:
        #     break
    da = data
    fw.write(da)
except Exception as e:
    print('文件传送出错')
    print(e)
finally:
    fw.close()
    sockfd.close()

