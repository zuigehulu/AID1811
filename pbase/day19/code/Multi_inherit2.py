#多继承名字冲突问题示例
class A:
    def m(self):
        print("A.m")

class B:
    def m(self):
        print("B.m")

class C(B,A):
    pass

c = C()
c.m()