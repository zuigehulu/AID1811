# closure2.py

# 创建一系列的函数:
# def pow2(x):
#     return x ** 2

# def pow3(x):
#     return x ** 3
# ...
# def pow300(x):
#     return x ** 300
# ...

def make_power(y):
    def fn(x):
        return x ** y
    return fn

pow2 = make_power(2)  # pow2绑定闭包函数
print(pow2(3))  # 9
print(pow2(4))  # 16

pow5 = make_power(5)
print(pow5(2))  # 32
print(pow5(4))  # 1024

