# 用while语句打印三角形, 输入一个三角形的宽度和高度,打印
#      相应的三角形:
#       如:
#         请输入三角形的宽度: 3
#       1) 打印如下:
#         *
#         **
#         ***
#       2) 打印如下:
#           *
#          **
#         ***
#       3) 打印如下:
#         ***
#          **
#           *
#       4) 打印如下:
#         ***
#         **
        # *
n = int(input("请输入三角形的边长:"))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*",end = "")
        j += 1
    else:
        print()
    i +=1

a = 1
while a <= n:
    j = 1
    print(" "*(n-a),end = "")
    while j <= a:
        print("*",end = "")
        j += 1
    else:
        print()
    a += 1

c = n
while c >= 1:
    j = 1
    print(" "*(n-c),end = "")
    while j <= c:
        print("*",end = "")
        j += 1
    else:
        print()
    c = c - 1

d = n
while d >= 1:
    j = 1
    while j <= d:
        print("*",end = "")
        j += 1
    else:
        print()
    d -= 1
