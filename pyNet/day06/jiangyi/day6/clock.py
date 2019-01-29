from multiprocessing import Process 
import time 

class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()

    # def funcname(self, parameter_list):
    #     pass

    #重写run方法
    def run(self):
        for i in range(5):
            print("The time is",time.ctime())
            time.sleep(self.value)

#创建自定义类进程对象
p = ClockProcess(2)
p.start()  #自动调用run
p.join()

