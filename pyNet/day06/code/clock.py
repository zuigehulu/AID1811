from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self,value,target):
        super().__init__()
        self.target = target
        self.value = value
    #重写run方法
    def run(self):
        for i in range(5):
            self.target()
            print("The time is",time.ctime())
            time.sleep(self.value)

def a():
    print("eeeee")

#创建自定义类进程对象
p =ClockProcess(2,target = a)
p.start()
p.join()