from multiprocessing import Process,Value
import random

va = Value('i',10000)

def boy():
    global va
    for x in range(10):
        me = random.randint(1,1000)
        va.value += me
def girl():
    global va
    for x in range(10):
        me = random.randint(100,1000)
        va.value -= me
p = Process(target = boy)
p1 = Process(target = girl)
p.start()
p1.start()
p.join()
p1.join()
print(va.value)
