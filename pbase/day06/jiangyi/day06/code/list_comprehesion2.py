# list_comprehesion.py


# 生成一个数字1 ~ 9的整数的平方的列表，即:
#    L = [1, 4, 9, 16, 25, .... 81]
L = []
for x in range(1, 10):
    if x % 2 == 1:
        L.append(x ** 2)

print(L)

# 以下用列表的推导式实现上述功能
L2 = [x**2 for x in range(1, 10) if x % 2 == 1]
print(L2)
