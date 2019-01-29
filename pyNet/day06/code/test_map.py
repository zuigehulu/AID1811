from multiprocessing import Pool
from time import sleep
L = [1,2,3,4,5]
def a(ne):
    print(ne**2)
    sleep(2)
pool = Pool()
pool.map(a,L)

pool.close()
pool.join()