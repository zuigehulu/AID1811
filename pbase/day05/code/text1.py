#1. 99乘法表
#  2.打印素数
# 3.输入一个整数，此整数代表树干的高度，打印一颗如下的圣诞树
# 4.算出100~999的水仙花数
for x in range(1,10):
    for y in range(1,x+1):
        print("%dX%d=%d"%(y,x,x*y),end = " ")
    else:
        print()