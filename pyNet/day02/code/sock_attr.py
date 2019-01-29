from socket import *
sock = socket()
#设置端口立即重用
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# print(s.type)  #套接字类型 
# print(s.family) #套接字地址类型
sock.bind(('172.40.76.185',8888))
# print(s.getsockname()) #获取绑定地址
# print(s.fileno()) #文件描述符

sock.listen(5)

c,addr = sock.accept()
print(c.getpeername())
