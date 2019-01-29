# diamond_inherit.py


class A:
    def go(self):
        print("A")
        super().go()  # 出错

class B(A):
    def go(self):
        print("B")
        super().go()   # C

class C(A):
    def go(self):
        print("C")
        super().go()  # A

class D(B, C):
    def go(self):
        print("D")
        super().go()

d = D()
d.go()  # ????







