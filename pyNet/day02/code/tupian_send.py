from socket import *
import time
socket = socket()
socket.connect(("127.0.0.1",8800))

fr = open('timd.jpg','wb')

while True:
    data = socket.recv(1024)
    if not data:
        break;
    fr.write(data)

fr.close()
socket.close()