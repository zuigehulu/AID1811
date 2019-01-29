class A:
    def __init__(self):
        self.__money = 100 #私有属性，只能用此类的方法来调用
    def __m(self):
        print("私有方法__m被调用")
    def show_info(self):
        self.__m()
        print(self.__money)

a = A()
a.show_info()
