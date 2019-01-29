#   2. 输入三个任意的数:
#     1) 打印出最大数是多少?
#     2) 打印出最小数是多少?
#     3) 打印出三个数的平均值是多少?

a = int(input('请输入第1个数: '))
b = int(input('请输入第2个数: '))
c = int(input('请输入第3个数: '))

# 方法2
zuida = a

if b > zuida:
    zuida = b

if c > zuida:
    zuida = c

print("最大值是:", zuida)
