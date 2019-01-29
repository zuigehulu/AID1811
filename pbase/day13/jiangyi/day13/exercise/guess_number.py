#   1. 猜数字游戏:
#     随机生成一个0~100之间的一个整数,用变量x绑定
#     让用户输入一个数用变量y绑定,然后输出猜数字的结果
#       1) 如果y 等于生成的数x,则提示用户"恭喜您猜对了", 并退出
#        程序
#       2) 如果 y 大于 x,则提示: 您猜的数字大了,然后继续猜
#       3) 如果 y 小于 x,则提示: 您猜小了, 然后继续猜

#     直到猜对为止,最后显示用户猜数字的次数

import random
x = random.randint(0, 100)
# print(x)

count = 0  # 计数

while True:
    y = int(input("请输入一个整数: "))
    count += 1
    if y == x:
        print("恭喜您猜对了")
        break
    elif y > x:
        print("您猜大了")
    elif y < x:
        print("您猜小了")

print("您共猜了%d次" % count)


