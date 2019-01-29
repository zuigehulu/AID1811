#   1. 写一个程序,输入圆的半径, 打印出这个圆的面积
#   2. 输入一个圆的面积,打印出这个圆的半径
#     (要求: 用math模块里的函数实现)
#       详见:>>> help(math)

import math as m

r = float(input('请输入圆的半径: '))
area = m.pi * r ** 2
print("半径为:", r, '的面积是:', area)

area2 = float(input("请输入圆的面积: "))
r2 = m.sqrt(area2 / m.pi)
print("面积为:", area2, '的半径是:', r2)

