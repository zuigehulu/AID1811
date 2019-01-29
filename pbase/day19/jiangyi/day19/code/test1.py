class A:
    def __init__(self,name):
        self.name = name
        self.__name = name
    def __jieqian(self):
        print("没钱")
    def gai(self,name):
        self.__name = name
    def gai_jieqian(self):
        self.__jieqian()
