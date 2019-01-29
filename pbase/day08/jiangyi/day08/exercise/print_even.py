#   2. 写一个函数 print_even, 传入一个参数n代表终止的整数
#     (注: 不包含n), 此函数打印:
#        0 2 4 6 8 ... 到n为止的全部偶数
#     如:
#       def print_even(n):
#          ....  # 此处自己实现
#       # 调用
#       print_even(10)  # 打印 0 2 4 6 8


def print_even(n):
    # for x in range(0, n, 2):
    #     print(x)
    for x in range(0, n, 2):
        print(x, end=' ')
    print() # 换行

# 调用
print_even(10)  # 打印 0 2 4 6 8
print_even(100)
