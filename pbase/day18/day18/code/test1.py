class Xi_youji:
    __count = 0
    __slots__ = ['name']
    def __init__(self,name):
        self.name = name
        print(self.name,'被创建')
        self.__class__.__count += 1
    def __del__(self):
        self.__class__.__count -= 1
        print(self.name,'被销毁')
    def prt(self):
        print(Xi_youji.__count)
L = [Xi_youji('悟空'),Xi_youji('八戒')]
xi = Xi_youji('沙僧')
xi.prt()
del L
xi.prt()
