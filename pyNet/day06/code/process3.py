from multiprocessing import Process
from time import sleep

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")
# p = Process(target = worker,args=(3,'Livi'))
p = Process(target = worker,args= (3,),kwargs = {'name':'Livi'})

p.start()

p.join()