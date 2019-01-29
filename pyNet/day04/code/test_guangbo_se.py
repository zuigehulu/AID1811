from socket import *
import time
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
ADDR=("192.168.43.255",8888)
while True:
    sockfd.sendto('该睡觉了'.encode(),ADDR)
    time.sleep(0.3)