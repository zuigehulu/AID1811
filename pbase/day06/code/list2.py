l = []
i = 0
while True:
    num = int(input("输入一些正整数，-1结束"))
    if num > 0:
        l += [num]
        i += 1
    else:
        break
print(l)
print("您输入的最大值是:",max(l))
print("您输入的平均值是:",sum(l)/i)