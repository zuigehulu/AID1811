# 1. 用字符串 * 运算符 打印三角形
#     要求输入一个数, 此整数代表此三角形离左侧的字符个数
#     如:
#       请输入左侧的空格数: 3
#         *
#        ***
#       *****
#      *******
num = int(input("请输入空格数:"))
a = 0
c = 1
while a<= num:
    b = 1
    while b <=num-a:
        print(" ",end ="")
        b += 1
    j = 1
    while True:
        if j <=a+c:
            print("*",sep="",end="")
            j += 1
        else:
            print()
            break
    a = a+1
    c = c+1