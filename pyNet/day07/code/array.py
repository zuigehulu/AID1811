from multiprocessing import Process,Array
import time

#创建共享内存
# shm = Array('i',[1,2,3,4])
#春如字符串
shm = Array('c',b'Hello')

def fun():
    for i in shm:
        print(i)
    shm[0] = b'h'

p = Process(target = fun)
p.start()
p.join()

print(shm.value) #打印字节串，value只能打印字节串