class Process(object):
    def __init__(self,pid):
        self.pid = pid 
    
    def start(self):
        #很复杂
        self.run()
    
    def run(self):
        pass 

class MyClass(Process):
    def __init__(self,value):
        self.value = value 
        super().__init__()

    def run(self):
        .......

p = MyClass()
p.start()