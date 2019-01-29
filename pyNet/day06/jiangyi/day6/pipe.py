from multiprocessing import Process,Pipe 
import os,time 

#创建管道对象
# fd1 --> 只读 recv
# fd2 --> 只写 send
fd1,fd2 = Pipe(False)

def fun(name):
    time.sleep(3)
    fd2.send([1,2,3,4])

jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

#父进程从管道读取消息
for i in range(5):
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
