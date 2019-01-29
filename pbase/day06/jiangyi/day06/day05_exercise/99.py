#   1. 写程序打印九九乘法表
#     1x1=1
#     1x2=2 2x2=4
#     1x3=3 2x3=6 3x3=9
#     ....
#     1x9=9 ..........  9x9=81

for x2 in range(1, 10):
    for x1 in range(1, x2 + 1):
        print("%dx%d=%d"%(x1, x2, x1 * x2), end=' ')
    print()  # 换行


