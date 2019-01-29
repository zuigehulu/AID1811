from multiprocessing import Process,Array

a = Array('c',b'hello')

def func():
    a[0] = b'H'

p = Process(target = func)
p.start()
p.join()

print(a.value)