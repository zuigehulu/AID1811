import os
from time import sleep

a = 10000
#创建进程
pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    print("Child Process")
    a = 2
    print(a)
    print(id(a))
else:
    sleep(0.1)
    print('a=',a)
    print("Parent Process")
    print(id(a))
