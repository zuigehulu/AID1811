# class_attribute.py


#  看懂下列代码中的类属性count 的作用是什么?

class Human:
    '''此示例示意类属性'''
    count = 0  # 创建类属性(类变量)

    def __init__(self, name):
        print(name, '对象被创建')
        self.name = name
        self.__class__.count += 1

    def __del__(self):
        print(self.name, '对象被销毁')
        self.__class__.count -= 1

L = [Human('孙悟空'), Human('猪八戒')]
h1 = Human('沙僧')
print("现在共有", Human.count, '个实例对象')
del L
print("现在共有", Human.count, '个实例对象')







