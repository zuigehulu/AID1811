class Human:
    count = 0
    def __init__(self,name):
        self.name = name
        print(name,'对象被创建')
        self.__class__.count += 1
    def __del__(self):
        print(self.name,'对象被销毁')
        self.__class__.count -= 1

L = [Human('孙悟空'),Human('猪八戒')]
h1 = Human('沙僧')
print(Human.count)
del L
print(Human.count)