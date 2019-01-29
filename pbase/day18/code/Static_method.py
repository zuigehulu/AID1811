class A:
    @staticmethod
    def myadd(a,b):
        return a+b

print(A.myadd(100,200))
print(A.myadd('ABC','123'))
a = A()
print(a.myadd(3,5))