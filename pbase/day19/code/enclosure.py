class A:
    def __init__(self):
        self.__money = 100 #私有属性，只能用此类的方法来调用
    def borrow(self,n):
        if n < self.__money:
            self.__money -= n
            return n
        return 0
    def shuchu_money(self):
        print(self.__money)

a = A()
print('借钱:',a.borrow(20))
a.shuchu_money()

# a.money -= 100 #由类的外部直接操作money属性
# print(a.__money)
