from multiprocessing import Pool
from time import sleep,ctime
import multiprocessing.pool.ApplyResult
def worker(msg):
    sleep(0.2)
    print(msg)
    return ctime()

#创建进程池
pool = Pool()

result = []
#向进程池添加事件
for i in range(10):
    msg = 'hello %d'%i
    r = pool.apply(func = worker,args = (msg,))
    result.append(r)

#关闭进程池
pool.close()

#回收进程
pool.join()
for r in result:
    print(r)
    # print(r.get()) #可以获得进程事件函数返回值

