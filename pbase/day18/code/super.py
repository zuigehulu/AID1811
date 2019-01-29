class A:
    def work(self):
        print("A.workBei被调用")

class B(A):
    def work(self):
        print("B.work被调用")
    def do_somthing(self):
        self.work()
        super().work()

b = B()
b.work()
super(B,b).work() #借助于b来调用Ａ类的方法
b.do_somthing()
