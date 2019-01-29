# enclosure2.py


class A:
    def __init__(self):
        self.__money = 100  # 私有属性,只能用此类的方法来调用

    def __m(self):
        print("私有方法__m 被调用")

    def show_info(self):
        self.__m()  # 可以调用
        print(self.__money)  # 可以访问

a = A()
# a.__m()  # 调用失败! 不允许访问
a.show_info()



