
# 此示例示意 序列传参

def myfun1(a, b, c):
    """这是一个有三个参数的函数"""
    print("a =", a)
    print("b =", b)
    print("c =", c)

L = [1, 2, 3]
myfun1(*L)  # 等同于 myfun1(L[0], L[1], L[2])

T = (100, 200, 300)
myfun1(*T)

s = "ABC"
myfun1(*s)





