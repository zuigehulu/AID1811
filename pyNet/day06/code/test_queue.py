from multiprocessing import Pool,Queue
from time import sleep
q = Queue()
def a(ne):
    sleep(2)
    q.put("get%s"%ne**2)
    print(ne**2)
def b(ne):
    print(ne**3)
    q.put("get2get2")
    sleep(3)
pool = Pool()
pool.apply_async(a,(2,))
pool.apply_async(b,(3,))
for x in (1,2):
    print(q.get())
pool.close()
pool.join()