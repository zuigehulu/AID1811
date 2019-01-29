from multiprocessing import Pool
from time import sleep
L = [1,2,3,4,5]
def a(ne):
    print(ne**2)
    sleep(2)
pool = Pool()
for i in L:
    pool.apply_async(a,(i,))

pool.close()
pool.join()