#    编写函数fun 基功能是计算下列多项式的和
#     Sn = 1 + 1/1! + 1/2! + 1/3! + .... + 1/n!
#     (建议用数学模块中的factorial)
#       求当n得20时 Sn的值
#     即:
#       print(fun(20))  # 2.718281828...
import math
# def sumfun(n):
#     Sn = 1
#     for x in range(1,n+1):
#         Sn += 1/math.factorial(x)
#     return Sn
# print(sumfun(20))
def sumfun(n):
    s = sum(map(lambda x :1/math.factorial(x),range(n+1)))
    print(s)
sumfun(20)