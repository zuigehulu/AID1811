# if2.py

# 输入一个数字,用程序来判断这个数字是正数,零,还是负数

num = int(input("请输入一个整数: "))

if num > 0:
    print(num, '是正数')
elif num < 0:
    print(num, '是负数')
# elif num == 0:
else:
    print(num, '是零')
