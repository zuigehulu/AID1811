# multi_inherit2.py

# 多继承的名字冲突问题示例 

# 小张写了一个类A
class A:
    def m(self):
        print("A.m() 被调用!")

# 小李写了一个类B
class B:
    def m(self):
        print("B.m() 被调用!")

# 小王感觉小张和小李写的类都可以用
class AB(A, B):
    pass

ab = AB()
ab.m()  # 请问调用谁?