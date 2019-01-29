# super.py

class A:
    def work(self):
        print("A.work被调用!!!")

class B(A):
    def work(self):
        print("B.work被调用!!!!!!!!")

    def do_somthing(self):
        # 1. 调用自己的 work
        self.work()
        # 2. 调用父类的 work
        # super(B, self).work()
        super().work()

b = B()
# super(B, b).work()  # 借助于b来调用A类的方法
b.do_somthing()





