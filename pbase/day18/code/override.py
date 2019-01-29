class A:
    def work(self):
        print("A.workBei被调用")

class B(A):
    def work(self):
        print("B.work被调用")

b = B()
b.work()

A.work(b)