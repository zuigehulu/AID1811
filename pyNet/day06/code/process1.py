import multiprocessing
import time

a = 1
#编写进程函数
def fun():
    time.sleep(3)
    global a
    a = 10000
    print(a)
    print("子进程事件")

#创建进程对象
p = multiprocessing.Process(target = fun)

#启动进程
p.start()

#回收进程
p.join()

# time.sleep(4)
print("父进程时间")
print(a)