# 练习:
#   生成一个1~9的整数的平方的元组,元组如下:
#     (1, 4, 9, 16, .... 81)

t = ()
for x in range(1, 10):
    t += (x**2,)

print(t)

t2 = tuple([x ** 2 for x in range(1, 10)])
print("t2 =", t2)

