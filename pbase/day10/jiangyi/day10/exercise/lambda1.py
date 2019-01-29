# 练习:
#   1. 写一个lambda 表达式:
#      fx = lambda n: .....
#    此表达式创建一个函数,判断n这个数的2次方+1能否被5整除,
#    如果能整除返回True,否则返回 False.
#     如:
#        print(fx(3))   # True
#        print(fx(4))   # False


def fx(n):
    return (n ** 2 + 1) % 5 == 0
    # return True if (n ** 2 + 1) % 5 == 0 else False

    # if (n ** 2 + 1) % 5 == 0:
    #     return True
    # return False

fx = lambda n: (n ** 2 + 1) % 5 == 0

print(fx(3))   # True
print(fx(4))   # False
