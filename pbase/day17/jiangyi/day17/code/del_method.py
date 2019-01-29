# del_method.py


# 此示例示意 析构方法的定义和使用
class Car:
    def __init__(self, info):
        self.info = info
        print("汽车:", info, '对象被创建!')
        # self.file = open("xxx.txt")

    def __del__(self):
        print('汽车:', self.info, '对象将被销毁!!')
        # self.file.close()
L = []
c1 = Car("BYD E6")

L.append(c1)  # 会把BYD E6 的引用计数+1
# del c1
c1 = None

input('请输入回车键继续: ')
print("程序正常退出")

