import threading
from time import sleep
import os

a = 1

#线程函数
def music():
    global a
    print('a:',a)
    a = 10000
    for i in range(5):
        sleep(2)
        print("播放好嗨哟")
def music1():
    global a
    print('a:',a)
    a = 100001
#创建线程对象
t1 = threading.Thread(target = music1)
sleep(1)
t = threading.Thread(target = music)
t.start()
t1.start()
for i in range(3):
    sleep(3)
    print("播放听说")
t.join()
t1.join()

