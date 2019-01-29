#   2. 输入三个任意的数:
#     1) 打印出最大数是多少?
#     2) 打印出最小数是多少?
#     3) 打印出三个数的平均值是多少?

a = int(input('请输入第1个数: '))
b = int(input('请输入第2个数: '))
c = int(input('请输入第3个数: '))

zuida = 0  # 用来记录最大数

if a > b:
    if a > c:
        zuida = a
    else:
        zuida = c
else:
    if b > c:
        zuida = b
    else:
        zuida = c
print("最大值是:", zuida)
