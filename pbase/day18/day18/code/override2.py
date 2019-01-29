# override.py


class A:
    def work(self):
        print("A.work被调用!!!")

class B(A):
    def work(self):
        print("B.work被调用!!!!!!!!")

b = B()
b.work()  # B.work被调用!!!!!!

A.work(b)  # A.work被调用!!!




