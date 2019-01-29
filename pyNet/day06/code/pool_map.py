from multiprocessing import Pool
from time import sleep,ctime

def fun(n):
    sleep(2)
    return n**2

pool = Pool()

#使用map讲事件放入进程池
r = pool.map(fun,[1,2,3,4,5,6])
pool.close()
pool.join()
for x in r:
    print(x)
