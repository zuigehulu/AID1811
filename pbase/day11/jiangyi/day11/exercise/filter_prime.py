# 练习:
#   用filter 函数将 1 ~ 100 之间所有的素数prime存放于列表中
  

def is_prime(x):
    '''判断x是否是素数,是素数返回True,不是返回False'''
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
# 用构造函数
# L = list(filter(is_prime, range(100)))
# print(L)
# 用推导式:
L = [x for x in filter(is_prime, range(100))]
print(L)