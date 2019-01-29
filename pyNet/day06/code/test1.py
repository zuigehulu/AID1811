from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self,name,target):
        super().__init__(target = target)
        self.name = name
    
    def run(self):
        # super().run()
        time.sleep(1)
        print(self.name)
def asd():
    print("打印一下")
L = ['q','qq','qqq','qqqq']
ls = []
for x in L:
    p = MyProcess(x,asd)
    p.start()
    ls.append(x)

for x in ls:
    x.join()