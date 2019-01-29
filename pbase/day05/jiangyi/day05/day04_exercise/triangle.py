#   2. 用while语句打印三角形, 输入一个三角形的宽度和高度,打印
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
#         *


w = int(input("请输入三角形的宽度: "))
stars = 1  # stars 代表星号的个数
while stars <= w:
    # 打印一行
    print("*" * stars)
    stars += 1

print("============")
stars = 1
while stars <= w:
    # 打印一行, 每行左侧添 w-stars 个空格
    blanks = w - stars  # 求出当前行空格的个数
    print(' ' * blanks + '*' * stars)
    stars += 1

print("============")
stars = w  # 起初的星号的个数
while stars > 0:
    blanks = w - stars
    print(' ' * blanks + '*' * stars)
    stars -= 1  # 星的个数每次减少一个

print("============")
stars = w  # 起初的星号的个数
while stars > 0:
    print('*' * stars)
    stars -= 1  # 星的个数每次减少一个

#       4) 打印如下:
#         ***
#         **
#         *
