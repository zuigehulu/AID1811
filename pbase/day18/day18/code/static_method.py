# static_method.py


class A:
    @staticmethod
    def myadd(a, b):
        return a + b
    
print(A.myadd(100, 200))  # 300
print(A.myadd("ABC", '123'))  # ABC123
a = A()
print(a.myadd(3, 5))  # 8


