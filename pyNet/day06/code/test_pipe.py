from multiprocessing import Pool,Pipe
from time import sleep

fd1,fd2 = Pipe()

def a(ne):
    fd1.send("fd1,fd1")
    sleep(2)
    print(ne**2)
def b(ne):
    print(ne**3)
    sleep(3)
    fd1.send("fd1")

pool = Pool()

pool.apply_async(a,(2,))
pool.apply_async(b,(3,))

for x in (0,1):
    print(fd2.recv())

pool.close()
pool.join()