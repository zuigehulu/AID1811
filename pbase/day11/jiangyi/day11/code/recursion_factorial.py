# recursion_factorial.py

# 阶乘公式(n!):
#     1            当 n == 0
#     n * (n-1)!   当 n > 0

def myfac(n):
    if n == 0:
        return 1
    s = n * myfac(n - 1)  # 求n的阶乘
    return s

print(myfac(5))