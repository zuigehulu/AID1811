#  编写函数fun ,其功能是计算并返回下列多项式的值
#     Sn = 1 + 1/2 + 1/3 + 1/4 + .... + 1/n
#       def fun(n):
#           ...
#       print(fun(2))   # 1.5
#       print(fun(3))   # 1.8333333333333
#       print(fun(10))  # ????
def fun(n1):
    sn = 0
    for x in range(1,n1+1):
        sn +=1/x
    return sn

print(fun(2))
print(fun(3))
print(fun(10))
