#   4. 写一个函数计算 1 + 2**2 + 3**3 + ... + n**n的和
#     (注: n给个小点的数)
# 方法1
def fun(n):
    s = 0
    for x in range(1, n + 1):
        s += x ** x
    return s

# 方法2
def fun(n):
    return sum(map(lambda x: x ** x, range(1, n+1)))

print(fun(3))  # 32