class A:
    def __init__(self):
        self.__em =100
    def xiu(self,n):
        self.__em -= n
        print(self.__em)

a = A()
a.xiu(20)
# print(a.__me)