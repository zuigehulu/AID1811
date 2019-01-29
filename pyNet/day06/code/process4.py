from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
p = Process(target = tm)
print('开始前:',p.is_alive())
p.daemon = True
p.start()
print(p.name)
print(p.pid)
print("执行中:",p.is_alive())
# p.join()
print("执行完毕:",p.is_alive())