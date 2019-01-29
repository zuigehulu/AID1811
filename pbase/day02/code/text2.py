# 2. 输入三个任意的数:
#     1) 打印出最大数是多少?
#     2) 打印出最小数是多少?
#     3) 打印出三个数的平均值是多少?
print("请输入三个数")
a = float(input("请输入第一个数:"))
b = float(input("请输入第二个数："))
c = float(input("请输入第三个数:"))
max1 = a
min1 = a
if a >= b:
    min1 = b
else:
    max1 = b
# 计算最大值
if  max1 >= c:
    print("最大数是：",max1)
else:
    print("最大数是：",c)
# 计算最小值
if  min1 >= c:
    print("最小数是：",c)
else:
    print("最小数是：",min1)
# 计算平均值
d = round((a + b + c)/3,2)
print("三个数的平均值是",d)



