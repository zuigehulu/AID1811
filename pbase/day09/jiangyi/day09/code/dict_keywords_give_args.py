
# 此示例示意 字典关键字传参

def myfun1(a, b, c):
    """这是一个有三个参数的函数"""
    print("a =", a)
    print("b =", b)
    print("c =", c)

d = {'c':33, 'b':22, 'a':11}
# myfun1(c=d['c'], b=d['b'], a=d['a'])
myfun1(**d)  # 等同于myfun1(c=33, b=22, a=11)

# 以下为错误示例
d2 = {'c':33, 'b':22, 'a':11, '123':456}
myfun1(**d2)











