from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('0.0.0.0',8888))
#确定数据结构
st = struct.Struct('i5sf')

while True:
    data,addr = sockfd.recvfrom(1024)
    if not data:
        break
    data =st.unpack(data)
    print(data)

sockfd.close()