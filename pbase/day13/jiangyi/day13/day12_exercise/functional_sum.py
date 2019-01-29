#   3. 编写函数fun 基功能是计算下列多项式的和
#     Sn = 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!
#     (建议用数学模块中的factorial)
#       求当n得20时 Sn的值
#     即:
#       print(fun(20))  # 2.718281828...
import math

# 方法1
# def fun(n):
#     Sn = 0
#     for x in range(n + 1):
#         Sn += 1 / math.factorial(x)
#     return Sn

# 方法2
# def fun(n):
#     Sn = 0
#     for fenmu in map(math.factorial, range(n + 1)):
#         Sn += 1 / fenmu
#     return Sn

# 方法3
def fun(n):
    Sn = sum([1 / math.factorial(x)
                   for x in range(n + 1)])
    return Sn

print(fun(20))
