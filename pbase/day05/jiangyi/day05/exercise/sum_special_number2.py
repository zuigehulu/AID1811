# 练习:
#   1. 求1 ~ 100 之间所有不能被2, 3, 5, 7中 任意一个数整
#     除的数的和(用continue来实现)

s = 0

for x in range(1, 101):
    if (x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or 
       x % 7 == 0):
       continue
    # if x % 2 == 0:
    #     continue
    # if x % 3 == 0:
    #     continue
    # if x % 5 == 0:
    #     continue
    # if x % 7 == 0:
    #     continue
    # print(x)
    s += x  # 把符合条件的数累加到s中

print('这些数的和是:', s)


