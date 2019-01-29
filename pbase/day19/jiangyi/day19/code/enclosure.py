# enclosure.py


class A:
    def __init__(self):
        self.__money = 100  # 私有属性,只能用此类的方法来调用

    def borrow(self, x):
        if x < self.__money:  # 此类的方法可以访问私有属性
            self.__money -= x
            return x
        return 0

a = A()
# 访问私有属性失败!!!
# print(a.__money)
# a.__money -= 100  # 由类的外部直接操作money属性
# print(a.__money)  # 0s

print("借钱:", a.borrow(20))


