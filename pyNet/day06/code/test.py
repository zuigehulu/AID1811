from multiprocessing import Process
import time

def ac(name):
    print(name)
    time.sleep(2)
    print(time.ctime())

L = []
for i in range(5):
    p = Process(target=ac,args=(i,))
    L.append(p)
    p.start()
print(p.name)
print(p.pid)
print(p.is_alive())


for i in L:
    i.join()